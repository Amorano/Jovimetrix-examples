[DELAY (JOV) ✋🏽](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/DELAY/DELAY.md)
------------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/CALC
  
Introduce pauses in the workflow that accept an optional input to pass through and a timer parameter to specify the duration of the delay. If no timer is provided, it defaults to a maximum delay. During the delay, it periodically checks for messages to interrupt the delay. Once the delay is completed, it returns the input passed to it. You can disable the screensaver with the `ENABLE` option  
![DELAY](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/DELAY/DELAY.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| 📥 | \* | Pass In |  |  |
| ⏱ | INT | Timer | 0 |  |
| ENABLE | BOOLEAN | Enable or disable the screensaver | True |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 📤 | \* | Pass Out |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project