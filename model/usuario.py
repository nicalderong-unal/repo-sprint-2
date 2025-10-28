from typing import Dict


class Usuario:
    #modelo de Usuario
    def __init__(self, username: str, password: str = ""):
        self.username = username
        self.password = password
    
    def to_dict(self) -> Dict[str, str]:
        return {"Password: ": self.password}
    
    def __repr__(self):
        return f"Usuario(username='{self.username}')"