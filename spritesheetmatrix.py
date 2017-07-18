# Adapted from https://pygame.org/wiki/Spritesheet

import pygame


class spritesheetmatrix(object):
    def __init__(self, filename, rows=3, cols=4, colorkey=None):
        try:
            self.rows = int(rows)
            self.cols = int(cols)
            self.colorkey = colorkey

            self.sprite_tuples = []

            self.sheet = pygame.image.load(filename)
            dimensions = self.sheet.get_rect().size
            self.sprite_width = int(dimensions[0] / cols)
            self.sprite_height = int(dimensions[1] / rows)

            self.sheet = self.sheet.convert()
            self.create_rects()
            self.sprites = self.images_at(colorkey)

        except:
            print("Unable to load spritesheet img: " + filename)
            raise SystemExit('Problem opening file')

    def create_rects(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                self.sprite_tuples.append((col * self.sprite_width, row * self.sprite_height, self.sprite_width, self.sprite_height))

    def image_at(self, rectangle, colorkey=None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()

        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, colorkey=None):
        return [self.image_at(rect, colorkey) for rect in self.sprite_tuples]

    def load_strip(self, rect, image_count, colorkey = None):
        """Loads a strip of images"""
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

    def get_sprite(self, index):
        """Loads a strip of images"""
        if index in range (0,self.get_num_sprites()):
            return self.sprites[index]

        return 0

    def get_sprite_width(self):
        return self.sprite_width

    def get_sprite_height(self):
        return self.sprite_height

    def get_num_sprites(self):
        return int(self.rows * self.cols)

    def get_forward_sprites(self):
        return self.sprites[0::4]

    def get_backward_sprites(self):
        return self.sprites[2::4]

    def get_right_sprites(self):
        return self.sprites[1::4]

    def get_left_sprites(self):
        return self.sprites[3::4]