# Daniela Villamar
# 19086
# EX3.MC Creación de Patrones Rítmicos


# Importar los módulos necesarios de la librería 'music'
from music import *

# Definir la cantidad de repeticiones del patrón de batería
repetitions = 8  # veces para repetir el patrón de batería

##### Definir la estructura de datos
# Crear la partitura (score) con un título y un tempo de 125 bpm
score = Score("Patrón de Máquina de Tambor #1", 125.0)

# Crear una parte (part) para los sonidos de batería, utilizando el canal MIDI 9 (percusión)
drumsPart = Part("Batería", 0, 9)

# Crear una frase (phrase) para cada sonido de batería (bombo, caja y hi-hat)
bassDrumPhrase = Phrase(0.0)  # bombo
snareDrumPhrase = Phrase(0.0)  # caja
hiHatPhrase = Phrase(0.0)  # hi-hat

##### Crear datos musicales
# Patrón de bombo (un bombo + un silencio de 1/4 nota) x 4 = 2 compases
bassPitches = [BDR, REST] * 4
bassDurations = [QN, QN] * 4
bassDrumPhrase.addNoteList(bassPitches, bassDurations)

# Patrón de caja (un silencio + una caja de 1/4 nota) x 4 = 2 compases
snarePitches = [REST, SNR] * 4
snareDurations = [QN, QN] * 4
snareDrumPhrase.addNoteList(snarePitches, snareDurations)

# Patrón de hi-hat (15 notas cerradas de 1/8 + 1 nota abierta de 1/8) = 2 compases
hiHatPitches = [CHH] * 15 + [OHH]
hiHatDurations = [EN] * 15 + [EN]
hiHatPhrase.addNoteList(hiHatPitches, hiHatDurations)

##### Repetir el material según sea necesario
Mod.repeat(bassDrumPhrase, repetitions)
Mod.repeat(snareDrumPhrase, repetitions)
Mod.repeat(hiHatPhrase, repetitions)

##### Combinar el material musical
drumsPart.addPhrase(bassDrumPhrase)
drumsPart.addPhrase(snareDrumPhrase)
drumsPart.addPhrase(hiHatPhrase)
score.addPart(drumsPart)

##### Visualizar y reproducir la partitura
View.sketch(score)
Play.midi(score)
