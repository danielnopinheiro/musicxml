from xml.etree.ElementTree import Element

from musicxml.utils import node_tag

TAG = "per-minute"


@node_tag(TAG)
def read(tree_node: Element) -> float:
    return float(tree_node.text.strip())
