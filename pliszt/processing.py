from music21 import midi
from music21.stream import Part
from music21.note import Note
from music21.chord import Chord
from typing import Text, Optional, List
from numbers import Real


def extract_notes(midi_part: Part) -> List[Note]:
    """Extract the notes from a part of a midi file.

    :param midi_part: A part of a midi file.
    :type midi_part: Part
    :return: A list of notes.
    :rtype: List[Note]
    """
    return [note for note in midi_part.flat.notes]

def get_frequency(notes: List[Note]) -> List[Real]:
    frequencies = []
    for note in notes:
        if isinstance(note, Chord):
            frequencies.extend(note.pitches.frequency)
        else:
            frequencies.append(note.pitch.frequency)
    return frequencies