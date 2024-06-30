import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("03/09/2019", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_calorie = ft.TextField(
            label="Calorie",
            width=200,

        )
        self.dd_tipo=ft.Dropdown(label="Tipo di Porzione")
        self.txt_passi= ft.TextField(
            label="Passi",
            width=200,

        )

        # button for the "hello" reply
        self.btn_analisi = ft.ElevatedButton(text="Analisi", on_click=self._controller.handle_analisi)
        self.btn_cammino = ft.ElevatedButton(text="Cammino", on_click=self._controller.handle_cerca)
        self.btn_correlate= ft.ElevatedButton(text="Correlate", on_click=self._controller.handle_correlate)
        row1 = ft.Row([self.txt_calorie,self.dd_tipo, self.btn_analisi, self.btn_correlate],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        row2 = ft.Row([self.txt_passi, self.btn_cammino],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
