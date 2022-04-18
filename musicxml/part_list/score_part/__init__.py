from xml.etree.ElementTree import Element

from musicxml.utils import node_tag, read_node
from . import part_name

TAG = "score-part"


class ScorePart:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    id = None
    name = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} '{self.id}' '{self.name}'>"


@node_tag(TAG)
def read(tree_node: Element) -> ScorePart:
    score_part_id = tree_node.attrib["id"]
    output, _, _ = read_node(tree_node, [part_name], show_warnings=False)
    score_part_name = output[0].content
    return ScorePart(score_part_id, score_part_name)
