from xml.etree.ElementTree import Element

from musicxml.utils import node_tag, print_node

TAG = "part"

@node_tag(TAG)
def read(tree_node: Element):
    print_node(tree_node)
