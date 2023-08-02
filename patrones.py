# Daniela Villamar
# 19086
# EX3.MC Creación de Patrones Rítmicos

import simpleaudio as sa
from music21 import *
import time

# Cargar los sonidos de bombo, caja y hi-hat desde archivos WAV
kick_sound = sa.WaveObject.from_wave_file("C:/Users/danie/OneDrive/Documentos/Musica/New folder/kick.wav")
snare_sound = sa.WaveObject.from_wave_file("C:/Users/danie/OneDrive/Documentos/Musica/New folder/snare.wav")
hihat_sound = sa.WaveObject.from_wave_file("C:/Users/danie/OneDrive/Documentos/Musica/New folder/hithat.wav")

# Función para generar el patrón de batería
def generar_patron_bateria():
    # Crear el patrón de bombo
    bass_drum_pattern = [note.Rest(quarterLength=0.25), note.Note("C")]
    
    # Crear la frase de bombo y repetirla 4 veces para 2 compases
    bass_drum_phrase = stream.Measure()
    for _ in range(4):
        for element in bass_drum_pattern:
            if isinstance(element, note.Note):
                new_note = note.Note()
                new_note.duration = element.duration
                new_note.pitch = element.pitch
                bass_drum_phrase.append(new_note)
            elif isinstance(element, note.Rest):
                # Pausa de duración equivalente
                pause = note.Rest(quarterLength=element.quarterLength)
                bass_drum_phrase.append(pause)

    # Crear la frase de caja
    snare_pattern = [note.Rest(quarterLength=0.25), note.Note("G")]
    snare_phrase = stream.Measure()
    for _ in range(4):
        for element in snare_pattern:
            if isinstance(element, note.Note):
                new_note = note.Note()
                new_note.duration = element.duration
                new_note.pitch = element.pitch
                snare_phrase.append(new_note)
            elif isinstance(element, note.Rest):
                # Pausa de duración equivalente
                pause = note.Rest(quarterLength=element.quarterLength)
                snare_phrase.append(pause)

    # Crear la frase de hi-hat
    hihat_pattern = [note.Rest(quarterLength=0.25)] * 16
    hihat_phrase = stream.Measure()
    for element in hihat_pattern:
        if isinstance(element, note.Rest):
            # Pausa de duración equivalente
            pause = note.Rest(quarterLength=element.quarterLength)
            hihat_phrase.append(pause)

    # Reproducir los patrones
    play_pattern(bass_drum_phrase, kick_sound)
    play_pattern(snare_phrase, snare_sound)
    play_pattern(hihat_phrase, hihat_sound)

# Función para reproducir una frase de música utilizando sonidos WAV
def play_pattern(phrase, sound):
    for note_or_rest in phrase.notesAndRests:
        if isinstance(note_or_rest, note.Note):
            sound.play()
        elif isinstance(note_or_rest, note.Rest):
            # Pausa de duración equivalente
            sa.stop_all()
            time.sleep(note_or_rest.quarterLength)
            
# Llamar a la función para generar y reproducir el patrón de batería
generar_patron_bateria()
