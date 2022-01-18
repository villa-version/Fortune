import pygame, sys, random


WIDTH, HEIGHT = 600, 600


class Circumference:

    def __init__(self, x, y, w, screen):
        self.x = x
        self.y = y
        self.w = w
        self.screen = screen
        self.angle = random.randint(0, 360)
        self.speed =   random.randint(1, 5)

    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), self.w)
        self.surface_rect = pygame.Rect(100, 150, 400, 300)
        self.surface = pygame.Surface(self.surface_rect.size, pygame.SRCALPHA)
        # Draw rect
        self.rotation()
        pygame.draw.polygon(self.surface, (0, 255, 0), points=[(175, 50), (200, 10), (225, 50)])
        self.surface = pygame.transform.rotate(self.surface, self.angle)
        self.screen.blit(self.surface, self.surface.get_rect(center=self.surface_rect.center))

    def rotation(self):
        if self.speed < 0.1:
            pass
        else:
            if self.angle >= 360:
                self.angle = 0
            self.angle += self.speed
            self.speed -= 0.001
            # print(self.angle)


class Choose:

    def __init__(self, x, y, w, h, screen):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.screen = screen

    def draw(self):
        obj = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, (255, 0, 255), obj)
        obj = pygame.Rect(self.x, self.y, self.w-5, self.h-5)
        pygame.draw.rect(self.screen, (255, 255, 255), obj)


class MainController:

    def __init__(self, screen):
        self.screen = screen
        self.circumference = Circumference(WIDTH/2, HEIGHT/2, 200, screen)
        self.chooses = [[], [], [], []]
        q = 1
        for i in range(q):
            chw = WIDTH/q
            chx = chw*i
            self.chooses[0].append(Choose(chx, 0, chw, 100, self.screen))
        for i in range(q):
            chw = WIDTH/q
            chx = chw*i
            self.chooses[1].append(Choose(chx, HEIGHT-100, chw, 100, self.screen))
        for i in range(q):
            chh = (HEIGHT-200)/q
            chy = 100+chh*i
            self.chooses[2].append(Choose(0, chy, 100, chh, self.screen))
        for i in range(q):
            chh = (HEIGHT-200)/q
            chy = 100+chh*i
            self.chooses[3].append(Choose(WIDTH-100, chy, 100, chh, self.screen))

    def update(self):
        for row in self.chooses:
            for ch in row:
                ch.draw()
        self.circumference.draw()
        self.highlight()

    def highlight(self):
        if self.circumference.speed < 0.1:
            #repetition = self.circumference.angle // 360
            if 45 >= self.circumference.angle >= -45:
                print(1)


def main():
    project_name = 'Fortune'
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(project_name)
    pygame.font.init()
    fpsClock = pygame.time.Clock()
    main_controller = MainController(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and main_controller.circumference.speed < 0.1:
                main_controller.circumference.speed = random.randint(1, 5)

        screen.fill((0, 0, 0))
        main_controller.update()
        pygame.display.update()
        # fpsClock.tick(10)


if __name__ == '__main__':
    main()
