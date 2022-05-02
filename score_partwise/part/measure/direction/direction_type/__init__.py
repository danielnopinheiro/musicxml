from xml.etree.ElementTree import Element
from score_partwise.part.measure.direction.direction_type import metronome

from score_partwise.utils import node_tag, print_node, read_node

TAG = "direction-type"


class DirectionType:
    def __init__(self, content) -> None:
        self.content = content

    content = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.content}>"


@node_tag(TAG)
def read(tree_node: Element) -> DirectionType:
    node_contents = read_node(tree_node, [metronome])
    for node_content in node_contents:
        if node_content.tag == metronome.TAG:
            content = node_content.content

    return DirectionType(content)
