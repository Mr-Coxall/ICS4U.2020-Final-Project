#!/usr/bin/env python3

# Created by: Jaeyoon Lee
# Created on: Jan 2019
# This is constants file

WIDTH = 1400
HEIGHT = 800
FPS = 60
N_PEOPLE = 100
RADIUS = 5
SPLASH_TIME = 3
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
FONT = None
TITLE = "Virus Simulator"
SETTING_TEXTS = ["Health colour:", "Infectious colour:", "Death/Background colour:"]
VARIABLE_TEXTS = [
    "Number of people:",
    "Probability of infection:",
    "Probability of death:",
    "Probability of mutation:",
    "Activity:",
]
HELPS = [
    "This program simulates the spread of a virus to people.",
    "When you start, you can set the virus name and start with a default virus model.",
    "In the simulation, you can observe while controlling the speed with buttons.",
    "If you want to set a new virus model, you can set it in 'Options'",
]

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (219, 20, 20)
GREY = (100, 100, 100)
GREEN = (50, 240, 100)
PURPLE = (210, 0, 250)
BLUE = (66, 135, 245)
