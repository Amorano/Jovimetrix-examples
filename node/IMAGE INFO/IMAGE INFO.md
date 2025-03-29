  
Exports and Displays immediate information about images.  
![IMAGE INFO](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/IMAGE%20INFO/IMAGE%20INFO.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 👾A | IMAGE, MASK | The image to examine |  |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🔟 | INT | Batch count |
| 🇼 | INT | Width |
| 🇭 | INT | Height |
| 🇨 | INT | Channels |
| 🇼🇭 | VEC2 | Width & Height as a VEC2 |
| 🇼🇭🇨 | VEC3 | Width, Height and Channels as a VEC3 |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project