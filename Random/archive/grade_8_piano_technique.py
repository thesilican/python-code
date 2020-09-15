import random

scales = [
    "Major Scale",
    "Minor Harmonic Scale",
    "Minor Melodic Scale",
    "Formula Pattern Scale"
    ]
chords = [
    "Major Chord",
    "Minor Chord",
    "Dom. 7th (Broken) Chord",
    "Dom. 7th (Solid) Chord",
    "Dim. 7th (Broken) Chord",
    "Dim. 7th (Solid) Chord",
    ]
arpeggios = [
    "Major Arpeggio",
    "Minor Arpeggio",
    "Dom. 7th Arpeggio",
    "Dim. 7th Arpeggio",
    ]

keys = [
    "C", "D", "E", "Bb", "Eb", "F#"
    ]

while True:
    key = random.choice(keys)
    play = random.choice(random.choice([
        scales,
        #chords,
        #arpeggios
        ]))
    print(key, play, end="")
    input()
