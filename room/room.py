from ursina import *
from room.chair import Chair
from room.wall import Wall
from room.floor import Floor
from room.door import Door
from room.book_case import BookCase
from room.bedBunk import BedBunk
from room.desk import Desk

wall_thickness = 0.2
wall_height = 10


def setup_wall():
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


def setup_room(roomSize=10):
    floor = Floor(position=(-10, 0, -10), scale=(20, 1, 20))

    setup_wall()
    door = Door(position=(0, 0, -9.5), scale=(4, 4, 1))
    book_case = BookCase(position=(5, 0, 5), scale=(5), rotation=(0, 0, 0))
    bed_bunk = BedBunk(position=(-9.6, 0, 4), scale=(5), rotation=(0, 0, 0))
    desk = Desk(position=(-5, 0, 8), scale=(5), rotation=(0, 0, 0))
    door.shadow = True
