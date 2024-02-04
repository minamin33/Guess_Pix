import pygame
from pygame.locals import *
from sys import exit #closes it out completely

#create button
class Button:
    def __init__(self, text, width,height,pos,elevation):
        #Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        #top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = 'black'

        #bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = "grey32"
        self.text_surf = gui_font.render(text, False,'white')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        #elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation
        pygame.draw.rect(SCREEN,self.bottom_color, self.bottom_rect,border_radius = 12)
        pygame.draw.rect(SCREEN,self.top_color,self.top_rect,border_radius = 12)
        SCREEN.blit(self.text_surf,self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = 'gold'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    print('click')
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = 'black'

#setup process
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT = (600,500)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Menu') #puts the game name on the top of the window
clock = pygame.time.Clock() #fps

gui_font = pygame.font.Font('/Users/sherina./Guess-Game/Font/VCR_OSD_MONO_1.001.ttf', 30)
bkgd = pygame.image.load('/Users/sherina./Guess-Game/Graphics/Clouds.png').convert()
detail = pygame.image.load('/Users/sherina./Guess-Game/Graphics/Hearts.png').convert_alpha()

Button1 = Button("Start", 120,45,(240,345),6)
x = 0
def events():
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 


    


     while True: 
        events()
        #if events.type == pygame.MOUSEBUTTONDOWN:
               # if Button1.checkForInput(MENU_MOUSE_POS):
                   # play()
        rel_x = x % bkgd.get_rect().width
        SCREEN.blit(bkgd,(rel_x - bkgd.get_rect().width,0))
        x-= 1
        if rel_x < SCREEN_WIDTH:
            SCREEN.blit(bkgd, (rel_x,0))
        SCREEN.blit(detail,(0,0))
        Button1.draw()
        pygame.display.update()
        clock.tick(60)#fps




'''




def get_font(size):
    return pygame.font.Font('/Users/sherina./Guess-Game/Font/Minecraft.ttf', size)
def start():
    while True:
        SCREEN.fill('black')


#text1 = font.render('START GAME', False, 'black')

while True: #keeps the window continously opened
    for event in pygame.event.get(): #need to create quit button before running screen
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  #closes it out completely

    screen.blit(surface1,(0,0))
    #screen.blit(text1,(130,360))

    pygame.display.update()
    clock.tick(60)#fps


'''


