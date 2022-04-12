from typing import List, Tuple
from xml.etree.ElementTree import Element


def node_tag(tag_name):
    def inner(func):
        def wrapper(tree_node):
            assert (
                tree_node.tag == tag_name
            ), f"Node tag '{tree_node.tag}' isn't '{tag_name}'"

            return func(tree_node)

        return wrapper

    return inner


class NodeContent:
    def __init__(self, tag: str = None, content=None) -> None:
        self.tag = tag
        self.content = content

    tag: str = None
    content = None

    def __str__(self) -> str:
        return f"'{self.tag}' = {self.content}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.__str__()}>"


def read_node(
    node: Element, children_functions: list
) -> Tuple[List[NodeContent], List[str], List[str]]:
    # TODO: create test
    outputs = [
        NodeContent(child.tag, children_functions[child.tag](child))
        for child in node
        if child.tag in children_functions
    ]
    unread_children = [
        child.tag for child in node if child.tag not in children_functions
    ]
    ignored_children = [
        child_tag
        for child_tag in children_functions
        if child_tag not in [child.tag for child in node]
    ]
    return outputs, unread_children, ignored_children


def print_node(el: Element):
    print(
        {
            "tag": el.tag,
            "text": el.text,
            "attrib": el.attrib,
            "tail": el.tail,
            "children": [child.tag for child in el.getchildren()],
        }
    )
