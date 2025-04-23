from window import Window
from maze import Maze
def main():
    win = Window(800,600)
    m1 = Maze(50,2, 10, 10, 25, 25, win,"42069")
    m1.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()