[GLSL (JOV) 🍩](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/GLSL/GLSL.md)
--------------------------------------------------------------------------------------------
### JOVIMETRIX 🔺🟩🔵/CREATE
  
Execute custom GLSL (OpenGL Shading Language) fragment shaders to generate images or apply effects. GLSL is a high-level shading language used for graphics programming, particularly in the context of rendering images or animations. This node allows for real-time rendering of shader effects, providing flexibility and creative control over image processing pipelines. It takes advantage of GPU acceleration for efficient computation, enabling the rapid generation of complex visual effects.  
![GLSL](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GLSL/GLSL.png)
### OUTPUT NODE?: False
INPUT
-----
### OPTIONAL
| Name | Type | Description | Default | Meta |
| --- | --- | --- | --- | --- |
| MODE | STRING | Decide whether the images should be resized to fit a specific dimension. Available modes include scaling to fit within given dimensions or keeping the original size | MATTE | MATTE, CROP, FIT, ASPECT, ASPECT SHORT, RESIZE MATTE |
| 🇼🇭 | VEC2INT | Width and Height as a Vector2 (x,y) | [512, 512] |  |
| 🎞️ | STRING | Select the method for resizing images. Options range from nearest neighbor to advanced methods like Lanczos, ensuring the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4, LINEAR EXACT, NEAREST EXACT |
| MATTE | VEC4INT | Define a background color for padding, if necessary. This is useful when images do not fit perfectly into the designated area and need a filler color | [0, 0, 0, 255] |  |
| EDGE\_X | STRING | Clip or Wrap the Canvas Edge | CLAMP | CLAMP, WRAP, MIRROR |
| EDGE\_Y | STRING | Clip or Wrap the Canvas Edge | CLAMP | CLAMP, WRAP, MIRROR |
| BATCH | INT | Output as a BATCH (all images in a single Tensor) or as a LIST of images (each image processed separately) | 0 |  |
| 🏎️ | INT | Frames per second | 24 |  |
| 🕛 | FLOAT | Time | 0 |  |
| VERTEX | STRING | Select a vertex program to load | // name: BASIC VERTEX SHADER
// desc: draws 2 triangles as a quad for a surface to manipulate
#version 460
precision highp float;
void main()
{
 vec2 verts[3] = vec2[](vec2(-1, -1), vec2(3, -1), vec2(-1, 3));
 gl\_Position = vec4(verts[gl\_VertexID], 0, 1);
}
 |  |
| FRAGMENT | STRING | Select a fragment program to load | // name: BASIC FRAGMENT SHADER
// desc: draws 2 triangles as a quad for a surface to manipulate
// hide: true
uniform sampler2D image;
void mainImage( out vec4 fragColor, vec2 fragCoord ) {
 vec2 uv = fragCoord / iResolution.xy;
 fragColor = texture(image, uv);
}
 |  |
OUTPUT
------
| Name | Type | Description |
| --- | --- | --- |
| 🖼️ | IMAGE | Image |
| 🌈 | IMAGE | RGB (no alpha) Color |
| 😷 | MASK | Mask or Image to use as Mask to control where adjustments are applied |
Original help system powered by [MelMass](https://github.com/melMass) & the [comfy\_mtb](https://github.com/melMass/comfy_mtb) project