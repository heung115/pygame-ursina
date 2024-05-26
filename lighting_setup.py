from ursina import *
from ursina.lights import DirectionalLight
from ursina.shaders import lit_with_shadows_shader


def setup_lighting():

    pivot = Entity()

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
    directional_light = DirectionalLight(shadows=True)
    directional_light.look_at(Vec3(1, -1, -1))
    # ambient_light = AmbientLight(color=color.white * 0.6)
    # light1 = PointLight(
    #     parent=pivot, position=(1, 10, 1), color=color.white, intensity=0.3
    # )
    # light2 = PointLight(
    #     parent=pivot, position=(-1, 10, -1), color=color.white, intensity=0.3
    # )


# return light
