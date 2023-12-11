from email.mime import image
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Trivia')

true_img = pygame.image.load('Quizz Project/check.png').convert_alpha()
false_img = pygame.image.load('Quizz Project/x.png').convert_alpha()

# Button Class
class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        """Draws the button on the screen"""
        screen.blit(self.image, (self.rect.x, self.rect.y))


# Start button instances
true_button = Button(100, 200, true_img)
false_button = Button(450, 200, false_img)





run = True
while run:

    screen.fill((202, 228, 241))

    true_button.draw()
    false_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()