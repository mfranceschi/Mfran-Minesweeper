# ENTRY POINT

from controller.controller_impl import ControllerImpl
from view.gui_impl import GUIImpl


controller = ControllerImpl()
gui = GUIImpl(
    grid_x=controller.difficulty.grid_x,
    grid_y=controller.difficulty.grid_y,
    controller=controller
)
controller.init_gui(gui)
gui.root.mainloop()
