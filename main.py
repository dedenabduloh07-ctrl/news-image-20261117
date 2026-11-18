# Copies the bundled entry image to /output/entry.png.
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
out = os.environ.get("ENTRY_OUTPUT", "/output/entry.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
shutil.copyfile(os.path.join(here, "entry.png"), out)
