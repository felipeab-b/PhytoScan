from terrain import Terrain

t = Terrain(5,5)
t.add_root(2,2)
t.add_obstacle(2,3)

print("Vizinhos livres da raiz:")
print(t.free_spaces(2, 2))