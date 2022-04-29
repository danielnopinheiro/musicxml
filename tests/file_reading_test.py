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
        musicxml.part.measure.barline,
        musicxml.part.measure.barline.repeat,
        musicxml.part.measure.barline.bar_style,
        musicxml.part.measure.attributes,
        musicxml.part.measure.attributes.divisions,
        musicxml.part.measure.attributes.key,
        musicxml.part.measure.attributes.key.fifths,
        musicxml.part.measure.attributes.time,
        musicxml.part.measure.attributes.time.beats,
        musicxml.part.measure.attributes.time.beat_type,
        musicxml.part.measure.attributes.clef,
        musicxml.part.measure.attributes.clef.sign,
        musicxml.part.measure.attributes.clef.line,
        musicxml.part.measure.attributes.clef.clef_octave_change,
    ],
)
def test_node_reading(module):
    with pytest.raises(AssertionError) as e:
        module.read(Element("foo"))
    assert module.TAG in e.value.args[0]
