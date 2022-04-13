from xml.etree.ElementTree import Element

from musicxml.utils import node_tag, read_node
from . import work_title

TAG = "work"


class Work:
    def __init__(self, work_title):
        self.work_title = work_title

    work_title = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} '{self.work_title}'>"


@node_tag(TAG)
def read(tree_node: Element) -> Work:
    output, _, _ = read_node(tree_node, {"work-title": work_title.read})
    return Work(output[0].content)
