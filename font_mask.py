import sys
import pygame as pg


SCREEN_SIZE = (500, 500)
CAPTION = "Font Masking"
BACKGROUND_COLOR = pg.Color("darkred")
FPS = 60

    
class App(object):
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.done = False
        self.clock = pg.time.Clock()
        self.text = self.make_font_mask("Hello, world.")
        text_center = self.screen_rect.center
        self.text_rect = self.text.get_rect(center=text_center)

    def make_font_mask(self, message):
        mask = FONT.render(message, True, pg.Color("white"))
        image = pg.Surface(mask.get_size()).convert_alpha()
        image_rect = FRAC.get_rect(center=image.get_rect().center)
        image.blit(FRAC, image_rect)
        image.blit(mask, (0,0), special_flags=pg.BLEND_RGBA_MULT)
        return image
        
    def event_loop(self):
        for event in pg.event.get():
            self.done = event.type == pg.QUIT
        
    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.screen.fill(BACKGROUND_COLOR)
            self.screen.blit(self.text, self.text_rect)
            pg.display.update()
            self.clock.tick(FPS)
            
            
def main():
    global FONT, FRAC
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    FONT = pg.font.Font(None, 100)
    FRAC = pg.image.load("frac.jpg").convert()
    App().main_loop()
    pg.quit()
    sys.exit()
                

if __name__ == "__main__":
    main()
            

        
        
        
        
        
        
        
        
        
        
    

