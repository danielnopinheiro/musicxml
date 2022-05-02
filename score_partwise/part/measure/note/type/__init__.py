from xml.etree.ElementTree import Element

from score_partwise.utils import LOG_VALUES, node_tag, NoteType

TAG = "type"


class Type:
    def __init__(self, name: str) -> None:
        self.note_type = NoteType(name.strip())

    note_type: NoteType = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.note_type}>"

    def __str__(self) -> str:
        return self.note_type

    def to_ly(self) -> str:
        if LOG_VALUES[self.note_type] >= 0:
            return 2 ** LOG_VALUES[self.note_type]
        else:
            return "\\%s" % self.note_type.value

    def quarters(self) -> float:
        return 2 ** (2 - LOG_VALUES[self.note_type])

    def wholes(self) -> float:
        return 2 ** (-LOG_VALUES[self.note_type])


@node_tag(TAG)
def read(tree_node: Element) -> Type:
    return Type(tree_node.text)
