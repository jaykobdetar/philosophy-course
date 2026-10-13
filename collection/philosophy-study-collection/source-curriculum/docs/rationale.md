# Rationale

Why the project is designed the way it is. This is a condensed and corrected version of the research report the project started from. Every claim below that needs a source cites one from the list at the end. If you add a claim that needs a source and don't have one yet, mark it **[citation needed]**.

## What this is, and isn't

A self-directed philosophy education modeled on the philosophy part of a strong undergraduate major: breadth across history, value theory, metaphysics and epistemology, logic, and mind; repeated writing and oral defense; and an independent capstone. It isn't a degree. It can reproduce much of a major's content, exercises, and standards, but not accreditation, the judgment of human faculty, a seminar of peers, library privileges, or the rest of a bachelor's degree.

## What university programs suggest

Serious philosophy majors keep returning to the same core (history, value theory, metaphysics and epistemology, and logic) and then add specialization and substantial independent work:

- **Princeton** requires at least eight courses, six of them spread as two courses in each of three of its four areas (metaphysics; ethics and philosophy of value; logic and philosophy of science; history of philosophy), **plus** a junior independent work group, a junior paper, and a senior thesis [1][2].
- **Harvard's** basic concentration is 11 courses: one in each of four areas (logic; contemporary metaphysics and epistemology, broadly construed; contemporary ethics, political philosophy, and aesthetics; history of philosophy), two tutorials, and five further courses. A thesis of at most 20,000 words, examined orally by two readers, is required only on the honors track [16].
- **Brown** requires 10 courses, including one each in ancient philosophy, early modern philosophy, logic, epistemology or metaphysics, and ethics or political philosophy [17][18], plus a capstone: a senior thesis of typically 40–60 pages, a 15–25-page independent-study paper, or a special project [19].
- **MIT's** philosophy major requires, among other things, subjects in the history of philosophy and in logic and a topics seminar, plus a coherent program of five further subjects, two of them in philosophy [20].
- **UC San Diego** requires 15 courses, including two in logic and a three-course history sequence (ancient, early modern, late modern) taken in order [21].

This project's 15 units sit at the larger end of that range, because each subject gets a full course's worth of material rather than half of one. See the [unit map](../curriculum/map.md).

## How people learn, and what that means here

The design leans on a few well-established findings. Most of the evidence comes from general education research and cognitive science rather than from studies of philosophy teaching, and one study below is a single teacher's report, so read these as good reasons, not guarantees.

- **Critical thinking improves with instruction.** A meta-analysis of 117 studies with 20,698 participants found a positive average effect of critical-thinking instruction (g+ = 0.341), with the type of intervention and its pedagogical grounding accounting for about a third of the variation [22]. In philosophy teaching specifically, Twardy reports that computer-based argument mapping more than tripled the gains made by other methods in his courses [23]. Hence the constant reconstruction and counterexample work, and argument mapping in particular.
- **Retrieval beats rereading, and early success misleads.** Students who took recall tests on prose passages remembered substantially more two days or a week later than students who restudied, even though restudying did better on a test five minutes later and made students more confident [24]. Hence the review queue, and hence the confirmation check a few weeks after every gate.
- **Spacing beats cramming, and the best gap grows.** In a study of more than 1,350 people, the best gap before a review grew as the final test moved further away, while shrinking as a share of that delay: from about 20–40% of a one-week delay to about 5–10% of a one-year delay [25]. A meta-analysis of 317 experiments found the same interaction [26]. Hence review intervals that keep growing across the whole program.
- **Feedback should build the learner's own judgment.** Nicol and Macfarlane-Dick argue that feedback should help students take control of their own learning, and set out seven principles of good feedback practice on that basis [27]. Hence diagnosis-only feedback memos and required revision.

From these comes the project's central rule: difficulty before explanation. If a tutor explains a text before the learner has struggled with it, the learner gets the feeling of understanding without the skill. So the learner always attempts first.

## Why six roles

Different teaching jobs pull in different directions: a tutor should be supportive, an examiner impartial, a debate partner stubborn, a verifier sceptical. Separating the roles makes each job clearer, and once roles can run as separate agents, it makes grading independent of tutoring.

For now each person gets one primary dot; OpenAI says that more dots, and teams of dots, will come later [3]. A single dot carries its context across everything it does [3], and conversations with dots can feed into ChatGPT's memory [4], so for now role separation depends on discipline, and the Examiner grades in a separate session with memory off.

Dots can take voice calls [3], which is why oral exams and debates are spoken: typed answers can be drafted and polished, spoken ones can't.

Dots also do proactive research in the background [3]. That's useful for logistics, and harmful for learning if it produces interpretations of texts the learner hasn't tried yet, so only the Director may act unprompted, and only about logistics.

## Why the repository is the memory

Individual dot memories currently can't be viewed, edited, or deleted one by one. The way to clear them is to delete the dot, which removes its own context but leaves in place the conversations and files it created and any separate ChatGPT memories [4]. (The original report described this as "resetting" the dot and overstated what it deletes.) A mastery record that can't be inspected or corrected isn't a good record. So the record lives in plain files in the learner's private repository, where every change is visible, dated, and reversible, and the git history doubles as a progress log. This also keeps the curriculum independent of any one product's memory feature.

## Why private copies, and how

On GitHub, a fork shares its original's visibility, so every fork of a public repository is public [5][6], and when a public repository is made private, its existing forks stay public [7]. A learner's essays and grades therefore belong in a private copy made with GitHub's template feature, which starts the new repository from a single fresh commit and lets you choose its visibility [8]. The workspace folder is excluded from git until setup confirms the repository is private.

## Why materials work the way they do

Free to read isn't the same as free to redistribute. The Stanford Encyclopedia of Philosophy reserves the online distribution of its entries to itself [9], and publishes fixed quarterly editions for citation [10]. So SEP entries are read on demand, never stored, and cited by fixed edition. Open licenses vary too: *forall x: Calgary* is licensed CC BY 4.0 [11]; MIT OpenCourseWare requires non-commercial use and share-alike terms [12]; Open Yale Courses licenses most of its material CC BY-NC-SA 3.0, excluding third-party content [28]; and Early Modern Texts allows personal and classroom use but not commercial use [29], so its modernized versions are linked, never stored. Books are sourced by the learner, and the curriculum cites standard reference numbers so any good edition works. The [materials catalog](../materials/catalog.md) records the source and rights status of every reading.

A community MCP server, philosophy-mcp (MIT-licensed), already retrieves from the SEP, PhilPapers and PhilArchive, Project Gutenberg, Wikisource, the Internet Archive, and open-access book collections, and can search and page through a local PDF. Its directory listing marks it inactive [13]. The retrieval tool in `tools/retrieval/` is a security-hardened copy of it, credited to its author, sea9401. In ChatGPT, custom MCP servers are added as plugins in developer mode [14]; dots can use plugins set up in ChatGPT [4]; and a server has to be reachable over the web, either hosted or through OpenAI's secure tunnel [15]. The tool currently speaks MCP only over stdio, a local connection, so connecting it to ChatGPT or a dot still needs an HTTP transport or a bridge. PhilPapers' OAI-PMH handler is at api.philpapers.org [30], and its API keys are free [31]; in a live test the handler refused data queries without a key, so the Director helps each learner get one.

## Sources

All checked on 29 September 2026.

1. Princeton University, Undergraduate Announcement, "Philosophy." https://ua.princeton.edu/fields-study/departmental-majors-degree-bachelor-arts/philosophy
2. Princeton University Department of Philosophy, "Prospective Students." https://philosophy.princeton.edu/undergraduate/prospective-students
3. OpenAI, "Introducing dots" (29 September 2026). https://openai.com/index/introducing-dots/
4. OpenAI Help Center, "Dots privacy, security, and safety FAQs." https://help.openai.com/en/articles/20001529-dots-privacy-security-and-safety-faqs
5. GitHub Docs, "About forks." https://docs.github.com/articles/about-forks
6. GitHub Docs (Enterprise Server 3.17), "About permissions and visibility of forks." https://docs.github.com/en/enterprise-server@3.17/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks
7. GitHub Docs text on what happens to forks when a repository changes visibility, as quoted in github/docs issue #44520. https://github.com/github/docs/issues/44520
8. GitHub Docs (Enterprise Server 3.21), "Creating a repository from a template." https://docs.github.com/en/enterprise-server@3.21/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template
9. Stanford Encyclopedia of Philosophy, "Policy on Course Readers" (Summer 2026 archive). https://plato.stanford.edu/archives/sum2026/course-readers.html
10. Indiana University Libraries, description of the Stanford Encyclopedia of Philosophy. https://libraries.indiana.edu/node/278
11. *forall x: Calgary*. https://forallx.openlogicproject.org/
12. MIT Learn Help Center, "What are the requirements of use for MIT OpenCourseWare?" https://support.learn.mit.edu/hc/en-us/articles/42909882604315-What-are-the-requirements-of-use-for-MIT-OpenCourseWare
13. Glama MCP directory, "philosophy-mcp." https://glama.ai/mcp/servers/sea9401/philosophy-mcp (code: https://github.com/sea9401/philosophy-mcp)
14. OpenAI Developers, plugins quickstart. https://developers.openai.com/plugins/quickstart
15. OpenAI Developers, "Build an MCP server." https://developers.openai.com/plugins/build/mcp-server
16. Harvard University Department of Philosophy, "The Concentration." https://philosophy.fas.harvard.edu/concentration.md
17. Brown University Bulletin, "Philosophy." https://bulletin.brown.edu/the-college/concentrations/phil/
18. Brown University Department of Philosophy, "Concentration Requirements." https://philosophy.brown.edu/undergraduate/concentration-requirements
19. Brown University Department of Philosophy, "Senior Capstone." https://philosophy.brown.edu/undergraduate/senior-capstone
20. MIT Department of Linguistics and Philosophy, "Undergraduate." https://philosophy.mit.edu/undergraduate/
21. UC San Diego Department of Philosophy, "Philosophy Major." https://philosophy.ucsd.edu/undergraduate/philosophy-major.html
22. Abrami, P. C., Bernard, R. M., Borokhovski, E., Wade, A., Surkes, M. A., Tamim, R., and Zhang, D. (2008). "Instructional Interventions Affecting Critical Thinking Skills and Dispositions: A Stage 1 Meta-Analysis." *Review of Educational Research* 78(4): 1102–1134. https://doi.org/10.3102/0034654308326084
23. Twardy, C. R. (2004). "Argument Maps Improve Critical Thinking." *Teaching Philosophy* 27(2): 95–116. https://philarchive.org/rec/TWAAMI
24. Roediger, H. L., and Karpicke, J. D. (2006). "Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention." *Psychological Science* 17(3): 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x
25. Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., and Pashler, H. (2008). "Spacing Effects in Learning: A Temporal Ridgeline of Optimal Retention." *Psychological Science* 19(11): 1095–1102. https://doi.org/10.1111/j.1467-9280.2008.02209.x
26. Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., and Rohrer, D. (2006). "Distributed Practice in Verbal Recall Tasks: A Review and Quantitative Synthesis." *Psychological Bulletin*. https://www.evullab.org/pdf/CepedaPashlerVulWixtedRohrer-PB-2006.pdf
27. Nicol, D. J., and Macfarlane-Dick, D. (2006). "Formative Assessment and Self-Regulated Learning: A Model and Seven Principles of Good Feedback Practice." *Studies in Higher Education* 31(2): 199–218. https://doi.org/10.1080/03075070600572090
28. Open Yale Courses, "Terms of Use." https://oyc.yale.edu/terms
29. Early Modern Texts, "Rights." https://earlymoderntexts.com/faqs/rights
30. PhilPapers, "OAI-PMH access." https://philpapers.org/help/oai.html
31. PhilPapers, "API documentation" (JSON API, including where to obtain a free API key). https://philpapers.org/help/api/json.html
