import pytest
from xml.etree.ElementTree import Element

import score_partwise


@pytest.mark.parametrize(
    "module",
    [
        score_partwise,
        score_partwise.work,
        score_partwise.work.work_title,
        score_partwise.part_list,
        score_partwise.part_list.part_group,
        score_partwise.part_list.score_part,
        score_partwise.part_list.score_part.part_name,
        score_partwise.part,
        score_partwise.part.measure,
        score_partwise.part.measure.note,
        score_partwise.part.measure.note.dot,
        score_partwise.part.measure.note.duration,
        score_partwise.part.measure.note.voice,
        score_partwise.part.measure.note.pitch,
        score_partwise.part.measure.note.pitch.step,
        score_partwise.part.measure.note.pitch.octave,
        score_partwise.part.measure.note.pitch.alter,
        score_partwise.part.measure.note.type,
        score_partwise.part.measure.note.lyric,
        score_partwise.part.measure.note.lyric.syllabic,
        score_partwise.part.measure.note.lyric.text,
        score_partwise.part.measure.note.notations,
        score_partwise.part.measure.note.notations.slur,
        score_partwise.part.measure.barline,
        score_partwise.part.measure.barline.repeat,
        score_partwise.part.measure.barline.bar_style,
        score_partwise.part.measure.attributes,
        score_partwise.part.measure.attributes.divisions,
        score_partwise.part.measure.attributes.key,
        score_partwise.part.measure.attributes.key.fifths,
        score_partwise.part.measure.attributes.time,
        score_partwise.part.measure.attributes.time.beats,
        score_partwise.part.measure.attributes.time.beat_type,
        score_partwise.part.measure.attributes.clef,
        score_partwise.part.measure.attributes.clef.sign,
        score_partwise.part.measure.attributes.clef.line,
        score_partwise.part.measure.attributes.clef.clef_octave_change,
        score_partwise.part.measure.direction,
        score_partwise.part.measure.direction.direction_type,
        score_partwise.part.measure.direction.direction_type.metronome,
        score_partwise.part.measure.direction.direction_type.metronome.beat_unit,
        score_partwise.part.measure.direction.direction_type.metronome.beat_unit_dot,
        score_partwise.part.measure.direction.direction_type.metronome.per_minute,
    ],
)
def test_node_reading(module):
    with pytest.raises(AssertionError) as e:
        module.read(Element("foo"))
    assert module.TAG in e.value.args[0]
