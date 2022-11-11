def on_button_pressed_a():
    global Rating, rating2
    Rating = [4, 7, 8, 6, 9]
    basic.show_string("" + str((Rating[randint(0, 5)])))
    rating2 = [3, 7, 1, 3, 8]
    basic.show_string("" + str((Rating[randint(0, 5)])))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global SWins, VWins
    if Rating > rating2:
        SWins += 1
        basic.show_number(SWins)
    else:
        VWins += 1
        basic.show_number(SWins)
input.on_button_pressed(Button.B, on_button_pressed_b)

VWins = 0
SWins = 0
rating2 = 0
Rating: List[number] = []
Superheroes = ["Iron-Man",
    "Thor",
    "Captain America",
    "Dr Strange",
    "Spiderman"]
Villains = ["Mandarin", "Loki", "Red Skull", "Wanda", "Green Goblin"]

def on_forever():
    pass
basic.forever(on_forever)
