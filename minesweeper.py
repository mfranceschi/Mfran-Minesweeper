# ENTRY POINT

from controller.controller import Controller
from game_engine.gridmanager import GridManager
from gui.mainwindow import MainWindow


controller = Controller()
main_window = MainWindow(grid_x=controller.difficulty.grid_x,
                         grid_y=controller.difficulty.grid_y, controller=controller)
main_window.set_grid(controller.grid_manager.get_grid_for_display())
main_window.root.mainloop()
