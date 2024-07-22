# GLSL (JOV) 🍩

## JOVIMETRIX 🔺🟩🔵/CREATE

Execute custom GLSL (OpenGL Shading Language) fragment shaders to generate images or apply effects. GLSL is a high-level shading language used for graphics programming, particularly in the context of rendering images or animations. This node allows for real-time rendering of shader effects, providing flexibility and creative control over image processing pipelines. It takes advantage of GPU acceleration for efficient computation, enabling the rapid generation of complex visual effects.

![GLSL](https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/master/node/GLSL/GLSL.png)

#### OUTPUT NODE?: `False`

### INPUT

#### OPTIONAL

name | type | desc | default | meta
:---:|:---:|---|:---:|---
🕛  |  FLOAT  | Time | 0 | 
BATCH  |  INT  | Output as a BATCH (all images in a single<br>Tensor) or as a LIST of images (each image<br>processed separately) | 0 | 
🏎️  |  INT  | Frames per second | 24 | 
🇼🇭  |  VEC2  | Set the target dimensions for the output<br>image if scaling is applied | (512, 512) | 
MATTE  |  VEC4  | Define a background color for padding, if<br>necessary. This is useful when images do<br>not fit perfectly into the designated area<br>and need a filler color | (0, 0, 0, 255) | 
✋🏽  |  BOOLEAN  | Wait | False | 
RESET  |  BOOLEAN  | Reset | False | 
VERTEX  |  STRING  | Select a vertex program to load | #version 330 core
void main()
{
    vec2 verts[3] = vec2[](vec2(-1, -1), vec2(3, -1), vec2(-1, 3));
    gl_Position = vec4(verts[gl_VertexID], 0, 1);
}
 | 
FRAGMENT  |  STRING  | Select a fragment program to load | uniform sampler2D imageA;

void mainImage( out vec4 fragColor, vec2 fragCoord ) {
  vec2 uv = fragCoord.xy / iResolution.xy;
  vec3 col = texture2D(imageA, uv).rgb;
  fragColor = vec4(col, 1.0);
}
 | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project