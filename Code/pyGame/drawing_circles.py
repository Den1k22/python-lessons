# Simple pygame program

# Import and initialize the pygame library
import pygame
import time
import random

SCREEN_MIN_X = 0
SCREEN_MAX_X = 500
SCREEN_MIN_Y = 0
SCREEN_MAX_Y = 500

class Circle:
  def __init__(self, x, y, direction_x, direction_y, radius, color):
    self.x = x
    self.y = y
    self.d_x = direction_x
    self.d_y = direction_y
    self.radius = radius
    self.color = color

  def draw(self, screen):
    pygame.draw.circle(screen, (self.color[0], self.color[1], self.color[2]), (self.x, self.y), self.radius)

  def move(self):
    if (self.x <= SCREEN_MIN_X + self.radius) or (self.x >= SCREEN_MAX_X - self.radius):
      self.d_x = -self.d_x

    if (self.y <= SCREEN_MIN_Y + self.radius) or (self.y >= SCREEN_MAX_Y - self.radius):
      self.d_y = -self.d_y

    self.x += 1 * self.d_x
    self.y += 1 * self.d_y


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_MAX_X, SCREEN_MAX_Y])

circles = []

for i in range(10):
  radius = random.randint(10, 100)
  x = random.randint(SCREEN_MIN_X + radius, SCREEN_MAX_X - radius)
  y = random.randint(SCREEN_MIN_Y + radius, SCREEN_MAX_Y - radius)
  direction_x = random.random() * 5
  direction_y = random.random() * 5
  color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  circles.append(Circle(x, y, direction_x, direction_y, radius, color))

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    for circle in circles:
      circle.draw(screen)
      circle.move()

    pygame.display.flip()

    time.sleep(0.01)

# Done! Time to quit.
pygame.quit()
