from xml.etree.ElementTree import Element

from score_partwise.utils import NoteType, node_tag

TAG = "beat-unit"


@node_tag(TAG)
def read(tree_node: Element) -> NoteType:
    return NoteType(tree_node.text.strip())
