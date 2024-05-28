# GLSL (JOV) 🍩

## JOVIMETRIX 🔺🟩🔵/GLSL

The GLSL Node executes custom GLSL (OpenGL Shading Language) fragment shaders to generate images or apply effects. GLSL is a high-level shading language used for graphics programming, particularly in the context of rendering images or animations. This node allows for real-time rendering of shader effects, providing flexibility and creative control over image processing pipelines. It takes advantage of GPU acceleration for efficient computation, enabling the rapid generation of complex visual effects.

![GLSL](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GLSL/GLSL.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
👾 | * | pixel data (rgba, rgb or<br>grayscale) |  | 
🕛 | FLOAT | time | 0 | 
BATCH | VEC2 | process multiple images | (1, 30) | 
✋🏽 | BOOLEAN | wait | False | 
RESET | BOOLEAN | reset | False | 
🇼🇭 | VEC2 | width and height | (32, 32) | 
FRAGMENT | STRING | shader fragment program | void main() {
    vec4 texColor = texture(iChannel0, fragCoord);
    vec4 color = vec4(fragCoord, abs(sin(iTime)), 1.0);
    fragColor = vec4((texColor.xyz + color.xyz) / 2.0, 1.0);
} | 
PARAM | STRING | parameters | {} | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️ | IMAGE | Image 
🌈 | IMAGE | RGB (no alpha) Color 
😷 | MASK | Mask or Image to use as Mask to control<br>where adjustments are applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project