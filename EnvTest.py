import pygame
import sys

# Initialize pygame (must be called before using any pygame functions)
pygame.init()

# Create the game window (width = 640, height = 480)
screen = pygame.display.set_mode((640, 480))

# Set the window title
pygame.display.set_caption("Pygame Environment Test")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a font object for rendering text (default font, size 36)
font = pygame.font.SysFont(None, 36)

# Control variable for the main loop
running = True

# Initial position of the circle (center of the screen)
x, y = 320, 240

# Movement speed (pixels per frame)
speed = 5

# ------------------------------
# Main Game Loop
# ------------------------------
while running:
    
    # Handle events (e.g., window close)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current keyboard state (continuous input)
    keys = pygame.key.get_pressed()

    # Update position based on arrow key input
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Clear the screen with a background color (dark gray)
    screen.fill((30, 30, 30))

    # Draw a circle at the current position
    pygame.draw.circle(screen, (100, 200, 255), (x, y), 20)

    # Render instruction text
    text = font.render(
        "If you can move the circle, setup works.",
        True,
        (255, 255, 255)
    )

    # Draw the text on the screen at position (60, 30)
    screen.blit(text, (60, 30))

    # Update the display (render everything to the screen)
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Clean up and exit
pygame.quit()
sys.exit()