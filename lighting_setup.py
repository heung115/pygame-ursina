from ursina import *
from ursina.lights import DirectionalLight
from ursina.shaders import lit_with_shadows_shader


def setup_lighting():

    # main_light = PointLight(
    #     parent=pivot,
    #     position=(0, 10, 0),
    #     color=color.rgb(200, 200, 200),
    #     intensity=0.2,
    # )
    # light = PointLight(
    #     parent=pivot,
    #     direction=(0, 10, 0),
    #     color=color.white,
    #     intensity=0.7,
    #     shadows=True,
    # )
    # directional_light = DirectionalLight(shadows=True)
    # directional_light.look_at(Vec3(1, -1, -1))
    ambient_light = AmbientLight(color=color.white * 0.6)
    # light1 = PointLight(
    #     position=(0, 10, 0),
    #     color=color.white,
    #     intensity=0.01,
    #     radius=20,
    #     shadows=True,
    #     constant_attenuation=0,
    #     linear_attenuation=0.04,
    #     quadratic_attenuation=0.01,
    # )


# return light
