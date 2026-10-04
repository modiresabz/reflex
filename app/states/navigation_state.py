import reflex as rx


class NavigationState(rx.State):
    menu_open: bool = False

    @rx.event
    def toggle_menu(self):
        self.menu_open = not self.menu_open

    @rx.event
    def close_menu(self):
        self.menu_open = False
