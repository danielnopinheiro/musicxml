from xml.etree.ElementTree import Element

from musicxml.utils import node_tag


@node_tag("part")
def read(tree_node: Element):
    print(tree_node)
