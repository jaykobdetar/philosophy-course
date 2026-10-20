#!/usr/bin/env python3
"""Reconcile authored additions with preserved, prerequisite-compatible routes."""

import argparse
import json
from pathlib import Path

from check_authoring import inspect
from course_model import COMMON, route_records

ROOT = Path(__file__).resolve().parents[1]


def build():
    errors, tracks, additions = inspect()
    if errors:
        raise ValueError("\n".join(errors))
    data = json.loads((ROOT / "data/course.json").read_text())
    known = {t["id"] for t in tracks}
    normalized = []
    for addition in additions:
        if not set(addition["applies_to"]) <= known:
            raise ValueError(f"Unknown route target: {addition['id']}")
        # PC-31's C10 bridge is needs-based support in the accepted plan.
        optional = addition["pc_task"] == "PC-31" and "C10" in addition["applies_to"]
        normalized.append({**addition, "budget_role": "optional support" if optional else "planned addition"})
    routes = []
    for choices, baseline in route_records(data["courses"]):
        route = set(COMMON + list(choices) + ["C14"])
        selected = [a for a in normalized if set(a["applies_to"]) & route]
        required = [a for a in selected if a["budget_role"] == "planned addition"]
        optional = [a for a in selected if a["budget_role"] == "optional support"]
        credits = []
        for a in required:
            credit = a.get("shared_credit")
            if credit and credit["target_track"] in route:
                credits.append({"from": a["id"], **credit})
        added = sum(a["net_hours"] for a in required)
        potential = sum(c["potential_credit_hours"] for c in credits)
        routes.append({
            "options": list(choices), "source_baseline_hours": baseline,
            "addition_ids": [a["id"] for a in required], "net_added_hours": added,
            "planned_hours_before_conditional_credit": baseline + added,
            "conditional_credits": credits, "potential_credit_hours": potential,
            "planned_hours_if_credit_earned": baseline + added - potential,
            "optional_support_ids": [a["id"] for a in optional],
            "optional_support_hours_if_taken": sum(a["net_hours"] for a in optional),
        })
    default_options = [x for x in data["default_route"] if x.startswith(("C11", "C12", "C13"))]
    default = next(r for r in routes if r["options"] == default_options)
    course_by_id = {c["id"]: c for c in data["courses"]}
    milestones = []
    for stop in (1, 2, 6, 10):
        completed = set(COMMON[:stop])
        baseline = sum(course_by_id[c]["baseline_hours"] for c in completed)
        selected = [a for a in normalized if set(a["applies_to"]) & completed]
        required = [a for a in selected if a["budget_role"] == "planned addition"]
        optional = [a for a in selected if a["budget_role"] == "optional support"]
        milestones.append({"through_course": stop, "source_baseline_hours": baseline,
            "net_added_hours": sum(a["net_hours"] for a in required),
            "planned_hours": baseline + sum(a["net_hours"] for a in required),
            "optional_support_hours": sum(a["net_hours"] for a in optional)})
    language = [a for a in normalized if a["id"] in {"C12-PC28-FOUNDATION", "C12-PC28-GRICE"}]
    language_hours = sum(a["net_hours"] for a in language)
    return {
        "schema_version": 1, "authored_on": "2026-10-20",
        "unit": "planned focused learner hours; not measured or piloted",
        "source_baseline_version": data["curriculum_version"],
        "formula": "source baseline + unique required net additions - only earned named overlap credits; optional support added separately",
        "additions": normalized, "routes": routes, "milestones": milestones,
        "common_core_language_extension_hours": language_hours,
        "common_core_with_language_hours": milestones[-1]["planned_hours"] + language_hours,
        "default_options": default_options,
        "default_planned_hours": default["planned_hours_before_conditional_credit"],
        "source_access_note": "An authored budget does not establish access to every required edition. Consult course source audits; unavailable reading-dependent tasks remain pending.",
        "credit_note": "C12A's 20-hour Frege/Russell foundation is already in its baseline. Other C12 routes add the shared bridge once. If later taking C12A, retain and credit that work once. C06 Sartre credit in C12C requires the specified evidence and Macomber check; no credit is assumed before it is earned.",
    }


def outputs():
    authored = build()
    ledger = json.loads((ROOT / "data/workload.json").read_text())
    ledger["authored_workload_source"] = "data/authored-workload.json"
    ledger["proposal_history_note"] = "specified_proposals preserves the earlier seed estimates and pending labels as historical planning evidence; the authored-workload source supersedes them for current packet budgets. Do not add both ledgers."
    ledger["revised_default_total"] = authored["default_planned_hours"]
    ledger["note"] = "The revised default total is an authored planning allocation, not measured learner time. 1,936/+46 remains a superseded estimate with different scope. Route-specific bridges, conditional credits and optional support are reconciled in authored-workload.json."
    lines = [
        "# Planned study workload", "",
        "The accepted curriculum's baseline stays unchanged. This view adds the completed PC-25–33 teaching packets once and reports conditional overlap credits separately. These are planning estimates; no real learner timing is claimed.", "",
        "| Options: Course 11 / 12 / 13 | Source baseline | Net additions | Before conditional credit | If named credit earned | Optional probability support |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for r in authored["routes"]:
        lines.append(f"| {' / '.join(r['options'])} | {r['source_baseline_hours']} | {r['net_added_hours']} | {r['planned_hours_before_conditional_credit']} | {r['planned_hours_if_credit_earned']} | +{r['optional_support_hours_if_taken']} |")
    lines += ["", "Only prerequisite-compatible routes are listed. Other combinations need the additional prerequisite course or documented equivalent; these totals do not waive it.", "", "## Stopping milestones", "", "| Through course | Source baseline | Required additions | Planned hours | Optional support |", "| --- | ---: | ---: | ---: | ---: |"]
    for m in authored["milestones"]:
        lines.append(f"| {m['through_course']} | {m['source_baseline_hours']} | {m['net_added_hours']} | {m['planned_hours']} | +{m['optional_support_hours']} |")
    lines += ["", f"For introductory language coverage at the Course 10 stop, complete the shared Frege/Russell foundation and Grice packet: +{authored['common_core_language_extension_hours']} hours, giving {authored['common_core_with_language_hours']} planned hours before optional probability support. These are the same packets used later. If proceeding to C12A, credit the foundation's 20 hours inside C12A-M01; if taking another C12 option, credit the completed bridge. Grice is charged once. The full-route table already counts the work once, so do not add the early language hours to it again.", "", "## Packet ledger", "", "| Packet | Gross hours | Replaced hours | Net hours | Applies to |", "| --- | ---: | ---: | ---: | --- |"]
    for a in authored["additions"]:
        lines.append(f"| [{a['id']}](../{a['path']}) | {a['hours']} | {a['replaces_hours']} | {a['net_hours']} | {', '.join(a['applies_to'])}; {a['budget_role']} |")
    lines += ["", "## Credit and access rules", "", authored["credit_note"], "", authored["source_access_note"], "", "Each module includes its own practice, feedback, assessment and delayed work. Delayed checks take time from the current calendar's study budget but remain charged to their originating course. Keep actual hours and any extra remediation separate.", "", "See [complete structured arithmetic and credit evidence](../data/authored-workload.json), [the original proposal history](../data/workload.json), and [all teaching materials](README.md).", ""]
    return {
        ROOT / "data/authored-workload.json": json.dumps(authored, ensure_ascii=False, indent=2) + "\n",
        ROOT / "data/workload.json": json.dumps(ledger, ensure_ascii=False, indent=2) + "\n",
        ROOT / "instruction/workload.md": "\n".join(lines),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for path, content in outputs().items():
        if args.check:
            if not path.exists() or path.read_text() != content:
                raise SystemExit(f"stale authored workload: {path.relative_to(ROOT)}")
        else:
            path.write_text(content)
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
