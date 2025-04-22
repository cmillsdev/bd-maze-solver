from window import Window
from maze import Maze
def main():
    win = Window(800,600)
    m1 = Maze(2,2, 10, 10, 20,20,win,"42069")
    win.wait_for_close()


if __name__ == "__main__":
    main()