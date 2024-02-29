# Anna Winter (acw8sg) and Eric Pilati (ep9ca)

#######################################
#   CS 1110 Final Project
#######################################

#This project was created in the Fall semester of 2017 at the University of Virginia

#######################################
#   Purpose of Project
#######################################

#The code uses a program called Gamebox that allows the programmer to create a game through the use of walls, physics, controls, timing, and saved files.

#This game gave the player different mazes, each progressively more difficult, in which they needed to gather all the coins around the level before returning to the treasure
#chest at the center. This advanced them to the next level.

#The code kept track of the player's time and even recorded the fastest time.

import pygame
import gamebox

camera = gamebox.Camera(500, 500)
background = gamebox.from_image(250, 250, "background.jpg")

# Start Screen
startscreen = [
    gamebox.from_text(250, 100, "Dungeon", "Arial", 80, "red", bold = True),
    gamebox.from_text(250, 200, "Explorer", "Arial", 80, "red", bold = True),
    gamebox.from_text(250, 430, "Press Spacebar to Start", "Arial", 40, "white"),
    gamebox.from_text(250, 480, "Anna Winter (acw8sg) and Eric Pilati (ep9ca)", "Arial", 20, "white"),
    gamebox.from_text(250, 290, "Use arrows to move character", "Arial", 20, "yellow", bold = True),
    gamebox.from_text(250, 335, "Collect all coins as fast as you can", "Arial", 20, "yellow"),
    gamebox.from_text(250, 360, "and then go to the chest to advance", "Arial", 20, "yellow"),
]
explorer = gamebox.load_sprite_sheet("explorer_sprites.png", 4, 4)
character = gamebox.from_color(250, 250, "red", 20, 20)
print(explorer)
treasure = gamebox.load_sprite_sheet("treasure.png", 1, 1)
startingpoint = gamebox.from_color(250, 250, "light blue", 40, 40)


# Close Screen
closescreen = [
    gamebox.from_text(250, 125, "Congrats!", "Arial", 80, "white", bold = True),
    gamebox.from_text(250, 250, "You completed the game in", "Arial", 40, "red"),
    gamebox.from_text(250, 360, "seconds", "Arial", 40, "red"),
    gamebox.from_text(250, 470, "Press ESCAPE to exit", "Arial", 30, "light blue")
]

# Maze 1
maze1vertical = [
    gamebox.from_color(3.75, 250, "white", 7.5, 500),
    gamebox.from_color(496.25, 250, "white", 7.5, 500),
    gamebox.from_color(47.5, 92.5, "white", 10, 100),
    gamebox.from_color(47.5, 272.5, "white", 10, 100),
    gamebox.from_color(92.5, 30, "white", 10, 45),
    gamebox.from_color(92.5, 182.5, "white", 10, 100),
    gamebox.from_color(92.5, 340, "white", 10, 145),
    gamebox.from_color(137.5, 70, "white", 10, 55),
    gamebox.from_color(137.5, 317.5, "white", 10, 190),
    gamebox.from_color(137.5, 470, "white", 10, 45),
    gamebox.from_color(182.5, 30, "white", 10, 45),
    gamebox.from_color(182.5, 227.5, "white", 10, 100),
    gamebox.from_color(182.5, 340, "white", 10, 55),
    gamebox.from_color(182.5, 430, "white", 10, 55),
    gamebox.from_color(227.5, 70, "white", 10, 55),
    gamebox.from_color(227.5, 385, "white", 10, 55),
    gamebox.from_color(227.5, 470, "white", 10, 45),
    gamebox.from_color(272.5, 30, "white", 10, 45),
    gamebox.from_color(272.5, 385, "white", 10, 145),
    gamebox.from_color(317.5, 137.5, "white", 10, 190),
    gamebox.from_color(317.5, 295, "white", 10, 55),
    gamebox.from_color(362.5, 115, "white", 10, 55),
    gamebox.from_color(362.5, 250, "white", 10, 55),
    gamebox.from_color(362.5, 340, "white", 10, 55),
    gamebox.from_color(362.5, 470, "white", 10, 45),
    gamebox.from_color(407.5, 52.5, "white", 10, 90),
    gamebox.from_color(407.5, 205, "white", 10, 55),
    gamebox.from_color(407.5, 317.5, "white", 10, 100),
    gamebox.from_color(407.5, 430, "white", 10, 55),
    gamebox.from_color(452.5, 205, "white", 10, 145),
    gamebox.from_color(452.5, 407.5, "white", 10, 100)
]
maze1horizontal = [
    gamebox.from_color(250, 3.75, "white", 500, 7.5),
    gamebox.from_color(250, 496.25, "white", 500, 7.5),
    gamebox.from_color(160, 47.5, "white", 55, 10),
    gamebox.from_color(340, 47.5, "white", 55, 10),
    gamebox.from_color(430, 47.5, "white", 55, 10),
    gamebox.from_color(92.5, 92.5,"white", 100, 10),
    gamebox.from_color(250, 92.5, "white", 145, 10),
    gamebox.from_color(470, 92.5, "white", 45, 10),
    gamebox.from_color(182.5, 137.5, "white", 190, 10),
    gamebox.from_color(407.5, 137.5, "white", 100, 10),
    gamebox.from_color(52.5, 182.5, "white", 90, 10),
    gamebox.from_color(182.5, 182.5, "white", 100, 10),
    gamebox.from_color(340, 182.5, "white", 145, 10),
    gamebox.from_color(470, 182.5, "white", 45, 10),
    gamebox.from_color(115, 227.5, "white", 55, 10),
    gamebox.from_color(340, 227.5, "white", 55, 10),
    gamebox.from_color(407.5, 272.5, "white", 100, 10),
    gamebox.from_color(30, 317.5, "white", 45, 10),
    gamebox.from_color(272.5, 317.5, "white", 190, 10),
    gamebox.from_color(470, 317.5, "white", 45, 10),
    gamebox.from_color(70, 362.5, "white", 55, 10),
    gamebox.from_color(340, 362.5, "white", 55, 10),
    gamebox.from_color(430, 362.5, "white", 55, 10),
    gamebox.from_color(30, 407.5, "white", 45, 10),
    gamebox.from_color(160, 407.5, "white", 145, 10),
    gamebox.from_color(340, 407.5, "white", 145, 10),
    gamebox.from_color(92.5, 452.5, "white", 100, 10),
    gamebox.from_color(250, 452.5, "white", 55, 10),
    gamebox.from_color(340, 452.5, "white", 55, 10)
]
coins1 = [
    gamebox.from_color(430, 25, "yellow", 12, 12),
    gamebox.from_color(25, 295, "yellow", 12, 12),
    gamebox.from_color(340, 340, "yellow", 12, 12)
]
maze1 = [maze1horizontal, maze1vertical]

# Maze 2
maze2vertical = [
    gamebox.from_color(7.5, 250, "white", 15, 500),
    gamebox.from_color(492.5, 250, "white", 15, 500),
    gamebox.from_color(50, 130, "white", 10, 170),
    gamebox.from_color(90, 310, "white", 10, 290),
    gamebox.from_color(130, 170, "white", 10, 90),
    gamebox.from_color(130, 310, "white", 10, 50),
    gamebox.from_color(170, 55, "white", 10, 80),
    gamebox.from_color(170, 210, "white", 10, 90),
    gamebox.from_color(170, 390, "white", 10, 50),
    gamebox.from_color(210, 70, "white", 10, 50),
    gamebox.from_color(210, 310, "white", 10, 130),
    gamebox.from_color(210, 445, "white", 10, 80),
    gamebox.from_color(250, 35, "white", 10, 40),
    gamebox.from_color(250, 170, "white", 10, 90),
    gamebox.from_color(250, 410, "white", 10, 90),
    gamebox.from_color(290, 230, "white", 10, 50),
    gamebox.from_color(290, 430, "white", 10, 50),
    gamebox.from_color(330, 55, "white", 10, 80),
    gamebox.from_color(330, 230, "white", 10, 130),
    gamebox.from_color(330, 370, "white", 10, 90),
    gamebox.from_color(370, 130, "white", 10, 170),
    gamebox.from_color(370, 465, "white", 10, 40),
    gamebox.from_color(410, 250, "white", 10, 170),
    gamebox.from_color(410, 430, "white", 10, 50),
    gamebox.from_color(450, 110, "white", 10, 50),
    gamebox.from_color(450, 370, "white", 10, 170)
]
maze2horizontal = [
    gamebox.from_color(250, 7.5, "white", 500, 15),
    gamebox.from_color(250, 492.5, "white", 500, 15),
    gamebox.from_color(90, 50, "white", 90, 10),
    gamebox.from_color(270, 50, "white", 50, 10),
    gamebox.from_color(445, 50, "white", 80, 10),
    gamebox.from_color(130, 90, "white", 90, 10),
    gamebox.from_color(270, 90, "white", 130, 10),
    gamebox.from_color(390, 90, "white", 50, 10),
    gamebox.from_color(90, 130, "white", 90, 10),
    gamebox.from_color(270, 130, "white", 210, 10),
    gamebox.from_color(445, 130, "white", 80, 10),
    gamebox.from_color(190, 170, "white", 50, 10),
    gamebox.from_color(310, 170, "white", 50, 10),
    gamebox.from_color(430, 170, "white", 50, 10),
    gamebox.from_color(35, 210, "white", 40, 10),
    gamebox.from_color(250, 210, "white", 90, 10),
    gamebox.from_color(465, 210, "white", 40, 10),
    gamebox.from_color(110, 250, "white", 130, 10),
    gamebox.from_color(410, 250, "white", 90, 10),
    gamebox.from_color(35, 290, "white", 40, 10),
    gamebox.from_color(250, 290, "white", 250, 10),
    gamebox.from_color(465, 290, "white", 40, 10),
    gamebox.from_color(70, 330, "white", 50, 10),
    gamebox.from_color(150, 330, "white", 50, 10),
    gamebox.from_color(330, 330, "white", 170, 10),
    gamebox.from_color(75, 370, "white", 120, 10),
    gamebox.from_color(250, 370, "white", 90, 10),
    gamebox.from_color(410, 370, "white", 90, 10),
    gamebox.from_color(35, 410, "white", 40, 10),
    gamebox.from_color(110, 450, "white", 130, 10),
    gamebox.from_color(330, 450, "white", 90, 10),
    gamebox.from_color(170, 410, "white", 90, 10),
    gamebox.from_color(370, 410, "white", 90, 10)
]
coins2 = [
    gamebox.from_color(310, 70, "yellow", 12, 12),
    gamebox.from_color(470, 390, "yellow", 12, 12),
    gamebox.from_color(30, 310, "yellow", 12, 12)
]
maze2 = [maze2horizontal, maze2vertical]

# Maze 3
maze3vertical = [
    gamebox.from_color(5, 250, "white", 10, 500),
    gamebox.from_color(495, 250, "white", 10, 500),
    gamebox.from_color(250, 5, "white", 500, 10),
    gamebox.from_color(250, 495, "white", 500, 10),
    gamebox.from_color(40, 232.5, "white", 10, 45),
    gamebox.from_color(40, 425, "white", 10, 80),
    gamebox.from_color(75, 62.5, "white", 10, 115),
    gamebox.from_color(110, 162.5, "white", 10, 255),
    gamebox.from_color(110, 407.5, "white", 10, 115),
    gamebox.from_color(145, 62.5, "white", 10, 105),
    gamebox.from_color(145, 215, "white", 10, 80),
    gamebox.from_color(145, 425, "white", 10, 80),
    gamebox.from_color(180, 57.5, "white", 10, 45),
    gamebox.from_color(180, 197.5, "white", 10, 45),
    gamebox.from_color(180, 390, "white", 10, 80),
    gamebox.from_color(215, 92.5, "white", 10, 45),
    gamebox.from_color(215, 232.5, "white", 10, 45),
    gamebox.from_color(215, 302.5, "white", 10, 45),
    gamebox.from_color(250, 92.5, "white", 10, 115),
    gamebox.from_color(250, 472.5, "white", 10, 35),
    gamebox.from_color(285, 62.5, "white", 10, 105),
    gamebox.from_color(285, 162.5, "white", 10, 45),
    gamebox.from_color(285, 250, "white", 10, 80),
    gamebox.from_color(285, 407.5, "white", 10, 115),
    gamebox.from_color(320, 57.5, "white", 10, 45),
    gamebox.from_color(320, 127.5, "white", 10, 45),
    gamebox.from_color(320, 215, "white", 10, 80),
    gamebox.from_color(320, 302.5, "white", 10, 45),
    gamebox.from_color(320, 407.5, "white", 10, 45),
    gamebox.from_color(355, 27.5, "white", 10, 35),
    gamebox.from_color(355, 127.5, "white", 10, 115),
    gamebox.from_color(355, 232.5, "white", 10, 45),
    gamebox.from_color(355, 337.5, "white", 10, 45),
    gamebox.from_color(355, 442.5, "white", 10, 45),
    gamebox.from_color(390, 75, "white", 10, 80),
    gamebox.from_color(390, 285, "white", 10, 80),
    gamebox.from_color(390, 437.5, "white", 10, 105),
    gamebox.from_color(425, 92.5, "white", 10, 45),
    gamebox.from_color(425, 372.5, "white", 10, 115),
    gamebox.from_color(460, 57.5, "white", 10, 45),
    gamebox.from_color(460, 180, "white", 10, 80),
    gamebox.from_color(460, 337.5, "white", 10, 115)
]
maze3horizontal = [
    gamebox.from_color(27.5, 40, "white", 35, 10),
    gamebox.from_color(215, 40, "white", 80, 10),
    gamebox.from_color(425, 40, "white", 80, 10),
    gamebox.from_color(57.5, 75, "white", 45, 10),
    gamebox.from_color(337.5, 75, "white", 45, 10),
    gamebox.from_color(27.5, 110, "white", 35, 10),
    gamebox.from_color(180, 110, "white", 80, 10),
    gamebox.from_color(302.5, 110, "white", 45, 10),
    gamebox.from_color(437.5, 110, "white", 105, 10),
    gamebox.from_color(92.5, 145, "white", 115, 10),
    gamebox.from_color(215, 145, "white", 80, 10),
    gamebox.from_color(425, 145, "white", 80, 10),
    gamebox.from_color(45, 180, "white", 70, 10),
    gamebox.from_color(162.5, 180, "white", 45, 10),
    gamebox.from_color(320, 180, "white", 220, 10),
    gamebox.from_color(75, 215, "white", 80, 10),
    gamebox.from_color(232.5, 215, "white", 45, 10),
    gamebox.from_color(407.5, 215, "white", 115, 10),
    gamebox.from_color(57.5, 250, "white", 45, 10),
    gamebox.from_color(180, 250, "white", 80, 10),
    gamebox.from_color(337.5, 250, "white", 45, 10),
    gamebox.from_color(455, 250, "white", 70, 10),
    gamebox.from_color(62.5, 285, "white", 105, 10),
    gamebox.from_color(180, 285, "white", 80, 10),
    gamebox.from_color(267.5, 285, "white", 45, 10),
    gamebox.from_color(390, 285, "white", 150, 10),
    gamebox.from_color(180, 320, "white", 290, 10),
    gamebox.from_color(80, 355, "white", 140, 10),
    gamebox.from_color(302.5, 355, "white", 255, 10),
    gamebox.from_color(57.5, 390, "white", 45, 10),
    gamebox.from_color(250, 390, "white", 80, 10),
    gamebox.from_color(355, 390, "white", 80, 10),
    gamebox.from_color(92.5, 425, "white", 45, 10),
    gamebox.from_color(215, 425, "white", 70, 10),
    gamebox.from_color(455, 425, "white", 70, 10),
    gamebox.from_color(45, 460, "white", 70, 10),
    gamebox.from_color(197.5, 460, "white", 115, 10),
    gamebox.from_color(320, 460, "white", 80, 10),
    gamebox.from_color(425, 460, "white", 80, 10)
]
coins3 = [
    gamebox.from_color(22.5, 92.5, "yellow", 12, 12),
    gamebox.from_color(407.5, 57.5, "yellow", 12, 12),
    gamebox.from_color(57.5, 372.5, "yellow", 12, 12)
]
maze3 = [maze3horizontal, maze3vertical]

# Maze 4
maze4vertical = [
    gamebox.from_color(250, 7.5, "white", 500, 15),
    gamebox.from_color(250, 492.5, "white", 500, 15),
    gamebox.from_color(7.5, 250, "white", 15, 500),
    gamebox.from_color(492.5, 250, "white", 15, 500),
    gamebox.from_color(40, 90, "white", 10, 150),
    gamebox.from_color(40, 205, "white", 10, 40),
    gamebox.from_color(40, 280, "white", 10, 70),
    gamebox.from_color(40, 370, "white", 10, 70),
    gamebox.from_color(70, 85, "white", 10, 85),
    gamebox.from_color(70, 175, "white", 10, 40),
    gamebox.from_color(70, 265, "white", 10, 40),
    gamebox.from_color(70, 325, "white", 10, 40),
    gamebox.from_color(70, 400, "white", 10, 70),
    gamebox.from_color(100, 130, "white", 10, 70),
    gamebox.from_color(100, 220, "white", 10, 70),
    gamebox.from_color(100, 355, "white", 10, 40),
    gamebox.from_color(100, 430, "white", 10, 70),
    gamebox.from_color(130, 100, "white", 10, 70),
    gamebox.from_color(130, 190, "white", 10, 70),
    gamebox.from_color(130, 310, "white", 10, 70),
    gamebox.from_color(130, 400, "white", 10, 70),
    gamebox.from_color(160, 55, "white", 10, 40),
    gamebox.from_color(160, 130, "white", 10, 70),
    gamebox.from_color(160, 265, "white", 10, 100),
    gamebox.from_color(160, 370, "white", 10, 70),
    gamebox.from_color(190, 55, "white", 10, 40),
    gamebox.from_color(190, 145, "white", 10, 40),
    gamebox.from_color(190, 205, "white", 10, 40),
    gamebox.from_color(190, 280, "white", 10, 70),
    gamebox.from_color(190, 415, "white", 10, 40),
    gamebox.from_color(220, 175, "white", 10, 40),
    gamebox.from_color(220, 415, "white", 10, 100),
    gamebox.from_color(250, 445, "white", 10, 40),
    gamebox.from_color(310, 70, "white", 10, 70),
    gamebox.from_color(310, 220, "white", 10, 70),
    gamebox.from_color(310, 295, "white", 10, 40),
    gamebox.from_color(310, 425, "white", 10, 120),
    gamebox.from_color(340, 60, "white", 10, 90),
    gamebox.from_color(340, 175, "white", 10, 40),
    gamebox.from_color(340, 340, "white", 10, 250),
    gamebox.from_color(370, 70, "white", 10, 70),
    gamebox.from_color(370, 145, "white", 10, 40),
    gamebox.from_color(370, 265, "white", 10, 100),
    gamebox.from_color(370, 455, "white", 10, 60),
    gamebox.from_color(400, 85, "white", 10, 40),
    gamebox.from_color(400, 250, "white", 10, 70),
    gamebox.from_color(430, 130, "white", 10, 70),
    gamebox.from_color(430, 415, "white", 10, 40),
    gamebox.from_color(460, 115, "white", 10, 100),
    gamebox.from_color(460, 280, "white", 10, 70),
    gamebox.from_color(460, 415, "white", 10, 100)
]
maze4horizontal = [
    gamebox.from_color(115, 40, "white", 100, 10),
    gamebox.from_color(250, 40, "white", 130, 10),
    gamebox.from_color(415, 40, "white", 100, 10),
    gamebox.from_color(130, 70, "white", 70, 10),
    gamebox.from_color(235, 70, "white", 100, 10),
    gamebox.from_color(430, 70, "white", 70, 10),
    gamebox.from_color(85, 100, "white", 40, 10),
    gamebox.from_color(235, 100, "white", 160, 10),
    gamebox.from_color(355, 100, "white", 40, 10),
    gamebox.from_color(220, 130, "white", 70, 10),
    gamebox.from_color(355, 130, "white", 160, 10),
    gamebox.from_color(100, 160, "white", 130, 10),
    gamebox.from_color(265, 160, "white", 100, 10),
    gamebox.from_color(415, 160, "white", 40, 10),
    gamebox.from_color(470, 160, "white", 30, 10),
    gamebox.from_color(205, 190, "white", 100, 10),
    gamebox.from_color(370, 190, "white", 190, 10),
    gamebox.from_color(60, 220, "white", 90, 10),
    gamebox.from_color(355, 220, "white", 40, 10),
    gamebox.from_color(440, 220, "white", 90, 10),
    gamebox.from_color(55, 250, "white", 40, 10),
    gamebox.from_color(130, 250, "white", 70, 10),
    gamebox.from_color(445, 250, "white", 40, 10),
    gamebox.from_color(100, 280, "white", 70, 10),
    gamebox.from_color(415, 280, "white", 40, 10),
    gamebox.from_color(85, 310, "white", 40, 10),
    gamebox.from_color(190, 310, "white", 70, 10),
    gamebox.from_color(280, 310, "white", 70, 10),
    gamebox.from_color(415, 310, "white", 100, 10),
    gamebox.from_color(45, 340, "white", 60, 10),
    gamebox.from_color(265, 340, "white", 340, 10),
    gamebox.from_color(470, 340, "white", 30, 10),
    gamebox.from_color(85, 370, "white", 40, 10),
    gamebox.from_color(250, 370, "white", 130, 10),
    gamebox.from_color(415, 370, "white", 100, 10),
    gamebox.from_color(175, 400, "white", 40, 10),
    gamebox.from_color(250, 400, "white", 70, 10),
    gamebox.from_color(370, 400, "white", 70, 10),
    gamebox.from_color(55, 430, "white", 40, 10),
    gamebox.from_color(160, 430, "white", 70, 10),
    gamebox.from_color(280, 430, "white", 70, 10),
    gamebox.from_color(400, 430, "white", 70, 10),
    gamebox.from_color(45, 460, "white", 60, 10),
    gamebox.from_color(160, 460, "white", 130, 10),
    gamebox.from_color(265, 460, "white", 40, 10),
    gamebox.from_color(430, 460, "white", 70, 10)
]
coins4 = [
    gamebox.from_color(235, 385, "yellow", 12, 12),
    gamebox.from_color(145, 55, "yellow", 12, 12),
    gamebox.from_color(475, 145, "yellow", 12, 12)
]
maze4 = [maze4horizontal, maze4vertical]

# music and sound
coin_sound = gamebox.load_sound("Coin.wav")
music1 = gamebox.load_sound("Music1 (online-audio-converter.com).wav")
# all music downloaded from soundimage.org as .mp3's, and then converted to .wav

# general lists
mazes = [maze1, maze2, maze3, maze4]
coins = [coins1, coins2, coins3, coins4]
backgroundmusic = [music1]

# defined varialbles with global scope
time = 0
ticks = 0
level = 0
finaltime = 0
game_on = False
coincount = 0

def tick(keys):
    global level
    global coincount
    global ticks
    global time
    global finaltime
    global game_on
    camera.clear("black")
    camera.draw(background)

    character.image = explorer[0]
    # character movement
    if pygame.K_UP in keys:
        character.y -= 5
        if 0 <= ticks % 12 < 3:
            character.image = explorer[13]
        elif 3 <= ticks % 12 < 6:
            character.image = explorer[14]
        elif 6 <= ticks % 12 < 9:
            character.image = explorer[15]
        elif 9 <= ticks % 12 <= 11:
            character.image = explorer[14]
    if pygame.K_DOWN in keys:
        character.y += 5
        if 0 <= ticks % 12 < 3:
            character.image = explorer[1]
        elif 3 <= ticks % 12 < 6:
            character.image = explorer[2]
        elif 6 <= ticks % 12 < 9:
            character.image = explorer[3]
        elif 9 <= ticks % 12 <= 11:
            character.image = explorer[2]
    if pygame.K_RIGHT in keys:
        character.x += 5
        if 0 <= ticks % 12 < 3:
            character.image = explorer[9]
        elif 3 <= ticks % 12 < 6:
            character.image = explorer[10]
        elif 6 <= ticks % 12 < 9:
            character.image = explorer[11]
        elif 9 <= ticks % 12 <= 11:
            character.image = explorer[10]
    if pygame.K_LEFT in keys:
        character.x -= 5
        if 0 <= ticks % 12 < 3:
            character.image = explorer[5]
        elif 3 <= ticks % 12 < 6:
            character.image = explorer[6]
        elif 6 <= ticks % 12 < 9:
            character.image = explorer[7]
        elif 9 <= ticks % 12 <= 11:
            character.image = explorer[6]

    # defining levels
    startingpoint.image = treasure[0]
    if level == 1:
        maze = maze1
        coins = coins1
    elif level == 2:
        maze = maze2
        coins = coins2
    elif level == 3:
        maze = maze3
        coins = coins3
    elif level == 4:
        maze = maze4
        coins = coins4

    # drawing mazes and character movement/movement restraints
    if 0 < level < 5:
        # character movement restraints
        for map in maze:
            for wall in map:
                if character.touches(wall, -5, 0):
                    character.move_to_stop_overlapping(wall)
        # collecting of coins
        for coin in coins:
            if character.touches(coin):
                coins.remove(coin)
                coincount += 1
                coin_sound.play()
            camera.draw(coin)
        # drawing maze
        camera.draw(startingpoint)
        for sides in range(len(maze)):
            for i in range(len(maze[sides])):
                camera.draw(maze[sides][i])
        # drawing character
        camera.draw(character)

        # timer
        if game_on:
            ticks += 1
            if ticks % 30 == 0:
                time += 1
        timer = gamebox.from_text(15, 15, str(time), "Arial", 20, "pink")
        timerbox = gamebox.from_color(15, 15, "dark blue", 30, 30)
        levelup = [
            gamebox.from_color(250, 250, "dark blue", 500, 200),
            gamebox.from_text(250, 220, "Level completed!", "Arial", 60, "pink"),
            gamebox.from_text(250, 310, "Press TAB to Continue", "Arial", 40, "yellow")
        ]
        camera.draw(timerbox)
        camera.draw(timer)

        # coint counter
        coincounter = gamebox.from_text(485, 485, str(coincount), "Arial", 20, "dark blue")
        coinbox = gamebox.from_color(485, 485, "yellow", 30, 30)
        camera.draw(coinbox)
        camera.draw(coincounter)

        # leveling up
        if coincount == 3 and character.touches(startingpoint):
            character.x = 250
            character.y = 250
            game_on = False
            for elements in levelup:
                camera.draw(elements)
                if pygame.K_TAB in keys:
                    finaltime += time
                    time = 0
                    coincount = 0
                    level += 1
                    game_on = True
                    keys.clear()

    # drawing start screen
    elif level == 0:
        for i in range(len(startscreen)):
            camera.draw(startscreen[i])
        if pygame.K_SPACE in keys:
            level = 1
            game_on = True

    # drawing close screen
    elif level == 5:
        game_on = False
        endtime = gamebox.from_text(250, 305, str(finaltime), "Arial", 60, "yellow", bold=True)
        lowest = scorebank(finaltime)
        highscore = gamebox.from_text(250, 410, "The fastest time is "+str(lowest), "Arial", 40, "Magenta")
        for i in range(len(closescreen)):
            camera.draw(closescreen[i])
            camera.draw(endtime)
            camera.draw(highscore)
            gamebox.pause()
            if pygame.K_ESCAPE in keys:
                gamebox.unpause()
                gamebox.stop_loop()

    music1.play()

    camera.display()

def scorebank(finaltime):
    # adding current score
    outfile = open("scores.txt", "a")
    outfile.write(str(finaltime)+"\n")
    outfile.close()

    # finding the lowest score
    infile = open("scores.txt", "r")
    allscores = infile.read()
    scorelist = allscores.split("\n")
    numbered = []
    for i in range(len(scorelist) - 1):
        numbered.append(int(scorelist[i]))
    lowest = min(numbered)
    infile.close()

    return lowest


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
