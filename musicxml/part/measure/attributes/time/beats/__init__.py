from xml.etree.ElementTree import Element

from musicxml.utils import node_tag

TAG = "beats"


@node_tag(TAG)
def read(tree_node: Element) -> int:
    return int(tree_node.text.strip())
