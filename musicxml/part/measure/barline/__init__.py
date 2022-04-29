from xml.etree.ElementTree import Element
from musicxml.part.measure.barline import bar_style, repeat
from musicxml.part.measure.barline.repeat import Repeat

from musicxml.utils import Location, node_tag, read_node

TAG = "barline"


class Barline:
    def __init__(self, location: Location) -> None:
        self.location = location

    location: Location = None
    style: bar_style.BarStyle = None
    repeat: Repeat = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.style}>"


@node_tag(TAG)
def read(tree_node: Element) -> Barline:
    location = (
        Location(tree_node.attrib["location"])
        if "location" in tree_node.attrib
        else Location("right")
    )
    barline = Barline(location)
    node_contents = read_node(tree_node, [bar_style, repeat])
    for node_content in node_contents:
        if node_content.tag == bar_style.TAG:
            barline.style = node_content.content
        if node_content.tag == repeat.TAG:
            barline.repeat == node_content.content
    return barline
