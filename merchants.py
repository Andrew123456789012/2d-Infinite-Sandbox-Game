from replit import clear
from colorama import Fore

class Item:
  def __init__(self, name, number):
    self.name = name
    self.number = number


def purchase(player, inv):
  while True:
    clear()
    print(f"{Fore.BLUE}you have encountered a merchant table!")
    print(f"you have {player.gold} gold.")
    print("what would you like to buy?")
    print("1. hammer (2 gold)      --█")
    print("2. pickaxe (3 gold)     --)")
    print("3. block (1 gold)        X")
    print("4. heart (10 gold)       ♡")
    print("5. heart slot (20 gold)  ♡")
    print("6. house (50 gold)       ♜")
    print("7. shovel (3 gold)      --⊃")
    print("8. exit                  ⏎")
    choice = input("enter your choice: ")

    if choice == "1" and player.gold > 1:
      player.hammers += 1
      player.gold -= 2
      print("you bought a hammer!")
    elif choice == "2" and player.gold > 2:
      player.pickaxes += 1
      player.gold -= 3
      print("you bought a pickaxe!")
    elif choice == "3" and player.gold > 0:
      inv.add_item(Item("X-BLOCK", 1))
      player.gold -= 1
      print("you bought a block!")
    elif choice == "4" and player.gold > 9 and player.health < 3:
      player.health += 1
      player.gold -= 10
      print("you bought a heart!")
    elif choice == "5" and player.gold > 19 and player.max_health <10:
      player.max_health += 1
      player.health = player.max_health
      player.gold -= 20
      print("you bought a heart slot!")
    elif choice == "6" and player.gold > 49:
      player.gold -= 50
      inv.add_item(Item("HOUSE", 1))
      print("you bought a house!")
    elif choice == "7" and player.gold > 2:
      player.shovels += 1
      player.gold -= 3
      print("you bought a shovel!")
    elif choice == "8":
      print("you exit the merchant.")
      break
    else:
      print("invalid choice or not enough gold.")
    input("press enter to continue.")
  print(Fore.WHITE)

def merchant(player, inv):
  purchase(player, inv)

