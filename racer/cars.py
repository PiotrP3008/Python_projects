
class Cars:

    def __init__(self, canvas, x1, y1, car, carVelocity, dir, random):
        self.canvas = canvas
        self.random = random
        self.image = canvas.create_image(x1, y1, image=car, anchor=dir)
        self.carVelocity = carVelocity

    def move(self):

        coordinates = self.canvas.coords(self.image)

        self.canvas.move(self.image, 0, self.carVelocity)



        if (coordinates[1] > 500):

            tl = self.random.randint(1, 2)
            distance = self.random.randint(1, 4)

            if(tl==1):
                if (coordinates[0] == 135):
                    self.canvas.move(self.image, 0, -1000*distance)
                else:
                    self.canvas.move(self.image, -135, -1000*distance)
            elif(tl==2):
                if (coordinates[0] == 270):
                    self.canvas.move(self.image, 0, -1000*distance)
                else:
                    self.canvas.move(self.image, 135, -1000*distance)


    def car_position(self):
        coordinates = self.canvas.coords(self.image)
        return coordinates



