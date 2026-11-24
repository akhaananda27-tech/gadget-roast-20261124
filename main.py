"""gadget-roast-20261124 — entry for the make.fun bounty
"One-Line Roast: The Gadget You Use Every Day".

The entry itself is a single one-line roast of the gadget I use every
day — my phone — stored verbatim in roast.txt. This script is the
entrypoint: it loads roast.txt from the directory next to this file
(never a relative path, so it works from any working directory) and
prints it exactly, byte for byte, with no trailing newline added.
"""

# The roast below pokes fun at a face-unlock sensor that cannot tell
# its owner apart from his brother — or a potato.
import pathlib

roast_path = pathlib.Path(__file__).resolve().parent / "roast.txt"
print(roast_path.read_text(encoding="utf-8"), end="")
