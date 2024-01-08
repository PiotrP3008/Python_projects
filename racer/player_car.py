from cars import *

class Playercar:

    def __init__(self, canvas, x1, y1, car, carVelocity, dir, random):
        self.canvas = canvas
        self.random = random
        self.image = canvas.create_image(x1, y1, image=car, anchor=dir)
        self.carVelocity = carVelocity

    def move_left(self, event):
        self.canvas.move(self.image, -5, 0)

        coordinates = self.canvas.coords(self.image)
        if (coordinates[0] < 120):
            self.canvas.move(self.image, 129-coordinates[0], 0)


    def move_right(self, event):
        self.canvas.move(self.image, 5, 0)

        coordinates = self.canvas.coords(self.image)
        if (coordinates[0] > 275):
            self.canvas.move(self.image, -(coordinates[0]-275), 0)

    def car_position(self):
        coordinates = self.canvas.coords(self.image)
        return coordinates
