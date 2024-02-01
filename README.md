# Description
This is a simple application that mimicks a typing test in most websites. I built this to primarily help children and teens learn about the fundamentals of programming.

# Usage
You may use this project however you see fit.

# How to start
Ensure you have [Python](https://www.python.org/downloads/) installed and optionally use an IDE. If you do not have the right version of Python, you should upgrade/downgrade as necessary.
Clone the repository with `git clone <url>`.
Install the necessary dependencies `pip install .`. 
Run the game with `python3 main.py`. 

# How to play
Use `WASD` to move your cursor. Avoid any bombs, and mine as many diamonds as possible. Use the number keys `123` to change the *strength* of your power.

# How it works
It uses 2 2D lists - 1 for the display and the other for everything *under* the display. After, mining a spot will reveal the object under it.
