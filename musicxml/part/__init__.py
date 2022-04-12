from xml.etree.ElementTree import Element

from musicxml.utils import node_tag, print_node


@node_tag("part")
def read(tree_node: Element):
    print_node(tree_node)
