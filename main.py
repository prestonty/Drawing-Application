# Drawing Application:
# Capable of drawing free-style and switching colours through colour palette. Current colour is also displayed
# Can fill entire screen with entire drawing screen with colour and erase everything off drawing screen
# can change drawing thickness through buttons
# Shapes can be drawn and its size can be changed through increasing length and width with buttons
# imported emojis are available to be used
# music is also imported with use of keyboard inputs and song selection
# Preston Tom-Ying and Patrick Zhang     Started: May 29, 2021      Finished: June 16, 2021


import pygame
pygame.init()  # initialize Pygame (resets all numbers)
from pygame import mixer

# window set up
win = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Drawing Application")
win.fill((255, 255, 255))

# VARIABLES  -----------------------------------------------------------------------------------------------------

# Colour palette
red = (255, 0, 0)
red2 = (128, 0, 128)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green = (128, 255, 0)
green2 = (0, 255, 0)
green3 = (0, 255, 128)
blue = (0, 255, 255)
blue2 = (0, 128, 255)
blue3 = (0, 0, 255)
purple = (128, 0, 255)
pink = (255, 0, 255)
brown = (100, 50, 0)
white = (255, 255, 255)  # use eraser
black = (0, 0, 0)  # use pencil image

colours = [red, red2, orange, yellow, green, green2, green3, blue, blue2, blue3, purple, pink, brown, white, black]

# col is the variable that changes when you select a colour. At beginning, colour is black.
col = black

# thickness.
# thick is the thickness variable. Changes the radius of the circle.
thick = 10
# these are the selections of the radius of the circle used to draw on the screen
thickArray = [7, 10, 20, 30, 40]
# this is only used in the toolbar since we can't fit the actual thicknesses in
displayThic = [2, 5, 10, 15, 20]

# shape variables
# shapes start out as a circle
shape = "circle"
# starting length is 40 of the shapes. Can increase and decrease
length = 40
# starting width of the shapes is 40. Can increase and decrease.
width = 40

# these are the coordinates for displaying the shapes on the toolbar. (use pygame.draw.polygon)
triangleTool = [(620, 60+30), (640, 60+60), (600, 60+60), (620, 60+30)]
hexagonTool = [(605 - 20+165, 105), (605 - 10+165, 105 - 17.5), (605 + 10+165, 105 - 17.5),
                (605 + 20+165, 105), (605 + 10+165, 105 + 17.5), (605 - 10+165, 105 + 17.5)]
pentagonTool = [(590+105, 100 - 20), (590 + 20+105, 100), (590 + 10+105, 100 + 20), (590 - 10+105, 100 + 20),
                (590 - 20+105, 100), (590+105, 100 - 20)]
starTool = [(590 + 2.5+245, 100 - 1.5), (590 + 6.5+245, 100 - 14.5),
                     (590 + 10+245, 100 - 1.5), (590 + 23+245, 100 - 1.5),
                     (590 + 11.5+245, 100 + 6.5), (590 + 16.5+245, 100 + 18.5),
                     (590 + 6.+245, 100 + 9.5), (590 - 4+245, 100 + 18.5),
                     (590 + 1+245, 100 + 5), (590 - 11+245, 100 - 1.5)]


# emoji variables
# load the emojis from your file
E1 = pygame.image.load('E1.png')
E2 = pygame.image.load('E2.png')
E3 = pygame.image.load('E3.png')
E4 = pygame.image.load('E4.png')
E5 = pygame.image.load('E5.png')
E6 = pygame.image.load('E6.png')
E7 = pygame.image.load('E7.png')
E8 = pygame.image.load('E8.png')
# an array where the images are stored (use in a for loop later)
emoji = [E1, E2, E3, E4, E5, E6, E7, E8]
# setEmoji takes an index from the emoji
setEmoji = [1]


# FUNCTIONS -----------------------------------------------------------------------------------------------------

# Used to print a sidebar on the right to display the creators' (Preston and Patrick) previous drawings
def hallOfFame():
    # prints a blue rectangle to lay everything on top of
    pygame.draw.rect(win, (175,238,238), (1000, 0, 200, 800))
    # Creates font
    font = pygame.font.SysFont("Quicksand", 30)
    # Will print "HALL OF FAME"
    hallWord = font.render("HALL OF FAME", True, (0, 0, 0))
    # Coordinates at very top of blue rectangle
    win.blit(hallWord, (1025, 170))

    # Searches for the png files in  of the drawings in the hall of fame
    h1 = pygame.image.load('sh1.png')
    h2 = pygame.image.load('sh2.png')
    h3 = pygame.image.load('sh3.png')
    h4 = pygame.image.load('sh4.png')
    # Prints the images 15 units apart each other
    win.blit(h1, (1005, 200))
    win.blit(h2, (1005, 320))
    win.blit(h3, (1005, 435))
    win.blit(h4, (1005, 550))

# function to make background white only in dimensions of drawing screen (not entire screen) No redraw function needed
def clear(win):
    # the dimensions of the drawing application is 1000 by 650
    pygame.draw.rect(win, (255, 255, 255), (0, 150, 1000, 650))

# function used to fill drawing screen (in colour chosen in colour palette)
def fill(win, col):
    pygame.draw.rect(win, col, (0, 150, 1000, 650))

# function used to draw a circle on where the mouse is pressed. Thic is the radius of circle
def drawing(mouseposX, mouseposY, col, thick):
    pygame.draw.circle(win, col, (mouseposX, mouseposY), thick, 0)

while True:
    # everything must be in the for loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # delay must be
        pygame.time.delay(0)

        # finds the position of the mouse and stores in these variables
        mouseposX, mouseposY = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pos()

# Shape variables -----------------------------------------------------------------------------------------------
        # coordinates for shapes that are drawn when shape button is selected. Prints where mouse is located
        starshape = [(mouseposX + 25, mouseposY - 15), (mouseposX + 65, mouseposY - 145),
                     (mouseposX + 100, mouseposY - 15), (mouseposX + 230, mouseposY - 15),
                     (mouseposX + 115, mouseposY + 65), (mouseposX + 165, mouseposY + 185),
                     (mouseposX + 65, mouseposY + 95), (mouseposX - 40, mouseposY + 185),
                     (mouseposX + 10, mouseposY + 50), (mouseposX - 110, mouseposY - 15)]
        triangle = [(mouseposX, mouseposY - 50), (mouseposX + 50, mouseposY + 50), (mouseposX - 50, mouseposY + 50),
                    (mouseposX, mouseposY - 50)]
        pentagon = [(mouseposX, mouseposY - 50), (mouseposX + 50, mouseposY), (mouseposX + 25, mouseposY + 50),
                    (mouseposX - 25, mouseposY + 50), (mouseposX - 50, mouseposY), (mouseposX, mouseposY - 50)]

# DRAWING TOOLBAR AND HALL OF FAME --------------------------------------------------------------------------------
        hallOfFame()
        # the hall of fame is just the creator's drawing that they want to share with user. Inspires them to draw.

        # toolbar dimensions are 1200 by 150
        # We have to redraw the toolbar everytime since the drawing might overlap if the thickness is maxed out
        pygame.draw.rect(win, (255, 147, 100), (0, 0, 1200, 150))

# COLOUR PALETTE ----------------------------------------------------------------------------------------------------

        # displays the colours in squares
        # there are 15 colours in total. Print them in 3 rows, 5 colours in each row
        for i in range(5):
            # row 1 of colour palette
            pygame.draw.rect(win, colours[i], (15 + 40 * i, 15, 40, 40))
            # row 2 of colour palette
            pygame.draw.rect(win, colours[i + 5], (15 + 40 * i, 55, 40, 40))
            # row 3 of colour palette
            pygame.draw.rect(win, colours[i + 10], (15 + 40 * i, 95, 40, 40))
            # if mouse is in a location 40*i indicates with the its index in colours[i]
            # if statement for detecting mouse pressed for row 1
            if 15 + 40 * i <= mouseposX <= 55 + 40 * i and 15 <= mouseposY <= 55 and pygame.mouse.get_pressed()[0]:
                col = colours[i]
            # elif statement for detecting mouse pressed for row 2
            elif 15 + 40 * i <= mouseposX <= 55 + 40 * i and 55 <= mouseposY <= 95 and pygame.mouse.get_pressed()[0]:
                col = colours[i + 5]
            # elif statement for detecting mouse pressed for row 3
            elif 15 + 40 * i <= mouseposX <= 55 + 40 * i and 95 <= mouseposY <= 135 and pygame.mouse.get_pressed()[0]:
                col = colours[i + 10]

# FILL AND CLEAR BUTTON ----------------------------------------------------------------------------------------------

        # fill button
        # draws rectangle for fill button
        pygame.draw.rect(win, (250, 250, 250), (230, 15, 75, 50))
        # prints "FILL" over the button (centred)
        font = pygame.font.SysFont("Quicksand", 30)
        fillWord = font.render("FILL", True, (0, 0, 90))
        win.blit(fillWord, (247.5, 30))
        # determines if button is clicked. (turns yellow when hovered over)
        if 230 <= mouseposX <= 305 and 15 <= mouseposY <= 65:
            pygame.draw.rect(win, (250, 250, 50), (230, 15, 75, 50), 10)
            if pygame.mouse.get_pressed()[0]:
                fill(win, col)

        # clear button
        # draws a rectangle that is the button for clear
        pygame.draw.rect(win, (255, 255, 255), (230, 85, 75, 50))
        # prints "CLEAR" over the button (in the centre of button)
        font2 = pygame.font.SysFont("Quicksand", 27)
        fillWord = font2.render("CLEAR", True, (0, 0, 90))
        win.blit(fillWord, (235, 100))
        # determines if button is clicked. (turns yellow when hovered over)
        if 230 <= mouseposX <= 305 and 85 <= mouseposY <= 135:
            pygame.draw.rect(win, (250, 250, 50), (230, 85, 75, 50), 10)
            if pygame.mouse.get_pressed()[0]:
                clear(win)

        # current colour
        Arialfont = pygame.font.SysFont("Arial", 20, bold=True)
        Currentcolor = Arialfont.render("Current color:", True, white)
        win.blit(Currentcolor, (330, 18))
        # draws a rectangle and its colour shows the colour selected
        pygame.draw.rect(win, col, (450, 15, 110, 30))
        # prints a border around current colour to make it look nicer
        pygame.draw.rect(win, black, (450, 15, 110, 30), 2)

# THICKNESS BUTTONS ------------------------------------------------------------------------------------------------

        # prints "Thickness" above the thickness boxes
        thickWord = Arialfont.render("Thickness: ", True, white)
        win.blit(thickWord, (330, 50))
        for i in range(5):
            # draws the thickness boxes
            pygame.draw.rect(win, (250, 160, 120), (330 + i * 50, 85, 40, 50))
            # draws the thicknesses on each box so the user can choose their desired thickness (the circle radius)
            pygame.draw.circle(win, (0, 0, 0), (330 + i * 50 + 20, 85 + 25), displayThic[i])
            # if the cursor is in dimension of thickness box and clicks thickness will change depending on box number
            if 330 + i * 50 < mouseposX <= 370 + i * 50 and 85 <= mouseposY <= 135 and pygame.mouse.get_pressed()[0]:
                thick = thickArray[i]
            # this gives an outline to the thickness box selected. Stays outlined until another thickness is selected
            if thick == thickArray[i]:
                pygame.draw.rect(win, (250, 250, 50), (330 + i * 50, 85, 40, 50), 5)

# SHAPE BUTTONS -----------------------------------------------------------------------------------------------------

        # creates the shape buttons through a for loop
        # there are 8 boxes (4 columns, 2 rows), so for loop runs 4 times to print each row and then duplicate row
        # row 1
        for i in range(4):
            pygame.draw.rect(win, white, (590 + i * 75, 15, 60, 50))
            if 590 <= mouseposX <= 650 and 15 <= mouseposY <= 65 and pygame.mouse.get_pressed()[0]:
                shape = "circle"
            if 665 <= mouseposX <= 725 and 15 <= mouseposY <= 65 and pygame.mouse.get_pressed()[0]:
                shape = "square"
            if 760 <= mouseposX <= 800 and 15 <= mouseposY <= 65 and pygame.mouse.get_pressed()[0]:
                shape = "rectangle"
            if 815 <= mouseposX <= 875 and 15 <= mouseposY <= 65 and pygame.mouse.get_pressed()[0]:
                shape = "ellipse"
            if 590 + i * 75 <= mouseposX <= 650 + i * 75 and 15 <= mouseposY <= 65:
                pygame.draw.rect(win, (250, 250, 50), (590 + i * 75, 15, 60, 50), 5)
            # row 2
            pygame.draw.rect(win, white, (590 + i * 75, 80, 60, 50))
            if 590 <= mouseposX <= 650 and 75 <= mouseposY <= 125 and pygame.mouse.get_pressed()[0]:
                shape = "triangle"
            if 665 <= mouseposX <= 725 and 75 <= mouseposY <= 125 and pygame.mouse.get_pressed()[0]:
                shape = "pentagon"
            if 760 <= mouseposX <= 800 and 75 <= mouseposY <= 125 and pygame.mouse.get_pressed()[0]:
                shape = "hexagon"
            if 815 <= mouseposX <= 875 and 75 <= mouseposY <= 125 and pygame.mouse.get_pressed()[0]:
                shape = "star"
            if 590 + i * 75 <= mouseposX <= 650 + i * 75 and 80 <= mouseposY <= 125:
                pygame.draw.rect(win, (250, 250, 50), (590 + i * 75, 80, 60, 50), 5)

            # labelling each button with its shape
            # draws the circle, square, rectangle, and ellipse on the tool bar on top of each button
            pygame.draw.circle(win, black, (620, 40), 20, 5)
            pygame.draw.rect(win, black, (680, 25, 30, 30), 5)
            pygame.draw.rect(win, black, (750, 25, 45, 30), 5)
            pygame.draw.ellipse(win, black, (820, 25, 45, 30), 5)
            # draws the triangle, hexagon, pentagon, and star on tool bar on top of buttons
            # they are smaller than actual drawing shapes
            pygame.draw.polygon(win, black, triangleTool, 5)
            pygame.draw.polygon(win, black, hexagonTool, 5)
            pygame.draw.polygon(win, black, pentagonTool, 5)
            pygame.draw.polygon(win, black, starTool, 0)

# PLUS AND MINUS BUTTONS FOR SHAPES -------------------------------------------------------------------------------
        # in a loop that runs 2 times because there are 2 of the same button (just duplicate them with a loop)
        for i in range(2):
            # draws the buttons for increasing length and width of shape
            pygame.draw.rect(win, (250, 160, 120), (920, 15 + i * 45, 30, 30))
            pygame.draw.rect(win, black, (920, 15 + i * 45, 30, 30), 1)
            # print the plus image on the button
            plusPic = pygame.image.load('plus.png')
            win.blit(plusPic, (923, 18+i*45))

            # draws the buttons for decreasing length of shape
            pygame.draw.rect(win, (250, 160, 120), (890, 15 + i * 45, 30, 30))
            pygame.draw.rect(win, black, (890, 15 + i * 45, 30, 30), 1)
            # prints the minus image on the button
            minusPic = pygame.image.load('minus.png')
            win.blit(minusPic, (893, 18+i*45))


        # the if statements for the decreasing the length and width of shapes
        # if you hover over boxes, they will light up in a yellow outline
        if 890 <= mouseposX < 920 and 15 <= mouseposY <= 45:
            pygame.draw.rect(win, (250, 250, 50), (890, 15, 30, 30), 2)
            if pygame.mouse.get_pressed()[0]:
                length -= 5
        elif 890 <= mouseposX < 920 and 60 <= mouseposY <= 90:
            pygame.draw.rect(win, (250, 250, 50), (890, 60, 30, 30), 2)
            if pygame.mouse.get_pressed()[0]:
                width -= 5

        # the if statements for the increasing the length and width of shapes
        # if you hover over boxes, they will light up in a yellow outline
        if 920 <= mouseposX <= 950 and 15 <= mouseposY <= 45:
            pygame.draw.rect(win, (250, 250, 50), (920, 15, 30, 30), 2)
            if pygame.mouse.get_pressed()[0]:
                length += 5
        elif 920 <= mouseposX <= 950 and 60 <= mouseposY <= 90:
            pygame.draw.rect(win, (250, 250, 50), (920, 60, 30, 30), 2)
            if pygame.mouse.get_pressed()[0]:
                width += 5

        # prints "length" and "width" above the increase and decrease boxes
        ArialSmallFont = pygame.font.SysFont("Arial", 9, bold=True)
        lName = ArialSmallFont.render("Length:", True, black)
        wName = ArialSmallFont.render("Width:", True, black)
        win.blit(lName, (910, 1))
        win.blit(wName, (910, 45))

# DRAWING EMOJI -----------------------------------------------------------------------------------------------------

        # emoji boxes
        for i in range(4):
            # row 1
            pygame.draw.circle(win, (250, 160, 120), (985 + 60 * i, 40), 28)
            # row 2
            pygame.draw.circle(win, (250, 160, 120), (985 + 60 * i, 40 + 60), 28)
            # basically if certain emoji is selected, its box will light up in a yellow outline.
            # outline if statement for row 1
            if setEmoji == emoji[i]:
                pygame.draw.circle(win, (250, 250, 50), (985 + 60 * i, 40), 28, 2)
            # outline if statement for row 2
            elif setEmoji == emoji[i+4]:
                pygame.draw.circle(win, (250, 250, 50), (985 + 60 * i, 100), 28, 2)

        # displays the 'emojis' on the toolbar
        # emojis row 1
        imageT1 = pygame.image.load('CimageT1.png')
        win.blit(imageT1, (965, 20))
        imageT2 = pygame.image.load('CimageT2.png')
        win.blit(imageT2, (960 + 60, 16))
        imageT3 = pygame.image.load('CimageT3.png')
        win.blit(imageT3, (962 + 120, 20))
        imageT4 = pygame.image.load('CimageT4.png')
        win.blit(imageT4, (962 + 180, 16))
        # emojis row 2
        imageT5 = pygame.image.load('CimageT5.png')
        win.blit(imageT5, (960, 75))
        imageT6 = pygame.image.load('CimageT6.png')
        win.blit(imageT6, (965 + 60, 80))
        imageT7 = pygame.image.load('CimageT7.png')
        win.blit(imageT7, (962 + 120, 85))
        imageT8 = pygame.image.load('CimageT8.png')
        win.blit(imageT8, (962 + 180, 85))

        # If mouse hovers over specific coordinates of the button AND mouse is clicked, shape will be set to that emoji
        # Shape = "E" means that you are using printing an emoji
        # When you draw on the drawing screen, you will print that emoji that you chose
        # detecting emoji button pressed row 1
        if 985-28 <= mouseposX <= 985+28 and 40-28 <= mouseposY <= 40+28 and pygame.mouse.get_pressed()[0]:
            shape = "E"
            setEmoji = emoji[0]
        elif 985-28+60 <= mouseposX <= 985+28+60 and 40-28 <= mouseposY <= 40+28 and pygame.mouse.get_pressed()[0]:
            shape = "E"
            setEmoji = emoji[1]
        elif 985-28+120 <= mouseposX <= 985+28+120 and 40-28 <= mouseposY <= 40+28 and pygame.mouse.get_pressed()[0]:
            shape = "E"
            setEmoji = emoji[2]
        elif 985-28+180 <= mouseposX <= 985+28+180 and 40-28 <= mouseposY <= 40+28 and pygame.mouse.get_pressed()[0]:
            shape = "E"
            setEmoji = emoji[3]
        # detecting emoji button pressed row 2
        elif 985-28 <= mouseposX <= 985+28 and 100-28 <= mouseposY <= 100+28 and pygame.mouse.get_pressed()[0]:
            shape = "E"
            setEmoji = emoji[4]
        elif 985-28+60 <= mouseposX <= 985+28+60 and 100-28 <= mouseposY <= 100+28 and pygame.mouse.get_pressed()[0]:
            shape = "E"
            setEmoji = emoji[5]
        elif 985-28+120 <= mouseposX <= 985+28+120 and 100-28 <= mouseposY <= 100+28 and pygame.mouse.get_pressed()[0]:
            shape = "E"
            setEmoji = emoji[6]
        elif 985-28+180 <= mouseposX <= 985+28+180 and 100-28 <= mouseposY <= 100+28 and pygame.mouse.get_pressed()[0]:
            shape = "E"
            setEmoji = emoji[7]

# DRAWING ON THE DRAWING SCREEN ---------------------------------------------------------------------------------------

        # this actually draws lines (press left mouse button)
        # When you left click mouse in dimensions of drawing area, draws the selected shape
        # the shape is printed where the mouse's x and y coordinates are (represented as mouseposX and mouseposY)
        # regular drawing shape (circle)
        if (pygame.mouse.get_pressed()[0] and mouseposX < 1000 and mouseposY > 150 and shape == "circle"):
            pygame.draw.circle(win, col, (mouseposX, mouseposY), thick, 0)
        # Square
        elif (pygame.mouse.get_pressed()[0] and mouseposX < 1000 and mouseposY > 150 and shape == "square"):
            pygame.draw.rect(win, col, ((mouseposX - length / 2), (mouseposY - width / 2), length, length))
        # Rectangle
        elif (pygame.mouse.get_pressed()[0] and mouseposX < 1000 and mouseposY > 150 and shape == "rectangle"):
            pygame.draw.rect(win, col, ((mouseposX - length / 2), (mouseposY - width / 2), length + 20, width))
        # Ellipse
        elif (pygame.mouse.get_pressed()[0] and mouseposX < 1000 and mouseposY > 150 and shape == "ellipse"):
            pygame.draw.ellipse(win, col, ((mouseposX - length / 2), (mouseposY - width / 2), length + 20, width))
        # Hexagon
        elif (pygame.mouse.get_pressed()[0] and mouseposX < 1000 and mouseposY > 150 and shape == "hexagon"):
            pygame.draw.polygon(win, col, (
                (mouseposX - 40, mouseposY), (mouseposX - 20, mouseposY - 35), (mouseposX + 20, mouseposY - 35),
                (mouseposX + 40, mouseposY), (mouseposX + 20, mouseposY + 35), (mouseposX - 20, mouseposY + 35)))
        # triangle
        elif (pygame.mouse.get_pressed()[0] and mouseposX < 1000 and mouseposY > 150 and shape == "triangle"):
            pygame.draw.polygon(win, col, triangle)
        # star
        elif (pygame.mouse.get_pressed()[0] and mouseposX < 1000 and mouseposY > 150 and shape == "star"):
            pygame.draw.polygon(win, col, starshape)
        elif (pygame.mouse.get_pressed()[0] and mouseposX < 1000 and mouseposY > 150 and shape == "pentagon"):
            pygame.draw.polygon(win, col, pentagon)
        # Prints the type of emoji stored in setEmoji (When user clicks)
        # setEmoji is an array and the index selected depends on which emoji button you press
        elif pygame.mouse.get_pressed()[0] and mouseposX < 1000 and mouseposY > 150 and shape == "E":
            win.blit(setEmoji, (mouseposX - 25, mouseposY - 25))

# MUSIC ----------------------------------------------------------------------------------------------------
        # drawins the 2 buttons for the 2 different types of music. Located in bottom right corner
        for i in range(2):
            pygame.draw.rect(win, white, (1010, 655 + i * 40, 30, 30), 5)
        # if statements if top button is pressed
        if 1010 <= mouseposX <= 1070 and 655 <= mouseposY <= 685 and pygame.mouse.get_pressed()[0]:
            # loads and plays song 1
            pygame.mixer.music.load('Fnf.wav')
            pygame.mixer.music.set_volume(0.08)
            pygame.mixer.music.play(-1)
        if 1010 <= mouseposX <= 1070 and 695 <= mouseposY <= 725 and pygame.mouse.get_pressed()[0]:
            # loads then plays song 2
            pygame.mixer.music.load('Animal.wav')
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)
        # If you pressed p on your keyboard, you will stop the music
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            pygame.mixer.music.pause()
        # instructions for music
        Music = Arialfont.render("Click to play music", True, white)
        Pause = Arialfont.render("Press P to pause", True, white)
        # differentiates the songs from one another with images
        Ruv = pygame.image.load("Ruv_stand.png")
        Isabelle = pygame.image.load("Isabelle.png")
        # Actually prints the text and images
        win.blit(Music, (1010, 740))
        win.blit(Pause, (1010, 760))
        win.blit(Ruv, (900, 435))
        win.blit(Isabelle, (680, 450))


    # updates the frames of the game
    pygame.display.update()
