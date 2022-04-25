
from functools import lru_cache
from app.core import ximea
class Recorder():
    def __init__(self):
        self.setupUi(self)
        xiC = ximea.XiCMonoConfig()
        self.camera = ximea.XimeaCamera(xiC.get_instance())

@lru_cache
def geter():
    record=Recorder()