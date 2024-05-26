from ursina import *
from room.chair import Chair
from room.wall import Wall
from room.floor import Floor
from room.door import Door

wall_thickness = 0.2
wall_height = 10


def setup_room(roomSize=10):
    # floor = Entity(
    #     model="cube",
    #     scale=(10, 10, 1),
    #     position=(0, -1, 0),
    #     rotation_x=90,
    #     texture="white_cube",
    #     collider="box",
    #     texture_scale=(10, 10),
    # )
    floor = Floor(position=(-10, 0, -10), scale=(20, 1, 20))
    Wall(
        position=(0, wall_height / 2, 10),
        scale=(20, wall_height, wall_thickness),
        rotation=(0, 0, 0),
    )
    Wall(
        position=(0, wall_height / 2, -10),
        scale=(20, wall_height, wall_thickness),
        rotation=(0, 0, 0),
    )
    Wall(
        position=(10, wall_height / 2, 0),
        scale=(wall_thickness, wall_height, 20),
        rotation=(0, 0, 0),
    )
    Wall(
        position=(-10, wall_height / 2, 0),
        scale=(wall_thickness, wall_height, 20),
        rotation=(0, 0, 0),
    )
    # ceiling = Entity(
    #     model="quad",
    #     scale_x=10,
    #     scale_z=10,
    #     rotation_x=-90,
    #     y=wall_height,
    #     texture="white_cube",
    #     texture_scale=(10, 10),
    # )
    door = Door(position=(0, 0, 5), scale=(4, 4, 1))
    door.shadow = True
