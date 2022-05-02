from xml.etree.ElementTree import Element
from score_partwise.part.measure.attributes import clef, divisions, key, time

from score_partwise.utils import node_tag, read_node

TAG = "attributes"


class Attributes:
    def __init__(self) -> None:
        self.attributes_list = []

    divisions: int = None
    attributes_list: list = None

    def add_key(self, key: key.Key):
        self.attributes_list += [key]

    def add_time(self, time: time.Time):
        self.attributes_list += [time]

    def add_clef(self, clef: clef.Clef):
        self.attributes_list += [clef]

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {len(self.attributes_list)} attributes>"

    def to_ly(self):
        raise NotImplementedError()


@node_tag(TAG)
def read(tree_node: Element) -> Attributes:
    attributes = Attributes()

    node_contents = read_node(tree_node, [divisions, key, time, clef])
    for node_content in node_contents:
        if node_content.tag == divisions.TAG:
            attributes.divisions = node_content.content
        elif node_content.tag == key.TAG:
            attributes.add_key(node_content.content)
        elif node_content.tag == time.TAG:
            attributes.add_time(node_content.content)
        elif node_content.tag == clef.TAG:
            attributes.add_clef(node_content.content)

    return attributes
