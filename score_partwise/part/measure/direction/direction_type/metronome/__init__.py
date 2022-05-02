from xml.etree.ElementTree import Element

from score_partwise.utils import LOG_VALUES, NoteType, node_tag, read_node
from . import beat_unit, beat_unit_dot, per_minute

TAG = "metronome"


class Metronome:
    def __init__(self, beat_unit: NoteType, dots: int, per_minute: float) -> None:
        self.beat_unit = beat_unit
        self.dots = dots
        self.per_minute = per_minute

    beat_unit: NoteType = None
    dots = 0
    per_minute: float = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.beat_unit}{'.'*self.dots} = {self.per_minute}>"

    def to_ly(self):
        raise NotImplementedError()

    def quarters_per_minute(self):
        if self.dots > 1:
            raise NotImplementedError(
                "idk how to compute multiple dots, e.g., two dots means 1.75 times or 1.25 times?"
            )

        quarters = (2 ** (2 - LOG_VALUES[self.beat_unit])) * (1.5**self.dots)
        return self.per_minute * quarters


@node_tag(TAG)
def read(tree_node: Element) -> Metronome:
    dots = 0
    node_contents = read_node(tree_node, [beat_unit, beat_unit_dot, per_minute])
    for node_content in node_contents:
        if node_content.tag == beat_unit.TAG:
            b_u = node_content.content
        elif node_content.tag == beat_unit_dot.TAG:
            dots += 1
        elif node_content.tag == per_minute.TAG:
            p_m = node_content.content

    return Metronome(b_u, dots, p_m)
