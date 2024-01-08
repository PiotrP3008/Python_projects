class Road_line:

    def __init__(self, canvas, x1, y1, line, lineVelocity, dir):
        self.canvas = canvas
        self.image = canvas.create_image(x1, y1, image=line, anchor=dir)
        self.lineVelocity = lineVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)
        #print(coordinates)

        self.canvas.move(self.image, 0, self.lineVelocity)

        if(coordinates[1]>500):
            self.canvas.move(self.image, 0, -750)



