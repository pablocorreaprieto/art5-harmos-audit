# Search log of ART 5

Every literature search made for the study, with what was opened, what was blocked and the conclusion
within what was opened (protocol rule 4, bounded novelty). Copied from the Recherches tab of the project
journal; the P2 searches of 1.11.2026 follow the P0 searches of 25.10.2026.

## P0, 25 October 2026 (main session, claude-opus-5-5, and its subagents)

| Tool | Exact query | Opened | Blocked | Stopped | Conclusion within what was opened |
|---|---|---|---|---|---|
| Scite | "large language models" AND readability AND children AND "text generation" | none | Scite, tool refused without subscription | yes, connector refused | No conclusion possible |
| Elicit | Do large language models generate reading texts at the requested school grade level for children? | none | Elicit, plan without API access | yes, connector refused | No conclusion possible |
| Consensus | large language models generate reading passages at target grade level readability evaluation | 10 abstracts | first try refused by the rate limit, rerun | no | Work in English on US grades, mostly medical documents (Bezirhan et al. 2023, Patel et al. 2023). None on French or HarmoS among the 10 |
| Consensus | ChatGPT generated texts readability adapted to children age or education level | 10 abstracts | | no | Murgia et al. 2023, Spina et al. 2024, Nguyen 2026 (CEFR), Karaca 2024 (Turkish). None on French-language grade labels among the 10 |
| Consensus | French readability of texts for primary school children grade level lexical frequency | none | Consensus, rate limit | yes, not rerun | No conclusion |
| alphaXiv | keywords readability, grade level, LLM; question on generating or adapting texts at a requested grade or age | 14 titles and abstract openings | | no | EduAdapt, difficulty-controlled children's stories, Arabic CEFR, LLM readability rating. None on French as a first language in primary school |
| alphaXiv | keywords French, readability; question on French readability assessment or controlled generation with LLMs | 15 titles and abstract openings | | no | FRENCH-YMCA (youth corpus), English-French simplification, LLM-rated readability. No generation for primary grades |
| alphaXiv | keywords grade level, school system, LLM; question on how non-US grade labels are interpreted (Year, CP to CM2, HarmoS) | 14 titles and abstract openings | | no | Oh et al. 2026 (US grades), K-12 standards, cultural adaptation of problems. No work on how non-US grade labels are read |
| Web search | LLM generated reading passages target grade level accuracy evaluation study | 9 links (titles) | | no | Nothing on French or HarmoS in the titles |
| Web search | ChatGPT texte de lecture niveau scolaire lisibilité élèves primaire étude | 9 links (titles) | | no | Murgia et al. 2023 and work in English, no French-language study in primary school in the titles |
| Web search | HarmoS "IA générative" textes de lecture élèves degré enseignants Suisse romande | 9 links (titles) | | no | Administrative documents on HarmoS, no study on AI |
| Web search | "IA générative" OR ChatGPT "textes adaptés" élèves lisibilité français étude 2025 génération de textes niveau CP CE1 | 9 links (titles) | | no | TraAM sheet (Nancy-Metz), VALS-ASLA bulletin (French as a foreign language), no study of grade labels |
| Web search | LLM grade level labels different countries school year naming "Year 5" "5th grade" readability mismatch study | 9 links (titles) | | no | Oh et al. 2026 and Huang et al. 2024, nothing on non-US grade systems |
| Web search | HarmoS grade "LLM" OR "ChatGPT" Swiss school grade labels "5H" OR "3H" generated texts | 9 links (titles) | | no | No result on HarmoS |
| Web search | génération de textes ChatGPT lisibilité élèves primaire Québec "1re année" OR "2e année" étude textes générés difficulté | 9 links (titles) | | no | No study on primary grades |

Other P0 searches (journals, model lists, Lexique, Manulex, HarmoS, Vikidia licence) are in the journal's Recherches tab; they bear on the design, not on novelty.

## P2, 1 November 2026

The reading session's own log follows unchanged (131 tool calls, Annex E format of the protocol). The main session also read three web pages on 1 November 2026, logged in the Recherches tab of the journal: education.gouv.fr, « L'école élémentaire » and « Le collège », and fr.vikidia.org, « Vikidia:À propos ».

Internal reading by a separate AI session. Not peer review.

### Search and reading log of the reading session (claude-sonnet-5-5, 1 November 2026)

All entries date from 2026-11-01. Entry numbers follow the order of tool calls; the numbers are only for cross-reference (calls that only read or wrote local files, ran local scripts or loaded tool definitions are not logged). "Query" is the exact search string for searches; for direct reading it names the address read. "Opened" means the tool returned text from that target; "result list only" means I saw titles and addresses but opened nothing from that search. Where a tool returned a machine summary instead of raw text (WebFetch), the entry says so.

1. Query: "dois = 10.1007/s40593-025-00520-7, 10.1111/bjet.13554, 10.1111/jcal.12776, 10.1007/s11145-025-10676-2, 10.1007/s11145-023-10493-5"   Date: 2026-11-01   Tool: Scite search_literature
   Opened: nothing
   Blocked: Scite refused: "MCP tools require a paid scite plan or an active free trial"
   Stopped: yes (connector refused: a paid scite plan is required)
   Conclusion: Scite could not be used; no record retrieved.

2. Query: "(direct read) https://arxiv.org/abs/2312.02065"   Date: 2026-11-01   Tool: alphaXiv get_paper_content (full text)
   Opened: Rooein et al., arXiv 2312.02065, full text
   Blocked: none
   Stopped: no
   Conclusion: Full text read; see rooein2023.

3. Query: "Rooein Cercas Curry Hovy "Know Your Audience" LLMs adapt to different age and education levels"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed arXiv, ar5iv and paperswithcode copies of the Rooein et al. preprint; none opened from this search (full text read in #2).

4. Query: "Oh Whang Evans Wang 2026 large language models generate texts "grade 3" students readability above target grade level"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed arXiv copies of the Oh et al. preprint (2601.06225), a Stanford SCALE page and papers on readability-controlled generation; the preprint was read in #6.

5. Query: "Nguyen 2026 LLM-generated texts CEFR levels large language models generate reading texts proficiency level accuracy"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed papers on CEFR-controlled text generation (a German-as-a-foreign-language study, an EMNLP Findings paper, others); no listed title was Nguyen (2026); the Thai teacher-guide record was opened in #8.

6. Query: "(direct read) https://arxiv.org/abs/2601.06225"   Date: 2026-11-01   Tool: alphaXiv get_paper_content (full text)
   Opened: Oh et al., arXiv 2601.06225 v2, full text (60 KB, read from the saved file)
   Blocked: none
   Stopped: no
   Conclusion: Full text of the arXiv v2 read; see oh2026.

7. Query: "(direct read) https://arxiv.org/abs/2406.12787"   Date: 2026-11-01   Tool: alphaXiv get_paper_content (full text)
   Opened: Huang, Wei & Huang, arXiv 2406.12787, full text
   Blocked: none
   Stopped: no
   Conclusion: Full text read; see huang2024.

8. Query: "(direct fetch) https://so04.tci-thaijo.org/index.php/LEARN/article/view/291541"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: so04.tci-thaijo.org record "Constructing CEFR-Aligned English Reading Assessments with AI" (Thai teachers, higher education)
   Blocked: none
   Stopped: no
   Conclusion: Record read; far from ART 5 and not used.

9. Query: "Watanabe ChatGPT, can you make this text easier? text simplification"   Date: 2026-11-01   Tool: Consensus search
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Ten Consensus records on text simplification; "Watanabe" does not occur in the result; the exact-title query in #114 found the record.

10. Query: "(direct read) https://doi.org/10.1007/s40593-025-00520-7; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv "completed with no output" for the Springer DOI of Watanabe (2025)
   Stopped: no
   Conclusion: No text obtained.

11. Query: "Nguyen large language models generate reading texts at CEFR levels English learners evaluation"   Date: 2026-11-01   Tool: Consensus search [year_min=2025]
   Opened: Consensus result list (10 records, year_min=2025); record [8] gives the abstract of Nguyen (2026)
   Blocked: none
   Stopped: no
   Conclusion: Abstract of Nguyen (2026) seen in record [8]; abstract-only (nguyen2026).

12. Query: ""Lexical Profile of ChatGPT-generated Reading Materials Targeting EFL Learners Across the CEFR Levels" Nguyen International Journal of TESOL Studies"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: No listed title was Nguyen (2026).

13. Query: "(direct fetch) https://link.springer.com/article/10.1007/s40593-025-00520-7"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: WebFetch client_error on link.springer.com/article/10.1007/s40593-025-00520-7
   Stopped: no
   Conclusion: Watanabe (2025) article page not read.

14. Query: ""Classroom AI: Large Language Models as Grade-Specific Teachers" npj Artificial Intelligence 2026"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed only arXiv copies of the preprint and aggregator pages, no journal page; the npj Artificial Intelligence record was found through Crossref in #40.

15. Query: "(direct fetch) https://arxiv.org/abs/2312.02065"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: arXiv abstract page of Rooein et al. (WebFetch extraction)
   Blocked: none
   Stopped: no
   Conclusion: Only v1 (2023-12-04) listed; no journal reference shown.

16. Query: "(direct fetch) https://api.openalex.org/works?filter=doi:10.1007/s40593-025-00520-7|10.1111/bjet.13554|10.1111/jcal.12776|10.1007/s11145-025-10676-2|10.1007/s11145-023-10493-5&select=doi,title,publication_year,open_access,best_oa_location"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: WebFetch client error on api.openalex.org
   Stopped: no
   Conclusion: No OpenAlex data for the five DOIs.

17. Query: "(direct fetch) https://api.crossref.org/works/10.1007/s40593-025-00520-7"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref record 10.1007/s40593-025-00520-7 (WebFetch extraction)
   Blocked: none
   Stopped: no
   Conclusion: Gave title, one author (Micah Watanabe), IJAIED 35(6) pp. 3922-3942; no abstract in the record.

18. Query: "(direct fetch) https://api.crossref.org/works/10.1111/bjet.13554"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref record 10.1111/bjet.13554
   Blocked: none
   Stopped: no
   Conclusion: Gave authors, BJET 56(3) 1092-1117, issued 2024-12-13; abstract only as a summary.

19. Query: "(direct fetch) https://api.crossref.org/works/10.1111/jcal.12776"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref record 10.1111/jcal.12776
   Blocked: none
   Stopped: no
   Conclusion: Gave authors, JCAL 39(3) 804-822, issued 2023-01-23.

20. Query: "(direct fetch) https://api.crossref.org/works/10.1007/s11145-025-10676-2"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref record 10.1007/s11145-025-10676-2
   Blocked: none
   Stopped: no
   Conclusion: Gave five authors, Reading and Writing, issued 2025-06-24; no volume or pages.

21. Query: "(direct fetch) https://api.crossref.org/works/10.1007/s11145-023-10493-5"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref record 10.1007/s11145-023-10493-5
   Blocked: none
   Stopped: no
   Conclusion: Gave Mesmer, Reading and Writing 38(1) 1-35, issued 2024-01-02; no abstract in the record.

22. Query: "(direct fetch) https://doi.org/10.1007/s40593-025-00520-7"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: doi.org/10.1007/s40593-025-00520-7 returned a redirect that the tool did not follow
   Stopped: no
   Conclusion: Nothing read.

23. Query: "(direct read) https://link.springer.com/content/pdf/10.1007/s40593-025-00520-7.pdf; 2 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on link.springer.com/content/pdf/...s40593-025-00520-7.pdf: "JavaScript is disabled" wall
   Stopped: no
   Conclusion: Watanabe (2025) PDF not read.

24. Query: "(direct fetch) https://link.springer.com/article/10.1007/s11145-023-10493-5"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Springer page of Mesmer (2024) via WebFetch: abstract and front matter only
   Blocked: none
   Stopped: no
   Conclusion: Paywalled ("preview of subscription content"); abstract-only (mesmer2024).

25. Query: "(direct fetch) https://onlinelibrary.wiley.com/doi/full/10.1111/jcal.12776"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: WebFetch client_error on onlinelibrary.wiley.com (Patel et al.)
   Stopped: no
   Conclusion: Wiley page not read.

26. Query: "(direct fetch) https://bera-journals.onlinelibrary.wiley.com/doi/full/10.1111/bjet.13554"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: WebFetch client_error on bera-journals.onlinelibrary.wiley.com (Li et al.)
   Stopped: no
   Conclusion: Wiley page not read.

27. Query: "(direct fetch) https://linkinghub.elsevier.com/retrieve/pii/S1560429226000892"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: linkinghub.elsevier.com page returned empty content
   Stopped: no
   Conclusion: Nothing read.

28. Query: ""Are simpler math stories better" automatic readability assessment GAI-generated multimodal mathematical stories validated by engagement"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: No listed title was an open full text of Li et al. (2024); nothing opened from this search.

29. Query: ""Improving mathematics assessment readability: Do large language models help?" Patel Lomas GPT-3 EngageNY pdf"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed the TU Delft repository record and file of Patel et al.; both were opened later (#33, #36).

30. Query: ""Does ChatGPT simplify texts like expert teachers? Linguistic features of simplified texts" Liu Lu Jin Kang Zhang"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed Penn State and City University of Hong Kong records of Liu et al. (2025); the Penn State record was opened in #34.

31. Query: ""Exploring the frequency contours in close reading texts" Mesmer Reading and Writing"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: No listed title was an open full text of Mesmer (2024); nothing opened from this search (the Springer preview page was opened in #24).

32. Query: "(direct read) https://repository.tudelft.nl/file/File_4b7e60bb-6c73-464b-9af1-288a4b24659f; 4 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on the TU Delft repository file: "The user aborted a request"
   Stopped: no
   Conclusion: Patel et al. raw text not obtained.

33. Query: "(direct fetch) https://repository.tudelft.nl/record/uuid:2c99d723-5903-4f39-b2bf-feb40daf3ec7"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: TU Delft repository record of Patel et al. (WebFetch)
   Blocked: none
   Stopped: no
   Conclusion: Record says final published version, embargo expired 2023-07-01; no licence listed.

34. Query: "(direct fetch) https://pure.psu.edu/en/publications/does-chatgpt-simplify-texts-like-expert-teachers-linguistic-featu/"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Penn State pure record of Liu et al. (WebFetch)
   Blocked: none
   Stopped: no
   Conclusion: Abstract only; no full-text file.

35. Query: "(direct read) https://repository.tudelft.nl/file/File_4b7e60bb-6c73-464b-9af1-288a4b24659f; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on the TU Delft repository file, second attempt: "The user aborted a request"
   Stopped: no
   Conclusion: Patel et al. raw text not obtained.

36. Query: "(direct fetch) https://repository.tudelft.nl/file/File_4b7e60bb-6c73-464b-9af1-288a4b24659f"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: TU Delft PDF of Patel et al. through the WebFetch extractor
   Blocked: none
   Stopped: no
   Conclusion: Extractor returned headings, numbers and limitations; label full-text-extracted, not read-directly (patel2023).

37. Query: "(direct read) https://aclanthology.org/2023.gem-1.18.pdf; 1 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: ACL Anthology PDF 2023.gem-1.18 (Imperial & Tayyar Madabushi), raw pages
   Blocked: none
   Stopped: no
   Conclusion: Pages 205-206, 208-212, 218-220 read; see imperial2023.

38. Query: "(direct fetch) https://api.crossref.org/works?query.title=Classroom+AI+Large+Language+Models+as+Grade-Specific+Teachers&rows=3&select=DOI,title,container-title,volume,issue,article-number,issued,author,license,link"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: WebFetch RATE_LIMIT_EXCEEDED (two Crossref fetches in parallel)
   Stopped: no (retried singly in #40)
   Conclusion: Retried singly in #40.

39. Query: "(direct fetch) https://api.crossref.org/works?query.title=Lexical+Profile+of+ChatGPT-generated+Reading+Materials+Targeting+EFL+Learners+Across+the+CEFR+Levels&rows=3&select=DOI,title,container-title,volume,issue,article-number,page,issued,author,license,link,URL"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: WebFetch RATE_LIMIT_EXCEEDED (two Crossref fetches in parallel)
   Stopped: no (retried singly in #41)
   Conclusion: Retried singly in #41.

40. Query: "(direct fetch) https://api.crossref.org/works?query.title=Classroom+AI+Large+Language+Models+as+Grade-Specific+Teachers&rows=3&select=DOI,title,container-title,volume,issue,article-number,issued,author,license,link"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref title query for "Classroom AI"
   Blocked: none
   Stopped: no
   Conclusion: Gave DOI 10.1038/s44387-026-00081-7, npj Artificial Intelligence, article 28.

41. Query: "(direct fetch) https://api.crossref.org/works?query.title=Lexical+Profile+of+ChatGPT-generated+Reading+Materials+Targeting+EFL+Learners+Across+the+CEFR+Levels&rows=2&select=DOI,title,container-title,volume,issue,article-number,page,issued,author,license,link,URL"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref title query for Nguyen (2026)
   Blocked: none
   Stopped: no
   Conclusion: Top hit was unrelated ("Complete Dental Cleaning"); no Crossref match for Nguyen.

42. Query: "Nhat Nguyen ChatGPT-generated texts six CEFR levels A1 to C2 lexical profile RANGE BNC/COCA 25,000 word family lists extensive reading"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: No listed title was Nguyen (2026).

43. Query: "(direct fetch) https://ijts.org/ojs/index.php/ijts/issue/archive"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: WebFetch PROVENANCE_REQUIRED on ijts.org archive
   Stopped: yes (fetch permission request not answered; not retried)
   Conclusion: Journal site not read.

44. Query: ""Lexical Profile of ChatGPT-generated Reading Materials""   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: No listed title was Nguyen (2026).

45. Query: "(direct fetch) https://consensus.app/papers/details/f1f895a93d515d0a8048d67ac0dfb2eb/?utm_source=claude_desktop"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: WebFetch PROVENANCE_REQUIRED on consensus.app record
   Stopped: yes (fetch permission request not answered; not retried)
   Conclusion: Not read.

46. Query: "International Journal of TESOL Studies 2026 ChatGPT generated reading materials CEFR A1 C2 lexical profile Nguyen "extensive reading" high-frequency words"   Date: 2026-11-01   Tool: WebSearch (standard) [allowed_domains: ijts.org, tesolijts.org, ijts-journal.com, researchgate.net, scholar.google.com, doi.org]
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed other studies on CEFR-level text generation (a ResearchGate copy of a ChatGPT-4o and CEFR study, an MDPI paper); no listed title was Nguyen (2026).

47. Query: ""ChatGPT-generated texts for the A1 and A2 levels require the same vocabulary sizes as those targeting the B1 level""   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: An exact-sentence search from the abstract returned unrelated papers; no listed title was Nguyen (2026).

48. Query: "Ripoll y Schmitz Sonnleitner GPT-4 reading texts Luxembourg Large-scale Assessments in Education 2025"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed the library.kab.ac.ug record of the Ripoll y Schmitz and Sonnleitner article and an orbilu.uni.lu record; both were opened (#51, #52).

49. Query: "Watanabe "ChatGPT, Can You Make this Text Easier?" Investigating the Utility of LLMs in Easing Text Readability"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed the Trott and Rivière preprint and related readability papers; no listed title was Watanabe (2025).

50. Query: "(direct read) ChatGPT, Can You Make this Text Easier? Investigating the Utility of LLMs in Easing Text Readability; 1 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv: "No exact title match" for Watanabe (2025) in its index
   Stopped: no
   Conclusion: No text obtained.

51. Query: "(direct fetch) https://orbilu.uni.lu/handle/10993/66460"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: orbilu.uni.lu record 10993/66460 (Luxembourg low achievers and assessment)
   Blocked: none
   Stopped: no
   Conclusion: Record read; not used.

52. Query: "(direct fetch) https://library.kab.ac.ug/Record/doaj-art-15ff8a051c954d81aa352e212018fba3/Description"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: library.kab.ac.ug DOAJ-style record of the Ripoll article (WebFetch)
   Blocked: none
   Stopped: no
   Conclusion: Gave metadata and abstract of the Ripoll article.

53. Query: "(direct fetch) https://doi.org/10.1186/s40536-025-00255-w"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: doi.org/10.1186/s40536-025-00255-w returned a redirect that the tool did not follow
   Stopped: no
   Conclusion: Followed by #54.

54. Query: "(direct fetch) https://link.springer.com/article/10.1186/s40536-025-00255-w?code=53feafd8-d522-48e6-a69c-96d649864b05&error=cookies_not_supported"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Springer HTML page of Ripoll article (WebFetch, truncated at 100,000 characters)
   Blocked: none
   Stopped: no
   Conclusion: Section outline only.

55. Query: "(direct read) https://link.springer.com/content/pdf/10.1186/s40536-025-00255-w.pdf; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: Springer PDF of the Ripoll article via alphaXiv, raw pages
   Blocked: none
   Stopped: no
   Conclusion: PDF pages 1, 6, 13, 14, 16-19, 21-24 read; see ripoll2025.

56. Query: "(direct read) https://link.springer.com/content/pdf/10.1186/s40536-025-00255-w.pdf; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on the same PDF: JavaScript error page
   Stopped: no
   Conclusion: Appendix A and limitations pages not obtained.

57. Query: "(direct read) https://link.springer.com/content/pdf/10.1186/s40536-025-00255-w.pdf; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on the same PDF, second try: JavaScript error page
   Stopped: no
   Conclusion: Appendix A and limitations pages not obtained.

58. Query: "New Pallier Brysbaert Ferrand 2004 "Lexique 2: A new French lexical database" Behavior Research Methods Instruments Computers pdf"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed typeset.io, HAL, scholarhub.vn, Springer and lexique.org README pages for Lexique 2; the typeset.io and HAL copies were tried in #65 and #77 (blocked).

59. Query: "New Brysbaert Véronis Pallier 2007 "The use of film subtitles to estimate word frequencies" Applied Psycholinguistics pdf"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed the HAL copy of New et al. (2007), the lexique.org README and other SUBTLEX papers; the HAL copy was tried in #63 and #76 (blocked).

60. Query: "van Heuven Mandera Keuleers Brysbaert 2014 "SUBTLEX-UK" new and improved word frequency database British English Zipf scale pdf"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed Nottingham eprints, Tilburg, worktribe, informahealthcare and a cendekia.unisza.edu.my catalogue record for SUBTLEX-UK; Tilburg and worktribe were opened in #71 and #70; the unisza record was opened later (#131) and only points back to the Nottingham eprints page.

61. Query: "Lété Sprenger-Charolles Colé 2004 "MANULEX" grade-level lexical database from French elementary school readers"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed Manulex pages (HAL, Springer, core.ac.uk); the Springer PDF was read in #66.

62. Query: "(direct read) https://link.springer.com/content/pdf/10.3758/BF03193029.pdf; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: Springer PDF BF03193029, raw pages
   Blocked: none
   Stopped: no
   Conclusion: The file appeared in the results of the Lexique 2 queries (#58, #61) but is Manulex-infra (Peereman et al., 2007), not Lexique 2; see peereman2007.

63. Query: "(direct read) https://hal.archives-ouvertes.fr/hal-02327556; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on hal.archives-ouvertes.fr/hal-02327556: Anubis bot check
   Stopped: no
   Conclusion: New et al. (2007) HAL copy not read.

64. Query: "(direct read) https://nottingham-repository.worktribe.com/OutputFile/721857; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on nottingham-repository.worktribe.com/OutputFile/721857: "Failed to fetch"
   Stopped: no
   Conclusion: SUBTLEX-UK PDF not read.

65. Query: "(direct read) https://typeset.io/pdf/lexique-2-a-new-french-lexical-database-2afvuxy0ew.pdf; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on typeset.io PDF of Lexique 2: JavaScript wall
   Stopped: no
   Conclusion: Lexique 2 text not read.

66. Query: "(direct read) https://link.springer.com/content/pdf/10.3758%2FBF03195560.pdf; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: Springer PDF 10.3758/BF03195560 (Manulex), raw pages
   Blocked: none
   Stopped: no
   Conclusion: Journal pages 156-162 and Appendix p. 165 read; see manulex2004.

67. Query: "(direct fetch) https://eprints.nottingham.ac.uk/2947/"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: WebFetch on eprints.nottingham.ac.uk/2947: redirect not followed
   Stopped: no
   Conclusion: Nothing read.

68. Query: "(direct read) https://informahealthcare.com/doi/full/10.1080/17470218.2013.850521; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on informahealthcare.com full text of SUBTLEX-UK: "Failed to fetch"
   Stopped: no
   Conclusion: SUBTLEX-UK not read.

69. Query: "(direct fetch) https://repository.nottingham.ac.uk/lucky-search?index=eprints-id&value=2947"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: WebFetch PROVENANCE_REQUIRED on repository.nottingham.ac.uk
   Stopped: yes (fetch permission request not answered; not retried)
   Conclusion: Nothing read.

70. Query: "(direct fetch) https://nottingham-repository.worktribe.com/output/721845"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Nottingham worktribe record 721845 (WebFetch)
   Blocked: none
   Stopped: no
   Conclusion: Metadata only; no PDF link.

71. Query: "(direct fetch) https://research.tilburguniversity.edu/en/publications/subtlex-uk-a-new-and-improved-word-frequency-database-for-british/"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Tilburg University research record of SUBTLEX-UK (WebFetch)
   Blocked: none
   Stopped: no
   Conclusion: Gave volume 67(6), pages 1176-1190 and DOI; no PDF.

72. Query: "Zipf scale "log10" frequency per billion words van Heuven 2014 SUBTLEX-UK "Zipf value" low-frequency 1-3 high-frequency 4-7 pdf"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed Nottingham worktribe and eprints, Tilburg, informahealthcare and unisza records of SUBTLEX-UK and the manuscript read in #74; no full text of van Heuven et al. (2014) was among the items I opened (the unisza record was opened in #131).

73. Query: ""film subtitles" word frequencies New Brysbaert Veronis Pallier 2007 Applied Psycholinguistics 28 661 French subtitles Lexique 3 freqfilms"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed other SUBTLEX papers (Chinese, Dutch), pylexique pages and a benjamins.com page; no listed title was an open copy of New et al. (2007).

74. Query: "(direct read) https://corpus.bfsu.edu.cn/__local/0/84/0F/24FF5CC649F50D785B3D1E51668_DA765091_22183.pdf?e=.pdf; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: Accepted manuscript of Brysbaert, Mandera & Keuleers (corpus.bfsu.edu.cn copy), raw pages
   Blocked: none
   Stopped: no
   Conclusion: Zipf definition and frequency-effect passages read; see brysbaert2018.

75. Query: "(direct fetch) https://lexique.org/databases/Lexique400/README-Lexique.txt"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: lexique.org README of Lexique 4.00 (WebFetch extraction)
   Blocked: none
   Stopped: no
   Conclusion: README is for version 4.00 (2026), not 3.83; not used for 3.83 claims.

76. Query: "(direct read) https://hal.science/hal-02327556/document; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on hal.science/hal-02327556/document: Anubis bot check (German)
   Stopped: no
   Conclusion: New et al. (2007) HAL copy not read.

77. Query: "(direct read) https://hal.science/hal-02341287/document; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on hal.science/hal-02341287/document: "The user aborted a request"
   Stopped: no
   Conclusion: Lexique 2 HAL copy not read.

78. Query: "The use of film subtitles to estimate word frequencies New Brysbaert Veronis Pallier"   Date: 2026-11-01   Tool: WebSearch (standard) [allowed_domains: core.ac.uk, semanticscholar.org, researchgate.net, cambridge.org, lexique.org, crr.ugent.be, psycnet.apa.org, europepmc.org]
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed the Cambridge abstract page of New et al. (2007) and ResearchGate or Semantic Scholar pages of other SUBTLEX papers; only the Cambridge page was opened later (#85).

79. Query: "Lexique 2 A new French lexical database New Pallier Brysbaert Ferrand 2004 full text"   Date: 2026-11-01   Tool: WebSearch (standard) [allowed_domains: core.ac.uk, semanticscholar.org, researchgate.net, springer.com, lexique.org, crr.ugent.be, europepmc.org, hal.science]
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed Semantic Scholar, ResearchGate and HAL pages for Lexique 2; none was readable (#77, #81).

80. Query: "(direct read) https://lexique.org/_documentation/Manuel_Lexique.3.2.pdf; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: lexique.org Manuel_Lexique.3.2.pdf, raw pages
   Blocked: none
   Stopped: no
   Conclusion: PDF pages 1-15, 17, 21-23 read; see lexique3manual.

81. Query: "(direct read) https://www.semanticscholar.org/paper/Lexique-2-:-A-new-French-lexical-database-New-Pallier/a047888622c576ccf06a7708ae18a5d9ec5f09fd; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on a Semantic Scholar page: schema error (no pdfUrl)
   Stopped: no
   Conclusion: Nothing read.

82. Query: "(direct fetch) https://api.crossref.org/works?query.bibliographic=Lexique+2+A+new+French+lexical+database+New+Pallier+Brysbaert+Ferrand+2004&rows=2&select=DOI,title,container-title,volume,issue,page,issued,author"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: WebFetch client error on a Crossref query.bibliographic URL
   Stopped: no
   Conclusion: Retried with query.title in #83.

83. Query: "(direct fetch) https://api.crossref.org/works?query.title=Lexique+2+A+new+French+lexical+database&rows=3&select=DOI,title,container-title,volume,issue,page,issued,author"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref title query for "Lexique 2: A new French lexical database"
   Blocked: none
   Stopped: no
   Conclusion: Gave DOI 10.3758/BF03195598; the 2004 paper is titled "Lexique 2".

84. Query: "(direct fetch) https://api.crossref.org/works?query.title=The+use+of+film+subtitles+to+estimate+word+frequencies&rows=3&select=DOI,title,container-title,volume,issue,page,issued,author,abstract"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref title query for New et al. (2007)
   Blocked: none
   Stopped: no
   Conclusion: Gave DOI 10.1017/S014271640707035X, Applied Psycholinguistics 28(4) 661-677.

85. Query: "(direct fetch) https://www.cambridge.org/core/journals/applied-psycholinguistics/article/abs/use-of-film-subtitles-to-estimate-word-frequencies/12CECAD298CF0875EAA5EEB69B470E8B"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Cambridge Core abstract page of New et al. (2007) (WebFetch)
   Blocked: none
   Stopped: no
   Conclusion: Abstract read; full text paywalled (new2007_subtitles).

86. Query: "(direct fetch) https://api.crossref.org/works?query.title=The+word+frequency+effect+in+word+processing+An+updated+review&rows=2&select=DOI,title,container-title,volume,issue,page,issued,author"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref title query for Brysbaert et al. (2018)
   Blocked: none
   Stopped: no
   Conclusion: Gave DOI 10.1177/0963721417727521, Current Directions in Psychological Science 27(1) 45-50.

87. Query: "Accord intercantonal sur l'harmonisation de la scolarité obligatoire (concordat HarmoS) 14 juin 2007 article 5 âge d'entrée école quatre ans révolus 31 juillet"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed copies of the accord at ne.ch, lexfind.ch, CEFAN (Laval), silgeneve.ch and fr.lexwork.naz.ch, plus court decisions; copies were tried in #89 to #94.

88. Query: "Vaud école obligatoire degrés 1P-8P 9S-11S HarmoS années scolaires désignation"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed Vaud government pages (vd.ch), including the page on the course of compulsory schooling, which was read in #95.

89. Query: "(direct fetch) https://www.lexfind.ch/tolv/136548/fr"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: lexfind.ch text of the HarmoS accord (WebFetch extraction)
   Blocked: none
   Stopped: no
   Conclusion: Extractor gave the document title and date, Art. 5 al. 1 and Art. 6; confirmed word for word by the raw texts in #93 and #94.

90. Query: "(direct read) (none); 2 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: Call rejected: required argument "paper" missing
   Stopped: no
   Conclusion: Nothing retrieved; my error.

91. Query: "(direct read) https://silgeneve.ch/legis/data/rsg/rsg_c1_06.pdf; 2 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on silgeneve.ch/legis/data/rsg/rsg_c1_06.pdf: "Failed to fetch"
   Stopped: no
   Conclusion: Geneva copy of the accord not read.

92. Query: "(direct read) https://www.ne.ch/autorites/DFDS/SEEO/projets/Documents/14_brochure_harmos.pdf; 2 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on the Neuchâtel brochure URL returned the SEEO web page, not the brochure (75 KB, no HarmoS text)
   Stopped: no
   Conclusion: No accord text obtained from this URL.

93. Query: "(direct read) https://fr.lexwork.naz.ch/fr/dta/416.2.pdf; 2 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: fr.lexwork.naz.ch file 416.2 (HarmoS accord, 7 pages, Fribourg legislation database), raw text
   Blocked: none
   Stopped: no
   Conclusion: Art. 4 to 6 and the entry-into-force note for Fribourg (1.5.2010) read; see harmos2007.

94. Query: "(direct read) https://axl.cefan.ulaval.ca/EtatsNsouverains/suisse-accord_intercantonal2007.htm; 2 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: CEFAN (Université Laval) copy of the HarmoS accord, raw text
   Blocked: none
   Stopped: no
   Conclusion: Same wording as #93, plus a signature and entry-into-force note.

95. Query: "(direct read) https://www.vd.ch/formation/enseignement-obligatoire-et-pedagogie-specialisee/deroulement-de-lecole-obligatoire-dans-le-canton-de-vaud/; 2 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: vd.ch page "Déroulement de l'école obligatoire dans le canton de Vaud", raw text
   Blocked: none
   Stopped: no
   Conclusion: 1P-4P, 5P-8P, 9S-11S and ages read; see vd_deroulement.

96. Query: "ge.ch enseignement primaire Genève 1P 8P degrés cycle élémentaire cycle moyen 5P 6P âge des élèves"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed Geneva pages (ge.ch), including "Bienvenue à l'école primaire", which was read in #99.

97. Query: "fr.ch école obligatoire canton de Fribourg 1H 2H 3H 4H 5H 6H 7H 8H cycle 1 cycle 2 degré primaire"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed Fribourg pages (fr.ch) on cycles 1 to 3; the overview and cycle 2 pages were read in #98 and #102.

98. Query: "(direct read) https://www.fr.ch/formation-et-ecoles/scolarite-obligatoire/ecoles-la-formation-dans-le-canton-de-fribourg; 1 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: fr.ch page "Ecoles - la formation dans le canton de Fribourg", raw text
   Blocked: none
   Stopped: no
   Conclusion: Eleven years, three cycles, entry at 4; see fr_cycle2.

99. Query: "(direct read) https://www.ge.ch/node/11636; 1 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: ge.ch/node/11636 "Bienvenue à l'école primaire", raw text
   Blocked: none
   Stopped: no
   Conclusion: 1P-4P and 5P-8P with ages read; see ge_primaire.

100. Query: "Plan d'études romand PER cycle 1 (1H-4H) cycle 2 (5H-8H) cycle 3 (9H-11H) CIIP plandetudes.ch"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed CIIP and edudoc PDFs of the PER and Fribourg and Vaud pages; the edudoc PDFs were tried in #101 and #105 (blocked).

101. Query: "(direct read) https://edudoc.ch/record/104591/files/cycle_2_webCIIP.pdf; 2 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on edudoc.ch cycle_2_webCIIP.pdf: bot check ("JavaScript is disabled")
   Stopped: no
   Conclusion: CIIP cycle 2 brochure not read.

102. Query: "(direct read) https://www.fr.ch/dics/formation-et-ecoles/4-15-ans/ecole-obligatoire-organisation-et-deroulement-cycle-2; 1 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: fr.ch page "Organisation et déroulement, Cycle 2", raw text
   Blocked: none
   Stopped: no
   Conclusion: 1H-11H, 5H, ages 8 to 12 read; see fr_cycle2.

103. Query: "PER Plan d'études romand "1H" "1P" correspondance dénomination années HarmoS cantons romands Vaud Genève Valais Neuchâtel Jura équivalence 5H 5P"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Result list only; no listed title was opened from this search to look for a statement of the 5H and 5P equivalence (the edudoc PER report was tried in #105, blocked).

104. Query: "(direct read) https://www.vd.ch/formation/enseignement-obligatoire-et-pedagogie-specialisee/deroulement-de-lecole-obligatoire-dans-le-canton-de-vaud/plan-detudes-romand-per; 1 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: vd.ch page "Plan d'études romand (PER)", raw text
   Blocked: none
   Stopped: no
   Conclusion: One-sentence description of the PER read; see vd_per.

105. Query: "(direct read) https://edudoc.ch/record/213204/files/PER_rapport.pdf; 2 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on edudoc.ch PER_rapport.pdf: bot check ("JavaScript is disabled")
   Stopped: no
   Conclusion: CIIP/PER report not read.

106. Query: "(direct read) https://portail.ciip.ch/per/domains; 1 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on portail.ciip.ch/per/domains: "completed with no output"
   Stopped: no
   Conclusion: PER portal not read.

107. Query: "education.gouv.fr organisation de la scolarité cycles école élémentaire CP CE1 CE2 CM1 CM2 collège sixième cinquième quatrième troisième âge"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed education.gouv.fr, Eduscol and Eurydice pages; the first two were tried in #108 and #109 (blocked), Eurydice was read in #110.

108. Query: "(direct read) https://www.education.gouv.fr/l-ecole-elementaire-9668; 1 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on education.gouv.fr/l-ecole-elementaire-9668: "Failed to fetch"
   Stopped: no
   Conclusion: Ministry page not read.

109. Query: "(direct read) https://eduscol.education.gouv.fr/5229/l-ecole-elementaire; 1 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on eduscol.education.gouv.fr/5229/l-ecole-elementaire: "Failed to fetch"
   Stopped: no
   Conclusion: Eduscol page not read.

110. Query: "(direct read) https://eurydice.eacea.ec.europa.eu/fr/eurypedia/france/enseignement-primaire; 1 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: Eurydice France "Enseignement primaire" page, raw text (last update 14 December 2023)
   Blocked: none
   Stopped: no
   Conclusion: CP, CE1, CE2, CM1, CM2 and 6e read; see eurydice_fr_primary.

111. Query: "(direct fetch) https://eurydice.eacea.ec.europa.eu/fr/eurypedia/france/organisation-de-lenseignement-secondaire-inferieur-general"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: WebFetch PROVENANCE_REQUIRED on the Eurydice secondary-education page
   Stopped: yes (fetch permission request not answered; not retried)
   Conclusion: Collège class names (5e) and ages not documented.

112. Query: "(direct fetch) https://api.crossref.org/works/10.1007/s40593-025-00520-7"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref record 10.1007/s40593-025-00520-7 (second, detailed fetch)
   Blocked: none
   Stopped: no
   Conclusion: Confirmed the Watanabe record and the CC BY-NC-ND 4.0 licence from 2026-04-22.

113. Query: ""ChatGPT, Can You Make this Text Easier?" Investigating the Utility of LLMs in Easing Text Readability Watanabe"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed related readability papers (Trott and Rivière; Farajidizaji et al.); no listed title was Watanabe (2025).

114. Query: "ChatGPT, Can You Make this Text Easier? Investigating the Utility of LLMs in Easing Text Readability"   Date: 2026-11-01   Tool: Consensus search
   Opened: Consensus result list; record [1] is Watanabe (2025)
   Blocked: none
   Stopped: no
   Conclusion: Abstract seen; abstract-only (watanabe2025).

115. Query: "(direct read) https://link.springer.com/article/10.1007/s11145-023-10493-5; 1 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: nothing
   Blocked: alphaXiv on the Springer page of Mesmer (2024): JavaScript error page
   Stopped: no
   Conclusion: Abstract already seen in #24.

116. Query: "(direct read) https://link.springer.com/article/10.1007/s11145-025-10676-2; 1 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: Springer page of Liu et al. (2025) via alphaXiv: abstract, notes and reference list; full text behind a subscription wall
   Blocked: none
   Stopped: no
   Conclusion: Abstract-only (liu2025).

117. Query: "(direct read) 2410.14028; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: arXiv 2410.14028 (Trott & Rivière), all pages
   Blocked: none
   Stopped: no
   Conclusion: Read; see trott2024.

118. Query: "(direct read) 2309.12551; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: arXiv 2309.12551 v2 (Farajidizaji, Raina & Gales), all pages
   Blocked: none
   Stopped: no
   Conclusion: Read; see farajidizaji2023.

119. Query: "Kandel Moles 1958 "Application de l'indice de Flesch à la langue française" Cahiers d'Études de Radio-Télévision"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed Primpied et al. (arXiv 2208.12924, read in #122), an rdrr.io readability-methods page and other French readability pages; the 1958 article itself was not among the listed titles.

120. Query: "teachers use of generative AI to prepare teaching materials survey Switzerland Swiss teachers ChatGPT lesson preparation study 2024 2025"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed arXiv and Linköping copies of a teachers case study, an NFER summary, ISRCTN trial records, the EPFL news item (read in #123) and an ijres.net paper; no Swiss primary-teacher survey was among the listed titles.

121. Query: "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or how I learned to start worrying about prompt formatting arXiv"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed arXiv 2310.11324 (title as listed: "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or..."), an ICLR poster page and mirrors; nothing opened from this search.

122. Query: "(direct read) 2208.12924; 3 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: arXiv 2208.12924 (Primpied, Beauchemin & Khoury), all pages
   Blocked: none
   Stopped: no
   Conclusion: Read; the Kandel and Moles formula as printed there; see primpied2022.

123. Query: "(direct read) https://actu.epfl.ch/news/chatgpt-is-shaking-up-the-world-of-education-wha-2; 1 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: EPFL news item on a survey of Vaud teachers (raw page text)
   Blocked: none
   Stopped: no
   Conclusion: Read; see epfl2023_vaud_teachers.

124. Query: "(direct fetch) https://api.crossref.org/works?query.title=MANULEX+A+grade-level+lexical+database+from+French+elementary+school+readers&rows=2&select=DOI,title,container-title,volume,issue,page,issued,author"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref title query for Manulex
   Blocked: none
   Stopped: no
   Conclusion: Confirmed Behavior Research Methods, Instruments, & Computers 36(1) 156-166, DOI 10.3758/BF03195560.

125. Query: "(direct fetch) https://api.crossref.org/works?query.title=Manulex-infra+Distributional+characteristics+of+grapheme-phoneme+mappings+and+infralexical+and+lexical+units+in+child-directed+written+material&rows=2&select=DOI,title,container-title,volume,issue,page,issued,author"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref title query for Manulex-infra
   Blocked: none
   Stopped: no
   Conclusion: The target record was not among the two items returned.

126. Query: "(direct fetch) https://api.crossref.org/works/10.3758/BF03193029"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: nothing
   Blocked: WebFetch client error on Crossref works/10.3758/BF03193029 (upper-case DOI)
   Stopped: no
   Conclusion: Retried in lower case in #127.

127. Query: "(direct fetch) https://api.crossref.org/works/10.3758/bf03193029"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: Crossref works/10.3758/bf03193029
   Blocked: none
   Stopped: no
   Conclusion: Confirmed Manulex-infra, Behavior Research Methods 39(3) 579-589, 2007-08.

128. Query: "word frequency as predictor of text difficulty for children readability grade level French primary school texts lexical frequency Lexique Manulex study"   Date: 2026-11-01   Tool: WebSearch (standard)
   Opened: result list only (titles and addresses)
   Blocked: none
   Stopped: no
   Conclusion: Results listed the Javourey-Drevet et al. (2022) open-access PDF (read in #129), Manulex pages and a French text-difficulty paper (LC-Score).

129. Query: "(direct read) https://cambridge.org/core/services/aop-cambridge-core/content/view/044CF6A2A378E7A0D4E0822157EE33C9/S014271642100062Xa.pdf/simplification-of-literary-and-scientific-texts-to-improve-reading-fluency-and-comprehension-in-beginning-readers-of-french.pdf; 4 question(s) to the reader"   Date: 2026-11-01   Tool: alphaXiv answer_pdf_queries (raw page reader)
   Opened: Open-access PDF of Javourey-Drevet et al. (2022), raw pages
   Blocked: none
   Stopped: no
   Conclusion: PDF pages 1, 2, 5, 7-11, 18, 24, 25, 28 read; see javourey2022.

130. Query: "(direct read) https://arxiv.org/abs/2310.11324"   Date: 2026-11-01   Tool: alphaXiv get_paper_content (full text)
   Opened: arXiv 2310.11324 v2 (Sclar et al.), full text saved to a file (99,304 characters); read: Abstract, Section 1, opening of Section 2, Sections 4.1-4.2, Section 6, Appendix C
   Blocked: none
   Stopped: no
   Conclusion: Read; see sclar2024. Sections 3 (rest), 4.3-4.5, 5 and Appendix B not read.

131. Query: "(direct fetch) https://cendekia.unisza.edu.my/neuaxis-e/Record/nottingham-2947/Description"   Date: 2026-11-01   Tool: WebFetch (returns a machine extraction of the page)
   Opened: cendekia.unisza.edu.my catalogue record of SUBTLEX-UK (WebFetch extraction)
   Blocked: none
   Stopped: no
   Conclusion: Metadata only; its sole access link is the Nottingham eprints landing page, which could not be opened in #67 (redirect not followed) or #69 (permission request unanswered); SUBTLEX-UK stays not accessible.

## Coverage and limits of these searches
(Written after the log, from the entries above; access label: reasoning.)

- Tools that returned results: WebSearch in standard mode, Consensus (three queries), Crossref through WebFetch (metadata only), the alphaXiv full-text reader for arXiv papers, and the alphaXiv raw-page reader for PDFs and web pages.
- Tools or indexes that did not work: Scite (paid plan, #1), OpenAlex (client error, #16), the Semantic Scholar page (#81). I did not query Google Scholar, ERIC, Scopus, Web of Science, Cairn or Persée; no search in this log was run in them.
- Sources that were blocked or refused (a negative result here is not evidence of absence): Springer article pages and PDFs for Watanabe and Mesmer (#13, #23, #115), Wiley pages for Patel et al. and Li et al. (#25, #26), the Elsevier linking hub (#27), HAL copies (bot wall; #63, #76, #77), typeset.io (#65), Nottingham worktribe, eprints and the informahealthcare page (#64, #67, #68, #69; the unisza catalogue record in #131 only links back to eprints), ijts.org and a consensus.app record (#43, #45), edudoc.ch PDFs (#101, #105), the PER portal (#106), education.gouv.fr and Eduscol (#108, #109), the Eurydice secondary-education page (#111), silgeneve.ch (#91) and a Neuchâtel brochure URL that returned a web page instead of the brochure (#92).
- Consequence: these searches can support only a bounded statement of the form given in the final report. They cannot support any claim that no earlier study exists.
