from typing import List, Tuple
from warnings import warn
from xml.etree.ElementTree import Element


def node_tag(tag_name: str):
    def inner(func):
        def wrapper(tree_node: Element):
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
    node: Element,
    children_modules: list,
    children_to_ignore: List[str] = [],
    show_warnings: bool = True,
    error_if_unread_children: bool = False,
) -> Tuple[List[NodeContent], List[str], List[str]]:
    # TODO: create test
    children_functions = {m.TAG: m.read for m in children_modules}
    outputs = [
        NodeContent(child.tag, children_functions[child.tag](child))
        for child in node
        if child.tag in children_functions
    ]

    unread_children = [
        child.tag
        for child in node
        if child.tag not in children_functions and child.tag not in children_to_ignore
    ]

    ignored_children = [
        child_tag
        for child_tag in children_functions
        if child_tag not in [child.tag for child in node]
        and child_tag not in children_to_ignore
    ]

    if show_warnings:
        if unread_children != []:
            warn(f"From '{node.tag}': didn't read nodes {', '.join(unread_children)}.")
        if ignored_children != []:
            warn(f"From '{node.tag}': ignored nodes {', '.join(ignored_children)}.")
    if error_if_unread_children:
        if unread_children != []:
            raise NotImplementedError(
                f"From '{node.tag}': didn't read nodes {', '.join(unread_children)}."
            )

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
