  
Save the output image along with its metadata to the specified path. Supports saving additional user metadata and prompt information.  
![SAVE OUTPUT](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/SAVE%20OUTPUT/SAVE%20OUTPUT.png)
### OUTPUT NODE?: True
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| image | IMAGE |  |  |  |
| path | STRING | Destination path to save the output |  |  |
| fname | STRING | Filename of the output | output |  |
| metadata | JSON | Extra metadata to save in the file |  |  |
| usermeta | STRING | Custom user metadat to save with the file |  |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project