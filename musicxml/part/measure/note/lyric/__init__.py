from xml.etree.ElementTree import Element

from musicxml.utils import node_tag, print_node, read_node
from . import syllabic, text
from .syllabic import Syllabic

TAG = "lyric"


class Lyric:
    def __init__(self, number: str, syllabic: Syllabic, text: str) -> None:
        self.number = number.strip()
        self.syllabic = syllabic
        self.text = text.strip()

    number: str = None
    syllabic: Syllabic = None
    text: str = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self.number}) {self.text}{' - ' if self.syllabic.hyphenizes() else ''}>"

    def to_ly(self):
        raise NotImplementedError()


@node_tag(TAG)
def read(tree_node: Element) -> Lyric:
    output, _, _ = read_node(tree_node, [syllabic, text], error_if_unread_children=True)
    t = ""
    for node_content in output:
        if node_content.tag == syllabic.TAG:
            s = node_content.content
        elif node_content.tag == text.TAG:
            t = node_content.content

    return Lyric(tree_node.attrib["number"], s, t)
