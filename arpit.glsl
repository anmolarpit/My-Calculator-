#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform float u_time;

vec3 palette (float t)
{ vec3 a = vec3(0.451, 0.6471, 0.9412);
vec3 b = vec3(0.6431, 0.7765, 0.0627);
vec3 c = vec3(0.7451, 0.6039, 0.6863);
vec3 d = vec3(0.5176, 0.0314, 0.1922);

return a+ b*cos(09.98*(c+c+c*t+d));
}
void main()
{
    vec2 uv = (gl_FragCoord.xy * 2.0 - u_resolution.xy) / u_resolution.y;
    float d = length(uv);
    vec3 col = palette(d);
    d= sin(d*8.0 + u_time)/8.0;
    d=abs(d);
    d = 0.02/d;
    col *= d;

    gl_FragColor = vec4(col, 1.0);
     
}
