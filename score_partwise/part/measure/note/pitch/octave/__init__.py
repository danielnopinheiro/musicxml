from xml.etree.ElementTree import Element

from score_partwise.utils import node_tag, print_node

TAG = "octave"


@node_tag(TAG)
def read(tree_node: Element) -> int:
    return int(tree_node.text)
