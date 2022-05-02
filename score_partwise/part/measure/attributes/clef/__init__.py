from xml.etree.ElementTree import Element

from . import sign, clef_octave_change, line
from score_partwise.utils import node_tag, read_node

TAG = "clef"


class Clef:
    def __init__(self, sign: str, line: int, clef_octave_change: int) -> None:
        self.sign = sign
        if line is None:
            if sign == "F":
                self.line = 4
            elif sign == "G":
                self.line = 2
            elif sign == "C":
                self.line = 3
        else:
            self.line = line
        self.clef_octave_change = clef_octave_change

    sign: str = None
    line: int = None
    clef_octave_change: int = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.sign}{'' if self.clef_octave_change == 0 else f'({self.clef_octave_change})'}{'' if self.line is None else self.line}>"

    def to_ly(self):
        raise NotImplementedError()


@node_tag(TAG)
def read(tree_node: Element) -> Clef:
    c_o_c = 0
    l = None
    node_contents = read_node(tree_node, [sign, clef_octave_change, line])
    for node_content in node_contents:
        if node_content.tag == sign.TAG:
            s = node_content.content
        elif node_content.tag == line.TAG:
            l = node_content.content
        elif node_content.tag == clef_octave_change.TAG:
            c_o_c = node_content.content

    return Clef(s, l, c_o_c)
