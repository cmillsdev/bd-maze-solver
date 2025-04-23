from window import Window
from maze import Maze
def main():
    win = Window(1000,800)
    m1 = Maze(50,2, 10, 10, 25, 25, win)
    m1.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()