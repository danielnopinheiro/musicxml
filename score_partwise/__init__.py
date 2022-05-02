from typing import List
from xml.etree.ElementTree import Element

from .utils import node_tag, read_node
from . import work, part_list, part
from .work import Work
from .part_list import PartList
from .part import Part
from .part.measure.direction.direction_type.metronome import Metronome

TAG = "score-partwise"


class ScorePartwise:
    def __init__(
        self,
        work: Work,
        part_list: PartList,
        parts: List[Part],
        divisions: int,
        metronome: Metronome,
    ):
        self.work = work
        self.part_list = part_list
        self.parts = parts
        self.divisions = divisions
        self.metronome = metronome
        # TODO assert things

    work: Work = None
    part_list: PartList = None
    parts: List[Part] = None

    divisions: int
    metronome: Metronome

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} '{self.work.work_title}' {'/'.join([p_l.name for p_l in self.part_list.score_part_list])}>"


@node_tag(TAG)
def read(tree_node: Element) -> ScorePartwise:
    node_contents = read_node(
        tree_node,
        [work, part_list, part],
        children_to_ignore=["identification", "defaults", "credit"],
        # TODO read credits and things
    )

    parts = []
    for node_content in node_contents:
        if node_content.tag == work.TAG:
            w = node_content.content
        elif node_content.tag == part_list.TAG:
            p_l = node_content.content
        elif node_content.tag == part.TAG:
            if not node_content.content.divisions is None:
                divisions = node_content.content.divisions
            if not node_content.content.metronome is None:
                metronome = node_content.content.metronome
            parts += [node_content.content]

    return ScorePartwise(w, p_l, parts, divisions, metronome)
