from grid import MinesweeperGridWidget
import tkinter as tk


WIN_WIDTH = 500


class MainWindow():
    def __init__(self, parent) -> None:
        top_frame = tk.Frame(master=parent, height=50,
                             width=WIN_WIDTH, bg="yellow")
        top_frame.pack(fill=tk.X)

        grid_frame = MinesweeperGridWidget(
            master=parent, height=WIN_WIDTH, bg="red")
        grid_frame.pack(fill=tk.X)

        bottom_frame = tk.Frame(master=parent, height=30, bg="blue")
        bottom_frame.pack(fill=tk.X)


def make_main_window() -> tk.Tk:
    root = tk.Tk()
    root.title("Mfran Minesweeper!")
    MainWindow(root)
    return root


if __name__ == "__main__":
    a = make_main_window()
    a.mainloop()
