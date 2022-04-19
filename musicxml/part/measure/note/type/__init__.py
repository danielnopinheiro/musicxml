from xml.etree.ElementTree import Element

from musicxml.utils import node_tag

TAG = "type"

LOG_VALUES = {
    "1024th": 10,
    "512th": 9,
    "256th": 8,
    "128th": 7,
    "64th": 6,
    "32nd": 5,
    "16th": 4,
    "eighth": 3,
    "quarter": 2,
    "half": 1,
    "whole": 0,
    "breve": -1,
    "long": -2,
    "maxima": -3,
}


class Type:
    def __init__(self, name: str) -> None:
        assert name.strip() in LOG_VALUES, f"{name} is not a valid type"
        self.name = name.strip()

    name: str = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    def __str__(self) -> str:
        return self.name

    def to_ly(self) -> str:
        if LOG_VALUES[self.name] >= 0:
            return 2 ** LOG_VALUES[self.name]
        else:
            return "\\%s" % self.name

    def quarters(self) -> float:
        return 2 ** (2 - LOG_VALUES[self.name])

    def wholes(self) -> float:
        return 2 ** (-LOG_VALUES[self.name])


@node_tag(TAG)
def read(tree_node: Element) -> Type:
    return Type(tree_node.text)
