from pliszt.reading import open_midi
import pathlib
import pytest

@pytest.fixture
def chopin_ballad():
    return (pathlib.Path(__file__).parent.parent /'data'/'chopin'/'chpn_op23.mid').as_posix()

def test_read(chopin_ballad):
    mid_stream = open_midi(chopin_ballad)
    assert mid_stream
