import pathlib

roast_path = pathlib.Path(__file__).resolve().parent / "roast.txt"
print(roast_path.read_text(encoding="utf-8"), end="")
