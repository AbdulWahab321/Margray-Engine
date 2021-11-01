import engine
import pygame

game = engine.Game()
screen = game.create_screen()
map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
tile_rects = []
rects = []
run = True
player = game.sprite()
playercolliding = False
fps = game.fps()
while run:
    game.set_bgcolor()
    player.draw()

    for ev in game.run():
        if ev.type == engine.QUIT:
            game.quit()
        if ev.type == engine.KEYDOWN:
            if ev.key == engine.Keys.KEY_UP_ARROW:
                player.moveUp(5)
            if ev.key == engine.Keys.KEY_D:player.destroy()    
        elif ev.type == engine.KEYUP:
            if ev.key == engine.Keys.KEY_UP_ARROW:player.moveDown(5)
            playercolliding = False
    y = 5

    if playercolliding == False:
        player.moveDown(10)
    for row in map:
        x = 0

        for tile in row:

            if tile == 0:
                
                game.display_image("./assets/grass.png", x*50, y*50, (50, 50))
            elif tile == 1:
                game.display_image("./assets/dirt.png", x*50, y*50, (50, 50))
            if tile != 3:
                tile_rects.append(
                    game.transparent_sprite(position=(x*50, y*50)))
                
            x += 1
        y += 1
        
    for i in tile_rects:
        i.draw()
        rects.append(i.get_rect())
            
    game.update()


      