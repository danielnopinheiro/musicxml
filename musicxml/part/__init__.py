from typing import List
from xml.etree.ElementTree import Element
from musicxml.part import measure

from musicxml.utils import node_tag, read_node

TAG = "part"


class Part:
    def __init__(self, id):
        self.id = id
        self.measure_list = []

    id = None

    measure_list: List[measure.Measure] = None

    def add_measure(self, measure: measure.Measure):
        self.measure_list += [measure]

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} '{self.id}' {len(self.measure_list)} measures>"
        )


@node_tag(TAG)
def read(tree_node: Element) -> Part:
    part = Part(tree_node.attrib["id"])
    output, _, _ = read_node(tree_node, [measure])

    for node_content in output:
        if node_content.tag == measure.TAG:
            part.add_measure(node_content.content)

    return part
