from typing import Optional, Dict
from model.tarea import Tarea
from repo.repo_tarea import TareaRepository


class TareaViewModel:
    '''ViewModel para gestión de tareas'''
    def __init__(self):
        self.repository = TareaRepository()
    
    def validar_importancia(self, importancia: int) -> bool:
        '''Valida que la importancia esté en el rango correcto'''
        return importancia in [1, 2, 3]
    
    def validar_categoria(self, categoria: int) -> bool:
        '''Valida que la categoría esté en el rango correcto'''
        return categoria in [1, 2, 3]
    
    def validar_tiempo(self, tiempo: int) -> bool:
        '''Valida que el tiempo sea positivo'''
        return tiempo > 0
    
    def agregar_tarea(self, username: str, nombre: str, importancia: int, 
                      categoria: int, tiempo: int) -> tuple[bool, str]:
        '''Agrega una nueva tarea. Retorna (éxito, mensaje)'''
        if not self.validar_importancia(importancia):
            return False, "Importancia debe ser 1, 2 o 3"
        
        if not self.validar_categoria(categoria):
            return False, "Categoría debe ser 1, 2 o 3"
        
        if not self.validar_tiempo(tiempo):
            return False, "El tiempo debe ser mayor a 0"
        
        tarea = Tarea(nombre, importancia, categoria, tiempo)
        if self.repository.agregar_tarea(username, tarea):
            return True, f"Tarea '{nombre}' agregada exitosamente"
        return False, "Error al agregar tarea"
    
    def actualizar_nombre_tarea(self, username: str, nombre_antiguo: str, 
                                nombre_nuevo: str) -> tuple[bool, str]:
        '''Actualiza el nombre de una tarea. Retorna (éxito, mensaje)'''
        if self.repository.actualizar_nombre_tarea(username, nombre_antiguo, nombre_nuevo):
            return True, f"Tarea renombrada de '{nombre_antiguo}' a '{nombre_nuevo}'"
        return False, "Error al actualizar nombre de tarea"
    
    def actualizar_importancia(self, username: str, nombre_tarea: str, 
                               importancia: int) -> tuple[bool, str]:
        '''Actualiza la importancia de una tarea. Retorna (éxito, mensaje)'''
        if not self.validar_importancia(importancia):
            return False, "Importancia debe ser 1, 2 o 3"
        
        if self.repository.actualizar_campo_tarea(username, nombre_tarea, 
                                                   "importancia de la Tarea", importancia):
            return True, f"Importancia de '{nombre_tarea}' actualizada"
        return False, "Error al actualizar importancia"
    
    def actualizar_categoria(self, username: str, nombre_tarea: str, 
                            categoria: int) -> tuple[bool, str]:
        '''Actualiza la categoría de una tarea. Retorna (éxito, mensaje)'''
        if not self.validar_categoria(categoria):
            return False, "Categoría debe ser 1, 2 o 3"
        
        if self.repository.actualizar_campo_tarea(username, nombre_tarea, 
                                                   "Categoria", categoria):
            return True, f"Categoría de '{nombre_tarea}' actualizada"
        return False, "Error al actualizar categoría"
    
    def actualizar_tiempo(self, username: str, nombre_tarea: str, 
                         tiempo: int) -> tuple[bool, str]:
        '''Actualiza el tiempo de una tarea. Retorna (éxito, mensaje)'''
        if not self.validar_tiempo(tiempo):
            return False, "El tiempo debe ser mayor a 0"
        
        if self.repository.actualizar_campo_tarea(username, nombre_tarea, 
                                                   "Tiempo", tiempo):
            return True, f"Tiempo de '{nombre_tarea}' actualizado"
        return False, "Error al actualizar tiempo"
    
    def marcar_completada(self, username: str, nombre_tarea: str) -> tuple[bool, str]:
        '''Marca una tarea como completada. Retorna (éxito, mensaje)'''
        if self.repository.actualizar_campo_tarea(username, nombre_tarea, "Estado", True):
            return True, f"Tarea '{nombre_tarea}' marcada como completada"
        return False, "Error al marcar tarea como completada"
    
    def eliminar_tarea(self, username: str, nombre_tarea: str) -> tuple[bool, str]:
        '''Elimina una tarea. Retorna (éxito, mensaje)'''
        if self.repository.eliminar_tarea(username, nombre_tarea):
            return True, f"Tarea '{nombre_tarea}' eliminada exitosamente"
        return False, "Error al eliminar tarea"
    
    def obtener_tareas(self, username: str) -> Optional[Dict]:
        '''Obtiene todas las tareas de un usuario'''
        return self.repository.obtener_tareas(username)