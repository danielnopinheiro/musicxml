from enum import Enum
from xml.etree.ElementTree import Element

from score_partwise.utils import node_tag, print_node

TAG = "syllabic"


class Syllabic(Enum):
    begin = "begin"
    end = "end"
    middle = "middle"
    single = "single"

    def hyphenizes(self) -> bool:
        return self == Syllabic.begin or self == Syllabic.middle


@node_tag(TAG)
def read(tree_node: Element) -> Syllabic:
    return Syllabic(tree_node.text.strip())
