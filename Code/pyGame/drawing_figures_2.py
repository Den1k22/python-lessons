
import pygame
import time
import random

SCREEN_MIN_X = 0
SCREEN_MAX_X = 500
SCREEN_MIN_Y = 0
SCREEN_MAX_Y = 500
FPS = 60

FRAME_TIME = 1 / FPS


class Figure:
  def __init__(self, x, y, direction_x, direction_y, color, velocity):
    self.x = x
    self.y = y
    self.d_x = direction_x
    self.d_y = direction_y
    self.color = color
    self.velocity = velocity

  def draw(self):
    pass

  def move(self):
    self.x += self.velocity * self.d_x * FRAME_TIME
    self.y += self.velocity * self.d_y * FRAME_TIME

  def update_velocity(self, velocity):
    self.velocity += velocity


class Circle(Figure):
  def __init__(self, x, y, direction_x, direction_y, radius, color, velocity=1):
    super().__init__(x, y, direction_x, direction_y, color, velocity)

    self.radius = radius

  def draw(self, screen):
    pygame.draw.circle(
        screen, (self.color[0], self.color[1], self.color[2]), (self.x, self.y), self.radius)

  def move(self):
    if (self.x <= SCREEN_MIN_X + self.radius) or (self.x >= SCREEN_MAX_X - self.radius):
      self.d_x = -self.d_x

    if (self.y <= SCREEN_MIN_Y + self.radius) or (self.y >= SCREEN_MAX_Y - self.radius):
      self.d_y = -self.d_y

    super().move()

class Rectangle(Figure):
  def __init__(self, x, y, width, height, direction_x, direction_y, color, velocity=1):
    super().__init__(x, y, direction_x, direction_y, color, velocity)

    self.width = width
    self.height = height

  def move(self):
    if (self.x >= SCREEN_MAX_X - self.width) or (self.x <= SCREEN_MIN_X):
      self.d_x = -self.d_x

    if (self.y >= SCREEN_MAX_Y - self.height) or (self.y <= SCREEN_MIN_Y):
      self.d_y = -self.d_y

    super().move()

  def draw(self, screen):
    pygame.draw.rect(screen, (self.color[0], self.color[1], self.color[2]),
                     (self.x, self.y, self.width, self.height), 0)


def change_velocity(figures, velocity): # velocity can be 1 or -1
  for figure in figures:
    figure.update_velocity(velocity)


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

    keystate = pygame.key.get_pressed()
    direction = keystate[pygame.K_UP] - keystate[pygame.K_DOWN]

    if (direction != 0):
      change_velocity(figures, direction)

    screen.fill((255, 255, 255))

    for figure in figures:
      figure.draw(screen)
      figure.move()

    pygame.display.flip()

    time.sleep(FRAME_TIME)

pygame.quit()
