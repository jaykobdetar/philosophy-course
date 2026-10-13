"""Small route and prerequisite model shared by generated views and checks."""

from itertools import product

COMMON = [f"C{i:02d}" for i in range(1, 11)]
OPTIONS = (
    ("C11A", "C11B"),
    ("C12A", "C12B", "C12C", "C12D"),
    ("C13A", "C13B", "C13C"),
)


def base(prerequisite):
    return prerequisite.split(":", 1)[0]


def requirements_met(course, completed):
    return all(base(p) in completed for p in course.get("prerequisites", [])) and all(
        any(base(p) in completed for p in group)
        for group in course.get("prerequisite_groups", [])
    )


def route_records(courses):
    """Return routes completed in order with no extra option or waived gate."""
    by_id = {c["id"]: c for c in courses}
    results = []
    for choice in product(*OPTIONS):
        route = COMMON + list(choice) + ["C14"]
        completed = set()
        for id_ in route:
            if not requirements_met(by_id[id_], completed):
                break
            completed.add(id_)
        else:
            results.append((choice, sum(by_id[id_]["baseline_hours"] for id_ in route)))
    return results
