from enum import Enum
from xml.etree.ElementTree import Element

from score_partwise.utils import node_tag

TAG = "repeat"


class Direction(Enum):
    forward = "forward"
    backward = "backward"


class Repeat:
    def __init__(self, direction: Direction, times: int = None) -> None:
        self.direction = direction
        if direction == Direction.forward:
            assert (
                times is None
            ), "'times' is only used with backward repeats that are not part of an ending"
        self.times = times

    direction: Direction = None
    times = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


@node_tag(TAG)
def read(tree_node: Element) -> Repeat:
    if "after-jump" in tree_node.attrib:
        raise NotImplementedError()

    if "times" in tree_node.attrib:
        return Repeat(
            Direction(tree_node.attrib["direction"]), tree_node.attrib["times"]
        )
    else:
        return Repeat(Direction(tree_node.attrib["direction"]))
