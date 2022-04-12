import pytest
from xml.etree.ElementTree import Element

import musicxml


@pytest.mark.parametrize(
    "node_name, func",
    [
        ("work", musicxml.work.read),
        ("work-title", musicxml.work.work_title.read),
        ("part-list", musicxml.part_list.read),
        ("part-group", musicxml.part_list.part_group.read),
        ("score-part", musicxml.part_list.score_part.read),
        ("part", musicxml.part.read),
    ],
)
def test_node_reading(node_name, func):
    with pytest.raises(AssertionError) as e:
        func(Element("foo"))
    assert node_name in e.value.args[0]
