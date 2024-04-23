import random
from colorama import Fore, Back
from merchants import merchant_interaction
from replit import clear
from blessed import Terminal
import time

grass = f"{Fore.LIGHTGREEN_EX}~ {Fore.WHITE}"
stone_floor = f"{Fore.LIGHTBLACK_EX}~ {Fore.WHITE}"
wall = f"{Fore.BLACK}x {Fore.WHITE}"
placed_wall = f"{Fore.BLACK}X {Fore.WHITE}"
broken_wall = f"{Fore.BLACK}- {Fore.WHITE}"
spike = f"{Fore.RED}ㅅ{Fore.WHITE}"
flat_spike = f"{Fore.RED}ㅡ{Fore.WHITE}"
chest = f"{Fore.YELLOW}[]{Fore.WHITE}"
looted_chest = f"{Fore.YELLOW}[ {Fore.WHITE}"
heart = f"{Fore.RED}♡ {Fore.WHITE}"
merchant = f"{Fore.YELLOW}ㅠ{Fore.WHITE}"
mineshaft = f"{Fore.YELLOW}⊓ {Fore.WHITE}"
exit = f"{Fore.YELLOW}⊔ {Fore.WHITE}"
ore = f"{Fore.YELLOW}◈ {Fore.WHITE}"

loot = ["hammer", "pickaxe", "block", "gold"]
loot_weights = [1, 1, 1, 5]


class World:

  def __init__(self, choices, weights, radius, ground, mine_block):
    self.board = {
        (0, 0): mine_block,
        (random.choice([5, -5]), random.choice([5, -5])): merchant,
    }
    self.radius = radius
    self.choices = choices
    self.weights = weights
    self.ground = ground

  def get_visible_window(self, x, y):
    visible = []
    for i in range(y - self.radius, y + self.radius + 1):
      row = []
      for j in range(x - self.radius, x + self.radius + 1):
        if (i, j) not in self.board:
          block = random.choices(self.choices, weights=self.weights)[0]
          self.board[i, j] = block
        row.append(self.board[i, j])
      visible.append(row)
    return visible

  def get_board_value(self, coord):
    return self.board.get((coord[1], coord[0]), None)

  def print_board(self, x, y):
    visible = self.get_visible_window(x, y)
    for row in visible:
      print("|" + Back.LIGHTGREEN_EX + "".join(row) + Back.RESET + "|")

  def set_board_value(self, coord, value):
    self.board[(coord[1], coord[0])] = value


class Player:

  def __init__(self, icon, coordinates, max_health=3, hammers=1, pickaxes=1):
    self.icon = icon
    self.coordinates = coordinates
    self.direction = "N"
    self.max_health = max_health
    self.health = max_health
    self.hammers = hammers
    self.pickaxes = pickaxes
    self.inventory = ["-", "-", "-"]
    self.blocks = 0
    self.gold = 0


def display(board, boardrange, players, layer):
  # board is a list of lists containing the environment that the current player can see
  # boardrange is a tuple of the rectangular range of the board that the player can see - i.e., ((-4,-4), (4,4)) for a board whose coordinates in both directions range from -4 to 4
  # players is a list of the active players
  for player in players:
    if boardrange[0][0] <= player.coordinates[0] <= boardrange[1][
        0] and boardrange[0][1] <= player.coordinates[1] <= boardrange[1][1]:
      board[player.coordinates[0] -
            boardrange[0][0]][player.coordinates[1] -
                              boardrange[0][1]] = player.icon
  if layer == 0:
    for row in board:
      print("|" + Back.BLACK + "".join(row) + Back.RESET + "|")
  elif layer == 1:
    for row in board:
      print("|" + Back.LIGHTGREEN_EX + "".join(row) + Back.RESET + "|")


def center_to_range(center, radius):
  return ((center[0] - radius, center[1] - radius), (center[0] + radius,
                                                     center[1] + radius))


def death(p, w):
  clear()
  print(f"({p.coordinates[0]}, {p.coordinates[1] * -1})")
  print("HEALTH: " + heart * p.health + "X " * (p.max_health - p.health))
  print(f"BLOCKS: {p.blocks}  GOLD: {p.gold}")
  print(f"HAMMERS: {p.hammers}  PICKAXES: {p.pickaxes}")
  print("-" * 32)
  display(w.board, center_to_range(p.coordinates, w.radius), [p], p.coordinates[2])
  print("-" * 32)
  print("you died (x_x)")
  input("press enter to respawn")


def game():
  p = Player('ツ', coordinates=[0, 0, 1])
  u = World([stone_floor, wall, spike, ore, chest, merchant, exit],
            [2, 2, 2, 0.1, 0.01, 0.005, 0.001], 5, stone_floor, exit)
  g = World([grass, wall, spike, chest, merchant, mineshaft],
            [20, 5, 1, 0.1, 0.01, 0.01], 7, grass, mineshaft)
  w = g
  
  while True:  #main menu
    clear()
    
    print("welcome to the game!")
    print("press 1 to play")
    print("press 2 to view controls")
    choice = input("")
    if choice == "1":
      break
    elif choice == "2":
      clear()
      print("controls:")
      print("WASD to move")
      print("E to place")
      print("Q to mine")
      print("")
      print("display:")
      print("(x,y) Direction")
      print("blocks  gold")
      print("hammers pickaxes")
      print("")
      input("press enter to go back")

  while True:  #game loop      
    
    clear()
    
    board = w.get_visible_window(p.coordinates[0], p.coordinates[1])

    #prints out the full display
    print(f"({p.coordinates[0]},{p.coordinates[1]*-1}){p.direction}")
    print("HEALTH: " + heart * p.health + "X " * (p.max_health - p.health))
    print(f"BLOCKS: {p.blocks}  GOLD: {p.gold}")
    print(f"HAMMERS: {p.hammers}  PICKAXES: {p.pickaxes}")
    print("-" * (4 * w.radius + 4))
    display(board, center_to_range(p.coordinates, w.radius), [p], p.coordinates[2])
    print("-" * (4 * w.radius + 4))

    time.sleep(0.2)

    with Terminal().cbreak():  #input detection and player movement

      print("")
      move = Terminal().inkey(timeout=60)
      candidate_move = p.coordinates.copy()

      if move == "w":
        p.direction = "N"
        candidate_move[1] -= 1
      elif move == "s":
        p.direction = "S"
        candidate_move[1] += 1
      elif move == "a":
        p.direction = "W"
        candidate_move[0] -= 1
      elif move == "d":
        p.direction = "E"
        candidate_move[0] += 1

      elif move == "e":  #placing
        if p.direction == "N":
          candidate_move[1] -= 1
        elif p.direction == "S":
          candidate_move[1] += 1
        elif p.direction == "W":
          candidate_move[0] -= 1
        elif p.direction == "E":
          candidate_move[0] += 1
        if w.get_board_value(candidate_move) == grass and p.blocks > 0:
          w.set_board_value(candidate_move, placed_wall)
          p.blocks -= 1
        candidate_move = p.coordinates

      elif move == "q":  #breaking
        if p.direction == "N":
          candidate_move[1] -= 1
        elif p.direction == "S":
          candidate_move[1] += 1
        elif p.direction == "W":
          candidate_move[0] -= 1
        elif p.direction == "E":
          candidate_move[0] += 1

        if w.get_board_value(candidate_move) == placed_wall:
          w.set_board_value(candidate_move, w.ground)
          p.blocks += 1

        if w.get_board_value(candidate_move) == wall and p.pickaxes > 0:
          p.pickaxes -= 1
          p.blocks += random.randint(1, 5)
          w.set_board_value(candidate_move, broken_wall)

        if w.get_board_value(candidate_move) == ore and p. pickaxes > 0:
          w.set_board_value(candidate_move, w.ground)
          p.pickaxes -= 1
          p.gold += random.randint(1, 5)

        candidate_move = p.coordinates

      #move validation
      if w.get_board_value(candidate_move) == mineshaft:
        w = u
        candidate_move[0] = round(candidate_move[0] * 0.5)
        candidate_move[1] = round(candidate_move[1] * 0.5)
        candidate_move[2] = 0
        w.set_board_value(candidate_move, exit)
        w.set_board_value([candidate_move[0], candidate_move[1] - 1], stone_floor)

      elif w.get_board_value(candidate_move) == exit:
        w = g
        candidate_move[0] = candidate_move[0] * 2
        candidate_move[1] = candidate_move[1] * 2
        candidate_move[2] = 1
        w.set_board_value(candidate_move, mineshaft)
      
      elif w.get_board_value(candidate_move) == broken_wall:
        w.set_board_value(candidate_move, w.ground)

      elif w.get_board_value(candidate_move) == wall:
        candidate_move = p.coordinates
        print("are you trying to break your skull?")

      elif w.get_board_value(candidate_move) == ore:
        candidate_move = p.coordinates
        w.set_board_value(candidate_move, w.ground)

      elif w.get_board_value(candidate_move) == placed_wall:
        candidate_move = p.coordinates

      elif w.get_board_value(candidate_move) == flat_spike:
        w.set_board_value(candidate_move, w.ground)

      elif w.get_board_value(candidate_move) == spike:
        if p.hammers > 0:
          p.hammers -= 1
          w.set_board_value(candidate_move, flat_spike)
          candidate_move = p.coordinates
        else:
          p.health -= 1

      elif w.get_board_value(candidate_move) == chest:
        chest_loot = random.choices(loot, weights=loot_weights, k=1)
        if chest_loot == ["hammer"]:
          p.hammers += random.randint(1, 3)
        elif chest_loot == ["pickaxe"]:
          p.pickaxes += random.randint(1, 3)
        elif chest_loot == ["block"]:
          p.blocks += random.randint(1, 3)
        elif chest_loot == ["gold"]:
          p.gold += random.randint(1, 5)

        w.set_board_value(candidate_move, looted_chest)

      elif w.get_board_value(candidate_move) == merchant:
        merchant_interaction(p)
        

      p.coordinates = candidate_move

    if p.health == 0:
      death(p, w)
