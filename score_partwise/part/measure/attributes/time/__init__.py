from xml.etree.ElementTree import Element
from score_partwise.part.measure.attributes.time import beats, beat_type

from score_partwise.utils import node_tag, read_node

TAG = "time"


class Time:
    def __init__(self, beats: int, beats_type: int) -> None:
        self.beats = beats
        self.beats_type = beats_type

    beats: int = None
    beats_type: int = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.beats}/{self.beats_type}>"

    def to_ly(self):
        raise NotImplementedError()


@node_tag(TAG)
def read(tree_node: Element) -> Time:
    node_contents = read_node(tree_node, [beats, beat_type])
    for node_content in node_contents:
        if node_content.tag == beats.TAG:
            b = node_content.content
        elif node_content.tag == beat_type.TAG:
            b_t = node_content.content

    return Time(b, b_t)
