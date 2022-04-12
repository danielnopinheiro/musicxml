from typing import List, Tuple


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
    def __init__(self, tag=None, content=None):
        self.tag = tag
        self.content = content

    tag: str = None
    content = None

    def __str__(self) -> str:
        return str({self.tag: self.content})

    def __repr__(self) -> str:
        return "<" + self.__class__.__name__ + " " + self.__str__() + ">"


def read_node(
    node, children_functions
) -> Tuple[List[NodeContent], List[str], List[str]]:
    # TODO: create test
    children = {child.tag: child for child in node}
    outputs = [
        NodeContent(child_tag, children_functions[child_tag](children[child_tag]))
        for child_tag in children
        if child_tag in children_functions
    ]
    unread_children = [
        child_tag for child_tag in children if child_tag not in children_functions
    ]
    ignored_children = [
        child_tag for child_tag in children_functions if child_tag not in children
    ]
    return outputs, unread_children, ignored_children
