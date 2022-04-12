from xml.etree.ElementTree import Element

from musicxml.utils import node_tag, read_node
from . import work_title


@node_tag("work")
def read(tree_node: Element) -> str:
    output, _, _ = read_node(tree_node, {"work-title": work_title.read})
    return output[0].content
