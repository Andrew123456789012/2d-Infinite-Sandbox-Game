from replit import clear
from colorama import Fore

def menu():
  while True:
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
      print("Q to mine")
      print("E to interact")
      print("12345 to place blocks")
      print("")
      print("display:")
      print("(x,y)  Direction")
      print("gold")
      print("health")
      print("tools")
      print("")
      input("press enter to go back ⏎")
