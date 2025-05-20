class TerrainElements:
    #Classe base de todas as coisas que ocupam alguma posição no terreno
    
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def get_position(self):
        return self._x, self._y
    
    def comportament(self):
        raise NotImplementedError("Método deve ser implementado em uma subclasse")
    
    def type(self):
        raise NotImplementedError("Método deve ser implementado em uma subclasse")
    
    def __str__(self):
        return f"{self.__class__.__name__} em ({self._x}, {self._y})"
    
class FreeSoil(TerrainElements):

    def comportament(self):
        return "Pode crescer raiz aqui"
    
    def type(self):
        return "soil"
    
class Obstacle(TerrainElements):

    def comportament(self):
        return "Não pode crescer raiz"
    
    def type(self):
        return "obstacle"
    
class Root(TerrainElements):
    
    def comportament(self):
        return "Raiz crescendo"
    
    def type(self):
        return "root"