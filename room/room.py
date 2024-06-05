from ursina import *


from room.cabinetTV import CabinetTelevision
from room.chair import Chair
from room.lounge_sofa import LoungeSofa
from room.pottedPlant import PottedPlant
from room.radio import Radio
from room.tableGlass import TableCoffeeGlass
from room.tv import TelevisionModern
from room.wall import Wall
from room.floor import Floor
from room.door import Door
from room.book_case import BookCase
from room.bedBunk import BedBunk
from room.desk import Desk
from room.rug_square import RugSquare
from room.safe_box import SafeBox
from room.bookcase2 import bookcase2
from room.bookcase3 import Bookcase_Closed
from room.book2 import book2
from room.sidetable import sidetable
from room.rug import rug
from room.desk_corner import DeskCorner
from room.laptop import Laptop
from room.chair_desk import ChairDesk
from room.cabinet_bed import CabinetBed
from room.door_open import Door_open
from room.ceilingFan import Ceiling_Fan
from room.computer import Computer

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


def setup_room(item_entity):
    floor = Floor(position=(-10, 0, -10), scale=(20, 1, 20))
    setup_wall()

    door = Door(position=(-2, 0, -9.9), scale=(6, 6, 2))
    door_open = Door_open(position=(-2, 0, -9.95), scale=(6, 6, 2))
    book_case = BookCase(position=(3, 0, 8.7), scale=(5), rotation=(0, 0, 0))
    bed_bunk = BedBunk(position=(-9.6, 0, 4), scale=(5), rotation=(0, 0, 0))

    desk = Desk(position=(-5, 0, 8), scale=(5), rotation=(0, 0, 0))
    chair = Chair(position=(-5, 0, 5), scale=(5), rotation=(0, 0, 0))

    safe_box = SafeBox(
        position=(-1, 0, 0),
        scale=(1.5),
        rotation=(180, 0, 180),
        key_to_show=item_entity["key_safe_box"],
    )

    rug_square = RugSquare(
        position=(0.5, 0.1, 0.5), scale=(10, 10, 10), rotation=(0, 0, 0)
    )

    television_modern = TelevisionModern(
        position=(5, 0, 4), scale=(10, 10, 10), rotation=(0, 0, 0), lock_num=3
    )
    lounge_sofa = LoungeSofa(position=(5, 0, 4), scale=(10, 10, 10), rotation=(0, 0, 0))

    potted_plant = PottedPlant(
        position=(3, 0, 4), scale=(10, 10, 10), rotation=(0, 0, 0)
    )

    cabinet_television = CabinetTelevision(
        position=(5, 0, 4), scale=(10, 10, 10), rotation=(0, 0, 0)
    )

    table_coffee_glass = TableCoffeeGlass(
        position=(5, 0, 4), scale=(10, 10, 10), rotation=(0, 0, 0)
    )

    radio = Radio(position=(5, 0, 4), scale=(10, 10, 10), rotation=(0, 0, 0))
    radio = Computer(position=(6.5, 2, 9), scale=(5), rotation=(0, 20, 0))
    radio = bookcase2(position=(-10, 0, -1), scale=(6, 6, 6), rotation=(0, 90, 0))
    bookcase = Bookcase_Closed(
        position=(-8.5, 0, -5.9), scale=(6, 6, 6), rotation=(0, -90, 0)
    )
    bookcase = Bookcase_Closed(
        position=(-8.5, 0, -8.3), scale=(6, 6, 6), rotation=(0, -90, 0)
    )
    radio = book2(position=(-9.7, 1.5, -0.6), scale=(6, 6, 6), rotation=(0, 0, 0))
    radio = sidetable(position=(-7, 0, -1), scale=(4, 4, 6), rotation=(0, 0, 0))
    radio = rug(position=(-5.5, 0.1, -5.5), scale=(60, 60, 60), rotation=(0, 0, 0))

    desk_corner = DeskCorner(position=(5, 0, 5), scale=(5), rotation=(0, 0, 0))
    laptop = Laptop(position=(8.5, 2, 8), scale=(5), rotation=(0, 80, 0))
    chair_desk = ChairDesk(position=(7, 0, 7), scale=(5), rotation=(0, 180, 0))
    cabinet_bed = CabinetBed(position=(5, 1.8, 9), scale=(5), rotation=(0, 0, 0))

    # celling_fan = Ceiling_Fan(position=(0, 10.5, 0), scale=12, rotation=(0, 0, 0))

    return {
        "floor": floor,
        "door": door,
        "book_case": book_case,
        "bed_bunk": bed_bunk,
        "desk": desk,
        "chair": chair,
        "rug_square": rug_square,
        "safe_box": safe_box,
        "television_modern": television_modern,
        "lounge_sofa": lounge_sofa,
        "potted_plant": potted_plant,
        "cabinet_television": cabinet_television,
        "table_coffee_glass": table_coffee_glass,
        "radio": radio,
        "desk_corner": desk_corner,
        "laptop": laptop,
        "chair_desk": chair_desk,
        "cabinet_bed": cabinet_bed,
    }
