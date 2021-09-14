
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
    pygame.draw.circle(
        screen, (self.color[0], self.color[1], self.color[2]), (self.x, self.y), self.radius)

  def move(self):
    if (self.x <= SCREEN_MIN_X + self.radius) or (self.x >= SCREEN_MAX_X - self.radius):
      self.d_x = -self.d_x

    if (self.y <= SCREEN_MIN_Y + self.radius) or (self.y >= SCREEN_MAX_Y - self.radius):
      self.d_y = -self.d_y

    self.x += 1 * self.d_x
    self.y += 1 * self.d_y


class Rectangle:
  def __init__(self, x, y, width, height, d_x, d_y, color):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.d_x = d_x
    self.d_y = d_y
    self.color = color

  def move(self):
    if (self.x >= SCREEN_MAX_X - self.width) or (self.x <= SCREEN_MIN_X):
      self.d_x = -self.d_x

    if (self.y >= SCREEN_MAX_Y - self.height) or (self.y <= SCREEN_MIN_Y):
      self.d_y = -self.d_y

    self.x += 1 * self.d_x  # use velocity like this: self.x += self.velocity * self.d_x
    self.y += 1 * self.d_y

  def draw(self, screen):
    pygame.draw.rect(screen, (self.color[0], self.color[1], self.color[2]),
                     (self.x, self.y, self.width, self.height), 0)


pygame.init()

screen = pygame.display.set_mode([SCREEN_MAX_X, SCREEN_MAX_Y])

figures = []

for i in range(10):
  radius = random.randint(10, 100)
  x = random.randint(SCREEN_MIN_X + radius, SCREEN_MAX_X - radius)
  y = random.randint(SCREEN_MIN_Y + radius, SCREEN_MAX_Y - radius)
  direction_x = random.random() * 5
  direction_y = random.random() * 5
  color = (random.randint(0, 255), random.randint(
      0, 255), random.randint(0, 255))
  figures.append(Circle(x, y, direction_x, direction_y, radius, color))

for i in range(10):
  width = random.randint(10, 100)
  height = random.randint(10, 100)
  x = random.randint(SCREEN_MIN_X + width, SCREEN_MAX_X - width)
  y = random.randint(SCREEN_MIN_Y + height, SCREEN_MAX_Y - height)
  direction_x = random.random() * 5
  direction_y = random.random() * 5
  color = (random.randint(0, 255), random.randint(
      0, 255), random.randint(0, 255))

  figures.append(Rectangle(x, y, width, height,
                           direction_x, direction_y, color))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for figure in figures:
      figure.draw(screen)
      figure.move()

    pygame.display.flip()

    time.sleep(0.01)

pygame.quit()
