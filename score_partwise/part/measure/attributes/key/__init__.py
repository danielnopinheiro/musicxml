from xml.etree.ElementTree import Element
from score_partwise.part.measure.attributes.key import fifths

from score_partwise.utils import node_tag, read_node

TAG = "key"


class Key:
    def __init__(self, fifths: int) -> None:
        self.fifths = fifths

    fifths: int = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.fifths}>"

    def to_ly(self):
        raise NotImplementedError()


@node_tag(TAG)
def read(tree_node: Element) -> Key:
    node_contents = read_node(tree_node, [fifths])

    return Key(node_contents[0].content)
