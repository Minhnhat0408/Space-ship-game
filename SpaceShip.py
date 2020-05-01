import pygame, math, random

pygame.init()
window = pygame.display.set_mode((300, 500))


class Enemy:
    alien = pygame.image.load("alien2.png")

    def __init__(self, y, color):
        self.x = random.randrange(5, 280)
        self.y = y
        self.color = color
        self.walk = False

    # self.path = 500

    def draw(self):
        # pygame.draw.rect(window,self.color,(self.x-10,self.y-5,30,30),2)
        window.blit(Enemy.alien, (self.x - 20, self.y - 5))
        # pygame.display.update()


def text(text, size, color, pos):
    font = pygame.font.SysFont("comicsans", size, True)
    display = font.render(text, 10, color)
    window.blit(display, pos)


def main():
    cha = pygame.image.load("pngguru.com (2).png")
    image = pygame.image.load("space.jfif")
    image1 = pygame.transform.scale(image, (300, 500))
    x = 130
    y = 400
    Gamework = True
    cur = (x, y)
    Fps = pygame.time.Clock()
    enemy = Enemy(5, (255, 0, 0))
    enemyloop = []
    score = 0
    while Gamework:
        Fps.tick(100)
        multiple = random.randrange(5, 500, 5)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            cur = pygame.mouse.get_pos()
            enemy.walk = True

        if round(x) == cur[0] and round(y) == cur[1]:
            pass
        else:
            dx = cur[0] - x
            dy = cur[1] - y
            anggle = math.atan2(dy, dx)
            x += 1 * math.cos(anggle)
            y += 1 * math.sin(anggle)
        window.blit(image1, (0, 0))
        if enemy.walk:
            if len(enemyloop) < 1:
                enemyloop.append(Enemy(5, (255, 0, 0)))
            if enemyloop[0].y == multiple:
                enemyloop.append(Enemy(5, (255, 0, 0)))
                print("hello")
        for i in enemyloop:
            if x - 15 <= i.x - 10 <= x + 15 or x - 15 < i.x + 20 <= x + 15:
                if i.y + 25 > y - 20 and i.y - 5 < y - 10:
                    score -= 5
                    h = 0
                    text("-5", 30, (0, 120, 0), (130, 240))
                    pygame.display.flip()
                    while h < 100:
                        pygame.time.delay(10)
                        h += 1
                    enemyloop.clear()
            if score < 0:
                Gamework = False
            if i.y < 500:
                i.y += 5
            else:
                enemyloop.pop(enemyloop.index(i))
                score += 1

        for i in enemyloop:
            i.draw()
        text(f"Score {score}", 30, (0, 120, 0), (200, 5))
        window.blit(cha, (x - 25, y - 20))
        # pygame.draw.rect(window, (255, 0, 0), (x-15, y-20,30,50), 2)
        pygame.display.update()


main()
