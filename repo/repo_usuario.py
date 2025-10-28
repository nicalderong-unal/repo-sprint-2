from typing import Optional, Dict
from model.config_firebase import FirebaseConfig
from model.usuario import Usuario


class UsuarioRepository:
    '''Repositorio para operaciones de Usuario en Firebase'''
    def __init__(self):
        self.config = FirebaseConfig.get_instance()
        self.config.initialize()
        self.ref = self.config.get_reference("Usuarios")
    
    def crear_usuario(self, usuario: Usuario) -> bool:
        try:
            self.ref.child(usuario.username).set(usuario.to_dict())
            return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False
    
    def obtener_usuario(self, username: str) -> Optional[Dict]:
        try:
            return self.ref.child(username).get()
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            return None
    
    def obtener_todos_usuarios(self) -> Optional[Dict]:
        try:
            return self.ref.get()
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return None
    
    def validar_credenciales(self, username: str, password: str) -> bool:
        usuario_data = self.obtener_usuario(username)
        if usuario_data and "Password: " in usuario_data:
            return password in usuario_data["Password: "]
        return False