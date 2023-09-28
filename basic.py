import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
width = 640
height = 480

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lab 1: Computer Graphics")

# Set the color (RGB) for the background
background_color = (0, 0, 0)

# Set the color (RGB) for the line
line_color = (255, 50, 10)

# Set the starting and ending points of the line
start_pos = (100, 100)
end_pos = (500, 400)

# Set the line thickness
line_thickness = 5

# Game loop
while True:
    # Clear the screen with the background color
    screen.fill(background_color)

    # Draw the line on the screen
    pygame.draw.line(screen, line_color, start_pos, end_pos, line_thickness)

    # Update the display
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()