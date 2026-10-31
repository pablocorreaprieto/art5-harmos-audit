# -*- coding: utf-8 -*-
"""Ten hand-written answers aimed at the v0.4.1 rules, of the kind a chat model may give to
'Écris {une histoire à lire | un texte documentaire à lire} pour des élèves de {label}, sur le thème {topic}.
 Réponds seulement avec un titre et le texte.'
Same piece kinds as the v0.4 battery: title, body (genuine line, must survive), meta (to be removed), rule, label.
Plausibility is my inference (no model was sampled): 'plausible' = I would expect it at a non-negligible rate,
'edge' = built to probe a rule, rare in practice.
Written by the v0.4.1 confirmation session (claude-sonnet-5-5, 25.10.2026), used unchanged.
"""
A = []


def add(id, kind, plaus, genre, pieces, note=""):
    A.append(dict(id=id, kind=kind, plaus=plaus, genre=genre, pieces=pieces, note=note))


# 1. documentary text with a closing "Note :" box about the subject, no word from the note-about-the-text list
add("N01", "doc", "plausible", "info", [
    ("title", "## Les volcans, montagnes de feu"),
    ("body", "Un volcan est une montagne qui peut cracher du feu. Sous la terre, la roche est si chaude qu'elle devient liquide. On l'appelle le magma."),
    ("body", "Quand le volcan se réveille, le magma monte dans une grande cheminée. Il sort par le cratère. Dehors, il prend le nom de lave. La lave est rouge et très chaude, mais elle devient noire en refroidissant."),
    ("body", "Il existe des volcans actifs et des volcans éteints. L'Etna, en Italie, est un volcan actif. Il crache souvent de la fumée."),
    ("body", "**Note :** un volcan éteint peut parfois se réveiller après des milliers d'années."),
], note="Note box about the subject (control, no trigger word)")

# 2. same shape, the Note box about the subject contains "niveau"
add("N02", "doc", "plausible", "info", [
    ("title", "# Les glaciers"),
    ("body", "Un glacier est comme une rivière de glace qui avance très lentement. Il se forme en montagne, là où la neige tombe en grande quantité et ne fond pas en été."),
    ("body", "Année après année, la neige s'entasse et se transforme en glace dure et bleue. Sous son propre poids, la glace glisse peu à peu vers la vallée."),
    ("body", "Aujourd'hui, avec la chaleur, beaucoup de glaciers fondent. L'eau coule dans les rivières et finit par rejoindre la mer."),
    ("body", "**Note :** quand les glaciers fondent, le niveau de la mer monte un peu plus chaque année."),
], note="Note box about the subject, contains 'niveau' (a word of the note-about-the-text list)")

# 3. history topic, "Remarque :" box about the subject containing "histoire", then a word count
add("N03", "doc", "plausible", "info", [
    ("title", "**Le chocolat**"),
    ("body", "Le chocolat vient d'un arbre qu'on appelle le cacaoyer. Cet arbre pousse dans les pays chauds et humides. Ses fruits contiennent des graines, les fèves de cacao."),
    ("body", "On fait sécher les fèves, puis on les grille et on les écrase. Avec cette pâte, on fabrique le chocolat que nous mangeons."),
    ("body", "En Suisse, on aime beaucoup le chocolat. Chaque habitant en mange plusieurs kilos par an."),
    ("body", "**Remarque :** l'histoire du chocolat commence il y a plus de trois mille ans, en Amérique centrale."),
    ("meta", "(Environ 90 mots)"),
], note="subject box with 'histoire' followed by a word-count line")

# 4. story opening with Voici + the grade label inside the story, no audience word
add("N04", "story", "edge", "story", [
    ("body", "Voici Noah, un garçon qui est en 5H cette année. Il adore les volcans et il en dessine partout, même sur ses cahiers."),
    ("body", "Un jour, la maîtresse demande à chacun d'apporter un objet de son choix. Noah réfléchit longtemps, puis il construit un volcan avec de la terre et du papier."),
    ("body", "Le lendemain, toute la classe regarde le volcan cracher une mousse rouge. Noah est très fier de lui."),
], note="untitled answer; Voici + 'en 5H' in the first paragraph")

# 5. story opening Voici l'histoire de ..., fairy-tale paragraph containing "destinée"
add("N05", "story", "edge", "story", [
    ("body", "Voici l'histoire de Mila, une princesse que personne n'attendait. Sa destinée était de garder le château, mais elle préférait explorer la forêt avec son chien."),
    ("body", "Un matin, elle rencontra un dragon tout vert qui pleurait au bord d'un ruisseau. Il avait perdu son feu."),
    ("body", "Mila lui prêta sa lanterne. Le dragon sourit, souffla dessus, et une belle flamme dorée éclaira toute la clairière."),
], note="untitled answer; Voici l'histoire de ... with 'destinée' in the same paragraph (AUDIENCE_RE lists destinée)")

# 6. story with --- around the body, a one-word ending and a word count after it
add("N06", "story", "plausible", "story", [
    ("title", "# Le petit nuage"),
    ("rule", "---"),
    ("body", "Un petit nuage gris flottait au-dessus d'un village. Il voulait faire de la pluie, mais il n'y arrivait pas."),
    ("body", "Un jour, un vent doux le poussa vers la montagne. Là, il rencontra un gros nuage noir qui lui apprit à se laisser aller."),
    ("body", "Le petit nuage ferma les yeux et pleura doucement. Les fleurs du village burent chaque goutte."),
    ("rule", "---"),
    ("body", "Fin"),
    ("meta", "(Environ 90 mots)"),
], note="rules around the body, 'Fin' kept, word count removed")

# 7. documentary text: preface with the label, rules, bold title, closing offer, rule
add("N07", "doc", "plausible", "info", [
    ("meta", "Bien sûr ! Voici un texte documentaire sur les abeilles pour des élèves de 5H :"),
    ("rule", "---"),
    ("title", "**Les abeilles, petites travailleuses**"),
    ("body", "Les abeilles vivent en grand nombre dans une ruche. Chaque abeille a son travail : certaines nettoient, d'autres gardent l'entrée, d'autres encore partent chercher du nectar."),
    ("body", "Pour fabriquer le miel, les ouvrières butinent les fleurs. Elles transportent le nectar dans leur jabot, puis le déposent dans les alvéoles de cire."),
    ("body", "Sans les abeilles, beaucoup de fruits ne pousseraient pas. Elles transportent le pollen d'une fleur à l'autre."),
    ("rule", "---"),
    ("meta", "Dites-moi si vous souhaitez une version plus courte ou des questions de compréhension."),
], note="preface + rule + title + rule + closing offer")

# 8. documentary text for pupils: tu questions, opening with 'Peux-tu me dire', closing with 'Dis-moi'
add("N08", "doc", "plausible", "info", [
    ("title", "Les araignées"),
    ("body", "Peux-tu me dire combien de pattes a une araignée ? Elle en a huit ! Les insectes, eux, n'en ont que six."),
    ("body", "Les araignées fabriquent des toiles avec un fil très fin qui sort de leur ventre. Ce fil est plus solide que l'acier, à grosseur égale."),
    ("body", "Quand un insecte touche la toile, elle tremble. L'araignée sent alors la secousse et vient attraper son repas."),
    ("body", "Dis-moi, quel est ton animal préféré ?"),
], note="tu questions: 'Peux-tu me dire' as first body line, 'Dis-moi, ...' as last line (a pupil-addressed ending)")

# 9. documentary text for pupils: tu hooks naming degrés and hours, closing tu question (controls for LABEL_Q_RE)
add("N09", "doc", "plausible", "info", [
    ("title", "# L'eau et la glace"),
    ("body", "Sais-tu à quelle température l'eau gèle ? À zéro degré ! Quand il fait plus froid, l'eau liquide devient de la glace dure."),
    ("body", "La glace est plus légère que l'eau, c'est pourquoi les glaçons flottent dans ton verre. Dans les lacs, la glace se forme en surface et protège les poissons du froid."),
    ("body", "Quand la température remonte, la glace fond et redevient de l'eau."),
    ("body", "Et toi, as-tu déjà vu de la glace fondre dans ta main ?"),
], note="'degré' + question mark in the first body line (LABEL_Q_RE lists degré)")

# 10. story with the label inside the story, in a narrative question outside quotation marks
add("N10", "story", "plausible", "story", [
    ("title", "## Un nouvel élève"),
    ("body", "Ce matin, dans la classe de 5H, il y a un nouvel élève. Comment s'appelle-t-il ? Il s'appelle Karim et il vient de très loin."),
    ("body", "— Bonjour, dit-il d'une petite voix."),
    ("body", "— Bienvenue, Karim ! répond la maîtresse. Viens t'asseoir à côté de Léa."),
    ("body", "À la récréation, Léa lui montre la cour et lui prête son ballon. Karim sourit pour la première fois."),
], note="'5H' + narrative question in the first body line, outside quotation marks and dialogue lines")
