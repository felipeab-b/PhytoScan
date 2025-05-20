from terrain import Terrain
from simulator import Simulator

t = Terrain(5,5)
t.add_root(2,2)
t.add_obstacle(2,3)

sim = Simulator(t)

for _ in range(3):
    cresceu = sim.step()
    print(f"Passo {sim.steps}: Cresceu? {cresceu}")
    #t.imprimir()