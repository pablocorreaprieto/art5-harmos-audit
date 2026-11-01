<!-- Export of the Google Doc 'PROTOCOLE — Article autonome par IA, modèle (CURRENT)' (version 1.1 of 25.10.2026, last modified 31.10.2026), read through the Google Drive connector on 1.11.2026 and copied without edits. Added to the repository after the internal reading R3 (P7). -->

# **Protocole d'article autonome par IA (modèle v1.1)**
*Version 1.1 du 25.10.2026, règle 11 (tout est noté) ajoutée le même jour à la demande de Pablo. Modèle à copier pour chaque article, premier usage prévu pour l'Article 5. Repères de lecture, \[constat\] = vérifié dans une source, un test ou un document du Drive, \[inférence\] = déduction, \[vue\] = recommandation, \[estimation\] = ordre de grandeur. Le journal de bord associé est la feuille *[*Journal, article autonome par IA (modèle)*](https://docs.google.com/spreadsheets/d/1ByYEd0AECJO-dJcUMHAfA3btpPcSqigCvfnAVgjRvvY/edit)*, dans le même dossier.*
## **En bref**
Claude conduit l'article de bout en bout, de la question au paquet de soumission, et tu interviens à deux portes. La porte G1 valide la conception avant toute collecte de données, la porte G2 valide le manuscrit final et passe par ta soumission depuis ton compte. Tout le reste est exécuté, vérifié et journalisé par l'IA, avec des contrôles qui bloquent la suite quand ils échouent.
  - **Ce que fait l'IA.** Cadrage, conception, rédaction du préenregistrement, recherche et lecture de la littérature, génération ou collecte des données dans GitHub Actions, analyse, rédaction en anglais, vérification des références et des nombres, relecture adverse par sous-agents, paquet de soumission, réponses aux évaluateurs.
  - **Porte G1, conception (toi).** Lire le dossier de conception de deux pages, valider le budget API, déposer le préenregistrement sur AsPredicted. Environ 45 minutes \[estimation\].
  - **Porte G2, soumission (toi).** Lire le manuscrit final et la liste d'exceptions, relire la déclaration IA, soumettre depuis ton compte. Environ deux à trois heures \[estimation\].
  - **Types d'études.** M1 audit de modèles de langue, M2 analyse secondaire de données ouvertes, M3 analyse documentaire codée par IA, M4 revue de portée ou systématique dépistée par IA.
  - **Revues.** Échelle de trois revues Q1 sans frais de publication, par la voie abonnement des revues hybrides.
  - **Durée.** Deux à quatre jours de travail de l'IA par article selon le module, plus tes deux portes \[estimation\].
## **Règles non négociables**
\[constat\] Adaptées de la compétence research-integrity disponible dans Claude.
1.  **L'IA n'est jamais autrice.** Tu valides la conception (G1) et tu soumets (G2), parce que les revues tiennent l'auteur humain pour responsable de tout le contenu.
2.  **Lire avant de citer.** Une source n'est citée pour un contenu précis que si le passage concerné a été lu en texte intégral (étiquette read-directly). Une source lue seulement en résumé est retirée, ou placée dans la liste d'exceptions de G2 avec le passage à vérifier.
3.  **Nombres traçables.** Chaque nombre du manuscrit est copié d'un champ nommé d'une exécution archivée (fichier numbers.json). Aucun nombre n'est tapé à la main.
4.  **Nouveauté bornée.** Aucune affirmation de priorité hors de la portée des recherches journalisées. Formule type, « les recherches dans X et Y n'ont trouvé aucun travail antérieur, Z n'a pas pu être consulté ».
5.  **Contrôles qui peuvent échouer.** Chaque contrôle est livré avec une faute introduite volontairement qu'il doit attraper, et il doit passer sans cette faute.
6.  **Relecture séparée.** La relecture adverse est faite par des sous-agents qui n'ont pas vu la rédaction, et chaque constat est soumis à une tentative de réfutation avant d'être appliqué. Ces lectures sont étiquetées comme lectures internes par IA, pas comme une évaluation par les pairs.
7.  **Déclaration complète.** La déclaration IA suit le gabarit de la revue, mais elle nomme tous les usages (idée, conception, code, génération ou codage des données, rédaction, relecture). Le format est minimal, le contenu est complet.
8.  **Une porte qui échoue bloque.** On ne modifie pas un contrôle pour faire passer un article. Si un contrôle doit changer, la modification et sa raison sont notées dans l'onglet Décisions avant l'usage.
9.  **Aucun secret exposé.** Aucune clé API ni aucun mot de passe dans le chat, le Drive ou le dépôt. Les clés vivent seulement dans les secrets GitHub.
10. **Aucun participant humain.** Les modules M1 à M4 n'utilisent que des sorties de modèles, des documents publics ou des données ouvertes anonymisées.
11. **Tout est noté.** Chaque action utile est notée au moment où elle est faite, assez précisément pour qu'une personne qui relit plus tard sache ce qui a été fait, quand, par qui, pourquoi et où en trouver la trace. L'onglet Historique du journal reçoit une ligne par action (création ou modification d'un fichier, d'un document ou d'une feuille, décision, contrôle lancé, relecture lancée ou reçue, écriture dans Todoist, l'agenda, le suivi des articles ou le dépôt), avec la date, l'heure, la phase, le détail et le résultat, le lien, l'auteur (session principale ou session de relecture, avec son modèle) et la version ou l'empreinte. L'onglet spécialisé garde le détail (Décisions, Recherches, Sources, Exécutions, Contrôles, Relectures IA). Chaque relecture est gardée en entier, consigne et rapport, dans le document des relectures de l'article. Chaque version du code et de la conception a son entrée dans CHANGELOG.md, avec les constats traités, les contrôles et les empreintes, et les scripts de contrôle sont conservés avec leurs sorties. Chaque contrôle a une ligne de succès exacte et un contrôle qui doit échouer, observé et noté, et un seul script les relance tous (checks/run\_all.sh). Une relance ne remplace jamais une sortie déjà citée, run\_all.sh garde la relance précédente dans checks/history avant d'écrire. Les versions antérieures du code sont gardées en différences avec leurs empreintes (history/). Rien ne reste seulement dans l'espace de travail d'une session, qui disparaît à sa fermeture, tout ce qui sert de trace est versé dans le projet Claude ou le dépôt avant la fin de la session. En fin de session, l'onglet État et la page 00 Reprendre ici sont à jour. Ce qui n'est pas noté ne compte pas comme fait.
## **Choix arrêtés le 25.10.2026**
|  |  |  |
| :- | :- | :- |
| **Décision** | **Option retenue** | **Conséquence dans le protocole** |
| Portée | Modèle réutilisable, instancié ensuite pour l'Article 5 | Les paramètres propres à un article sont notés entre accolades, par exemple {WORKING\_TITLE} |
| Types d'études | M1, M2, M3 et M4 | Un module par type, section Modules |
| Portes humaines | Deux, G1 conception et G2 soumission | L'IA vérifie les citations en texte intégral, le reste passe dans la liste d'exceptions de G2 |
| Revues | Échelle Q1 sans frais | Trois revues par article, voie abonnement, politique IA vérifiée |
| Appels aux modèles | GitHub Actions, clés en secrets du dépôt | Claude ne voit jamais les clés |
| Domaines du bac à sable de Claude | À ouvrir dans les paramètres de claude.ai | Vérification automatique des DOI, sinon repli sur GitHub Actions |
| Outils de littérature | Scite, Elicit Pro, Consensus, alphaXiv et recherche web | Scite pour lire et vérifier, Elicit surtout pour M4 |
| Mode d'exécution | Une session par article, avec sous-agents | Les relecteurs sont des sous-agents séparés |
| Validation de M3 et M4 | Accord entre deux modèles de fournisseurs différents, un troisième tranche | Pas d'échantillon humain, limite déclarée dans l'article |
| Déclaration IA | Gabarit de la revue | Contenu complet, voir la règle 7 |
| Préenregistrement et archives | AsPredicted, et Zenodo relié à GitHub | Indépendant de l'arrêt des nouveaux projets OSF au 16.11 noté dans la fiche de l'Article 1 |
| Langue | Protocole en français, prompts et manuscrits en anglais | Les prompts sont prêts à copier |

## **Mise en place unique**
À faire une seule fois, en une à deux heures \[estimation\]. Chaque nouvel article réutilise ensuite cette installation.
### **GitHub et GitHub Actions**
1.  Créer sur GitHub un dépôt privé nommé modele-article-ia et cocher Template repository (Settings, General). Au premier usage, Claude y pousse l'ossature de l'annexe A et le workflow de l'annexe B.
2.  Pour chaque article, créer un dépôt à partir de ce modèle (bouton Use this template), par exemple art5-etiquettes-harmos, et le garder privé jusqu'à la soumission.
3.  Dans ce dépôt, ouvrir Settings, Secrets and variables, Actions, puis New repository secret, et créer ANTHROPIC\_API\_KEY, OPENAI\_API\_KEY et MISTRAL\_API\_KEY, seulement ceux dont l'article a besoin. Dans l'onglet Variables du même écran, créer CONTACT\_EMAIL avec ton adresse de recherche, que Crossref, OpenAlex et Unpaywall demandent comme contact.
4.  Dans Settings, Actions, General, vérifier que les Actions sont autorisées et choisir Read and write permissions sous Workflow permissions, pour que le workflow puisse enregistrer ses sorties dans le dépôt.
5.  Dans une conversation du projet Claude de l'article, donner le nom du dépôt. Claude l'attache avec un accès en écriture, pousse le code, lance les exécutions avec gh workflow run et suit leur avancement.
\[constat\] Test du 25.10.2026, le bac à sable de Claude joint api.github.com et l'outil gh y est installé.
### **Clés API et plafonds**
  - Une clé dédiée par article et par fournisseur, créée dans la console du fournisseur, avec un plafond de dépense si la console le propose.
  - La clé est collée seulement dans les secrets GitHub, jamais dans le chat. Elle est révoquée à la fin de l'article.
  - Le budget de chaque exécution est fixé à G1 et passé au workflow (paramètre max\_cost\_usd). Le script s'arrête quand il l'atteint, et l'onglet Budget du journal suit la dépense.
### **Ouvrir les domaines de recherche du bac à sable de Claude**
\[constat\] Test du 25.10.2026 depuis le bac à sable. api.anthropic.com et api.github.com répondent, alors que api.crossref.org, api.openalex.org, zenodo.org, api.openai.com et api.mistral.ai sont refusés par le proxy.
\[constat\] Selon le message du proxy, sur une offre individuelle payante c'est toi qui règles les domaines autorisés, sur claude.ai dans un navigateur, sous Settings puis Capabilities. Sur une offre Team ou Enterprise, l'administrateur le fait dans les paramètres de l'organisation. Sur l'offre gratuite, seuls les gestionnaires de paquets peuvent être autorisés.
1.  Ouvrir claude.ai dans un navigateur d'ordinateur (pas l'application mobile), cliquer sur ton nom ou tes initiales, puis sur Settings, puis sur Capabilities.
2.  Vérifier que l'exécution de code est activée. L'interrupteur s'appelle Code execution and file creation, ou Create and edit files dans la nouvelle présentation \[constat, aide de claude.ai\].
3.  Dans le réglage d'accès réseau (Allow network egress), choisir l'option qui autorise les gestionnaires de paquets et des domaines précis, puis ajouter les domaines un par un.
4.  Ajouter les huit domaines du tableau ci-dessous.
5.  Ne pas choisir l'option qui ouvre tous les domaines. \[constat\] L'aide de claude.ai la présente comme la plus risquée, parce qu'une instruction cachée dans une page ou un fichier pourrait faire envoyer des données à un tiers.
6.  Ouvrir une nouvelle conversation et demander à Claude le test de connectivité de l'annexe D. Chaque domaine doit répondre, un code 200 ou une erreur d'authentification prouvant qu'il est joignable. \[inférence\] Le réglage s'applique probablement aux nouvelles sessions plutôt qu'à celle en cours.
|  |  |
| :- | :- |
| **Domaine** | **Usage** |
| api.crossref.org | Métadonnées des DOI, corrections et rétractations déclarées par les éditeurs |
| api.openalex.org | Recherche bibliographique, métadonnées, liens vers les versions en accès ouvert |
| api.unpaywall.org | Localisation des PDF en accès ouvert légal, pour lire les sources en texte intégral |
| doi.org | Résolution des DOI |
| api.datacite.org | DOI de données et de logiciels (Zenodo, OSF) |
| zenodo.org | Dépôt et lecture des archives |
| export.arxiv.org | Métadonnées des prépublications arXiv |
| api.ies.ed.gov | API de la base ERIC, utile en sciences de l'éducation |

**Si ton écran n'offre qu'un interrupteur.** \[constat\] L'article d'aide de claude.ai ne décrit, pour les offres individuelles, qu'un interrupteur sans liste de domaines, alors que le message du proxy parle d'une liste réglable. Si aucune liste n'apparaît, ne pas ouvrir l'accès à tous les domaines. Les vérifications bibliographiques tournent alors dans GitHub Actions (étape verify\_refs), dont les machines ont un accès internet ouvert, et rien n'est perdu.
\[constat\] Les connecteurs (Scite, Consensus, Elicit, alphaXiv) et la recherche web de Claude ne dépendent pas de ce réglage.
### **Zenodo**
1.  Se connecter à zenodo.org avec le compte GitHub.
2.  Dans le menu du compte, ouvrir la page GitHub de Zenodo, synchroniser la liste, puis activer l'interrupteur du dépôt de l'article.
3.  Chaque release publiée sur GitHub crée alors une version archivée avec un DOI. Le fichier .zenodo.json du dépôt (annexe C) fixe le titre, l'auteur, l'ORCID et la licence.
4.  Pour une revue en double aveugle, publier la release seulement après l'acceptation, et donner aux évaluateurs une copie anonymisée (annexe A).
### **AsPredicted**
  - Créer un compte sur aspredicted.org. À G1, Claude fournit les réponses en anglais, tu les colles et tu soumets.
  - \[constat\] Un préenregistrement AsPredicted reste privé jusqu'à ce qu'un auteur le rende public.
  - Pour une évaluation en double aveugle, vérifier au moment du dépôt comment le partager sans ton nom. À défaut, joindre une copie anonymisée en annexe de la soumission.
### **Scite, Elicit et les outils gratuits**
  - **Scite.** Démarrer l'essai gratuit ou l'abonnement juste avant la fenêtre de travail d'un article. \[constat\] Après la souscription, l'accès peut prendre jusqu'à 15 minutes, ou s'active tout de suite si tu déconnectes puis reconnectes le connecteur Scite dans claude.ai.
  - **Elicit Pro.** \[constat\] Le connecteur exige l'offre Pro ou supérieure et refuse les appels sans elle. Il sert surtout à M4, et règlerait aussi la décision en attente pour l'Article 3.
  - **Consensus et alphaXiv.** Ils fonctionnent déjà sans abonnement. \[constat\] L'offre gratuite de Consensus renvoie 10 résultats par recherche.
### **Claude**
  - Un projet Claude par article (celui de l'Article 5 existe déjà).
  - Opus pour la conception, la rédaction et la relecture, conformément à ta règle pour les articles de recherche. Les sous-agents relecteurs utilisent au moins deux modèles différents.
  - Chaque session commence par le prompt de démarrage (section Prompts). Si une session devient trop longue, Claude en ouvre une nouvelle avec le même prompt et reprend depuis l'onglet État.
## **Architecture**
### **Où vit quoi**
|  |  |  |
| :- | :- | :- |
| **Lieu** | **Contenu** | **Fait foi pour** |
| Dossier Drive de l'article | Dossier de conception, document des relectures (consignes et rapports complets), manuscrit (Google Doc), lettre, déclaration, notes de lecture | Le texte et les décisions |
| Journal de bord de l'article (feuille) | État des phases, historique de chaque action, décisions, recherches, sources, exécutions, contrôles, relectures, revues, budget | L'avancement, Claude reprend toujours depuis l'onglet État |
| Dépôt GitHub | Prompts, code, CHANGELOG.md, scripts de contrôle et leurs sorties (checks/), versions antérieures en différences (history/), données brutes et dérivées, résultats, journaux d'exécution, numbers.json | Les données et les nombres |
| Zenodo | Versions archivées avec DOI | La citation des données et du code |
| AsPredicted | Préenregistrement | Les hypothèses et les analyses annoncées |
| Projet Claude de l'article | Lien vers ce protocole, conversations de travail | Le contexte des sessions |

### **Dossier d'un article dans le Drive**
Sous 01 🔬 RECHERCHE puis 01 📄 ARTICLES, un dossier {NN} 📄 ART {N} {NOM} qui suit le squelette habituel des articles.
  - **À la racine.** Le document 00 Reprendre ici (une page, état et prochaine étape, tenu à jour par Claude) et le journal de bord de l'article, dont l'onglet Sources tient lieu de registre des sources.
  - **01 📚 Bibliothèque.** Notes de lecture et PDF lus.
  - **02 ✍️ Rédaction.** Manuscrit, lettre à la rédaction, déclaration IA, réponses aux évaluateurs.
  - **03 🗃️ Corpus et données.** Exports légers et liens vers le dépôt, sans copie des données lourdes.
  - **04 🧪 Protocole et instruments.** Dossier de conception, document des relectures, texte du préenregistrement, prompts gelés.
  - **05 💻 Scripts.** Lien vers le dépôt GitHub, sans copie du code.
  - **99 🗄️ ARCHIVE.** Versions remplacées.
### **Connecteurs et outils**
|  |  |  |  |
| :- | :- | :- | :- |
| **Outil** | **Rôle** | **Phases** | **État au 25.10.2026** |
| Google Drive, Docs et Sheets | Dossier, manuscrit, journal de bord | Toutes | Fonctionne |
| GitHub (dépôt attaché, outil gh) | Code, exécutions, versions | P1, P3 à P8 | Joignable, dépôts à créer |
| API Anthropic, OpenAI et Mistral, appelées depuis GitHub Actions | Génération (M1), codage (M3), dépistage (M4), pilotes | P1, P3 | Clés à placer dans les secrets |
| Scite | Lecture en texte intégral, citations qui soutiennent ou contredisent, avis de rétractation | P2, P6 | Refusé sans abonnement |
| Elicit Pro | Recherche, dépistage et extraction à grande échelle | P2, surtout M4 | Refusé sans offre Pro |
| Consensus | Recherche sémantique dans la littérature évaluée par les pairs | P0, P2 | Fonctionne, 10 résultats par recherche |
| alphaXiv | Prépublications arXiv, lecture et questions sur le PDF | P0, P2, P6 | Fonctionne |
| Recherche et lecture web de Claude | Littérature grise, consignes et politiques IA des revues | P0, P1, P2, P8 | Fonctionne |
| Crossref, OpenAlex, Unpaywall, DataCite, ERIC | Vérification des DOI, accès ouvert, littérature en éducation | P2, P6 | À ouvrir dans les paramètres, sinon via GitHub Actions |
| Compétences research-desk de Claude | research-litnote, paper-compare, related-work, citation-check, paper-critique, llm-council, decision-matrix | P0 à P7 | Disponibles |
| Compétence research-integrity | Règles et formats de journal | Toutes | Disponible |
| Todoist et Google Agenda (🍇 GRAPE) | Rappels des deux portes, bloc de travail | P1, P8 | Fonctionnent |
| Claude in Chrome | Remplir les champs du portail de soumission après ta connexion et avec ton accord, sans cliquer sur Soumettre | P8, en option | Disponible |

## **Le pipeline, phase par phase**
Chaque phase a un objectif, des étapes, un livrable et un critère de sortie. Claude note chaque étape dans le journal avant de passer à la suivante, avec une ligne par action dans l'onglet Historique (règle 11). Les durées sont des estimations du temps de travail de l'IA.
|  |  |  |
| :- | :- | :- |
| **Jour** | **Phases** | **Fin de journée** |
| 1 | P0, P1 | Porte G1 |
| 2 | P2, P3 | Données gelées |
| 3 | P4, P5, P6 | Rapport de vérification |
| 4 | P7, P8 | Porte G2 et soumission |

Déroulé type sur quatre jours \[estimation\]. M2 et M4 peuvent demander un jour de plus pour les données ou le dépistage.
### **P0 Cadrage et choix de la question**
**Objectif.** Une question faisable sans participants humains, utile pour ta thèse et publiable dans une revue de l'échelle Q1.
1.  Partir d'un thème ou d'une idée que tu donnes. Claude formule trois à cinq questions candidates, chacune rattachée à un module.
2.  Balayage de l'antériorité pour chacune (Consensus, alphaXiv, recherche web, et Scite ou Elicit s'ils sont actifs), journalisé dans l'onglet Recherches.
3.  Notation avec la compétence decision-matrix sur six critères. Autonomie, disponibilité des données, écart avec l'existant dans la portée des recherches, lien avec ta thèse, adéquation aux revues visées, risques (coût, pilote, évolution des modèles).
4.  Test d'arrêt. Si une étude publiée répond déjà à la question, abandon ou pivot, noté dans l'onglet Décisions.
**Livrable.** Fiche projet d'une page (question, module, contribution attendue, trois revues pressenties).
**Sortie.** Une question retenue. Une à deux heures \[estimation\].
### **P1 Conception, pilote et préenregistrement**
1.  **Dossier de conception de deux pages.** Question et hypothèses, plan (facteurs, unités, taille), variables et mesures, analyses confirmatoires, règles d'exclusion, contrôles d'échec prévus, règles d'arrêt, budget API, échelle de revues, menaces à la validité.
2.  **Taille de l'échantillon.** Justifiée par simulation dans un script versionné, avec une puissance visée de 0,80 \[vue\].
3.  **Pilote.** Une exécution minimale, par exemple 30 à 40 unités, vérifie que la chaîne mesure ce qu'elle doit mesurer. Le pilote est exclu des analyses confirmatoires et déclaré comme tel dans le préenregistrement.
4.  **Échelle de revues.** Pour chaque revue candidate, Claude lit les consignes aux auteurs et la politique IA, puis remplit l'onglet Revues (quartile vérifié avec sa source, absence de frais en voie abonnement, limite de mots, type d'évaluation, texte exact de la politique IA, deux articles récents proches du sujet). Une revue dont la politique exclut un manuscrit développé avec l'IA est retirée.
5.  **Préenregistrement.** Réponses au formulaire AsPredicted rédigées en anglais (prompt de la section Prompts), prêtes à coller.
**Porte G1 (toi).** Lire le dossier de deux pages, répondre « go » ou demander des changements dans la conversation, valider le budget, déposer le préenregistrement sur AsPredicted et donner le lien à Claude. Aucune donnée confirmatoire n'est produite avant ce feu vert.
**Sortie.** Préenregistrement déposé, budget validé, échelle de revues figée. Trois à cinq heures \[estimation\].
### **P2 Littérature**
1.  **Plan de recherche.** Écrit avant de chercher (concepts, synonymes en anglais et en français, bases, années). Chaque requête est journalisée avec les sources ouvertes, les sources bloquées et la conclusion dans la portée de ce qui a été ouvert.
2.  **Recherche.** Scite, Elicit, Consensus, alphaXiv, ERIC et OpenAlex quand ils sont ouverts, et le web pour la littérature grise.
3.  **Sélection.** Pour M4, le dépistage suit le module M4. Pour M1 à M3, Claude retient les sources nécessaires à l'introduction, à la méthode et à la discussion.
4.  **Lecture.** Pour chaque source citée, une note de lecture (compétence research-litnote) indique la section ou la page du passage utilisé et l'étiquette d'accès (read-directly, abstract-only, search-summary). Le texte intégral vient de Scite, d'Unpaywall, d'alphaXiv ou de la page de l'éditeur en accès ouvert.
5.  **Positionnement.** Comparaison avec les trois à cinq travaux les plus proches (compétence paper-compare).
6.  **Phrase de nouveauté.** Rédigée dans la portée des recherches, avec la liste des bases bloquées.
**Sortie.** Onglet Sources complet, chaque citation prévue reliée à une note read-directly. Trois à six heures \[estimation\].
### **P3 Données et exécutions**
1.  Les prompts, les paramètres (identifiant exact et version datée du modèle, température, longueur maximale) et le plan d'exécution sont gelés dans le dépôt avant la première exécution confirmatoire, avec un tag prereg.
2.  Claude lance le workflow de l'annexe B avec le budget validé à G1, suit l'exécution et récupère les sorties.
3.  Chaque sortie brute est enregistrée telle quelle en JSONL, avec son empreinte SHA-256, l'horodatage, l'identifiant du modèle et le coût. Une exécution relancée crée de nouveaux fichiers, sans écraser les anciens.
4.  Le jeu de données final est gelé par un tag data-v1. La suite dépend du module (section Modules).
**Sortie.** Données gelées, onglet Exécutions à jour, coût réel sous le budget. Deux à six heures selon le module \[estimation\].
### **P4 Analyse**
1.  Analyses confirmatoires exactement comme préenregistrées, puis analyses exploratoires étiquetées comme telles.
2.  Les résultats vont dans results/, et chaque nombre destiné au manuscrit est placé dans numbers.json sous un nom stable (par exemple h1\_slope\_grade).
3.  Chaque contrôle a sa faute volontaire. Par exemple, des étiquettes permutées au hasard doivent faire disparaître l'effet, et une valeur modifiée dans une copie du manuscrit doit être détectée.
4.  Les figures sont produites par le code à partir des données, jamais par un générateur d'images, et le rôle de l'IA dans l'écriture du code est déclaré. \[constat\] Elsevier interdit les images créées ou modifiées par IA générative, et le résumé des lignes directrices de Wiley publié par Enago indique une interdiction semblable pour les données et les résultats, visualisations comprises.
**Sortie.** Résultats gelés, numbers.json complet, contrôles inscrits dans l'onglet Contrôles. Deux à quatre heures \[estimation\].
### **P5 Rédaction**
**Ordre.** Méthode, puis résultats générés depuis numbers.json, puis introduction et cadre (compétence related-work, seulement à partir des sources lues), puis discussion. Le résumé et le titre viennent en dernier.
**Règles.** Gabarit et limite de mots de la revue de premier rang, APA 7 sauf consigne contraire, anglais. Chaque affirmation factuelle porte sa citation ou renvoie à un résultat. Les limites mentionnent le rôle de l'IA quand il compte, par exemple M3 et M4 sans échantillon humain, ou des modèles qui évoluent.
**Écriture.** Les règles d'écriture, le mode académique, la passe d'éditeur, la vérification des faits et la passe de style suivent le [Master prompt: excellent article (Claude Fable)](https://docs.google.com/document/d/1pwdxUDbcTA78eE7sbAJhrBurPwS29KIaRkKw_GEHljQ/edit) du même dossier. Ce protocole ajoute les portes, les contrôles et la traçabilité.
**Livrable.** Manuscrit v1 dans 02 ✍️ Rédaction (Google Doc) et export .docx.
**Sortie.** Manuscrit complet sous la limite de mots. Trois à cinq heures \[estimation\].
### **P6 Vérification**
C'est la phase qui rend possibles les deux seules portes humaines.
1.  **Références.** Compétence citation-check, puis script verify\_refs (Crossref, OpenAlex, DataCite). Chaque référence existe, ses métadonnées correspondent, et toute rétractation ou correction est détectée (Scite, Crossref).
2.  **Couples phrase et citation.** Pour chaque phrase citée, Claude retrouve le passage dans le texte intégral et note la correspondance dans l'onglet Sources. Si le passage ne soutient pas la phrase, la phrase est corrigée ou la citation retirée. Si le texte intégral est inaccessible, la citation est retirée ou passe dans la liste d'exceptions de G2 avec le passage à vérifier.
3.  **Nombres.** Le script check\_numbers extrait chaque nombre du manuscrit et le compare à numbers.json. Une valeur modifiée volontairement doit le faire échouer.
4.  **Reproductibilité.** Une nouvelle exécution depuis le tag data-v1 reproduit à l'identique tous les fichiers de results/. La génération par les modèles n'est pas rejouée, ses sorties sont archivées.
5.  **Nouveauté.** Chaque formule de priorité est confrontée au journal des recherches, et les formules à éviter sont remplacées (annexe E).
**Livrable.** Rapport de vérification et liste d'exceptions pour G2, idéalement vide.
**Sortie.** Tous les contrôles au vert, ou exceptions listées. Deux à quatre heures \[estimation\].
### **P7 Relecture adverse par sous-agents**
1.  Trois sous-agents lancés séparément reçoivent seulement le manuscrit, le dépôt et les consignes de la revue. R1 évalue le fond (compétence paper-critique), R2 la méthode et les statistiques, R3 joue le rédacteur en chef et juge le risque de refus sans évaluation.
2.  Les relecteurs utilisent au moins deux modèles différents.
3.  Chaque constat bloquant est confié à un ou deux autres sous-agents chargés de le réfuter. Seuls les constats qui résistent sont appliqués, et les constats réfutés restent notés.
4.  Les corrections sont faites par la session principale, puis relues par un sous-agent qui ne les a pas faites.
5.  Chaque rapport commence par la mention « Internal reading by a separate AI session. Not peer review. » Il est gardé en entier, avec la consigne donnée au relecteur, dans le document des relectures de l'article.
**Sortie.** Onglet Relectures IA à jour, aucun constat bloquant ouvert. Deux à trois heures \[estimation\].
### **P8 Paquet de soumission**
  - Manuscrit au format de la revue, anonymisé si l'évaluation est en double aveugle (nom, remerciements et liens vers le dépôt ou le préenregistrement retirés ou remplacés par des liens anonymes).
  - Page de titre séparée si la revue la demande, avec ton ORCID.
  - Lettre à la rédaction (la contribution en trois phrases, l'adéquation montrée par deux articles récents de la revue, l'absence de participants humains).
  - Déclaration IA au gabarit de la revue (section Déclaration IA).
  - Déclarations de disponibilité des données (Zenodo, ou lien anonyme pendant l'évaluation), de préenregistrement, de conflits d'intérêts, de financement et d'éthique (pas de participants humains, données publiques ou générées).
  - Textes prêts pour les champs du portail (titre, résumé, mots-clés, catégories).
**Porte G2 (toi).** Lire le manuscrit en entier, lire la liste d'exceptions, relire la déclaration IA, puis te connecter au portail et soumettre. En option, après ta connexion et avec ton accord, Claude in Chrome remplit les champs, et c'est toi qui cliques sur Soumettre.
**Après G2.** Tag submitted-v1 dans le dépôt, mise à jour de [Suivi des articles (CURRENT)](https://docs.google.com/spreadsheets/d/1d2L1uQpbr1e5Imi1wKaBC-W62MdSC1WOInsL_ZkMTDw/edit), tâche Todoist de suivi.
**Sortie.** Article soumis. Une à deux heures pour l'IA, deux à trois heures pour toi \[estimation\].
### **P9 Après la soumission**
  - **Refus sans évaluation.** Claude adapte le manuscrit à la revue suivante de l'échelle dans les 48 heures (format, longueur, lettre), puis courte porte G2. Accepter un transfert proposé par l'éditeur si la revue de destination est sur l'échelle ou la vaut.
  - **Évaluations reçues.** Tableau point par point (remarque, réponse, modification, emplacement), mêmes vérifications qu'en P6 sur chaque modification, relecture adverse des réponses, puis ta validation et ta soumission.
  - **Refus après évaluation.** Intégrer les remarques utiles, puis passer à la revue suivante.
  - **Acceptation.** Vérifier les épreuves (nombres et références à nouveau), publier la release Zenodo si elle attendait, mettre à jour ORCID, le site et le suivi des articles.
## **Modules par type d'étude**
### **M1 Audit de modèles de langue**
Les données sont des sorties de modèles produites selon un plan expérimental, et les variables sont calculées par programme.
  - Plan factoriel explicite (conditions de prompt, modèles, thèmes ou items, répétitions) et ordre des appels randomisé.
  - Au moins deux fournisseurs, versions datées notées, température et paramètres fixés et déclarés.
  - Variables principales calculées par des mesures reconnues dans la littérature quand elles existent, par exemple des normes lexicales par niveau scolaire pour la difficulté d'un texte.
  - Contrôle d'échec de la mesure. Un texte de niveau connu doit être classé correctement, et un texte dont les mots sont mélangés doit dégrader le score.
  - Limites types. Modèles qui évoluent vite, sensibilité au prompt, écart entre la mesure et l'usage réel en classe.
  - Premier usage prévu. L'Article 5, calibrage des textes générés selon les étiquettes de degré HarmoS.
### **M2 Analyse secondaire de données ouvertes**
  - Source officielle (OCDE, IEA, OFS ou équivalent) téléchargée par le workflow, avec l'empreinte du fichier, la version et la date de diffusion.
  - Licence et conditions d'utilisation lues avant toute analyse.
  - Plan d'échantillonnage respecté (poids, réplications, valeurs plausibles) selon les méthodes prévues par le producteur des données.
  - Préenregistrement possible sur des données existantes, à condition de déclarer ce qui a déjà été consulté \[vue\].
  - Limites types. Variables imposées par l'enquête, causalité hors de portée, ancienneté des données.
### **M3 Analyse documentaire codée par IA**
  - Corpus de textes publics, critères d'inclusion écrits avant la collecte, inventaire avec l'URL, la date d'accès et l'empreinte de chaque texte.
  - Grille de codage figée avant le codage, avec définitions et exemples.
  - Deux modèles de fournisseurs différents codent séparément, sans voir le codage de l'autre. Un troisième modèle tranche les désaccords sans savoir quel modèle a produit quel codage.
  - Accord mesuré par l'alpha de Krippendorff pour chaque code. Règle préenregistrée \[vue\], un code sous 0,667 est exclu des analyses confirmatoires et rapporté comme exploratoire.
  - Limite déclarée. Aucun échantillon codé par un humain (choix du 25.10.2026), ce qui réduit les chances dans les revues Q1 \[inférence\].
### **M4 Revue de portée ou systématique dépistée par IA**
  - Protocole PRISMA-ScR ou PRISMA 2020 déposé sur Zenodo avec un DOI avant toute recherche.
  - Au moins deux bases plus la littérature grise, avec les équations complètes en annexe de l'article.
  - Dépistage sur titre et résumé, puis sur texte intégral, par deux modèles de fournisseurs différents qui travaillent séparément, un troisième tranchant les désaccords. L'accord est rapporté à chaque étape.
  - Extraction en double par deux modèles, avec une grille figée et les désaccords tranchés.
  - Diagramme de flux PRISMA produit par le code depuis les décisions journalisées.
  - Elicit Pro sert à la recherche et à l'extraction assistée, mais les décisions qui comptent passent par le pipeline scripté pour rester reproductibles.
  - Limite déclarée. Aucun dépisteur humain, alors que PRISMA-ScR en attend un second, comme le relève déjà la fiche de l'Article 3. Certaines revues refuseront pour cette raison \[inférence\].
## **Stratégie de revues**
  - **Échelle.** Trois revues par article, de la plus ambitieuse réaliste à la plus sûre, toutes sans frais en voie abonnement.
  - **Critères d'entrée.** Quartile vérifié au moment du choix (JCR ou SJR, avec la source), politique IA compatible avec un manuscrit développé avec l'IA et déclaré, au moins deux articles récents proches du sujet, limite de mots compatible.
  - **Candidates à évaluer pour tes thèmes** \[vue, quartile et politique à vérifier à chaque article\]. Journal of Computer Assisted Learning, British Journal of Educational Technology, Computers & Education, Reading and Writing, International Journal of Artificial Intelligence in Education, Learning, Media and Technology, Technology, Pedagogy and Education, Teaching and Teacher Education, European Journal of Teacher Education. Education and Information Technologies est déjà visée par l'Article 4.
  - **Politiques IA.** \[constat\] Selon le résumé des lignes directrices de Wiley publié par Enago (mars 2026), Wiley permet d'utiliser l'IA pour développer le contenu d'un manuscrit si cet usage est décrit de façon transparente, par exemple dans la méthode, l'auteur restant entièrement responsable. \[constat\] La lecture qu'en fait CASRAI distingue l'IA comme outil, permise avec déclaration, de l'IA qui génère le contenu intellectuel substantiel, d'où la porte G1. Le texte exact de la politique de chaque revue est copié dans l'onglet Revues au moment du choix.
  - **Éviter le refus sans évaluation.** Titre et résumé qui annoncent la contribution, adéquation montrée par des articles de la revue, longueur respectée, données et code disponibles, limites franches, lettre courte.
  - **Délais.** \[inférence\] Compter plusieurs mois entre la soumission et une décision après évaluation dans ces revues, et recalculer pour chaque article ce que cela laisse avant le dossier de doctorat.
## **Déclaration IA**
Format de la revue, contenu complet (règle 7). Gabarit en anglais à adapter, à placer là où la revue le demande (section dédiée, méthode ou remerciements). Il ne dit pas que tu as vérifié chaque référence toi-même, puisque ce contrôle est fait par les scripts et les sous-agents dont tu lis le rapport.
Declaration of generative AI use. This study was conceived and designed with the assistance of Claude ({MODEL\_ID}, Anthropic), which also searched and summarised the literature, wrote the analysis code, drafted the manuscript and ran internal error checks.  
\[M1\] Outputs of {MODELS} were generated as the research data of this study. Prompts, parameters and outputs are archived at {DOI}.  
\[M3 or M4\] Documents were coded (or records screened) by {MODEL\_A} and {MODEL\_B}, and disagreements were resolved by {MODEL\_C}. Prompts and decisions are archived at {DOI}.  
Reference and number checks were performed by scripted tools and by separate AI sessions, and the author reviewed their reports. The author approved the study design before data collection, reviewed and edited the full manuscript, and takes full responsibility for the content of the publication.
## **Règles d'arrêt**
|  |  |
| :- | :- |
| **Situation** | **Décision** |
| Une étude publiée répond déjà à la question (P0 ou P2) | Arrêt ou pivot, noté dans Décisions |
| Le pilote montre que la mesure ne fonctionne pas (P1) | Revoir la conception avant G1 |
| La dépense atteint le budget validé | Arrêt automatique du workflow, nouvelle validation |
| Alpha inférieur à 0,667 sur le code principal (M3) ou sur l'inclusion (M4) | Hypothèse principale non testable, rapport descriptif ou arrêt |
| Une affirmation clé repose sur une source illisible en texte intégral | Affirmation retirée, ou exception pour G2 |
| La revue exclut les manuscrits développés avec l'IA | Revue retirée de l'échelle |
| Un modèle audité est retiré pendant l'étude | Sorties archivées conservées, version déclarée, aucun remplacement silencieux |
| Un contrôle ou une relecture n'a pas pu aller au bout | Le dire en tête du rapport, pas de soumission |

## **Prompts**
En anglais, prêts à copier. Les champs entre accolades sont à remplir.
### **Démarrage d'une session**
You are running the Autonomous AI Article Protocol v1.1 for {ARTICLE\_CODE}, working title "{WORKING\_TITLE}".  
Protocol (binding, read it first): {PROTOCOL\_LINK}  
Journal sheet (state and logs): {JOURNAL\_LINK}  
Article folder: {DRIVE\_FOLDER\_LINK}  
Repository: {OWNER}/{REPO}  
Module: {M1 | M2 | M3 | M4}  
  
1\. Load the research-integrity skill before any research step.  
2\. Read the État tab and resume at the first phase that is not done.  
3\. Log every action in the journal before moving on, one line per action in the Historique tab (date, time, phase, what was done and its result, link, who, version or hash), plus the relevant specialised tab. Keep every reviewer brief and full report in the article's review document, and every design or code version in CHANGELOG.md.  
4\. Follow the ten non-negotiable rules of the protocol.  
5\. Stop and ask me only at gate G1, at gate G2, or when a stop rule fires.  
6\. Write the manuscript in English and your messages to me in French.
### **Préenregistrement**
Draft the AsPredicted preregistration for this study from the design dossier ({DESIGN\_DOSSIER\_LINK}).  
Answer each question on the AsPredicted form in plain English.  
Say which data, if any, already exist (pilot only, excluded from confirmatory tests).  
Give the exact confirmatory test for each hypothesis, the exclusion rules, and the sample size with its justification.  
Do not include anything that is not in the design dossier.
### **Relecteur R1, fond**
You are an external referee for {JOURNAL}. You did not see how this paper was produced.  
Read the manuscript ({MANUSCRIPT\_LINK}) and the repository ({OWNER}/{REPO}).  
Find errors, unsupported claims, missing baselines or controls, and threats to validity.  
For each finding give the location, the problem, why it matters, a severity (must-fix, should-fix or minor) and a concrete fix. Do not praise.  
Begin your report with: "Internal reading by a separate AI session. Not peer review."
### **Relecteur R2, méthode et statistiques**
You are a methods and statistics referee.  
Check that every analysis matches the preregistration ({PREREG\_LINK}), that each reported number appears in results/numbers.json with the same value and rounding, that the assumptions of each model hold, and that the sample-size and power claims follow from the code.  
Re-run the analysis from tag data-v1 if needed.  
For each finding give the location, the problem, the evidence, a severity and a fix.  
Begin your report with: "Internal reading by a separate AI session. Not peer review."
### **Relecteur R3, rédaction de la revue**
You are the handling editor of {JOURNAL}.  
Using the journal's aims and scope, author guidelines and AI policy ({JOURNAL\_LINKS}), decide whether you would desk-reject this submission.  
List the reasons an editor would give, in order of weight, and the change that would remove each one.  
Check length, structure, fit with recent articles in the journal, and the AI-use declaration.  
Begin your report with: "Internal reading by a separate AI session. Not peer review."
### **Réfutation**
A reviewer raised this finding about the manuscript: {FINDING}  
Try to refute it. Check it against the manuscript, the repository and the cited sources.  
Answer "refuted", "stands" or "partly stands", with the evidence (file and line, or source passage).  
If you cannot check it, say so.
### **Vérification des citations**
For each sentence below and the source cited for it, find the passage in the full text that supports the sentence.  
Report the sentence, the source, the access level (read-directly, abstract-only or not accessible), the location of the passage (section or page), and a verdict (supports, partly supports, does not support, cannot check).  
Never mark a pair as supported from an abstract or a search snippet.  
{SENTENCE\_SOURCE\_PAIRS}
### **Codage (M3) et dépistage (M4)**
System: You are coding documents for a research study. Apply the codebook exactly as written. When the text does not give enough evidence, answer "insufficient evidence" rather than guessing. Return JSON only, following the schema.  
User: Codebook: {CODEBOOK}  
Document {DOC\_ID}: {TEXT}  
Schema: {"doc\_id": "...", "codes": \[{"code": "...", "value": "...", "evidence": "short quote from the document", "confidence": 0.0}\]}  
  
For M4 screening, use the same structure with the inclusion criteria in place of the codebook, and return for each record the decision (include, exclude or unsure) and the criterion that decides it.
## **Annexes**
### **Annexe A. Ossature du dépôt**
modele-article-ia/  
  README.md             what the study is, how to reproduce it, licences  
  PREREG.md             text of the AsPredicted preregistration and its link  
  .zenodo.json          archive metadata (annex C)  
  requirements.txt      pinned package versions  
  prompts/              frozen prompts, one file per condition  
  src/  
    pipeline.py         entry point, called with --step (annex B)  
    generate.py         model calls with budget guard, retries and logging  
    compute.py          measures computed from raw outputs  
    analyze.py          confirmatory, then exploratory analyses  
    verify\_refs.py      Crossref, OpenAlex, DataCite and Unpaywall checks  
    check\_numbers.py    manuscript numbers against results/numbers.json  
  data/raw/             JSONL outputs, never edited  
  data/derived/         computed tables  
  results/              tables, figures, numbers.json  
  logs/                 run logs, costs, hashes  
  .github/workflows/run.yml
**Double aveugle.** Pendant l'évaluation, donner aux évaluateurs une copie du dépôt sans nom, par exemple via un service de dépôt anonymisé ou une archive jointe en annexe, et ne publier la release Zenodo qu'après l'acceptation \[vue\].
### **Annexe B. Workflow GitHub Actions**
Fichier .github/workflows/run.yml. Claude vérifie au premier usage s'il existe des versions plus récentes des actions utilisées.
name: run  
  
on:  
  workflow\_dispatch:  
    inputs:  
      step:  
        description: "generate | compute | analyze | verify\_refs | all"  
        required: true  
        default: "all"  
      max\_cost\_usd:  
        description: "Budget cap for this run, in USD"  
        required: true  
        default: "10"  
  
permissions:  
  contents: write  
  
jobs:  
  run:  
    runs-on: ubuntu-latest  
    timeout-minutes: 180  
    steps:  
      - uses: actions/checkout@v4  
  
      - uses: actions/setup-python@v5  
        with:  
          python-version: "3.12"  
  
      - name: Install dependencies  
        run: pip install -r requirements.txt  
  
      - name: Run pipeline step  
        env:  
          STEP: ${{ inputs.step }}  
          MAX\_COST\_USD: ${{ inputs.max\_cost\_usd }}  
          ANTHROPIC\_API\_KEY: ${{ secrets.ANTHROPIC\_API\_KEY }}  
          OPENAI\_API\_KEY: ${{ secrets.OPENAI\_API\_KEY }}  
          MISTRAL\_API\_KEY: ${{ secrets.MISTRAL\_API\_KEY }}  
          CONTACT\_EMAIL: ${{ vars.CONTACT\_EMAIL }}  
        run: python -m src.pipeline --step "$STEP" --max-cost "$MAX\_COST\_USD"  
  
      - name: Save outputs to the repository  
        env:  
          STEP: ${{ inputs.step }}  
        run: |  
          git config user.name "github-actions\[bot\]"  
          git config user.email "41898282+github-actions\[bot\]@users.noreply.github.com"  
          git add -A  
          git diff --cached --quiet || git commit -m "run ${{ github.run\_id }}: $STEP"  
          git push  
  
      - uses: actions/upload-artifact@v4  
        if: always()  
        with:  
          name: run-${{ github.run\_id }}  
          path: |  
            logs/  
            results/
Commandes que Claude utilise pour lancer et suivre une exécution.
gh workflow run run.yml -R {OWNER}/{REPO} -f step=generate -f max\_cost\_usd=10  
gh run list -R {OWNER}/{REPO} --workflow run.yml --limit 1  
gh run watch {RUN\_ID} -R {OWNER}/{REPO}  
git pull
### **Annexe C. Métadonnées Zenodo**
Fichier .zenodo.json à la racine du dépôt.
{  
  "title": "{WORKING\_TITLE}: data, code and run logs",  
  "upload\_type": "software",  
  "description": "Materials for {ARTICLE\_CODE}: prompts, generated outputs, analysis code and run logs. See README.md to reproduce the results.",  
  "creators": \[  
    {  
      "name": "Correa Prieto, Pablo",  
      "orcid": "0009-0009-1844-7453",  
      "affiliation": "{AFFILIATION}"  
    }  
  \],  
  "license": "cc-by-4.0",  
  "keywords": \["{KEYWORD\_1}", "{KEYWORD\_2}", "{KEYWORD\_3}"\],  
  "related\_identifiers": \[  
    {"identifier": "{PREREG\_URL}", "relation": "references"}  
  \]  
}
### **Annexe D. Test de connectivité**
À lancer par Claude dans le bac à sable après l'ouverture des domaines.
import os, urllib.request  
  
email = os.environ.get("CONTACT\_EMAIL", "{CONTACT\_EMAIL}")  
urls = \[  
    "https://api.crossref.org/works?rows=1",  
    "https://api.openalex.org/works?per-page=1",  
    f"https://api.unpaywall.org/v2/10.3758/BF03195560?email={email}",  
    "https://doi.org/api/handles/10.3758/BF03195560",  
    "https://api.datacite.org/dois?query=readability\&page%5Bsize%5D=1",  
    "https://zenodo.org/api/records?size=1",  
    "https://export.arxiv.org/api/query?search\_query=all:readability\&max\_results=1",  
    "https://api.ies.ed.gov/eric/?search=readability\&rows=1\&format=json",  
\]  
for url in urls:  
    try:  
        with urllib.request.urlopen(url, timeout=20) as r:  
            print(r.status, url)  
    except Exception as e:  
        print("FAIL", getattr(e, "code", ""), url, e)
### **Annexe E. Formats de journal et formules à éviter**
Formats repris de la compétence research-integrity, en anglais comme dans le journal de bord.
Claim: one sentence  
Status: proved | computer-assisted | cited | numerical | conjectured  
Access: read-directly | abstract-only | search-summary | repository | reasoning  
Source: file and line, citation, or none  
Not claimed: what this sentence does not show  
  
Query: "exact query"   Date: YYYY-MM-DD  
Opened: sources actually read  
Blocked: sources that failed to load, were paywalled, or were refused  
Stopped: no | yes (budget, timeout, or a connector that did not load)  
Conclusion: one sentence, within what was opened  
  
Check: program, for claim  
Binds: commit, file hash, or source version  
Success match: exact pattern that failure output does not match  
Failure control: the fault, why it must fail. Observed: fail or pass  
Number taken from: named field of this run
|  |  |
| :- | :- |
| **À éviter** | **À écrire** |
| This is the first study to... | Searches of X and Y found no earlier study. Z could not be accessed. |
| No prior work exists | No prior work was found in the sources searched (listed in the supplement). |
| Verified (sans programme) | Checked by check\_numbers.py, which fails on a planted wrong value. |
| Independently reviewed | Rien dans le manuscrit. Les lectures internes par IA ne sont pas une évaluation par les pairs. |

### **Annexe F. Instancier le modèle pour un article**
1.  Créer le dossier {NN} 📄 ART {N} {NOM} sous 01 📄 ARTICLES, avec les sous-dossiers habituels.
2.  Copier le journal modèle dans ce dossier et le renommer en Journal de bord ART {N} CURRENT.
3.  Créer le dépôt GitHub à partir du modèle, ajouter les secrets nécessaires et la variable CONTACT\_EMAIL, puis activer le dépôt dans Zenodo.
4.  Créer le document 00 Reprendre ici, que Claude tiendra à jour.
5.  Ajouter une ligne dans Suivi des articles (CURRENT).
6.  Créer deux tâches Todoist, une pour G1 et une pour G2, et un bloc 🍇 GRAPE pour la fenêtre de travail.
7.  Ouvrir une conversation dans le projet Claude de l'article et coller le prompt de démarrage.
8.  Créer dans 04 🧪 Protocole et instruments le document des relectures de l'article, qui recevra chaque consigne et chaque rapport complet, et commencer l'onglet Historique du journal dès la première action.
## **Sources consultées le 25.10.2026**
  - [Aide claude.ai, Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude) (réglages Capabilities et accès réseau).
  - [Résumé des lignes directrices IA de Wiley, Enago](https://www.enago.jp/responsible-ai-movement/publisher-ai-guidelines/wiley-ai-guidelines).
  - [CASRAI, déclaration de l'IA générative dans les publications (2026)](https://casrai.org/news/genai-disclosure-scholarly-authorship-2026).
  - [Elsevier, politiques sur l'IA générative pour les revues](https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals).
  - [AsPredicted](https://aspredicted.org/).
  - [01 Doctorat, fiches par article (CURRENT)](https://docs.google.com/document/d/1hdkKmNAHjYznmLxdECwtVTdj4CNjLRxFNhf-HsOb1M0/edit), pour la date OSF et le second dépisteur.
  - Test de connectivité et messages d'erreur des connecteurs Scite et Elicit, bac à sable de Claude, 25.10.2026.

