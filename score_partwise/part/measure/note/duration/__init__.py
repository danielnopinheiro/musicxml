from xml.etree.ElementTree import Element

from score_partwise.utils import node_tag

TAG = "duration"


@node_tag(TAG)
def read(tree_node: Element) -> int:
    assert int(tree_node.text) == float(tree_node.text)
    return int(tree_node.text)
