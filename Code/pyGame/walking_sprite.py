

import pygame


SCREEN_MIN_X = 0
SCREEN_MAX_X = 500
SCREEN_MIN_Y = 0
SCREEN_MAX_Y = 500
FPS = 60


class Player(pygame.sprite.Sprite):
  def __init__(self, pos, image):
    super().__init__()
    self.image = image
    self.pos = pos
    self.rect = self.image.get_rect(center=pos)

  def draw(self, screen):
    screen.blit(self.image, self.rect)

  def move(self, d_x, d_y):
    self.pos = (self.pos[0] + d_x, self.pos[1] + d_y)
    self.rect = self.image.get_rect(center=self.pos)

    # Keep player on the screen
    if self.rect.left < 0:
      self.rect.left = 0
    elif self.rect.right > SCREEN_MAX_X:
      self.rect.right = SCREEN_MAX_X
    if self.rect.top <= 0:
      self.rect.top = 0
    elif self.rect.bottom >= SCREEN_MAX_Y:
      self.rect.bottom = SCREEN_MAX_Y

def main():
  pygame.init()
  screen = pygame.display.set_mode([SCREEN_MAX_X, SCREEN_MAX_Y])

  player_image = pygame.image.load("player.png").convert_alpha()
  player = Player((250, 250), player_image)

  clock = pygame.time.Clock()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    keystate = pygame.key.get_pressed()
    x_direction = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
    y_direction = keystate[pygame.K_DOWN] - keystate[pygame.K_UP]

    if keystate[pygame.K_ESCAPE]:
      running = False

    player.move(x_direction, y_direction)

    screen.fill((255, 255, 255))

    player.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

  pygame.quit()


if __name__ == "__main__":
  main()
