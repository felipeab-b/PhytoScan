from models import FreeSoil, Obstacle, Root

class Terrain:

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