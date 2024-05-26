from ursina import Shader


def get_basic_lighting_shader():
    vertex_shader = """
    #version 330 core
    layout(location = 0) in vec3 p3d_Vertex;
    layout(location = 1) in vec2 p3d_MultiTexCoord0;
    layout(location = 2) in vec3 p3d_Normal;

    uniform mat4 p3d_ModelViewProjectionMatrix;
    uniform mat4 p3d_ModelMatrix;

    out vec2 texcoord;
    out vec3 world_normal;

    void main() {
        gl_Position = p3d_ModelViewProjectionMatrix * vec4(p3d_Vertex, 1.0);
        texcoord = p3d_MultiTexCoord0;
        world_normal = normalize(mat3(p3d_ModelMatrix) * p3d_Normal);
    }
    """

    fragment_shader = """
    #version 330 core
    in vec2 texcoord;
    in vec3 world_normal;

    uniform sampler2D p3d_Texture0;
    uniform vec4 p3d_ColorScale;

    out vec4 fragColor;

    void main() {
        vec4 norm = vec4(world_normal * 0.5 + 0.5, 1);
        float grey = 0.21 * norm.r + 0.71 * norm.g + 0.07 * norm.b;
        norm = vec4(grey, grey, grey, 1);
        vec4 color = texture(p3d_Texture0, texcoord) * p3d_ColorScale * norm;
        fragColor = color;
    }
    """

    return Shader(language=Shader.GLSL, vertex=vertex_shader, fragment=fragment_shader)
