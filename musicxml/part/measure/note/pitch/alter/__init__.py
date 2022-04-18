from xml.etree.ElementTree import Element

from musicxml.utils import node_tag

TAG = "alter"


@node_tag(TAG)
def read(tree_node: Element) -> int:
    value = int(tree_node.text)

    if int(tree_node.text) != float(tree_node.text) or value not in [-1, 0, 1]:
        raise NotImplementedError(f"Pitch alter '{tree_node.text}'")

    return value
