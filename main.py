from blessed import Terminal

import game
import menu

menu.menu()

game_stats = game.game_start()

i = game_stats[0]#inventory
p = game_stats[1]#player
u = game_stats[2]#underground
g = game_stats[3]#ground
w = game_stats[4]#world
b = game_stats[5]#biomes

game.update(p, w, i, b)

while True:
  with Terminal().cbreak():  #input detection and player movement
    print("")
    move = Terminal().inkey(timeout=60)
  game.player_move(p, g, u, w, i, move)
  game.update(p, w, i, b)
