from typing import Optional, Dict, Any
from model.config_firebase import FirebaseConfig
from model.tarea import Tarea


class TareaRepository:
    #repo para operaciones de Tarea en Firebase
    def __init__(self):
        self.config = FirebaseConfig.get_instance()
        self.config.initialize()
        self.usuarios_ref = self.config.get_reference("Usuarios")
    
    def agregar_tarea(self, username: str, tarea: Tarea) -> bool:
        try:
            self.usuarios_ref.child(username).child("Tareas").child(tarea.nombre).set(tarea.to_dict())
            return True
        except Exception as e:
            print(f"Error al agregar tarea: {e}")
            return False
    
    def obtener_tareas(self, username: str) -> Optional[Dict]:
        try:
            return self.usuarios_ref.child(username).child("Tareas").get()
        except Exception as e:
            print(f"Error al obtener tareas: {e}")
            return None
    
    def actualizar_nombre_tarea(self, username: str, nombre_antiguo: str, nombre_nuevo: str) -> bool:
        try:
            tarea_data = self.usuarios_ref.child(username).child("Tareas").child(nombre_antiguo).get()
            if tarea_data:
                self.usuarios_ref.child(username).child("Tareas").child(nombre_nuevo).set(tarea_data)
                self.usuarios_ref.child(username).child("Tareas").child(nombre_antiguo).delete()
                return True
            return False
        except Exception as e:
            print(f"Error al actualizar nombre de tarea: {e}")
            return False
    
    def actualizar_campo_tarea(self, username: str, nombre_tarea: str, campo: str, valor: Any) -> bool:
        try:
            self.usuarios_ref.child(username).child("Tareas").child(nombre_tarea).update({campo: valor})
            return True
        except Exception as e:
            print(f"Error al actualizar campo de tarea: {e}")
            return False
    
    def eliminar_tarea(self, username: str, nombre_tarea: str) -> bool:
        try:
            self.usuarios_ref.child(username).child("Tareas").child(nombre_tarea).delete()
            return True
        except Exception as e:
            print(f"Error al eliminar tarea: {e}")
            return False