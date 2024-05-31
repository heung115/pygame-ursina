from abc import ABC, ABCMeta
from ursina import *


class CommonMeta(ABCMeta, type(Entity)):
    pass
