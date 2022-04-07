import pytest

import musicxml


class foo:
    def __init__(self, tag):
        self.tag = tag


def test_part_list_node():
    with pytest.raises(AssertionError) as e:
        musicxml.get_part_list(foo("foo"))
    assert "part-list" in e.value.args[0]
    musicxml.get_part_list(foo("part-list"))


def test_part_node():
    with pytest.raises(AssertionError) as e:
        musicxml.get_part(foo("foo"))
    assert "part" in e.value.args[0]
    musicxml.get_part(foo("part"))
