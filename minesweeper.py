# ENTRY POINT

from controller.controller import Controller
from gui.mainwindow import MainWindow


controller = Controller()
main_window = MainWindow(
    grid_x=controller.difficulty.grid_x,
    grid_y=controller.difficulty.grid_y,
    controller=controller
)
controller.init_gui(main_window)
main_window.root.mainloop()
