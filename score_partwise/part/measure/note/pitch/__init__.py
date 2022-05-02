from xml.etree.ElementTree import Element

from score_partwise.utils import node_tag, read_node
from . import octave, step, alter

TAG = "pitch"


class Pitch:
    def __init__(self, step: str, octave: int, alter: int) -> None:
        self.step = step
        self.octave = octave
        self.alter = alter

    step: str = None
    octave: int = None
    alter: int = None

    def __str__(self) -> str:
        return f"{self.step}{'#' if self.alter == 1 else 'b' if self.alter == -1 else ''}{self.octave}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self}>"

    def to_ly(self):
        raise NotImplementedError()


@node_tag(TAG)
def read(tree_node: Element) -> Pitch:
    node_contents = read_node(tree_node, [step, octave, alter])
    a = 0
    for node_content in node_contents:
        if node_content.tag == octave.TAG:
            o = node_content.content
        elif node_content.tag == step.TAG:
            s = node_content.content
        elif node_content.tag == alter.TAG:
            a = node_content.content

    return Pitch(s, o, a)
