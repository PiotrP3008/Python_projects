from tkinter import *
from road_line import *
from player_car import *
import time
import random


def colision(cp_posx1, cp_posx2, cp_posy1, cp_posy2,
             c1_posx1, c1_posx2, c1_posy1, c1_posy2,
             c2_posx1, c2_posx2, c2_posy1, c2_posy2):

    if((cp_posx1 <= c1_posx2 and cp_posx1 >= c1_posx1) and (cp_posy1 <= c1_posy2 and cp_posy1 >= c1_posy1) or
    (cp_posx2 <= c1_posx2 and cp_posx2 >= c1_posx1) and (cp_posy1 <= c1_posy2 and cp_posy1 >= c1_posy1) or
    (cp_posx1 <= c1_posx2 and cp_posx1 >= c1_posx1) and (cp_posy2 <= c1_posy2 and cp_posy2 >= c1_posy1) or
    (cp_posx2 <= c1_posx2 and cp_posx2 >= c1_posx1) and (cp_posy2 <= c1_posy2 and cp_posy2 >= c1_posy1)):
        return True

    elif ((cp_posx1 <= c2_posx2 and cp_posx1 >= c2_posx1) and (cp_posy1 <= c2_posy2 and cp_posy1 >= c2_posy1) or
    (cp_posx2 <= c2_posx2 and cp_posx2 >= c2_posx1) and (cp_posy1 <= c2_posy2 and cp_posy1 >= c2_posy1) or
    (cp_posx1 <= c2_posx2 and cp_posx1 >= c2_posx1) and (cp_posy2 <= c2_posy2 and cp_posy2 >= c2_posy1) or
    (cp_posx2 <= c2_posx2 and cp_posx2 >= c2_posx1) and (cp_posy2 <= c2_posy2 and cp_posy2 >= c2_posy1)):
        return True

    else:
        return False

def game_over(canvas):
    canvas.create_image(0, 0, image=endgame, anchor=NW)


def startgame():


    CARVELOCITY = 4
    ROADVELOCITY = 7
    LINELENGHT = 75

    LEFTTRAFFICLANE = 135
    RIGHTTRAFFICLANE = 270

    RS = 10

    yl1 = -10
    yl2 = 140
    yl3 = 290
    yl4 = 440


    road_photo = PhotoImage(file='road.png')
    background = canvas.create_image(0, 0, image=road_photo, anchor=NW)

    line_image = PhotoImage(file='road_line.png')
    car1_img = PhotoImage(file='car1.png')
    car2_img = PhotoImage(file='car2.png')
    car3_img = PhotoImage(file='car3.png')

    window.iconphoto(True, car3_img)

    line0 = Road_line(canvas, 239, -2 * LINELENGHT, line_image, ROADVELOCITY, NW)
    line1 = Road_line(canvas, 239, 0, line_image, ROADVELOCITY, NW)
    line2 = Road_line(canvas, 239, 2 * LINELENGHT, line_image, ROADVELOCITY, NW)
    line3 = Road_line(canvas, 239, 4 * LINELENGHT, line_image, ROADVELOCITY, NW)
    line4 = Road_line(canvas, 239, 6 * LINELENGHT, line_image, ROADVELOCITY, NW)

    car1 = Cars(canvas, RIGHTTRAFFICLANE, -250, car1_img, CARVELOCITY, NW, random)
    car2 = Cars(canvas, LEFTTRAFFICLANE, -800, car2_img, CARVELOCITY, NW, random)
    carply = Playercar(canvas, RIGHTTRAFFICLANE - 50, 350, car3_img, CARVELOCITY, NW, random)

    window.bind("<Left>", carply.move_left)
    window.bind("<Right>", carply.move_right)

    score_text = "0"
    i = 0

    while True:
        score.set(score_text)
        line0.move()
        line1.move()
        line2.move()
        line3.move()
        line4.move()
        car1.move()
        car2.move()
        window.update()
        time.sleep(0.01)

        i += 1

        if (i == 100):
            score_text = str(eval(score_text) + 1)
            i = 0

        if (colision(carply.car_position()[0] + RS, carply.car_position()[0] + PhotoImage.width(car3_img) - RS,
                     carply.car_position()[1] + RS, carply.car_position()[1] + PhotoImage.height(car3_img) - RS,
                     car1.car_position()[0] + RS, car1.car_position()[0] + PhotoImage.width(car1_img) - RS,
                     car1.car_position()[1] + RS, car1.car_position()[1] + PhotoImage.height(car1_img) - RS,
                     car2.car_position()[0] + RS, car2.car_position()[0] + PhotoImage.width(car2_img) - RS,
                     car2.car_position()[1] + RS, car2.car_position()[1] + PhotoImage.height(car2_img) - RS)):
            break

    game_over(canvas)




window = Tk()
window.geometry("500x560")
window.resizable(False, False)
window.title("Racer game")
window.config(bg="black")

frame = Frame(window, width=50, height=20)
frame.pack(side="top")

score = StringVar()

label = Label(frame, text="Score:", font=("Comic sans", 20), fg="yellow", bg="black", width=6, height=2)
label.grid(row=0, column=0, sticky=NW)

label2 = Label(frame, textvariable=score, font=("Comic sans", 20), fg="yellow", bg="black", width=10, height=2,
               anchor=W)
label2.grid(row=0, column=1)

tryagain = Button(frame, text="Try again", height=1, width=7, fg="yellow", bg="black", activebackground="black",
                  font=("Comic sans", 20), relief="flat", command=startgame)
tryagain.grid(row=0, column=2, sticky=NS)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

endgame = PhotoImage(file="end_game.png")



startgame()

window.mainloop()