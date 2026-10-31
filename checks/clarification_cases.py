# -*- coding: utf-8 -*-
"""Cases for checks/clarifications.py. Written by the v0.4.1 confirmation session (claude-sonnet-5-5,
25.10.2026) as N2 and N4 of its check; copied unchanged from its n2_n4_cases.py.
CLARIF: requests for clarification, expected to be excluded. GENUINE: genuine texts whose first lines
come close to a refusal phrase, expected to be kept."""

STORY = ("Le loup regarde la forêt. Il cherche un abri pour la nuit. La pluie tombe sur les arbres. "
         "Un petit renard dort sous une grande racine, et le loup le regarde sans bruit. ")


def v(mod, text):
    r = verdict(mod, lex, text)
    if r["excl"] == "refusal":
        return "EXCL"
    if r["excl"]:
        return r["excl"][:6]
    return "kept+FLAG" if r["flag"] else "kept"


# ---- N2: clarifications, 25 to 40 words each, written for this check -----------------------------------------
CLARIF = [
    # new opener "navré"
    ("N2 navré, ligne 1", "Navré, je ne connais pas le niveau 5H. Pourriez-vous m'indiquer l'âge des élèves pour que j'écrive une histoire sur les volcans adaptée à leur lecture ?"),
    ("N2 je suis navrée mais", "Je suis navrée, mais je ne sais pas à quel âge correspond 5P en Suisse. Pourriez-vous me le préciser avant que j'écrive le texte sur les abeilles ?"),
    ("N2 navré de vous décevoir", "Navré de vous décevoir, mais je ne connais pas la désignation 5H. Pouvez-vous m'indiquer l'âge des élèves pour que j'adapte le vocabulaire du texte sur la mer ?"),
    ("N2 bold navré", "**Navré !**\nJe ne connais pas la désignation 5P. Pourriez-vous m'indiquer l'âge des élèves pour que j'adapte le vocabulaire du texte sur la mer et la longueur des phrases ?"),
    # unlisted openers, vous
    ("N2 pour écrire, pourriez-vous préciser", "Pour écrire un texte adapté, pourriez-vous préciser à quel âge correspond 5H ? Je pourrai alors proposer une histoire sur les volcans avec un vocabulaire simple."),
    ("N2 s'agit-il de (label)", "S'agit-il d'élèves de 5H au sens du système HarmoS, c'est-à-dire de 8 à 9 ans ? Dites-moi et j'écrirai une histoire sur les volcans adaptée à ces élèves."),
    ("N2 quel âge ont (label)", "Quel âge ont les élèves de 5P ? Je voudrais adapter le vocabulaire et la longueur de l'histoire sur les volcans à leur niveau, mais je ne connais pas bien cette désignation."),
    ("N2 excusez-moi, label in 2nd sentence", "Excusez-moi, je voudrais être sûr de bien adapter le texte. Que signifie 5H pour vous ? Un âge, ou une classe du système scolaire suisse ? Je commencerai ensuite."),
    ("N2 hmm, no label", "Hmm, je ne suis pas sûr de bien comprendre le niveau demandé. Si vous pouvez me donner l'âge des élèves, je pourrai écrire une histoire sur les volcans bien adaptée."),
    ("N2 avant de commencer, no label", "Avant de commencer, j'aimerais savoir quel âge ont les élèves et quelle longueur vous souhaitez pour le texte sur les volcans. Cela m'aiderait à choisir les mots justes."),
    ("N2 label in 2nd line, no question mark", "Je voudrais adapter le texte au bon niveau.\nPouvez-vous me dire à quel âge correspondent les élèves de 5H en Suisse romande, afin que j'écrive une histoire sur les volcans."),
    # tu forms (the prompt is written with tu: "Écris ...", so a model may answer with tu)
    ("N2/N4 tu: Pourrais-tu préciser (no me)", "Pourrais-tu préciser ce que signifie 5H ? Je voudrais écrire une histoire sur les volcans qui convienne bien à l'âge des élèves, mais je ne connais pas ce niveau."),
    ("N2/N4 tu: Peux-tu préciser (no me)", "Peux-tu préciser l'âge des élèves de 5H ? Je pourrai alors écrire une histoire sur les volcans avec un vocabulaire adapté et des phrases courtes pour eux."),
    ("N2/N4 tu: Peux-tu préciser, no label", "Peux-tu préciser l'âge des élèves et la longueur souhaitée ? Je pourrai alors écrire une histoire sur les volcans avec un vocabulaire adapté et des phrases courtes pour eux."),
    ("N2/N4 tu: Pourrais-tu me donner", "Pourrais-tu me donner l'âge des élèves de 5H ? Je pourrai alors écrire une histoire sur les volcans avec un vocabulaire adapté et des phrases courtes pour eux, promis."),
    ("N2/N4 tu: Pourrais-tu m'indiquer", "Pourrais-tu m'indiquer l'âge des élèves de 5H ? Je pourrai alors écrire une histoire sur les volcans avec un vocabulaire adapté et des phrases courtes pour eux, promis."),
    ("N2/N4 tu: Peux-tu me dire l'âge", "Peux-tu me dire l'âge des élèves ? Je pourrai alors écrire une histoire sur les volcans avec un vocabulaire adapté et des phrases courtes pour eux, promis."),
    ("N2/N4 tu: Peux-tu me dire quel âge", "Peux-tu me dire quel âge ont les élèves de 5H ? Je pourrai alors écrire une histoire sur les volcans avec un vocabulaire adapté et des phrases courtes pour eux."),
    ("N2/N4 tu: Qu'entends-tu exactement par", "Qu'entends-tu exactement par 5H ? Je voudrais écrire une histoire sur les volcans qui convienne bien à l'âge des élèves, mais je ne connais pas bien ce niveau scolaire."),
    ("N2/N4 tu: Tu veux dire quel âge", "Tu veux dire quel âge, avec 5H ? Je voudrais écrire une histoire sur les volcans qui convienne bien aux élèves, mais je ne connais pas bien ce niveau scolaire en Suisse."),
    ("N2 tu: Dis-moi quel âge", "Dis-moi quel âge ont les élèves de 5H et je pourrai écrire une histoire sur les volcans avec un vocabulaire adapté et des phrases courtes pour eux, sans problème."),
]
# ---- N4: genuine texts that start (title + first body line) with a phrase close to a refusal -----------------
GENUINE = [
    ("N4 doc hook Qu'entends-tu", "Les bruits de la forêt\nQu'entends-tu quand tu marches dans la forêt ? Le vent, un geai, un écureuil qui saute. " + STORY),
    ("N4 doc hook Qu'entends-tu par (mot)", "Le mot volcan\nQu'entends-tu par le mot « volcan » ? C'est une montagne qui crache du feu et de la fumée. " + STORY),
    ("N4 doc hook Peux-tu dire", "Les araignées\nPeux-tu dire combien de pattes a une araignée ? Elle en a huit, et deux pinces. " + STORY),
    ("N4 doc hook Peux-tu me dire combien", "Les araignées\nPeux-tu me dire combien de pattes a une araignée ? Elle en a huit, et deux pinces. " + STORY),
    ("N4 doc hook Pourrais-tu citer", "Les oiseaux\nPourrais-tu citer trois oiseaux qui migrent en automne ? Voici la réponse. " + STORY),
    ("N4 story 1st person Malheureusement, j'ai", "Mon doudou\nMalheureusement, j'ai perdu mon doudou à l'école. Je le cherche partout, sous les tables et dans la cour. " + STORY),
    ("N4 story Malheureusement, je suis", "Le petit hérisson\nMalheureusement, je suis trop petit pour traverser la rue, dit le hérisson. " + STORY),
    ("N4 story Malheureusement, il pleuvait", "La sortie\nMalheureusement, il pleuvait ce matin-là. " + STORY),
    ("N4 doc Malheureusement, il n'y a pas (neige)", "La neige\nMalheureusement, il n'y a pas de neige tous les hivers dans les petites villes de plaine. " + STORY),
    ("N4 doc Malheureusement, il n'existe plus (dino)", "Les dinosaures\nMalheureusement, il n'existe plus de dinosaures vivants aujourd'hui, mais on retrouve leurs os. " + STORY),
    ("N4 story Malheureusement, je ne trouve plus", "Le chat perdu\nMalheureusement, je ne trouve plus mon chat, dit Léa en pleurant. " + STORY),
    ("N4 story Navré, 1st line (character)", "Le renard poli\nNavré, le renard marcha sur la queue du hibou sans le vouloir. " + STORY),
    ("N4 story Désolé, le (character)", "Le lapin\nDésolé, le lapin n'avait pas fait exprès de casser la tasse. " + STORY),
    ("N4 story Je ne suis pas sûre", "Le grand saut\nJe ne suis pas sûre d'avoir envie de sauter dans l'eau froide, pense Léa. " + STORY),
    ("N4 doc vous hook Pouvez-vous expliquer", "Les volcans\nPouvez-vous expliquer pourquoi un volcan crache du feu ? Voici la réponse. " + STORY),
    ("N4 doc vous hook Savez-vous", "Les volcans\nSavez-vous pourquoi un volcan crache du feu ? Voici la réponse. " + STORY),
]
