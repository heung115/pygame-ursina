from ursina import Ursina, EditorCamera, color, Vec3, Vec2
from ursina import Entity, DirectionalLight
from basic_lighting_shader import get_basic_lighting_shader

app = Ursina()
basic_lighting_shader = get_basic_lighting_shader()
EditorCamera()
plane = Entity(model="plane", scale=10, color=color.gray, shader=basic_lighting_shader)
middle = Entity(model="cube", y=1, shader=basic_lighting_shader, color=color.light_gray)

light = DirectionalLight(shadows=True)
light.look_at(Vec3(1, -1, 1))
light.shadow_map_resolution = Vec2(2048, 2048)
light.shadow_bias = 0.001

dont_cast_shadow = Entity(
    model="cube", y=1, shader=basic_lighting_shader, x=2, color=color.light_gray
)
dont_cast_shadow.hide(0b0001)

unlit_entity = Entity(model="cube", y=1, x=-2, unlit=True, color=color.light_gray)

bar = Entity(
    model="cube",
    position=(0, 3, -2),
    shader=basic_lighting_shader,
    scale=(10, 0.2, 0.2),
    color=color.light_gray,
)

app.run()
