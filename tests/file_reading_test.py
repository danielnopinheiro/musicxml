import pytest
from xml.etree.ElementTree import Element

import musicxml


@pytest.mark.parametrize(
    "module",
    [
        musicxml.work,
        musicxml.work.work_title,
        musicxml.part_list,
        musicxml.part_list.part_group,
        musicxml.part_list.score_part,
        musicxml.part_list.score_part.part_name,
        musicxml.part,
        musicxml.part.measure,
        musicxml.part.measure.note,
        musicxml.part.measure.note.dot,
        musicxml.part.measure.note.duration,
        musicxml.part.measure.note.voice,
        musicxml.part.measure.note.pitch,
        musicxml.part.measure.note.pitch.step,
        musicxml.part.measure.note.pitch.octave,
        musicxml.part.measure.note.pitch.alter,
        musicxml.part.measure.note.type,
        musicxml.part.measure.note.lyric,
        musicxml.part.measure.note.lyric.syllabic,
        musicxml.part.measure.note.lyric.text,
        musicxml.part.measure.note.notations,
        musicxml.part.measure.note.notations.slur,
    ],
)
def test_node_reading(module):
    with pytest.raises(AssertionError) as e:
        module.read(Element("foo"))
    assert module.TAG in e.value.args[0]
