from music21 import midi
from music21.stream import Stream
from typing import Text, Optional

def open_midi(midi_path: Text) -> Stream:
    """Open a midi file and return a music21 Stream. Remove the drums (channel 10) from a file if specified from each track.

    :param midi_path: A path to the mid file
    :type midi_path: Text
    :return: A music21 IOstream of the midi file. 
    :rtype: Stream
    """
    mf = midi.MidiFile()
    mf.open(midi_path)
    mf.read()
    mf.close()
    return midi.translate.midiFileToStream(mf)