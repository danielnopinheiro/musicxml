from typing import List
from xml.etree.ElementTree import Element
from musicxml.part.measure import note

from musicxml.utils import node_tag, read_node

TAG = "measure"


class Measure:
    def __init__(self, number):
        self.number = number
        self.note_list = []

    number = None
    note_list: List[note.Note] = None

    def add_note(self, note: note.Note):
        self.note_list += [note]

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} '{self.number}'>"


@node_tag(TAG)
def read(tree_node: Element) -> Measure:
    measure = Measure(tree_node.attrib["number"])
    output, _, _ = read_node(tree_node, [note])

    for node_content in output:
        if node_content.tag == note.TAG:
            measure.add_note(node_content.content)

    return measure
