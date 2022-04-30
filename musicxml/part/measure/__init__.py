from xml.etree.ElementTree import Element
from musicxml.part.measure import direction, note, barline, attributes
from .direction.direction_type.metronome import Metronome

from musicxml.utils import node_tag, read_node

TAG = "measure"


class Measure:
    def __init__(self, number):
        self.number = number
        self.contents = []

    number = None
    contents: list = None

    def add_note(self, note: note.Note):
        self.contents += [note]

    def add_barline(self, barline: barline.Barline):
        self.contents += [barline]

    def add_attribute(self, attribute: attributes.Attributes):
        self.contents += [attribute]

    def add_direction(self, direction: direction.Direction):
        self.contents += [direction]

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} '{self.number}' {len(self.contents)} contents>"
        )

    def to_ly(self):
        raise NotImplementedError()


@node_tag(TAG)
def read(tree_node: Element) -> Measure:
    measure = Measure(tree_node.attrib["number"])
    node_contents = read_node(
        tree_node, [note, barline, attributes, direction], children_to_ignore=["print"]
    )

    for node_content in node_contents:
        if node_content.tag == note.TAG:
            measure.add_note(node_content.content)

        elif node_content.tag == barline.TAG:
            measure.add_barline(node_content.content)

        elif node_content.tag == attributes.TAG:
            if not node_content.content.divisions is None:
                raise NotImplementedError()
            measure.add_attribute(node_content.content)

        elif node_content.tag == direction.TAG:
            directions = node_content.content
            for direc in directions:
                if type(direc) == Metronome:
                    raise NotImplementedError()
                else:
                    measure.add_direction(direc)

    return measure
