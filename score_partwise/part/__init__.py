from typing import List
from xml.etree.ElementTree import Element

from score_partwise.part import measure
from score_partwise.part.measure.direction.direction_type.metronome import Metronome
from score_partwise.utils import node_tag, read_node

TAG = "part"


class Part:
    def __init__(self, id):
        self.id = id
        self.measure_list = []

    id = None
    divisions: int = None
    metronome: Metronome = None

    measure_list: List[measure.Measure] = None

    def add_measure(self, measure: measure.Measure):
        self.measure_list += [measure]

    def set_divisions(self, divisions: int):
        self.divisions = divisions

    def set_metronome(self, metronome: Metronome):
        self.metronome = metronome

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} '{self.id}' {len(self.measure_list)} measures>"
        )


@node_tag(TAG)
def read(tree_node: Element) -> Part:
    part = Part(tree_node.attrib["id"])
    node_contents = read_node(tree_node, [measure])

    for node_content in node_contents:
        if node_content.tag == measure.TAG:
            if not node_content.content.divisions is None:
                part.set_divisions(node_content.content.divisions)
            if not node_content.content.metronome is None:
                part.set_metronome(node_content.content.metronome)
            part.add_measure(node_content.content)

    return part
