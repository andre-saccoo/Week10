import flet as ft
import model

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    # dice al model di creare il grafo
    def handleCreaGrafo(self,e):
        self._model.creaGrafo()

    def handleCercaRaggiungibili(self,e):
        pass

    #dobbiamo chiedere al model di passarci le fermate
    def populate_dropdown(self,dd):
        self._model.getAllFermate()
        #le fermate sono nel model in lista fermate
        for fermata in self._model._lista_fermate:
            dd.options.append(ft.dropdown.Option(key=fermata.id_fermata,text=fermata.nome))
            #quando l'utente usa l'interfaccia vede i nomi, ma nel programma gira l'id
