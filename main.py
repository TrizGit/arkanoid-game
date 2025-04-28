import pygame

pygame.init()

bg = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(bg)
clock = pygame.time.Clock()

class Area():
    def __init__(self, x, y, w, h, color=None):
        self.rect = pygame.Rect(x, y, w, h)
        if color:
            self.fill_color = color
        else:
            self.fill_color = bg
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Picture(Area):
    def __init__(self, filename, x=0, y=0, w=0, h=0):
        Area.__init__(self, x=x, y=y, w=w, h=h, color=None)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
class Label(Area):
    def setText(self, text, fSize, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fSize).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', 200, 285, 100, 30)
monsters = []
c1 = 9
start_x = 5
start_y = 5
for i in range(3):
    x = start_x + (27.5 * i)
    y = start_y + (55 * i)
    for j in range(c1):
        monster = Picture('enemy.png', x, y, 50, 50)
        monsters.append(monster)
        x += 55
    c1 -= 1
# print(monsters)

speed_x = 3
speed_y = 3
move_left = False
move_right = False
gameOver = False

while not gameOver:
    platform.fill()
    ball.fill()
    for m in monsters:
        m.draw()
        if m.colliderect(ball.rect):
            monsters.remove(m)
            m.fill()
            speed_y *= -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False

    if move_left and platform.rect.x >= 0:
        platform.rect.x -= 3
    if move_right and platform.rect.x <= 400:
        platform.rect.x += 3

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.colliderect(platform.rect):
        speed_y *= -1
    if ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x < 0 or ball.rect.x > 450:
        speed_x *= -1

    if ball.rect.y > 300:
        end_text = Label(150, 150, 50, 50)
        end_text.setText('YOU LOSE!!!', 60, (255, 0, 0))
        end_text.draw(10, 10)
        gameOver = True
    elif len(monsters) == 0:
        end_text = Label(150, 150, 50, 50)
        end_text.setText('YOU WIN!!!', 60, (0, 255, 0))
        end_text.draw(10, 10)
        gameOver = True

    ball.draw()
    platform.draw()
    pygame.display.update()
    clock.tick(40)