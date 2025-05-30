from models import FreeSoil, Obstacle, Root
from interface import ITerrain
import json
from mixins import SerializableMixin

class Terrain(SerializableMixin, ITerrain):

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._grid = [
            [FreeSoil(x,y) for x in range(width)]
            for y in range(height)
        ]
        self._roots = []

    def get_element(self,x,y):
        return self._grid[y][x]
    
    def add_obstacle(self,x,y):
        self._grid[y][x] = Obstacle(x,y)
    
    def add_root(self,x,y):
        root = Root(x,y)
        self._grid[y][x] = root
        self._roots.append(root)

    def get_root(self):
        return self._roots

    def free_spaces(self,x,y):
        spaces = []
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self._width and 0 <= ny < self._height:
                space = self.get_element(nx,ny)
                if isinstance(space, FreeSoil):
                    spaces.append((nx,ny))
        return spaces
    
    #def imprimir(self):
    #    print("    " + " ".join(f"{x:2}" for x in range(self._largura)))  # Cabeçalho x
    #    for y, linha in enumerate(self._grade):
    #        print(f"{y:2} | " + " ".join([
    #            "R" if isinstance(e, Raiz) else
    #            "X" if isinstance(e, Obstaculo) else
    #            "." for e in linha
    #        ]))
    #    print()
    # Função para debug; ver a grid visualemente no terminal !

    def to_dict(self):
        data = {
            "height": self._height,
            "width": self._width,
            "grid": []
        }

        for line in self._grid:
            serializada = []
            for element in line:
                serializada.append({
                    "type": element.type(),
                    "x": element._x,
                    "y": element._y
                })
            data["grid"].append(serializada)
        return data
    
    def load_json(self,caminho):
        from models import FreeSoil, Obstacle, Root

        with open(caminho, "r") as f:
            data = json.load(f)

        self._height = data["height"]
        self._width = data["width"]
        self._grid = []
        self._roots = []

        for line_json in data["grid"]:
            line = []
            for element_json in line_json:
                type = element_json["type"]
                x = element_json["x"]
                y = element_json["y"]

                if type == "soil":
                    line.append(FreeSoil(x,y))
                elif type == "root":
                    root = Root(x,y)
                    line.append(Root(x,y))
                    self._roots.append(root)
                elif type == "obstacle":
                    line.append(Obstacle(x,y))

            self._grid.append(line)