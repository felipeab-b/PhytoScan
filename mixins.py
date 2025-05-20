import json

class SerializableMixin:

    def to_dict(self):
        raise NotImplementedError("Subclasse deve implementar to_dict()")
    
    def to_json(self, caminho):
        with open(caminho, "w") as f:
            json.dump(self.to_dict(), f, indent=4)