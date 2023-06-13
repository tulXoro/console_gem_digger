from replit import clear
from readchar import readkey, key
from time import sleep

from gem_board import *

# Board Vars
ROWS = 10
COL = 10

cursor = "⛏️ "
cursor2= ""

posX = 0
posY = 0

# Gameplay vars
health = 100
tool = 1
maxTool = 4

def displayHUD():
  bar = ""
  for i in range(int(health/10)):
    bar+="🟥"
  for i in range(10 - len(bar)):
    bar+="⬜"
  print("INTEGRETY:\n", bar)
  print("TOOL POWER:", tool)

def handle_key():
  global posX, posY, cursor2, tool, health
  # Read Keys
  k = readkey()
  board[posY][posX] = cursor2
  if k == key.SPACE:
    tool = (tool+1) % maxTool
  elif k == key.UP and posY > 0:
    posY -= 1
  elif k == key.DOWN and posY < ROWS-1:
    posY += 1
  elif k == key.RIGHT and posX < COL-1:
    posX += 1
  elif k == key.LEFT and posX > 0:
    posX -= 1
  elif k == '0':
    tool = 0
  elif k == '1':
    tool = 1
  elif k == '2':
    tool = 2
  elif k == '3':
    tool = 3
  elif k == key.ENTER:
    clearX(tool, posX, posY)
    clearY(tool, posX, posY)

    health = health - random.randint(tool+5, 2*(tool+3))
    
    clear()
    displayHUD()
    displayBoard()
    sleep(0.5)
    
  cursor2 = board[posY][posX]
  board[posY][posX] = cursor

if __name__ == "__main__":
  initBoard(COL,ROWS)
  cursor2 = board[posY][posX]
  board[posY][posX] = cursor
  
  while True:
    clear()
    if health <= 0:
      print("GAME OVER!")
      displayBoard()
      break
    displayHUD()
    displayBoard()

    print("Use Arrow keys to move.")
    print("Press 0, 1, 2, 3, or SPACE to cycle tool..")
    print("Press ENTER to hit the rock!")

    handle_key()
    

  
    
