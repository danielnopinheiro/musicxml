from xml.etree.ElementTree import Element

from musicxml.utils import node_tag, print_node

TAG = "text"


@node_tag(TAG)
def read(tree_node: Element) -> str:
    return tree_node.text.strip()
