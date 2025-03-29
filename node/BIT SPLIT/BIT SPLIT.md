  
Split an input into separate bits.  
BOOL, INT and FLOAT use their numbers,  
STRING is treated as a list of CHARACTER.  
IMAGE and MASK will return a TRUE bit for any non-black pixel, as a stream of bits for all pixels in the image.  
![BIT SPLIT](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/BIT%20SPLIT/BIT%20SPLIT.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| VALUE | \* | the value to convert into bits |  |  |
| BITS | INT | number of output bits requested | 8 |  |
| MSB | BOOLEAN | return the most signifigant bits (True) or least signifigant bits first | False |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
|  | \* | Bits as Numerical output (0 or 1) |
| 🇴 | BOOLEAN | Bits as Boolean output (True or False) |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project