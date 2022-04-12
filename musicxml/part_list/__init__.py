from xml.etree.ElementTree import Element

from musicxml.utils import node_tag, read_node
from . import score_part, part_group


@node_tag("part-list")
def read(tree_node: Element):
    output, unread_children, ignored_children = read_node(
        tree_node, {"score-part": score_part.read, "part-group": part_group.read}
    )
    print(output, unread_children, ignored_children)
