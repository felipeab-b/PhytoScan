import tkinter as tk
from tkinter import messagebox
from terrain import Terrain
from simulator import Simulator
import json

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
        data = self.terrain.serializar()
        with open("state_terrain.json", "w") as f:
            json.dump(data, f, indent=4)
        messagebox.showinfo("Salvo","Terreno salvo em state_terrain.json")    
      