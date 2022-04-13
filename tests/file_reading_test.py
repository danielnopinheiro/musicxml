import pytest
from xml.etree.ElementTree import Element

import musicxml


@pytest.mark.parametrize(
    "node_name, func",
    [
        (musicxml.work.TAG, musicxml.work.read),
        (musicxml.work.work_title.TAG, musicxml.work.work_title.read),
        (musicxml.part_list.TAG, musicxml.part_list.read),
        (musicxml.part_list.part_group.TAG, musicxml.part_list.part_group.read),
        (musicxml.part_list.score_part.TAG, musicxml.part_list.score_part.read),
        (
            musicxml.part_list.score_part.part_name.TAG,
            musicxml.part_list.score_part.part_name.read,
        ),
        (musicxml.part.TAG, musicxml.part.read),
    ],
)
def test_node_reading(node_name, func):
    with pytest.raises(AssertionError) as e:
        func(Element("foo"))
    assert node_name in e.value.args[0]
