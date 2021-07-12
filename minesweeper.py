# ENTRY POINT

from game_engine.gridmanager import GridManager
from gui.mainwindow import MainWindow


GRID_X = 10
GRID_Y = 20
main_window = MainWindow(grid_x=GRID_X, grid_y=GRID_Y)
game_engine = GridManager(grid_x=GRID_X, grid_y=GRID_Y)
main_window.game_engine = game_engine
main_window.set_grid(game_engine.get_grid_for_display())
main_window.root.mainloop()
