from xml.etree.ElementTree import Element

from musicxml.utils import node_tag

TAG = "part-group"


class PartGroup:
    def __init__(self, type, number):
        self.type = type
        self.number = number

    type: str = None
    number: str = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} '{self.type}' '{self.number}'>"


@node_tag(TAG)
def read(tree_node: Element) -> PartGroup:
    return PartGroup(tree_node.attrib["type"], tree_node.attrib["number"])
