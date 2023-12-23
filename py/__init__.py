#

import os
from PIL.PngImagePlugin import PngInfo
from PIL import Image

# =============================================================================
# === Jovimetrix Cleanup Support ===
# =============================================================================

def merge_metadata(fn: str, out: str, data: dict) -> None:
    with Image.open(fn) as image:
        metadata = PngInfo()
        for i in image.text:
            if i == 'workflow':
                continue
            metadata.add_text(i, str(image.text[i]))
        metadata.add_text("workflow", data.encode('utf-8'))
        image.save(out, pnginfo=metadata)
        print(f"{fn} ==> {out}")

def merge_all_metadata(root: str, target: str) -> None:
    for r, _, fs in os.walk(root):
        for f in fs:
            f, ext = os.path.splitext(f)
            if ext != '.json':
                continue

            img = f"{r}/{f}.png"
            if not os.path.isfile(img):
                continue

            fn = f"{r}/{f}.json"
            with open(fn, "r", encoding="utf-8") as out:
                data = out.read()

            out = f"{target}/{f}.png"
            # merge_metadata(img, out, data)
            print(img, out, len(data))

# =============================================================================
# === ASILE 5 ===
# =============================================================================

if __name__ == "__main__":
    merge_all_metadata('.')