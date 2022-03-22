
import random
import pygame
import math


SCREEN_MIN_X = 0
SCREEN_MAX_X = 500
SCREEN_MIN_Y = 0
SCREEN_MAX_Y = 500
FPS = 60

AMOUNT_OF_FIGURES = 100

VELOCITY_COEFFICIENT = 0.1


class Figure:
  def __init__(self, x, y, direction_x, direction_y, color, velocity):
    self.x = x
    self.y = y
    self.d_x = direction_x
    self.d_y = direction_y
    self.color = color
    self.velocity = velocity

  def move(self):
    self.x += self.velocity * self.d_x * VELOCITY_COEFFICIENT
    self.y += self.velocity * self.d_y * VELOCITY_COEFFICIENT

  def update_velocity(self, velocity):
    self.velocity += velocity

  def stop_figure(self):
    self.velocity = 0

  def update_color(self, color):
    new_color = []
    for sub_color in self.color:
      new_sub_color = sub_color + color

      if (new_sub_color < 0 or new_sub_color > 255):
        new_sub_color = sub_color

      new_color.append(new_sub_color)

    self.color = (new_color[0], new_color[1], new_color[2])


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

  def clicked(self, pos):
    return math.sqrt((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2) < self.radius


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

  def clicked(self, pos):
    return ((self.x < pos[0] and pos[0] < self.x + self.width)
            and (self.y < pos[1] and pos[1] < self.y + self.height))


def change_velocity(figures, velocity):  # velocity can be 1 or -1
  for figure in figures:
    figure.update_velocity(velocity)


def change_color(figures, color):
  for figure in figures:
    figure.update_color(color)


def stop_figures(figures):
  for figure in figures:
    figure.stop_figure()


def init_figure():
  if random.randint(0, 1):
    radius = random.randint(10, 100)
    x = random.randint(SCREEN_MIN_X + radius, SCREEN_MAX_X - radius)
    y = random.randint(SCREEN_MIN_Y + radius, SCREEN_MAX_Y - radius)
    direction_x = random.random() * 5 - 2.5
    direction_y = random.random() * 5 - 2.5
    color = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    return Circle(x, y, direction_x, direction_y, radius, color)
  else:
    width = random.randint(10, 100)
    height = random.randint(10, 100)
    x = random.randint(SCREEN_MIN_X + width, SCREEN_MAX_X - width)
    y = random.randint(SCREEN_MIN_Y + height, SCREEN_MAX_Y - height)
    direction_x = random.random() * 5 - 2.5
    direction_y = random.random() * 5 - 2.5
    color = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    return Rectangle(x, y, width, height, direction_x, direction_y, color)


def init_figures(n=AMOUNT_OF_FIGURES):
  figures = []

  for _ in range(n):
    figures.append(init_figure())

  return figures


def main():
  pygame.init()
  screen = pygame.display.set_mode([SCREEN_MAX_X, SCREEN_MAX_Y])

  figures = init_figures()

  clock = pygame.time.Clock()
  running = True
  mouse_down = False
  score = 0

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_down = True

      if event.type == pygame.MOUSEBUTTONUP:
        mouse_down = False

    if mouse_down:
      mouse_pos = pygame.mouse.get_pos()
      figures = [
          figure for figure in figures if not figure.clicked(mouse_pos)]

      if len(figures) < AMOUNT_OF_FIGURES:
          removed_figures = AMOUNT_OF_FIGURES - len(figures)
          score += removed_figures
          figures.extend(init_figures(removed_figures))

    keystate = pygame.key.get_pressed()
    direction = keystate[pygame.K_UP] - keystate[pygame.K_DOWN]
    color = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
    stop = keystate[pygame.K_SPACE]

    if keystate[pygame.K_ESCAPE]:
      running = False

    if direction != 0:
      change_velocity(figures, direction)

    if color != 0:
      change_color(figures, color)

    if stop != 0:
      stop_figures(figures)

    screen.fill((255, 255, 255))

    for figure in figures:
      figure.draw(screen)
      figure.move()

    score_font = pygame.font.SysFont("Verdana", 32)
    score_font.bold = True
    score_surface = score_font.render(str(score), True, (0, 0, 0))
    screen.blit(score_surface, (SCREEN_MAX_X/2 - score_surface.get_width()/2, 10))

    pygame.display.flip()

    clock.tick(FPS)

  pygame.quit()


if __name__ == "__main__":
  main()
