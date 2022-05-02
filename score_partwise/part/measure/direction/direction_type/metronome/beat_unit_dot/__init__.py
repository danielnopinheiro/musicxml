from xml.etree.ElementTree import Element

from score_partwise.utils import node_tag

TAG = "beat-unit-dot"


class BeatUnitDot:
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


@node_tag(TAG)
def read(tree_node: Element) -> BeatUnitDot:
    return BeatUnitDot()
