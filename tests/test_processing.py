from pliszt.reading import open_midi
from pliszt.processing import extract_notes, get_frequency
import pathlib
import pytest

@pytest.fixture
def chopin_ballad_file():
    return (pathlib.Path(__file__).parent.parent /'data'/'chopin'/'chpn_op23.mid').as_posix()

@pytest.fixture
def chopin_ballad(chopin_ballad_file):
    return open_midi(chopin_ballad_file)

def test_reading_notes(chopin_ballad):
    left_hand = chopin_ballad.parts[0] # This is a Part despite the propperty name...
    left_hand_notes = extract_notes(left_hand)

    right_hand = chopin_ballad.parts[1] # This is a Part despite the propperty name...
    right_hand_notes = extract_notes(right_hand)

    # Chopin's Ballad starts with a 'C3' on the left hand
    assert left_hand_notes[0].nameWithOctave == 'C3'

    # Chopin's Ballad starts with a 'C2' on the right hand
    assert right_hand_notes[0].nameWithOctave == 'C2'


def test_get_frequency(chopin_ballad):
    left_hand = chopin_ballad.parts[0].flat.notes
    left_hand_notes = extract_notes(left_hand)

    frequencies = get_frequency([left_hand_notes[0]])

    # A C3 is about 130 Hz
    assert frequencies[0] == pytest.approx(130.8, .1)