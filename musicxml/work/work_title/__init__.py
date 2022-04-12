from xml.etree.ElementTree import Element

from musicxml.utils import node_tag


@node_tag("work-title")
def read(tree_node: Element) -> str:
    return tree_node.text.strip()
