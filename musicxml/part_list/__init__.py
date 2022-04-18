from typing import List
from xml.etree.ElementTree import Element

from musicxml.utils import node_tag, read_node
from . import score_part, part_group

TAG = "part-list"


class PartList:
    def __init__(self):
        self.score_part_list = []

    score_part_list: List[score_part.ScorePart] = None

    def add_score_part(self, score_part: score_part.ScorePart):
        self.score_part_list += [score_part]

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {len(self.score_part_list)} score-parts>"


@node_tag(TAG)
def read(tree_node: Element):
    output, _, _ = read_node(tree_node, [score_part, part_group])
    part_list = PartList()
    for node_content in output:
        if node_content.tag == part_group.TAG:
            # TODO
            pass
        elif node_content.tag == score_part.TAG:
            part_list.add_score_part(node_content.content)

    return part_list
