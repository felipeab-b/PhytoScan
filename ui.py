import tkinter as tk
from tkinter import messagebox
from terrain import Terrain
from simulator import Simulator
import json
import os

class Interface:

    def __init__(self, master):
        self.master = master
        self.master.title("Simulador de Crescimento de Raízes")

        self.width = 10
        self.heigth = 10
        self.terrain = Terrain(self.width, self.heigth)
        self.sim = Simulator(self.terrain)

        self.buttons = []
        self.steps_text = tk.Label(master, text = "Passos: 0")
        self.steps_text.pack()

        self.grid_div = tk.Frame(master)
        self.grid_div.pack()

        for y in range(self.heigth):
            line = []
            for x in range(self.width):
                button = tk.Button(self.grid_div, width=3, height=1,
                                   command=lambda x=x,y=y: self.toggle(x,y))
                button.grid(row = y, column = x)
                line.append(button)
            self.buttons.append(line)

        self.refresh()

        button_div = tk.Frame(master)
        button_div.pack(pady=10)

        self.button_step = tk.Button(button_div, text = "Próximo passo", command=self.run_step)
        self.button_step.grid(row=0,column=0,padx=5)

        self.button_save = tk.Button(button_div, text="Salvar em JSON", command=self.save)
        self.button_save.grid(row=0, column=1,padx=5)

        self.button_load = tk.Button(button_div, text="Carregar JSON", command=self.load)
        self.button_load.grid(row=0,column=2,padx=5)

    def toggle(self,x,y):
        element = self.terrain.get_element(x,y)
        from models import FreeSoil, Root, Obstacle

        if isinstance(element, FreeSoil):
            self.terrain.add_root(x,y)
        elif isinstance(element, Root):
            self.terrain.add_obstacle(x,y)
        elif isinstance(element, Obstacle):
            self.terrain._grid[y][x] = FreeSoil(x,y)

        self.refresh()

    def run_step(self):
        grow = self.sim.step()
        self.steps_text.config(text=f"Passos: {self.sim.step}")
        self.refresh()

        if not grow:
            messagebox.showinfo("Fim", "As raízes não podem mais crescer")

    def refresh(self):
        from models import FreeSoil, Root, Obstacle

        for y in range(self.heigth):
            for x in range(self.width):
                element = self.terrain.get_element(x,y)
                color = 'white'
                if isinstance(element, FreeSoil):
                    color = 'lightgreen'
                if isinstance(element, Root):
                    color = 'saddlebrown'
                if isinstance(element, Obstacle):
                    color = 'black'

                self.buttons[y][x].config(bg = color)

    def save(self):
        os.makedirs("data", exist_ok=True)
        self.terrain.to_json("data/state_terrain.json")
        messagebox.showinfo("Salvo","Terreno salvo em state_terrain.json")   

    def load(self):
        self.terrain.load_json("data/state_terrain.json") 
        self.sim = Simulator(self.terrain)

        self.width = self.terrain._width
        self.heigth = self.terrain._height

        for widget in self.grid_div.winfo_children():
            widget.destroy()

        self.buttons = []
        for y in range(self.heigth):
            line = []
            for x in range(self.width):
                button = tk.Button(self.grid_div, width=3, height=1,
                                command=lambda x=x, y=y: self.toggle(x, y))
                button.grid(row=y, column=x)
                line.append(button)
            self.buttons.append(line)

        self.refresh()
        self.steps_text.config(text = "Passos: 0")
        messagebox.showinfo("Carregado","Terreno carregado com sucesso!")
      