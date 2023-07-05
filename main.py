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

mined_gems = 0

def displayHUD():
  bar = ""
  for i in range(int(health/10)):
    bar+="🟥"
  for i in range(10 - len(bar)):
    bar+="⬜"
  print("INTEGRETY:\n", bar)
  print("TOOL POWER:", tool)

def handle_key():
  global posX, posY, cursor2, tool, health, mined_gems, board
  # Read Keys
  dead = 0
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
    

    if tool == 0 or tool == 1:
      res = 0
      res2 = 0
      res, res2 = clearX(tool, posX, posY)
      mined_gems += res
      dead += res2
      res, res2 = clearY(tool, posX, posY)
      mined_gems += res
      dead += res2
    elif tool==2:
      minX = posX-tool+1
      maxX = posX+tool
      minY = posY-tool+1
      maxY = posY+tool
      
      maxX = len(board) if maxX > len(board) else maxX
      minX = 0 if minX < 0 else minX
      maxY = len(board) if maxY > len(board) else maxY
      minY = 0 if minY < 0 else minY
      
      for i in range(minY, maxY):
        for j in range(minX, maxX):
          board[i][j] = board_a[i][j]
          if board_a[i][j] == "💣":
            dead += 1
          if board_a[i][j] == gem: 
            mined_gems += 1
    else:
      tool=2
      minX = posX-tool+1
      maxX = posX+tool
      minY = posY-tool+1
      maxY = posY+tool
      
      maxX = len(board) if maxX > len(board) else maxX
      minX = 0 if minX < 0 else minX
      maxY = len(board) if maxY > len(board) else maxY
      minY = 0 if minY < 0 else minY
      
      for i in range(minY, maxY):
        for j in range(minX, maxX):
          if posX != j and posY != i:
            board[i][j] = board_a[i][j]
            if board_a[i][j] == "💣":
              dead += 1
            if board_a[i][j] == "💎": 
              mined_gems += 1
      res = 0
      res2 = 0
      res, res2 = clearX(2, posX, posY)
      mined_gems += res
      dead += res2
      res, res2 = clearY(2, posX, posY)
      mined_gems += res
      dead += res2
  
      
      tool=3
      
    health = health - random.randint(10*tool, 15*(tool))
    if dead > 0:
      health -= 100
    clear()
    displayHUD()
    displayBoard()
    sleep(0.5)
    
  cursor2 = board[posY][posX]
  board[posY][posX] = cursor

bomb_cnt = 0

if __name__ == "__main__":
  bomb_cnt = initBoard(COL,ROWS)
  cursor2 = board[posY][posX]
  board[posY][posX] = cursor
  
  while True:
    clear()
    if health <= 0:
      print("GAME OVER!")
      
      board[posY][posX] = cursor2
      displayBoard()
      break
    displayHUD()
    displayBoard()
    
    print("You have mined", mined_gems, "!")
    print("There are", bomb_cnt, "bombs")
    print("Use Arrow keys to move.")
    print("Press 0, 1, 2, 3, or SPACE to cycle tool..")
    print("Press ENTER to hit the rock!")

    handle_key()

print("You mined", mined_gems)

  
    
