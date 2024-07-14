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
BATCH  |  INT  | Output as a BATCH (all images in a single<br>Tensor) or as a LIST of images (each image<br>processed separately) | 1 | 
🏎️  |  INT  | Frames per second | 24 | 
🇼🇭  |  VEC2  | Set the target dimensions for the output<br>image if scaling is applied | (512, 512) | 
✋🏽  |  BOOLEAN  | Wait | False | 
RESET  |  BOOLEAN  | Reset | False | 
FRAGMENT  |  STRING  | Shader Fragment Program | 
uniform sampler2D imageA;
uniform sampler2D imageB;
uniform float size; // 7.
uniform float time_scale; // 19.

void mainImage( out vec4 fragColor, vec2 fragCoord ) {
  vec2 u = floor(fragCoord / size);
  float s = dot(u, u) + iTime / time_scale;
  u = mod(u, 2.);

  vec2 uv = fragCoord.xy / iResolution.xy;
  //vec3 col2 = texture2D(imageB, uv).rgb;
  vec3 col = texture2D(imageA, uv).rgb;


  fragColor = vec4(col + (floor(sin(s)) - u.y - floor(cos(s)) - u.xxxx).rgb, 1.0);
}
 | 

### OUTPUT

name | type | desc
:---:|:---:|---
🖼️  |  IMAGE  | Image 
🌈  |  IMAGE  | RGB (no alpha) Color 
😷  |  MASK  | Mask or Image to use as Mask to control where adjustments are<br>applied 

help powered by [MelMass](https://github.com/melMass) & [comfy_mtb](https://github.com/melMass/comfy_mtb) project