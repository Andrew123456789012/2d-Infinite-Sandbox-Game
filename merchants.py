from replit import clear
from colorama import Fore

class Item:
  def __init__(self, name, number, value):
    self.name = name
    self.number = number
    self.value = value


def sale(player, inv):
  valid = ["1", "2", "3", "4", "5"]
  while True:
    clear()
    print("what would you like to sell")
    print("name : number : value")
    print(f"1. {inv._bag[0].name} : {inv._bag[0].number} : {inv._bag[0].value}")
    print(f"2. {inv._bag[1].name} : {inv._bag[1].number} : {inv._bag[1].value}")
    print(f"3. {inv._bag[2].name} : {inv._bag[2].number} : {inv._bag[2].value}")
    print(f"4. {inv._bag[3].name} : {inv._bag[3].number} : {inv._bag[3].value}")
    print(f"5. {inv._bag[4].name} : {inv._bag[4].number} : {inv._bag[4].value}")
    print("6. exit")
    choice = input("enter your choice: ")

    if choice == "6":
      break
    if choice in valid:
      choice = int(choice)
      if inv._bag[choice - 1].number == 0:
        print("you don't have any of that")
      if inv._bag[choice - 1].name is not None:
        print(f"you sold a {inv._bag[choice - 1].name}")
        print(f"you got {inv._bag[choice - 1].value} gold")
        player.gold += inv._bag[choice - 1].value
        inv.remove_item(choice - 1)
    else:
      print("invalid choice")
      
    input("press enter to continue")

def purchase(player, inv):
  while True:
    clear()
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
  print(f"{Fore.BLUE}you have encountered a merchant table!")
  while True:
    clear()
    print("what would you like")
    print("1. buy")
    print("2. sell")
    print("3. exit")
    choice = input("enter your choice: ")
    if choice == "1":
      purchase(player, inv)
    if choice == "2":
      sale(player, inv)
    if choice == "3":
      break
    else:
      print("invalid choice")

