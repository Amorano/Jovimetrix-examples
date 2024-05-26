# IMAGE DIFF (JOV) 📏

## JOVIMETRIX 🔺🟩🔵/UTILITY

The Image Diff node compares two input images pixel by pixel to identify differences between them. It takes two images as input, labeled as Image A and Image B. The node then calculates the absolute difference between the two images, producing two additional outputs: a difference mask and a threshold mask. The threshold parameter determines the sensitivity of the comparison, with higher values indicating more tolerance for differences. The node returns Image A, Image B, the difference mask, and the threshold mask.

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name|type|desc|default|meta
:---:|:---:|---|:---:|---
👾A| * | pixel data (rgba, rgb or grayscale) |  | 
👾B| * | pixel data (rgba, rgb or grayscale) |  | 
📉| FLOAT | threshold | 0.5 | 

### OUTPUT

name|type|desc
:---:|:---:|---
🅰️| IMAGE | Input A 
🅱️| IMAGE | Input B 
DIFF| MASK | Difference 
📉| MASK | Threshold 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project