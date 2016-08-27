import pygame
from pygame.locals import *

def toggle_fullscreen():
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007 
    
    w,h = screen.get_width(),screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()
    
    pygame.display.quit()
    pygame.display.init()
    
    screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.display.set_caption(*caption)
 
    pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??
 
    pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007
    
    return screen


class App:
    def __init__(self):
        self._running = True
        self._display = None
        self._splash = None
        self._splash_running = True
        self.size = self.weight, self.height = 1280, 800
 
    def on_init(self):
        self._display = pygame.display.set_mode(
                self.size, pygame.HWSURFACE | pygame.FULLSCREEN
        )
        pygame.display.set_caption('Shadows of Brimstone HexCrawl')
        self.world = pygame.image.load('assets/world_default_high.jpg')
        self.background = pygame.Surface(self.world.get_size())
        self.background.blit(self.world, (0, 0))
        pygame.transform.scale(self.background, self.size, self._display)
        #self._display.blit(self.background, (0, 0))
        self._running = True
 
    def on_event(self, event):
        print('Got', event)
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == KEYDOWN:
            if event.key == K_q:
                self._running = False
        if event.type == MOUSEBUTTONDOWN:
            pass

            # toggle_fullscreen()
            # print('W', self._display.get_width())
            # print('H', self._display.get_height())
            # print('Flags', self._display.get_flags())
            # print('Bits', self._display.get_bitsize())

    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            #pygame.display.update()
            pygame.display.flip()

        self.on_cleanup()

 

def sob_main():
    '''

    '''
    app = App()
    app.on_execute()

if __name__ == "__main__" :
    sob_main()
