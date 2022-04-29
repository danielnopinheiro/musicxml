from xml.etree.ElementTree import Element

from musicxml.utils import node_tag, print_node

TAG = "fifths"


class Fifths:
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


@node_tag(TAG)
def read(tree_node: Element) -> Fifths:
    return int(tree_node.text.strip())
