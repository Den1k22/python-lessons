import math
import pygame


SCREEN_MIN_X = 0
SCREEN_MAX_X = 500
SCREEN_MIN_Y = 0
SCREEN_MAX_Y = 500
FPS = 60


def calculate_rotation(point, angle):
  # angle here is rotation way which can be -1 or 1,
  # but for calculations the angle must be positive
  if angle < 0:
    angle = -angle
    new_point = (point[0] * math.cos(math.radians(angle)) +
                 point[1] * math.sin(math.radians(angle)),
                 point[0] * -math.sin(math.radians(angle)) +
                 point[1] * math.cos(math.radians(angle)))
  else:
    new_point = (point[0] * math.cos(math.radians(angle)) -
                 point[1] * math.sin(math.radians(angle)),
                 point[0] * math.sin(math.radians(angle)) +
                 point[1] * math.cos(math.radians(angle)))
  return new_point


class Square():
  def __init__(self, center_x, center_y, size):
    self.center_x = center_x
    self.center_y = center_y

    # Each point is relation from center of square
    self.point1 = (-size, -size)
    self.point2 = (size, -size)
    self.point3 = (size, size)
    self.point4 = (-size, size)

  def move(self, direction_x, direction_y):
    self.center_x += direction_x
    self.center_y += direction_y

  def get_points_absolute(self):
    absolute = [
        (self.point1[0] + self.center_x, self.point1[1] + self.center_y),
        (self.point2[0] + self.center_x, self.point2[1] + self.center_y),
        (self.point3[0] + self.center_x, self.point3[1] + self.center_y),
        (self.point4[0] + self.center_x, self.point4[1] + self.center_y)
    ]

    return absolute

  def draw(self, screen):
    pygame.draw.lines(screen, (255, 0, 0), True, self.get_points_absolute(), 5)

  def rotate(self, direction):
    if direction == 0:
      return

    # The center of figure is the point around which rotation is calculated
    # Therefore we calculate rotation for points of square (which are relation from center point)
    self.point1 = calculate_rotation(self.point1, direction)
    self.point2 = calculate_rotation(self.point2, direction)
    self.point3 = calculate_rotation(self.point3, direction)
    self.point4 = calculate_rotation(self.point4, direction)


def main():
  pygame.init()
  screen = pygame.display.set_mode([SCREEN_MAX_X, SCREEN_MAX_Y])

  square = Square(SCREEN_MAX_X / 2, SCREEN_MAX_Y / 2, 50)

  clock = pygame.time.Clock()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    keystate = pygame.key.get_pressed()
    x_direction = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
    y_direction = keystate[pygame.K_DOWN] - keystate[pygame.K_UP]

    rotation = keystate[pygame.K_k] - keystate[pygame.K_l]

    if keystate[pygame.K_ESCAPE]:
      running = False

    square.move(x_direction, y_direction)
    square.rotate(rotation * 2)

    screen.fill((255, 255, 255))

    square.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

  pygame.quit()


if __name__ == "__main__":
  main()
