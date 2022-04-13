import xml.etree.ElementTree as ET

from .utils import read_node
from . import work, part_list, part


def read_musicxml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    assert root.tag == "score-partwise"

    print("\n-------------------\n")

    outputs, _, _ = read_node(
        root, {"work": work.read, "part-list": part_list.read, "part": part.read}
    )

    print("\n-------------------\n")

    print(outputs)
