
import pygame

SCREEN_MIN_X = 0
SCREEN_MAX_X = 500
SCREEN_MIN_Y = 0
SCREEN_MAX_Y = 500
FPS = 60

BULLET_SPEED = 2
PLAYER_SPEED = 1

class Player:
  def __init__(self, x, y, width, height, color):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.direction = 0

  def move(self, d_x, d_y, other_figures):
    if d_x == 1:
      self.direction = 1
    elif d_x == -1:
      self.direction = 3
    elif d_y == 1:
      self.direction = 2
    elif d_y == -1:
      self.direction = 0

    if self.x <= SCREEN_MIN_X:
      if d_x == -1:
        return
    if self.x + self.width >= SCREEN_MAX_X:
      if d_x == 1:
        return

    if self.y <= SCREEN_MIN_Y:
      if d_y == -1:
        return
    if self.y + self.height >= SCREEN_MAX_Y:
      if d_y == 1:
        return

    # check collision
    for other_figure in other_figures:
      if other_figure == self:
        continue

      if (self.x + self.width + d_x > other_figure.x and
          self.x + d_x < other_figure.x + other_figure.width and
          self.y + self.height + d_y > other_figure.y and
              self.y + d_y < other_figure.y + other_figure.height):
        return

    self.x += d_x * PLAYER_SPEED
    self.y += d_y * PLAYER_SPEED

  def shoot(self):
    if self.direction == 0:
      bullet_x = self.x + self.width / 2
      bullet_y = self.y - 10
    elif self.direction == 1:
      bullet_x = self.x + self.width + 10
      bullet_y = self.y + self.height / 2
    elif self.direction == 2:
      bullet_x = self.x + self.width / 2
      bullet_y = self.y + self.height + 10
    else:
      bullet_x = self.x - 10
      bullet_y = self.y + self.height / 2

    return Bullet(bullet_x, bullet_y, self.direction)


  def draw(self, screen):
    pygame.draw.rect(screen, (self.color[0], self.color[1], self.color[2]),
                     (self.x, self.y, self.width, self.height), 0)

    # show direction
    if self.direction == 0:
      direction_figure_rect = (self.x + self.width / 2 - 5, self.y, 10, 10)
    elif self.direction == 1:
      direction_figure_rect = (
          self.x + self.width - 10, self.y + self.height / 2 - 5, 10, 10)
    elif self.direction == 2:
      direction_figure_rect = (self.x + self.width / 2 - 5,
                               self.y + self.height - 10, 10, 10)
    else:
      direction_figure_rect = (self.x, self.y + self.height / 2 - 5, 10, 10)

    pygame.draw.rect(screen, (255, 0, 0), direction_figure_rect, 0)

class Bullet:
  def __init__(self, x, y, direction):
    self.x = x - 5
    self.y = y - 5
    self.width = 10
    self.height = 10
    self.color = (255, 0, 0)
    self.direction = direction

  def move(self):
    if self.direction == 0:
      self.y -= BULLET_SPEED
    elif self.direction == 1:
      self.x += BULLET_SPEED
    elif self.direction == 2:
      self.y += BULLET_SPEED
    else:
      self.x -= BULLET_SPEED

  def still_on_screen(self) -> bool:
    if ((self.x + self.width < SCREEN_MIN_X) or (self.x > SCREEN_MAX_X)
         or (self.y + self.height < SCREEN_MIN_Y) or (self.y > SCREEN_MAX_Y)):
      return False

    return True

  def draw(self, screen):
    pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height), 0)

  def collide(self, player) -> bool:
    if (self.x + self.width > player.x and
        self.x < player.x + player.width and
        self.y + self.height > player.y and
        self.y < player.y + player.height):
      return True

    return False

def main():
  pygame.init()
  screen = pygame.display.set_mode([SCREEN_MAX_X, SCREEN_MAX_Y])

  player_width = 50
  player_height = 50

  player1 = Player(50, 50, player_width, player_height, (0, 0, 255))
  player2 = Player(400, 400, player_width, player_height, (0, 255, 0))

  objects = []
  objects.append(player1)
  objects.append(player2)

  bullets = []

  player_1_shoot = False
  player_2_shoot = False
  winner_text = ""

  clock = pygame.time.Clock()
  running = True
  pressed_quit = False
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        pressed_quit = True

      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            running = False
            pressed_quit = True

          if event.key == pygame.K_e:
              player_1_shoot = True

          if event.key == pygame.K_SPACE:
              player_2_shoot = True

    keystate = pygame.key.get_pressed()
    direction_x1 = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
    direction_y1 = keystate[pygame.K_DOWN] - keystate[pygame.K_UP]

    direction_x2 = keystate[pygame.K_d] - keystate[pygame.K_a]
    direction_y2 = keystate[pygame.K_s] - keystate[pygame.K_w]

    if keystate[pygame.K_ESCAPE]:
      running = False

    player1.move(direction_x1, direction_y1, objects)
    player2.move(direction_x2, direction_y2, objects)

    if player_1_shoot:
      player_1_shoot = False
      bullets.append(player1.shoot())

    if player_2_shoot:
      player_2_shoot = False
      bullets.append(player2.shoot())

    remain_bullets = []
    for bullet in bullets:
      if bullet.collide(player1):
        winner_text = "player2 won"
        running = False
        break
      elif bullet.collide(player2):
        winner_text = "player1 won"
        running = False
        break

      if bullet.still_on_screen():
        remain_bullets.append(bullet)

    bullets = remain_bullets

    for bullet in bullets:
      bullet.move()


    screen.fill((255, 255, 255))

    for object in objects:
      object.draw(screen)

    for bullet in bullets:
      bullet.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

  running = not pressed_quit
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        running = False

    screen.fill((255, 255, 255))

    exit_message_font = pygame.font.SysFont("Verdana", 24)
    exit_message_surface = exit_message_font.render(
        "Press any button to exit", True, (0, 0, 0))
    score_font = pygame.font.SysFont("Verdana", 32)
    score_font.bold = True
    score_surface = score_font.render(winner_text, True, (0, 0, 0))

    screen.blit(exit_message_surface, (SCREEN_MAX_X/2 -
                exit_message_surface.get_width()/2, 10))
    screen.blit(score_surface, (SCREEN_MAX_X/2 -
                score_surface.get_width()/2, SCREEN_MAX_Y/2 - score_surface.get_height()/2))

    pygame.display.flip()

    clock.tick(FPS)

  pygame.quit()

main()
