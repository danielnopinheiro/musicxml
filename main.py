import xml.etree.ElementTree as ET

import score_partwise

filename = "sample.musicxml"

tree = ET.parse(filename)
root = tree.getroot()

if root.tag == "score-partwise":
    score_contents = score_partwise.read(root)
else:
    raise NotImplementedError()

print("Done!")
