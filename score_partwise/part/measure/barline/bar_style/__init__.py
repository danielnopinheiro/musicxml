from enum import Enum
from xml.etree.ElementTree import Element

from score_partwise.utils import node_tag

TAG = "bar-style"


class BarStyle(Enum):
    dashed = "dashed"
    dotted = "dotted"
    heavy = "heavy"
    heavy_heavy = "heavy-heavy"
    heavy_light = "heavy-light"
    light_heavy = "light-heavy"
    light_light = "light-light"
    none = "none"
    regular = "regular"
    short = "short"
    tick = "tick"

    def to_ly():
        raise NotImplementedError


@node_tag(TAG)
def read(tree_node: Element) -> BarStyle:
    return BarStyle(tree_node.text.strip())
