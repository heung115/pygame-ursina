#version 120

varying vec4 vertex_color;
void main() {
    vec2 uv = gl_FragCoord.xy / vec2(800.0, 600.0);  // 화면 크기에 맞게 조정
    float edge_width = 0.01;  // 테두리 두께

    if (uv.x < edge_width || uv.x > (1.0 - edge_width) || uv.y < edge_width || uv.y > (1.0 - edge_width)) {
        gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);  // 검은색 테두리
    } else {
        gl_FragColor = vertex_color;
    }
}
