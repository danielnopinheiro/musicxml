from enum import Enum
from typing import List
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


class StartContinueStop(Enum):
    start = "start"
    cont = "continue"
    stop = "stop"


class Location(Enum):
    left = "left"
    middle = "middle"
    right = "right"


class NoteType(Enum):
    _1024th = "1024th"
    _512th = "512th"
    _256th = "256th"
    _128th = "128th"
    _64th = "64th"
    _32nd = "32nd"
    _16th = "16th"
    eighth = "eighth"
    quarter = "quarter"
    half = "half"
    whole = "whole"
    breve = "breve"
    long = "long"
    maxima = "maxima"


LOG_VALUES = {
    NoteType._1024th: 10,
    NoteType._512th: 9,
    NoteType._256th: 8,
    NoteType._128th: 7,
    NoteType._64th: 6,
    NoteType._32nd: 5,
    NoteType._16th: 4,
    NoteType.eighth: 3,
    NoteType.quarter: 2,
    NoteType.half: 1,
    NoteType.whole: 0,
    NoteType.breve: -1,
    NoteType.long: -2,
    NoteType.maxima: -3,
}


def read_node(
    node: Element,
    children_modules: list,
    children_to_ignore: List[str] = [],
    show_warnings: bool = False,
    error_if_unread_children: bool = True,
) -> List[NodeContent]:
    # TODO: create test
    children_functions = {m.TAG: m.read for m in children_modules}
    node_contents = [
        NodeContent(child.tag, children_functions[child.tag](child))
        for child in node
        if child.tag in children_functions
    ]

    if show_warnings or error_if_unread_children:
        unread_children = [
            child.tag
            for child in node
            if child.tag not in children_functions
            and child.tag not in children_to_ignore
        ]

        ignored_children = [
            child_tag
            for child_tag in children_functions
            if child_tag not in [child.tag for child in node]
            and child_tag not in children_to_ignore
        ]

        if show_warnings:
            if unread_children != []:
                warn(
                    f"From '{node.tag}': didn't read nodes {', '.join(unread_children)}."
                )
            if ignored_children != []:
                warn(f"From '{node.tag}': ignored nodes {', '.join(ignored_children)}.")
        if error_if_unread_children:
            if unread_children != []:
                raise NotImplementedError(
                    f"From '{node.tag}': didn't read nodes {', '.join(unread_children)}."
                )

    return node_contents


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
