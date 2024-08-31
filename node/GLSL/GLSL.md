## [GLSL (JOV) 🍩](https://github.com/Amorano/Jovimetrix-examples/blob/master/node/GLSL/GLSL.md)

## JOVIMETRIX 🔺🟩🔵/CREATE


Execute custom GLSL (OpenGL Shading Language) fragment shaders to generate images or apply effects. GLSL is a high-level shading language used for graphics programming, particularly in the context of rendering images or animations. This node allows for real-time rendering of shader effects, providing flexibility and creative control over image processing pipelines. It takes advantage of GPU acceleration for efficient computation, enabling the rapid generation of complex visual effects.


![GLSL](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GLSL/GLSL.png)

#### OUTPUT NODE?: `False`

## INPUT

### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
MODE  |  STRING  | Decide whether the images should be<br>resized to fit a specific dimension.<br>Available modes include scaling to fit<br>within given dimensions or keeping the<br>original size | NONE | NONE, CROP, MATTE, FIT, ASPECT, ASPECT<br>SHORT
🇼🇭  |  VEC2INT  | Width and Height as a Vector2 (x,y) | [512, 512] | 
🎞️  |  STRING  | Select the method for resizing images.<br>Options range from nearest neighbor to<br>advanced methods like Lanczos, ensuring<br>the best quality for the specific use case | LANCZOS4 | NEAREST, LINEAR, CUBIC, AREA, LANCZOS4,<br>LINEAR EXACT, NEAREST EXACT
MATTE  |  VEC4INT  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | [0, 0, 0, 255] | 
BATCH  |  INT  | Output as a BATCH (all images in a single<br>Tensor) or as a LIST of images (each image<br>processed separately) | 0 | 
🏎️  |  INT  | Frames per second | 24 | 
🕛  |  FLOAT  | Time | 0 | 
VERTEX  |  STRING  | Select a vertex program to load | 
#version 330 core

precision highp float;

void main()
{
    vec2 verts[3] = vec2[](vec2(-1, -1), vec2(3, -1), vec2(-1, 3));
    gl_Position = vec4(verts[gl_VertexID], 0, 1);
}
 | 
FRAGMENT  |  STRING  | Select a fragment program to load | 
uniform sampler2D image;

void mainImage( out vec4 fragColor, vec2 fragCoord ) {
    vec2 uv = fragCoord / iResolution.xy;
    // Correcting for aspect ratio
    // uv.y *= (iResolution.x / iResolution.y);
    fragColor = texture(image, uv);
}
 | 

## OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

original help system powered by [MelMass](https://github.com/melMass) & the [comfy_mtb](https://github.com/melMass/comfy_mtb) project