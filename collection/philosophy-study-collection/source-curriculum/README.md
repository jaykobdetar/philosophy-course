# Philosophy Curriculum

A self-paced, university-level philosophy education, taught by AI agents playing six roles, with this repository as their shared memory.

It's designed around OpenAI's dots (always-on ChatGPT agents), but the instructions are plain text and work with any capable agent that can read and write a repository. It isn't an accredited degree.

**Public repository:** _add the URL here once published_

## Status

| Part | State |
|---|---|
| Roles, rubrics, templates | Done |
| Unit map (15 units) | Done |
| Introduction to Philosophy | Complete, step by step |
| The other 14 units | Outlines: prerequisites, anchor readings, mastery criteria, gate |
| Reading sources and rights | Done: see the [materials catalog](materials/catalog.md). Publisher links for in-copyright books aren't included |
| Retrieval tool | Included: a security-hardened copy of [philosophy-mcp](https://github.com/sea9401/philosophy-mcp) by sea9401 ([tools/retrieval](tools/retrieval/README.md)). Works with local MCP clients; not yet connectable to ChatGPT or dots. PhilPapers lookups need a free API key (the Director helps set it up), and PhilArchive PDFs have to be downloaded in a browser |
| Citations in the rationale | Done: see [docs/rationale.md](docs/rationale.md) |

## How it works

- **Six roles.** A Director of Studies keeps your record and plans sessions; a Tutor teaches by questioning; an Assignment Designer builds exercises; a Debate Partner argues with you; an Examiner runs gates; a Verifier checks claims about texts against sources. For now one dot plays all six; see the [ground rules](roles/ground-rules.md).
- **Units, not semesters.** Fifteen units, each sized to a real university course and linked by prerequisites. Read ahead freely. A unit counts as mastered once you've passed its gate, passed a confirmation check about four weeks later, and mastered its prerequisites. See the [unit map](curriculum/map.md).
- **Your pace, fixed standards.** No deadlines. Start a session whenever you have time and say how long you have; the Director plans it. Gates keep the standards constant: a written exam taken without AI help, an oral exam by voice, and a revised paper.
- **Review that never stops.** Material from every unit comes back at growing intervals.
- **The repository is the memory.** Your record lives in files you can read, correct, and version, not in an agent's hidden memory.

## Start here

1. **Make a private copy.** On GitHub, click **Use this template** and choose **Private**. Don't fork this repository to study: forks of public repositories are public and can't be made private. Fork only to contribute changes back.
2. **Connect your dot.** Give it access to your private copy (for example through ChatGPT's GitHub plugin), then send it:

   ```
   You're my Director of Studies for the philosophy curriculum in this repository: <link to your private copy>.
   Read roles/ground-rules.md and roles/director-of-studies.md, then run setup.
   ```

3. **Setup.** The Director confirms the repository is private, creates your `learner/` workspace, records your background, and runs a short diagnostic. Until setup confirms privacy, `learner/` is excluded from git, so nothing personal can be pushed by accident.
4. **Get your books.** You source the books yourself; see the [materials catalog](materials/catalog.md). Record your editions in `learner/editions.md`.
5. **Begin** with [Introduction to Philosophy](curriculum/units/introduction.md), with [Logic I](curriculum/units/logic-1.md) alongside it if you like.

To work with a role, name it: "Tutor, let's go through Meno 80d." If you don't name a role, you're talking to the Director.

## Repository layout

```
philosophy-curriculum/
├── README.md                    this file
├── LICENSE                      MIT (original content only)
├── .gitignore                   keeps learner/ out of git until setup
├── .github/                     CI: docs check and retrieval-tool tests
├── roles/                       the six roles, and the rules they all follow
│   ├── ground-rules.md
│   ├── director-of-studies.md
│   ├── tutor.md
│   ├── assignment-designer.md
│   ├── debate-partner.md
│   ├── examiner.md
│   └── verifier.md
├── curriculum/
│   ├── map.md                   the 15 units, prerequisites, and the unit cycle
│   └── units/                   one file per unit
├── rubrics/
│   ├── analytic-essay.md
│   ├── oral-exam.md
│   ├── mastery-dashboard.md
│   └── gates.md                 what passing a gate requires
├── templates/                   formats for exercises, feedback, exams, and logs
│   └── learner/                 copied to learner/ at setup
├── materials/
│   ├── catalog.md               every source: type, access, license, reference system
│   └── texts/                   short redistributable texts only (none yet)
├── tools/
│   ├── check_docs.py            consistency checks for these documents
│   └── retrieval/               retrieval tool: MCP server based on sea9401/philosophy-mcp
├── docs/
│   ├── rationale.md             why the design is the way it is, with sources
│   └── decisions.md             what was decided, when, and why
└── learner/                     your private workspace (created at setup)
```

## Principles

- Attempt before assistance: you always try first.
- Primary texts first; secondary sources test your reading.
- Nobody invents a quotation, citation, or position, and claims get checked against sources.
- No role writes your work; feedback diagnoses and asks questions.
- Honest grades, spoken defenses, and a record you own.

## Licensing and credits

The original content in this repository is under the [MIT License](LICENSE). Third-party materials keep their own licenses, which are recorded in the [materials catalog](materials/catalog.md).

The retrieval tool in `tools/retrieval/` is based on **[philosophy-mcp](https://github.com/sea9401/philosophy-mcp) by sea9401**, used under the MIT License. It keeps its original copyright notice in [tools/retrieval/LICENSE](tools/retrieval/LICENSE); this copy adds security hardening.

## Contributing

Fork the repository, make your changes, and open a pull request. Before committing, run:

    python3 tools/check_docs.py

It checks that internal links resolve, that the unit map and unit files agree, and that the layout above matches the files. CI runs the same check, plus a network-free check of the retrieval tool, on every push and pull request to `main`. Record design changes in [docs/decisions.md](docs/decisions.md).

## Disclaimer

This isn't an accredited program, and AI agents make mistakes. That's why the Verifier exists: check what matters.
