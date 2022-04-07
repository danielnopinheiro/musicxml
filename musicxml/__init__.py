import xml.etree.ElementTree as ET


def read_musicxml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    for child in root:
        if child.tag == "part-list":
            get_part_list(child)
        elif child.tag == "part":
            get_part(child)

    print(tree)


def get_part_list(tree_node):
    assert tree_node.tag == "part-list", f"Node tag '{tree_node.tag}' isn't 'part-list'"

    print(tree_node)


def get_part(tree_node):
    assert tree_node.tag == "part", f"Node tag '{tree_node.tag}' isn't 'part'"

    print(tree_node)
