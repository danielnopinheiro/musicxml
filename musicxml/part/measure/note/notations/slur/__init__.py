from xml.etree.ElementTree import Element

from musicxml.utils import StartContinueStop, node_tag

TAG = "slur"


class Slur:
    def __init__(self, scs: StartContinueStop, number: str) -> None:
        self.scs = scs
        self.number = number

    scs: StartContinueStop = None
    number: str = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self.number}) {self.scs.value}>"


@node_tag(TAG)
def read(tree_node: Element) -> Slur:
    if "number" in tree_node.attrib:
        return Slur(
            StartContinueStop(tree_node.attrib["type"]), tree_node.attrib["number"]
        )
    else:
        return Slur(tree_node.attrib["type"], "1")
