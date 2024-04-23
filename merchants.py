from replit import clear
from colorama import Fore


def merchant_interaction(player):
  while True:
    clear()
    print(f"{Fore.BLUE}you have encountered a merchant table!")
    print(f"you have {player.gold} gold.")
    print("what would you like to buy?")
    print("1. hammer (2 gold)")
    print("2. pickaxe (3 gold)")
    print("3. block (1 gold)")
    print("4. heart (10 gold)")
    print("5. heart slot (20 gold)")
    print("6. exit")
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
      player.blocks += 1
      player.gold -= 1
      print("you bought a block!")
    elif choice == "4" and player.gold > 9 and player.health < 3:
      player.health += 1
      player.gold -= 10
      print("you bought a heart!")
    elif choice == "5" and player.gold > 19:
      player.max_health += 1
      player.health = player.max_health
      player.gold -= 20
      print("you bought a heart slot!")
    elif choice == "6":
      print("you exit the merchant.")
      break
    else:
      print("invalid choice or not enough gold.")
      input("press enter to continue.")
  print({Fore.WHITE})
