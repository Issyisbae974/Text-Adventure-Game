from shortcuts import Color, clear_screen, type_text
import readchar 

class RPGInfo():
    def __init__ (self, game_name):
        self.title = game_name
    
def introduction():
        clear_screen
        type_text(("Weclome dear traveller,"), 0.05, Color.bright_cyan_shortcut)
        type_text(("This land was once peaceful, a village of sorts where the folk would sing and dance\nHowever, an evil has corrupted this world"), 0.05, Color.cyan_shortcut)
            
        while True:
            key = readchar.readkey()
            if key == readchar.key.ENTER:
                break