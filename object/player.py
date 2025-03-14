import pygame

LOCAL_PATH = "C:/Users/nick9/OneDrive/文件/GitHub/Game/data/image/object/player"

class PhysicEntities:
    def __init__(self):
        

        self.img = pygame.image.load(LOCAL_PATH + "/banana-151553_640.webp")

    def update(self):
        pass