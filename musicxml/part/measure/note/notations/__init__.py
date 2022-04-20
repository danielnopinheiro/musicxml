from xml.etree.ElementTree import Element

from musicxml.utils import node_tag, print_node, read_node

from . import slur
from .slur import Slur

TAG = "notations"


class Notations:

    slur: Slur = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


@node_tag(TAG)
def read(tree_node: Element) -> Notations:
    print_node(tree_node)
    notations = Notations()
    node_contents = read_node(tree_node, [slur], error_if_unread_children=True)
    for node_content in node_contents:
        if node_content.tag == slur.TAG:
            notations.slur = node_content.content

    return notations
