from xml.etree.ElementTree import Element

from score_partwise.part.measure.direction.direction_type.metronome import Metronome

from . import direction_type
from score_partwise.utils import node_tag, print_node, read_node

TAG = "direction"


class Direction:
    def __init__(self) -> None:
        self.directions_list = []

    directions_list: list = None

    def add_metronome(self, metronome: Metronome):
        self.directions_list += [metronome]

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {len(self.directions_list)} directions>"

    def to_ly(self):
        raise NotImplementedError()


@node_tag(TAG)
def read(tree_node: Element) -> Direction:
    direction = Direction()

    node_contents = read_node(tree_node, [direction_type], children_to_ignore=["sound"])
    # TODO "sound" has important data
    for node_content in node_contents:
        if node_content.tag == direction_type.TAG:
            if type(node_content.content.content) == Metronome:
                direction.add_metronome(node_content.content.content)
            else:
                raise NotImplementedError()

    return direction
