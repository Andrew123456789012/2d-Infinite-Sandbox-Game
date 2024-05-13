from blessed import Terminal
import game
import menu

menu.menu()

game_stats = game.game_start()

i = game_stats[0]
p = game_stats[1]
u = game_stats[2]
g = game_stats[3]
w = game_stats[4]
b = game_stats[5]

game.update(p, w, i, b)

while True:
  with Terminal().cbreak():  #input detection and player movement
    print("")
    move = Terminal().inkey(timeout=60)
  game.player_move(p, g, u, w, i, move)
  game.update(p, w, i, b)
