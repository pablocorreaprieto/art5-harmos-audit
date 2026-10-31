# -*- coding: utf-8 -*-
"""Hand-written answers of the kind current chat models give to
'Écris {une histoire à lire | un texte documentaire à lire} pour des élèves {label}, sur le thème {topic}.
 Réponds seulement avec un titre et le texte.'
Each answer is a list of pieces (kind, text). kinds:
  title  = the title line (rendered as given, may carry markdown)
  body   = a genuine text line that must survive cleaning and be measured
  meta   = a preface/closing line addressed to the user, that should be removed (R2b)
  label  = a label line ('Titre :', 'Texte :') that should disappear
  rule   = a markdown horizontal rule or other non-text decoration (ignored by the check)
'plausible' = what I would expect a current chat model to produce at a non-negligible rate (my judgement, inference);
'edge'      = constructed to probe a rule, would be rare in practice (inference).
Pieces are joined by a blank line, except consecutive 'body' pieces flagged 'tight' which are joined by a newline.
Written by the v0.4 confirmation session (claude-sonnet-5-5, 25.10.2026), used unchanged.
"""
A = []
def add(id, kind, plaus, genre, pieces, note=""):
    A.append(dict(id=id, kind=kind, plaus=plaus, genre=genre, pieces=pieces, note=note))

# ---------- stories ----------
add("S01", "story", "plausible", "story", [
 ("title", "# Le Secret du Volcan Endormi"),
 ("body", "Il était une fois un petit village au pied d'une grande montagne. Les habitants l'appelaient Grand-Père Feu, car, il y a très longtemps, la montagne avait craché des flammes."),
 ("body", "Léa, une fillette de huit ans, adorait cette montagne. Chaque matin, elle montait sur le chemin de pierre pour écouter le volcan respirer."),
 ("body", "— Pourquoi le volcan dort-il ? demanda-t-elle à sa grand-mère."),
 ("body", "— Parce qu'il est fatigué, répondit la vieille dame en souriant. Il a travaillé pendant des milliers d'années."),
 ("body", "Un soir, la terre se mit à trembler doucement. Léa courut dans le village pour prévenir tout le monde. Les habitants se réunirent sur la place, et le maire leur dit de rester calmes."),
 ("body", "Le lendemain, un petit nuage de fumée sortit du sommet. Le volcan avait fait un grand bâillement, c'était tout. Léa éclata de rire, et le village fit une fête."),
 ("body", "Depuis ce jour, chaque enfant sait qu'il faut écouter la montagne avec respect."),
])
add("S02", "story", "plausible", "story", [
 ("title", "**La petite abeille qui avait peur de voler**"),
 ("body", "Dans une ruche toute dorée vivait une petite abeille nommée Mila. Ses sœurs volaient déjà de fleur en fleur, mais Mila restait toujours au bord de la ruche."),
 ("body", "« Viens avec nous ! » lui dirent ses amies. « Je n'ose pas », répondit Mila en baissant ses antennes."),
 ("body", "Un matin, une grosse goutte de pluie tomba près d'elle. Mila fit un petit saut, puis un deuxième, et soudain elle sentit le vent sous ses ailes. « Je vole ! » cria-t-elle, toute surprise."),
 ("body", "Ce jour-là, Mila découvrit un champ de lavande et rapporta beaucoup de nectar à la ruche. Ses sœurs l'applaudirent."),
 ("body", "Et toi, as-tu déjà eu peur de faire quelque chose de nouveau ?"),
])
add("S03", "story", "plausible", "story", [
 ("title", "**Titre : Le réveil de Volcanus**"),
 ("label", "**Texte :**"),
 ("body", "Il était une fois un volcan nommé Volcanus qui dormait depuis cent ans. Les oiseaux faisaient leur nid sur sa tête et les chèvres broutaient l'herbe sur ses pentes."),
 ("body", "Un jour, Volcanus grogna : « Hmm, j'ai faim ! » La montagne trembla, et tous les animaux s'enfuirent."),
 ("body", "Seule la petite chèvre Blanchette resta. Elle lui apporta une botte de foin. Volcanus la goba, et il se sentit mieux."),
 ("body", "Depuis ce jour, Volcanus dort paisiblement et Blanchette lui apporte du foin chaque soir."),
])
add("S04", "story", "plausible", "story", [
 ("title", "Le renard et la lune"),
 ("body", "Une nuit d'hiver, un petit renard sortit de son terrier. La lune brillait au-dessus des sapins, ronde et blanche comme un fromage."),
 ("body", "– Je vais l'attraper, se dit le renard."),
 ("body", "Il grimpa sur la colline, puis sauta aussi haut qu'il put. Mais la lune restait toujours aussi loin."),
 ("body", "– Que fais-tu là ? demanda un vieux hibou perché sur une branche."),
 ("body", "– Je veux goûter la lune, répondit le renard."),
 ("body", "Le hibou rit doucement. Il lui montra la lune dans l'eau de la mare. Le renard y plongea la patte, et la lune se brisa en mille morceaux brillants."),
 ("body", "Fin"),
])
add("S05", "story", "plausible", "story", [
 ("title", "Le train de Max"),
 ("body", "Max prend le train pour la première fois. Il a un grand sac rouge et un sandwich au fromage."),
 ("body", "- Regarde, maman, les vaches ! dit Max."),
 ("body", "- Oui, elles sont belles, répond sa maman."),
 ("body", "Le train passe dans un tunnel. Il fait tout noir. Max serre la main de sa maman. Puis la lumière revient, et le lac apparaît, bleu et brillant."),
 ("body", "- C'est le plus beau voyage du monde ! s'écrie Max."),
])
add("S06", "story", "plausible", "story", [
 ("title", "Les excuses de l'ours"),
 ("body", "Un matin, l'ours Bruno marcha sur la queue du petit écureuil Noisette. Noisette poussa un cri."),
 ("body", "– Désolé, petit écureuil, dit l'ours. Je ne t'avais pas vu."),
 ("body", "– Je ne peux pas dormir avec ce bruit, grogna le hérisson derrière un buisson."),
 ("body", "Pour se faire pardonner, Bruno apporta des noisettes à tout le monde. Ce soir-là, la forêt retrouva son calme."),
])
add("S07", "story", "plausible", "story", [
 ("title", "« Le secret du vieux chêne »"),
 ("body", "Au bord d'un chemin se dressait un très vieux chêne. Les enfants du village jouaient souvent sous ses branches."),
 ("body", "« Je ne peux pas t'aider à grimper », dit Paul à son petit frère. « Mais je peux te montrer le trou secret dans le tronc. »"),
 ("body", "Dans le trou, ils trouvèrent une vieille boîte en fer. Elle contenait une lettre et une bille bleue. La lettre disait : « Merci d'avoir pris soin de cet arbre. »"),
 ("body", "Depuis ce jour, Paul et son frère viennent chaque semaine arroser les racines du chêne."),
])
add("S08", "story", "plausible", "story", [
 ("title", "## Le petit pompier courageux"),
 ("body", "Tom rêvait d'être pompier. Tous les samedis, il visitait la caserne avec son oncle."),
 ("body", "Un jour, l'alarme sonna. Tom monta dans le grand camion rouge. La sirène retentit dans toute la ville."),
 ("body", "Devant une petite maison, un chat était coincé sur un toit. Les pompiers dressèrent une échelle. Tom tint l'échelle bien fort pendant que son oncle montait chercher le chat."),
 ("body", "« Bravo, Tom ! » dit le chef. Le chat ronronna dans les bras du petit garçon."),
 ("body", "Morale : le courage, c'est aussi aider les autres sans avoir peur."),
])
add("S09", "story", "plausible", "story", [
 ("meta", "Bien sûr ! Voici une histoire sur les volcans pour des élèves de 5H :"),
 ("title", "**Le volcan qui avait mal au ventre**"),
 ("body", "Il était une fois un volcan qui avait très mal au ventre. Il grondait, il grognait et il fumait de partout."),
 ("body", "Les animaux de la forêt se réunirent autour de lui. Le vieux hibou dit : « Il a mangé trop de cailloux brûlants ! »"),
 ("body", "La taupe creusa un long tunnel pour laisser sortir la chaleur. Le volcan poussa un grand soupir, et une jolie fumée blanche monta vers le ciel."),
 ("body", "Le volcan se sentit enfin mieux et il remercia tous ses amis."),
 ("meta", "N'hésitez pas à me demander une autre version de cette histoire pour vos élèves !"),
])
add("S10", "story", "plausible", "story", [
 ("meta", "Voici une histoire pour des élèves de 8 à 9 ans :"),
 ("title", "# La cabane dans les bois"),
 ("body", "Zoé et Lucas ont construit une cabane dans les bois avec des branches et de la mousse. C'est leur cachette secrète."),
 ("body", "Un soir d'orage, ils y trouvent un petit hérisson tout mouillé. Zoé l'enveloppe dans son écharpe. Lucas lui apporte un peu de lait chaud."),
 ("body", "Le lendemain, le soleil revient. Le hérisson repart dans la forêt, mais chaque soir il revient dire bonjour."),
 ("meta", "J'espère que cette histoire plaira à vos élèves !"),
])
add("S11", "story", "plausible", "story", [
 ("title", "# Le dragon de la montagne"),
 ("rule", "---"),
 ("body", "Au sommet d'une haute montagne vivait un petit dragon vert. Il ne savait pas encore cracher du feu, il crachait seulement de petites bulles."),
 ("body", "Les autres dragons se moquaient de lui. Alors il partit explorer le monde et rencontra une fée du vent."),
 ("body", "La fée lui apprit à respirer lentement. Un matin, une flamme jaillit, douce et chaude, juste assez pour faire cuire une châtaigne."),
 ("rule", "---"),
 ("body", "Fin"),
])
add("S12", "story", "plausible", "story", [
 ("title", "**Mamie Rose et la fête de famille**"),
 ("body", "Samedi, toute la famille se retrouve chez Mamie Rose. Il y a des cousins, des oncles, des tantes et même un chien."),
 ("body", "Dans la cuisine, Mamie prépare un énorme gâteau au chocolat. Léo goûte un peu de crème en cachette."),
 ("body", "– Léo, je t'ai vu ! dit Mamie en riant."),
 ("body", "Le soir, tout le monde chante autour de la table. Léo s'endort sur les genoux de son grand-père, le ventre plein et le cœur heureux."),
])
add("S13", "story", "plausible", "story", [
 ("title", "Titre : Le petit bateau"),
 ("body", "Un petit bateau bleu vivait dans un grand port. Il rêvait de traverser la mer, mais il était trop petit."),
 ("body", "Un jour, une grosse tempête arriva. Tous les grands bateaux restèrent au port. Le petit bateau, lui, glissa entre les vagues et ramena un pêcheur sain et sauf."),
 ("body", "Depuis, tout le monde sait qu'être petit n'empêche pas d'être courageux."),
])
add("S14", "story", "plausible", "story", [
 ("title", "## Les bonnes manières"),
 ("body", "Lina a un grand jardin. Chaque matin, elle arrose ses fleurs avec un petit arrosoir jaune."),
 ("body", "Un jour, le chat du voisin entre dans le jardin et écrase une rose. Lina est triste."),
 ("body", "— Désolé, miaule le chat, je ne voulais pas faire de mal."),
 ("body", "Lina sourit. Elle lui donne un bol de lait. Depuis ce jour, le chat et Lina sont les meilleurs amis du quartier."),
])
add("S15", "story", "plausible", "story", [
 ("title", "# Le trésor de la rivière"),
 ("body", "Chaque été, Hugo pêche au bord de la rivière avec son grand-père. Cette année, il trouve une pierre brillante dans le sable."),
 ("body", "— Est-ce un diamant ? demande-t-il."),
 ("body", "— Non, c'est mieux, répond son grand-père. C'est un morceau de rivière qui a voyagé très longtemps."),
 ("body", "Hugo garde la pierre dans sa poche. Quand il la touche, il entend presque l'eau chanter."),
 ("body", "Et vous, quel objet de la nature garderiez-vous dans votre poche ?"),
], note="ends with a 'vous' question to the reader (genuine text)")
add("S16", "story", "edge", "story", [
 ("title", "Le voyage de Clara"),
 ("body", "Clara monte dans le train avec sa valise bleue. Elle va voir sa tante qui habite près de la mer."),
 ("body", "Pendant le voyage, elle regarde les champs, les ponts et les petites gares. Un monsieur lui offre une pomme."),
 ("body", "Quand le train s'arrête, Clara voit sa tante sur le quai. Elle court vers elle et la serre fort dans ses bras."),
 ("body", "Voulez-vous savoir ce que Clara a fait au bord de la mer ? Alors lisez la suite demain !"),
], note="teaser ending with a 'vous' question (genuine text), same shape as a meta closing")

# ---------- documentary texts ----------
add("D01", "doc", "plausible", "info", [
 ("title", "# Les abeilles, des insectes précieux"),
 ("body", "Les abeilles sont des insectes qui vivent en groupe dans une ruche. Elles butinent les fleurs pour récolter le nectar et le pollen."),
 ("body", "## Qui vit dans la ruche ?"),
 ("body", "Dans une ruche, on trouve trois sortes d'abeilles :"),
 ("body", "- **La reine** : elle pond les œufs."),
 ("body", "- **Les ouvrières** : elles fabriquent le miel et nettoient la ruche."),
 ("body", "- **Les faux-bourdons** : ce sont les mâles."),
 ("body", "**Le savais-tu ?** Pour fabriquer un seul pot de miel, les abeilles doivent visiter des millions de fleurs !"),
 ("body", "Alors, la prochaine fois que tu verras une abeille, souviens-toi de tout ce qu'elle fait pour nous."),
], note="bullets tight")
add("D02", "doc", "plausible", "info", [
 ("title", "**Le cycle de l'eau**"),
 ("body", "L'eau voyage sans cesse autour de la Terre. Ce voyage s'appelle le cycle de l'eau."),
 ("body", "Le soleil chauffe la mer, les lacs et les rivières. L'eau se transforme en vapeur et monte dans le ciel. Là-haut, il fait froid : la vapeur devient de petites gouttes qui forment les nuages."),
 ("body", "Quand les gouttes deviennent trop lourdes, elles tombent sous forme de pluie, de neige ou de grêle. L'eau coule ensuite dans les rivières et retourne à la mer."),
 ("body", "Et toi, sais-tu combien de fois la même goutte d'eau a déjà fait ce voyage ?"),
])
add("D03", "doc", "plausible", "info", [
 ("title", "Les volcans"),
 ("body", "Un volcan est une montagne qui crache du feu. Sous la terre, il y a une roche très chaude et liquide : le magma."),
 ("body", "Quand le magma monte, il sort par le cratère. On l'appelle alors de la lave. La lave coule sur les pentes et refroidit en devenant de la roche dure."),
 ("body", "Il existe des volcans actifs, qui peuvent entrer en éruption, et des volcans éteints, qui dorment pour toujours."),
 ("body", "En Europe, l'Etna, en Sicile, est l'un des volcans les plus actifs."),
])
add("D04", "doc", "plausible", "info", [
 ("title", "# Les oiseaux migrateurs"),
 ("body", "Chaque automne, des millions d'oiseaux quittent nos régions. Ils partent vers des pays plus chauds où ils trouvent de la nourriture pendant l'hiver."),
 ("body", "On appelle ce grand voyage la migration. Les hirondelles, les cigognes et les oies sauvages migrent. Certaines volent plus de dix mille kilomètres !"),
 ("body", "Pour ne pas se perdre, les oiseaux utilisent le soleil, les étoiles et même le champ magnétique de la Terre. Au printemps, ils reviennent."),
])
add("D05", "doc", "plausible", "info", [
 ("meta", "Voici un texte documentaire sur les pompiers, adapté à des élèves de 6H :"),
 ("title", "**Les pompiers, des héros du quotidien**"),
 ("body", "Les pompiers éteignent les incendies, mais ils font beaucoup d'autres choses. Ils secourent des personnes blessées, aident lors des inondations et sauvent même des animaux."),
 ("body", "Dans la caserne, les pompiers s'entraînent chaque jour. Ils vérifient leurs camions, leurs tuyaux et leurs échelles."),
 ("body", "Quand l'alarme sonne, ils enfilent leur casque et leur veste en quelques secondes. Le numéro à appeler en Suisse est le 118."),
 ("meta", "Si vous souhaitez, je peux aussi proposer des questions de compréhension."),
])
add("D06", "doc", "plausible", "info", [
 ("title", "## La neige en montagne"),
 ("body", "La neige est faite de petits cristaux de glace qui se forment dans les nuages. Chaque flocon a une forme différente."),
 ("body", "En montagne, la neige peut devenir dangereuse. Quand elle glisse d'un coup le long d'une pente, on parle d'avalanche."),
 ("body", "Les gardiens de pistes surveillent la neige tous les jours. Ils utilisent parfois des chiens pour retrouver des personnes ensevelies."),
 ("body", "Si tu vas à la montagne l'hiver, écoute toujours les consignes des guides."),
])
add("D07", "doc", "plausible", "info", [
 ("title", "# Le recyclage"),
 ("body", "Chaque jour, nous jetons beaucoup d'objets. Mais beaucoup d'entre eux peuvent avoir une seconde vie."),
 ("body", "Le verre, le papier, l'aluminium et certains plastiques sont triés puis transformés en objets neufs. Ainsi, on économise de l'énergie et on protège la nature."),
 ("body", "**À retenir :** trier ses déchets, c'est un petit geste qui aide beaucoup la planète."),
 ("body", "Bonne découverte !"),
])
add("D08", "doc", "plausible", "info", [
 ("title", "Les châteaux forts"),
 ("body", "Au Moyen Âge, les seigneurs vivaient dans des châteaux forts. Ces grands bâtiments en pierre les protégeaient des attaques."),
 ("body", "Un château fort avait de hauts murs, des tours et un fossé rempli d'eau. Pour entrer, il fallait passer sur un pont-levis."),
 ("body", "Voici les principales parties d'un château :"),
 ("body", "1. Le donjon, la grande tour centrale."),
 ("body", "2. La cour, où vivaient les paysans et les soldats."),
 ("body", "3. Les remparts, qui entourent le château."),
], note="'Voici ...:' is the 2nd line (after the title), a genuine intro line")
add("D09", "doc", "plausible", "info", [
 ("title", "# Les dinosaures"),
 ("body", "Il y a très longtemps, bien avant les humains, des animaux gigantesques vivaient sur la Terre : les dinosaures."),
 ("body", "Certains mangeaient des plantes, comme le diplodocus. D'autres mangeaient de la viande, comme le tyrannosaure."),
 ("body", "Les dinosaures ont disparu il y a environ soixante-six millions d'années. Les scientifiques pensent qu'un énorme météorite est tombé sur la Terre."),
 ("body", "Aujourd'hui, les oiseaux sont les descendants des dinosaures."),
 ("meta", "Souhaitez-vous que j'ajoute quelques questions pour vérifier la compréhension du texte ?"),
])
add("D10", "doc", "plausible", "info", [
 ("title", "**Le marché du samedi**"),
 ("body", "Chaque samedi matin, la place du village se remplit de petits stands. Les marchands y vendent des fruits, des légumes, du fromage et du pain."),
 ("body", "Savez-vous d'où viennent tous ces produits ? La plupart viennent de fermes situées à quelques kilomètres du village."),
 ("body", "Acheter au marché, c'est soutenir les paysans de la région et manger des produits de saison."),
], note="'vous' question to the reader in the 2nd body line, 'Savez-vous' is not in META_RE")

# ---------- edges for the new rules ----------
add("E01", "edge", "edge", "story", [
 ("meta", "Voici une histoire pour tes élèves de 5H sur les volcans."),
 ("title", "Le volcan qui toussait"),
 ("body", "Un petit volcan toussait beaucoup. Il crachait de la fumée grise dans le ciel bleu. Les oiseaux s'éloignaient de lui."),
 ("body", "Un jour, une petite fille lui apporta une tisane au miel. Le volcan but une gorgée et cessa de tousser."),
])
add("E02", "edge", "edge", "story", [
 ("meta", "Voici une histoire sur les volcans."),
 ("title", "Le volcan qui toussait"),
 ("body", "Un petit volcan toussait beaucoup. Il crachait de la fumée grise dans le ciel bleu. Les oiseaux s'éloignaient de lui."),
 ("body", "Un jour, une petite fille lui apporta une tisane au miel. Le volcan but une gorgée et cessa de tousser."),
], note="'Voici' preface without colon and without audience word")
add("E03", "edge", "edge", "story", [
 ("body", "Voici Tom, un élève de CM1 qui rêvait de voler. Chaque matin, il regardait les oiseaux dans la cour de l'école et il imaginait des ailes dans son dos."),
 ("body", "Un jour, il construisit un grand cerf-volant avec sa maîtresse. Le vent le souleva, et Tom courut dans la cour en riant."),
 ("title", "x"),
], note="untitled story whose first paragraph opens with 'Voici' + a school word; also tests title-less answers (title piece is a dummy and not rendered)")
add("E04", "edge", "edge", "story", [
 ("meta", "Voici ton histoire :"),
 ("rule", "---"),
 ("title", "# Le secret du volcan"),
 ("body", "Il était une fois un volcan qui gardait un secret. Chaque nuit, il murmurait à la lune des mots que personne ne comprenait."),
 ("body", "Un jour, une petite fille s'approcha et écouta. Le volcan chantait une berceuse."),
], note="horizontal rule between the preface and the markdown title")
add("E05", "edge", "edge", "doc", [
 ("title", "Les volcans"),
 ("body", "Un volcan est une montagne qui crache du feu. Le magma monte depuis l'intérieur de la Terre et sort par le cratère."),
 ("body", "Quand le magma sort, on l'appelle de la lave. Elle refroidit et devient de la roche noire."),
 ("body", "Note : le magma s'appelle de la lave seulement quand il est sorti du volcan."),
], note="genuine last line that opens with 'Note :'")
add("E06", "edge", "edge", "doc", [
 ("body", "Voici les trois types de volcans :"),
 ("body", "- Les volcans actifs, qui peuvent entrer en éruption."),
 ("body", "- Les volcans endormis, qui n'ont pas craché depuis longtemps."),
 ("body", "- Les volcans éteints, qui ne se réveilleront plus."),
 ("title", "x"),
], note="no title; first line is a genuine intro ending with a colon")
add("E07", "edge", "edge", "doc", [
 ("title", "Le corps humain"),
 ("body", "Ton corps est une machine incroyable. Ton cœur bat plus de cent mille fois par jour et envoie le sang dans tout ton corps."),
 ("body", "Tes poumons respirent l'air. Tes muscles te permettent de courir, de sauter et de jouer."),
 ("body", "Si vous voulez en savoir plus sur le corps humain, allez visiter un musée des sciences."),
], note="closing line opens with 'Si vous voulez', addressed to the pupils, not the teacher")
add("E08", "edge", "edge", "doc", [
 ("title", "Les fourmis"),
 ("body", "Pouvez-vous imaginer un animal qui porte cinquante fois son poids ? C'est ce que fait la fourmi, tous les jours."),
 ("body", "Les fourmis vivent en grandes familles dans des fourmilières. Chaque fourmi a un travail : chercher la nourriture, soigner les petits ou garder l'entrée."),
 ("body", "Elles communiquent grâce à des odeurs que l'on appelle des phéromones."),
], note="'vous' hook in the first body line (flag_meta region)")
add("E09", "edge", "edge", "story", [
 ("title", "Mon premier jour d'école"),
 ("body", "Je ne peux pas dormir. Demain, c'est mon premier jour d'école et mon cœur bat très fort."),
 ("body", "Maman entre dans ma chambre et s'assoit sur mon lit. Elle me raconte son premier jour, il y a longtemps."),
 ("body", "Alors je ferme les yeux et je souris, parce que je sais que tout va bien se passer."),
], note="first-person story whose first body line opens 'Je ne peux pas dormir' (self-test only has it as a title)")
add("E10", "edge", "edge", "story", [
 ("title", "La fête des lumières"),
 ("body", "Malheureusement, j'ai oublié mes gants ce matin. Il fait très froid sur la place du village et mes doigts sont tout bleus."),
 ("body", "Heureusement, ma voisine me prête les siens. Ensemble, nous regardons les lanternes monter dans le ciel."),
], note="first-person story whose first body line opens 'Malheureusement, j'ai'")
add("E11", "edge", "edge", "doc", [
 ("title", "Les animaux de la forêt"),
 ("body", "Qu'entends-tu quand tu marches dans la forêt ? Le vent dans les feuilles, le cri d'un geai, le bruit léger d'un écureuil qui saute de branche en branche."),
 ("body", "La forêt est la maison de nombreux animaux : le chevreuil, le renard, le sanglier et le hibou."),
 ("body", "Chacun a sa façon de vivre. Le renard chasse la nuit, le chevreuil mange de l'herbe à l'aube."),
], note="tu hook opening the first body line")
add("E12", "edge", "edge", "story", [
 ("title", "Le goûter"),
 ("body", "Aujourd'hui, Emma prépare un goûter pour ses amis. Elle sort le pain, le chocolat et un grand pot de confiture."),
 ("body", "— Peux-tu me dire où sont les assiettes ? demande Emma à son frère."),
 ("body", "— Dans le placard du haut, répond Noah."),
 ("body", "Ils mettent la table ensemble. Quand les amis arrivent, tout est prêt."),
])
add("E13", "edge", "edge", "story", [
 ("title", "La cloche de l'école"),
 ("body", "Chaque matin, la cloche de l'école sonne huit fois. Les enfants courent dans la cour."),
 ("body", "Ce matin-là, Sam arrive en retard. Il pousse la porte tout doucement."),
 ("body", "— Désolé, madame, dit-il. Mon vélo avait un pneu crevé."),
 ("body", "— Ce n'est pas grave, répond la maîtresse. Va t'asseoir."),
])
add("E14", "edge", "edge", "doc", [
 ("title", "Les saisons"),
 ("body", "Il y a quatre saisons : le printemps, l'été, l'automne et l'hiver. Chaque saison dure environ trois mois."),
 ("body", "Au printemps, les fleurs s'ouvrent. En été, il fait chaud. En automne, les feuilles tombent. En hiver, il fait froid et parfois il neige."),
 ("rule", "---"),
 ("meta", "N.B. : le vocabulaire a été simplifié pour des élèves de 5H."),
 ("meta", "(Environ 80 mots)"),
])
add("E15", "edge", "edge", "story", [
 ("title", "Le chat perdu"),
 ("body", "Un petit chat gris se perd dans la ville. Il a faim et il a froid."),
 ("body", "Une dame le trouve devant sa porte et lui donne du lait. Le chat s'endort sur un coussin."),
 ("meta", "Dites-moi si vous souhaitez une autre histoire !"),
])


# ---------- more mainstream shapes (added after the first run, to widen the plausible set) ----------
add("P01", "story", "plausible", "story", [
 ("title", "**Qui a mangé le gâteau ?**"),
 ("body", "« Qui a mangé mon gâteau ? » demanda Maman en regardant la table vide."),
 ("body", "Tom regarda ses pieds. Léa regarda le plafond. Le chien, lui, se lécha les babines."),
 ("body", "« Désolé, Maman, dit Tom enfin. Je n'ai pas pu résister. »"),
 ("body", "Maman sourit et sortit un deuxième gâteau du four. Ce jour-là, toute la famille mangea ensemble."),
])
add("P02", "story", "plausible", "story", [
 ("title", "# Le petit bonhomme de neige"),
 ("body", "— Désolé, petit bonhomme, je ne peux pas t'emmener à la maison, dit le papa. Tu vas fondre."),
 ("body", "Le bonhomme de neige resta dans le jardin. Chaque matin, le soleil se levait un peu plus tôt, et le bonhomme devenait un peu plus petit."),
 ("body", "Au printemps, il ne resta plus qu'une écharpe rouge et deux boutons noirs. Mais dans la terre, une petite fleur ouvrit ses pétales."),
])
add("P03", "doc", "plausible", "info", [
 ("title", "**Titre : Les volcans, des montagnes de feu**"),
 ("label", "**Texte :**"),
 ("body", "Les volcans sont des montagnes spéciales. À l'intérieur, la roche est si chaude qu'elle devient liquide."),
 ("body", "Quand la pression est trop forte, le volcan se réveille. C'est une éruption !"),
 ("body", "**À retenir :**"),
 ("body", "- Un volcan est une ouverture dans la croûte terrestre."),
 ("body", "- Le magma devient de la lave quand il sort."),
 ("body", "- Il existe des volcans actifs et des volcans éteints."),
])
add("P04", "doc", "plausible", "info", [
 ("title", "# Les saisons"),
 ("body", "Il y a quatre saisons dans l'année. Elles changent la nature autour de nous."),
 ("body", "## Le printemps"),
 ("body", "Au printemps, les jours rallongent. Les bourgeons s'ouvrent et les oiseaux chantent."),
 ("body", "## L'été"),
 ("body", "En été, il fait chaud. On peut se baigner dans la rivière ou manger des glaces."),
 ("body", "## En résumé"),
 ("body", "Chaque saison a sa beauté. Et toi, quelle est ta saison préférée ?"),
])
add("P05", "story", "plausible", "story", [
 ("title", "Chapitre 1 : Le départ"),
 ("body", "Ce matin, Nina et son papa partent à vélo. Le ciel est bleu. Les oiseaux chantent dans les arbres."),
 ("body", "— On va où ? demande Nina."),
 ("body", "— Au bord du lac, répond son papa. Tu vas voir, c'est magnifique."),
 ("body", "Ils pédalent longtemps. Quand ils arrivent, Nina ouvre de grands yeux : l'eau brille comme un miroir."),
])
add("P06", "story", "plausible", "story", [
 ("title", "Le cirque de la nuit"),
 ("body", "Chaque été, le cirque s'installe au bout du village. Les enfants ont le droit d'y aller une seule fois."),
 ("body", "« Regarde, le clown ! » crie Hugo en tirant la manche de sa sœur. Le clown lance trois balles, puis quatre, puis cinq."),
 ("body", "Soudain, une balle roule vers Hugo. Il la ramasse et la lance à son tour. Tout le monde applaudit."),
 ("body", "Ce soir-là, Hugo rentre à la maison avec des étoiles dans les yeux."),
])
add("P07", "doc", "plausible", "info", [
 ("title", "Les insectes"),
 ("body", "Imagine une petite bête avec six pattes, deux antennes et parfois des ailes : c'est un insecte !"),
 ("body", "Il existe plus d'un million d'espèces d'insectes. Les fourmis, les papillons, les coccinelles et les mouches en font partie."),
 ("body", "Les insectes sont très utiles. Ils pollinisent les fleurs, nourrissent les oiseaux et recyclent les feuilles mortes."),
])
add("P08", "story", "plausible", "story", [
 ("title", "Le dernier jour de l'automne"),
 ("body", "Il était une fois un vieux chêne qui perdait ses feuilles. Chaque feuille tombait en tourbillonnant et se posait sur le sol."),
 ("body", "Un petit garçon nommé Sacha les ramassait une à une. Il en fit un grand bouquet roux et doré."),
 ("body", "Quand il rentra chez lui, sa mamie lui dit : « Tu as ramené tout l'automne dans tes mains ! »"),
])
