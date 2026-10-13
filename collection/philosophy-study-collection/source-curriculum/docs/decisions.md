# Decisions

What was decided, when, and why. Update this file whenever the design changes, so the other documents can be checked against it.

## 2026-09-29: initial design

These decisions came out of a review of the original research report, "A University-Level Philosophy Education with OpenAI Dots as Tutor".

### Roles and agents

1. **Six roles, one file each** (Director of Studies, Tutor, Assignment Designer, Debate Partner, Examiner, Verifier), plus shared ground rules. *Why:* each teaching job needs a different stance. One dot plays all the roles for now; each file can become a separate dot's instructions when that's possible.
2. **Examiner independence:** until separate dots exist, grading happens in a separate session with memory off. *Why:* a single dot remembers the tutoring, and dot conversations can feed ChatGPT's memory.
3. **Only the Director acts unprompted, and only about logistics.** *Why:* dots do proactive background research, which could hand the learner interpretations before they've tried.
4. **Oral exams and debates are spoken.** *Why:* typed answers can be drafted and polished.

### Repository

5. **The repository is the memory.** The learner's record lives in `learner/` and is committed with session summaries. *Why:* individual dot memories can't be viewed or corrected.
6. **One public repository under the MIT License; learners study in private copies** made with GitHub's template button. Forking is only for contributing. *Why:* forks of public repositories are public and can't be made private.
7. **Privacy is a hard stop.** The Director writes nothing personal until it confirms the repository is private, and re-checks every session. `learner/` is git-ignored until then. *Why:* making a repository private later doesn't recall existing copies, and the dot can't prevent the learner's own commits.
8. **Personal files stay in `learner/`,** so curriculum updates can arrive as pull requests without touching them.

### Materials

9. **Four access types:** stored, retrieve, link, and learner. Every entry keeps a link as a fallback.
10. **Books are sourced by the learner.** *Why:* they're the hardest material to license and the least suited to a repository.
11. **Cite by standard reference numbers** (Stephanus, Bekker, AT, Akademie, and so on), and record the learner's editions in `learner/editions.md`. *Why:* any good edition then works.
12. **Legitimate sources only.** Restricted material is fetched on demand and never committed. SEP entries are cited by fixed quarterly edition.
13. **Retrieval tool** (planned, second build pass): start from philosophy-mcp (MIT), add a DOI lookup, and offer both an MCP server and command-line commands. Each learner runs their own copy. *(Built differently in the end: see 33–36.)*

### Pace and progression

14. **Self-paced and mastery-based:** units instead of semesters, gates instead of deadlines, sessions instead of schedules, and stages (Foundations, Core, Advanced, Capstone) instead of years. *Why:* a personal AI teacher removes the need for a fixed schedule; the standards stay fixed.
15. **Gates:** a written exam without AI help, a spoken oral exam, and a revised paper scoring 80 or more. Test-outs are allowed. The other thresholds in `rubrics/gates.md` (exam marks, oral scores, paper lengths by stage) are defaults set during the build.
16. **A confirmation check about four weeks after each gate.** *Why:* performance right after studying overstates what lasts.
17. **Review runs on a clock,** with growing intervals across the whole program. This replaced the report's review schedule, which stopped at the end of each term.
18. **Read ahead freely; a unit counts as mastered only when its prerequisites are mastered.**
19. **The Director learns the learner's reading pace** in place of fixed page targets. Learners can set optional goals, and the Director nudges after long gaps, but never sets deadlines.

### Curriculum

20. **Fifteen units,** each sized to a real university course: Introduction, Logic I, Ancient & Medieval, Early Modern, Kant & the 19th Century, Ethics, Political Philosophy, Epistemology, Metaphysics, Philosophy of Language, Philosophy of Mind, Aesthetics, two electives, and Research & Thesis. *Why:* the report paired subjects, giving each about half a course.
21. **Philosophy of Language is a unit of its own.** Kripke's *Naming and Necessity* is split: Lectures I–II in Language, Lecture III in Metaphysics.
22. **Gaps filled:** medieval readings named; the *Critique of Pure Reason* scheduled; Hegel, Marx, and Kierkegaard added; metaethics added; Frege, Russell, Quine, Kripke, Lewis, and Wittgenstein added; the report's placeholder readings replaced with named ones.
23. **Electives:** one non-European tradition and one contemporary area. Logic II can fill the contemporary slot. A full medieval unit is available as an extra elective but doesn't fill that slot. *(Clarified during the build: the design discussion had said a medieval unit "could also count".)*
24. **Introduction written in full, step by step; the other 14 units as outlines** (prerequisites, anchor readings, mastery criteria, gate).

### Documents and tools

25. **The report is split into the repository's files,** and its timelines, weekly schedules, and hour totals are dropped.
26. **Only verified sources are cited;** every other claim that needs one is marked [citation needed].
27. **A documentation check,** `tools/check_docs.py`, verifies internal links, agreement between the unit map and unit files, and the README's layout. *Why:* the documents cross-reference each other heavily and have to stay accurate.
28. **Postponed:** involving human reviewers or examiners. **Out of scope:** pricing.

## 2026-09-29, later: sourcing pass and citations

29. **The catalog is sourced.** Every anchor reading has checked publication details and, where one exists, a legal free copy (Project Gutenberg, Wikisource, the Internet Archive, HathiTrust, or a publisher's or university's repository). Articles carry a DOI or JSTOR link where one was found. *Why:* learners and the retrieval tool need stable identifiers.
30. **Rights labels:** PD (US and life-plus-70 countries), PD (US), ©, or the licence the source states. Public-domain status outside the US is claimed only where the author's or translator's death date is known.
31. **No publisher links for in-copyright books.** Any scholarly edition that prints the standard reference numbers works. The suggested modern editions carried over from the report haven't been re-checked.
32. **Every citation is resolved.** The nine claims marked [citation needed] now cite sources, and their wording was adjusted where a source said something narrower: Harvard's thesis belongs only to its honors track, Brown's thesis is one of three capstone options, and the feedback claim now follows Nicol and Macfarlane-Dick.

## 2026-09-29, later: retrieval tool

33. **The retrieval tool is a security-hardened copy of philosophy-mcp by sea9401** (version 0.5.0), kept in `tools/retrieval/` with its original MIT notice and credited in both READMEs. It provides 20 tools: PhilPapers and PhilArchive search and full text, Project Gutenberg, the Internet Archive, Wikisource, Open Library, DOAB, the SEP, an allowlist-only `fetch_text`, and local-document reading. Its offline test suite passes (45 tests, plus a smoke test confirming that all 20 tools register).
34. **Differences from the plan in decision 13:** there's no DOI-to-open-access lookup and no command-line interface, and the server speaks MCP over stdio only. It works with local MCP clients but can't yet be connected to ChatGPT or dots, which need a server reachable over the web.
35. **Safe defaults and placement:** local documents and `fetch_text` stay off until enabled, and the tool's download and document folders should sit outside the repository so retrieved or personal texts can't be committed.
36. **CI moved to the repository root** (`.github/workflows/ci.yml`), because GitHub runs workflows only from the root `.github/workflows` folder. It runs the documentation check and the tool's `npm test` on Node 22 and 24. The tool's npm publishing workflow was dropped, since this copy isn't published.
37. **The test suite was removed** to keep the repository lean, after it had passed (see 33): the 45 security and integration tests, their fixtures, the smoke test, and two older test clients. `check-tools.mjs` replaces them: `npm run check` calls all 20 tools against the real sources, and `npm test` runs a network-free version (startup, tool registry, local-document tools) that CI uses. *Trade-off:* changes that weaken the hardening are no longer caught automatically; the hardened release still has the tests if they're needed again.

## 2026-09-29, later: PhilPapers access

38. **Live check results.** A live run of `npm run check` by another agent: 15 tools worked, `research` returned partial results, and `get_paper`, `list_recent`, `fetch_pdf`, and `get_fulltext` were blocked with HTTP 403.
39. **PhilPapers record lookups need an API key.** The tool's OAI-PMH endpoint was outdated. It now uses the documented handler, `api.philpapers.org/oai.pl`, which refused data queries without a valid API key. The tool reads `PHILPAPERS_API_ID` and `PHILPAPERS_API_KEY`, sends them only to that host (as `apiId` and `apiKey`, the parameters PhilPapers documents for its JSON API; still to be confirmed with a real key), and redacts them from errors. Without a key, those tools explain how to get one, and `research` notes that its abstracts come from OpenAlex only.
40. **The Director helps each learner get a key** during setup. The learner enters it into the tool's configuration themselves, and keys never go into the repository; ground rule 6 now covers secrets.
41. **PhilArchive PDFs need a browser.** PhilPapers answered automated PDF downloads with a Cloudflare browser check. The tool now recognizes it and tells the learner to download the PDF in a browser into their documents folder and use the local-document tools. It doesn't try to get around the check.
42. **The functional check** reports SKIP when no key is set and LIMIT for the browser check, and its network-free mode also checks the missing-key message.

## Corrections to the original report

- Its citation markers were unreadable placeholders, so none of its sources could be checked.
- It said that "resetting" a dot deletes its conversations, memories, and tasks. OpenAI's FAQ describes deleting the dot, which removes the dot's own context but not the conversations and files it created, or separate ChatGPT memories.
- Its comparison with Princeton's eight courses left out Princeton's required junior independent work group, junior paper, and senior thesis.
- Its reading target of 50–100 pages in about four hours was too fast for careful reading of primary texts.
- It described Harvard's basic concentration as including an honors thesis and oral examination; those belong only to Harvard's honors track.
