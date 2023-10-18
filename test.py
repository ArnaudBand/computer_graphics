# https://github.com/ArnaudBand/computer_graphics/blob/main/test.py

import pygame

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

class Shape:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, 50, 50))  # Draw a colored rectangle

# Initialize pygame
pygame.init()

# Set up the canvas
canvas_width = 800
canvas_height = 600
canvas = Canvas(canvas_width, canvas_height)

# Create a shape and add it to the canvas
my_shape = Shape((250, 100), (255, 0, 0))  # Red color
canvas.add_shape(my_shape)

# Create another shape and add it to the canvas
another_shape = Shape((200, 200), (150, 100, 50))  # Blue color
canvas.add_shape(another_shape)

# Create the display window
screen = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Canvas with Shapes")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((5, 5, 5))  # Fill the screen with white

    for shape in canvas.shapes:
        shape.draw(screen)

    pygame.display.flip()

# Quit pygame
pygame.quit()
