from typing import List
from xml.etree.ElementTree import Element
from musicxml.part.measure.note import dot, duration, lyric, pitch, voice
import musicxml.part.measure.note.type as note_type
from musicxml.part.measure.note.pitch import Pitch

from musicxml.utils import node_tag, read_node

TAG = "note"


class Note:
    def __init__(self) -> None:
        self.lyrics = []

    pitch: Pitch = None
    duration: int = None
    chord = False
    tie = None
    dots: int = 0
    voice: str = None
    note_type: str = None  # assert equivalency with duration
    lyrics: List[lyric.Lyric] = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.pitch} duration={self.duration} ({self.note_type}{'.'*self.dots})>"

    def to_ly(self):
        raise NotImplementedError()


@node_tag(TAG)
def read(tree_node: Element) -> Note:
    output, _, _ = read_node(
        tree_node,
        [dot, duration, voice, pitch, note_type, lyric],
        children_to_ignore=["stem", "beam"],
        error_if_unread_children=True,
    )
    # print(output)
    note = Note()
    for node_content in output:
        if node_content.tag == dot.TAG:
            note.dots += 1
        elif node_content.tag == duration.TAG:
            note.duration = node_content.content
        elif node_content.tag == voice.TAG:
            note.voice = node_content.content
        elif node_content.tag == pitch.TAG:
            note.pitch = node_content.content
        elif node_content.tag == note_type.TAG:
            note.note_type = node_content.content
        elif node_content.tag == lyric.TAG:
            note.lyrics += [node_content.content]

    # print_node(tree_node)
    return note
