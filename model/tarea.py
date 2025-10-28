from typing import Dict, Any


class Tarea:
    '''Modelo de Tarea'''
    def __init__(self, nombre: str, importancia: int, categoria: int, 
                 tiempo: int, estado: bool = False):
        self.nombre = nombre
        self.importancia = importancia
        self.categoria = categoria
        self.tiempo = tiempo
        self.estado = estado
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "importancia de la Tarea": self.importancia,
            "Categoria": self.categoria,
            "Tiempo": self.tiempo,
            "Estado": self.estado
        }
    
    @staticmethod
    def from_dict(nombre: str, data: Dict[str, Any]) -> 'Tarea':
        return Tarea(
            nombre=nombre,
            importancia=data.get("importancia de la Tarea", 1),
            categoria=data.get("Categoria", 1),
            tiempo=data.get("Tiempo", 1),
            estado=data.get("Estado", False)
        )
    
    def __repr__(self):
        return f"Tarea(nombre='{self.nombre}', importancia={self.importancia}, estado={self.estado})"