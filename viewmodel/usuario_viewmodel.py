from typing import Optional
from model.usuario import Usuario
from repo.repo_usuario import UsuarioRepository


class UsuarioViewModel:
    '''ViewModel para gestión de usuarios'''
    def __init__(self):
        self.repository = UsuarioRepository()
        self.usuario_actual: Optional[str] = None
    
    def crear_usuario(self, username: str, password: str) -> tuple[bool, str]:
        '''Crea un nuevo usuario. Retorna (éxito, mensaje)'''
        if not username or not password:
            return False, "Usuario y contraseña son obligatorios"
        
        usuario = Usuario(username, password)
        if self.repository.crear_usuario(usuario):
            return True, f"Usuario '{username}' creado exitosamente"
        return False, "Error al crear usuario"
    
    def login(self, username: str, password: str) -> tuple[bool, str]:
        '''Intenta iniciar sesión. Retorna (éxito, mensaje)'''
        usuarios = self.repository.obtener_todos_usuarios()
        
        if usuarios is None:
            return False, "No existen usuarios registrados"
        
        if username not in usuarios:
            return False, f"El usuario '{username}' no existe"
        
        if self.repository.validar_credenciales(username, password):
            self.usuario_actual = username
            return True, f"Bienvenido, {username}"
        
        return False, "Contraseña incorrecta"
    
    def obtener_usuario_actual(self) -> Optional[str]:
        return self.usuario_actual