import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analisi(self, e):
        calorie = self._view.txt_calorie.value
        if calorie is None:
            self._view.create_alert("Inserire un valore numerico per le calorie")
            return
        grafo = self._model.creaGrafo( int(calorie))
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        for nodo in grafo.nodes():
            self._view.dd_tipo.options.append(ft.dropdown.Option(
                text=nodo))
        self._view.update_page()


    def handle_correlate(self, e):
        tipo = self._view.dd_tipo.value
        if tipo is None:
            self._view.create_alert("Selezionare un tipo")
            return
        analisi=self._model.getAnalisi(tipo)
        for (nodo,peso) in analisi:
            self._view.txt_result.controls.append(ft.Text(f"{nodo} con peso={peso}"))
        self._view.update_page()

