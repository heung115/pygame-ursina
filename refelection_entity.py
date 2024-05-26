from ursina import *
from ursina.shaders import lit_with_shadows_shader


class ReflectiveEntity(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.shader = Shader(
        #     language=Shader.GLSL,
        #     vertex="""
        # #version 140
        # uniform mat4 p3d_ModelViewProjectionMatrix;
        # in vec4 p3d_Vertex;
        # void main() {
        #     gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
        # }
        # """,
        #     fragment="""
        # #version 140
        # out vec4 fragColor;
        # void main() {
        #     fragColor = vec4(1.0, 0.85, 0.75, 1.0);
        # }
        # """,
        # )
        self.shader = lit_with_shadows_shader
