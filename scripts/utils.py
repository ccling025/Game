import pygame

LOCAL_PATH = "C:/Users/nick9/OneDrive/文件/GitHub/Game/data/image/object/player"

def load_image(path):
    img = pygame.image.load(LOCAL_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img