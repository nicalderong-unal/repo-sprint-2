from typing import Optional, Dict
from viewmodel.usuario_viewmodel import UsuarioViewModel
from viewmodel.tarea_viewmodel import TareaViewModel


class ConsoleView:
    '''Vista de consola para interactuar con el usuario'''
    def __init__(self):
        self.usuario_vm = UsuarioViewModel()
        self.tarea_vm = TareaViewModel()
    
    def mostrar_mensaje(self, mensaje: str):
        '''Muestra un mensaje en consola'''
        print(mensaje)
    
    def solicitar_input(self, prompt: str) -> str:
        '''Solicita entrada del usuario'''
        return input(prompt)
    
    def solicitar_input_int(self, prompt: str) -> int:
        '''Solicita entrada numérica del usuario'''
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Por favor ingrese un número válido")
    
    def crear_usuario(self):
        '''Flujo para crear un nuevo usuario'''
        username = self.solicitar_input("Crea el nombre de tu nueva cuenta: ")
        password = self.solicitar_input("Crea una contraseña para tu nueva cuenta: ")
        
        exito, mensaje = self.usuario_vm.crear_usuario(username, password)
        self.mostrar_mensaje(mensaje)
        return exito
    
    def login(self) -> bool:
        '''Flujo de inicio de sesión'''
        username = self.solicitar_input("Ingrese su usuario: ")
        password = self.solicitar_input("Ingrese su contraseña: ")
        
        exito, mensaje = self.usuario_vm.login(username, password)
        self.mostrar_mensaje(mensaje)
        
        if not exito and "incorrecta" in mensaje:
            intentos = 3
            while intentos > 0:
                password = self.solicitar_input("Contraseña incorrecta, intente nuevamente: ")
                exito, mensaje = self.usuario_vm.login(username, password)
                if exito:
                    self.mostrar_mensaje(mensaje)
                    break
                intentos -= 1
        
        return exito
    
    def agregar_tarea(self):
        '''Flujo para agregar una nueva tarea'''
        username = self.usuario_vm.obtener_usuario_actual()
        if not username:
            self.mostrar_mensaje("Debe iniciar sesión primero")
            return
        
        nombre = self.solicitar_input("Ingrese el nombre de su nueva tarea: ")
        
        importancia = self.solicitar_input_int(
            "Ingrese un valor del 1 al 3 para establecer la importancia de la tarea (1 mínima, 2 medio, 3 máxima): "
        )
        while not self.tarea_vm.validar_importancia(importancia):
            importancia = self.solicitar_input_int("Nivel de importancia incoherente (rango de 1 a 3): ")
        
        categoria = self.solicitar_input_int(
            "Ingrese un valor del 1 al 3 para establecer la categoría de la tarea (1 personal, 2 estudios, 3 trabajo): "
        )
        while not self.tarea_vm.validar_categoria(categoria):
            categoria = self.solicitar_input_int("Categoría inválida (rango de 1 a 3): ")
        
        tiempo = self.solicitar_input_int("¿Cuál es el tiempo límite de tu tarea (En días)?: ")
        while not self.tarea_vm.validar_tiempo(tiempo):
            tiempo = self.solicitar_input_int("Ingrese números mayores a 0: ")
        
        exito, mensaje = self.tarea_vm.agregar_tarea(username, nombre, importancia, categoria, tiempo)
        self.mostrar_mensaje(mensaje)
    
    def actualizar_tarea(self):
        '''Flujo para actualizar una tarea'''
        username = self.usuario_vm.obtener_usuario_actual()
        if not username:
            self.mostrar_mensaje("Debe iniciar sesión primero")
            return
        
        nombre_tarea = self.solicitar_input("Ingrese el nombre de la tarea: ")
        
        self.mostrar_mensaje("\\nEditor de tarea:")
        self.mostrar_mensaje("1: Nombre")
        self.mostrar_mensaje("2: Importancia")
        self.mostrar_mensaje("3: Categoría")
        self.mostrar_mensaje("4: Tiempo")
        self.mostrar_mensaje("5: Estado")
        
        opcion = self.solicitar_input_int("Seleccione una opción: ")
        
        if opcion == 1:
            nombre_nuevo = self.solicitar_input("Ingrese el nuevo nombre de la tarea: ")
            exito, mensaje = self.tarea_vm.actualizar_nombre_tarea(username, nombre_tarea, nombre_nuevo)
            self.mostrar_mensaje(mensaje)
        
        elif opcion == 2:
            importancia = self.solicitar_input_int("Ingrese un valor del 1 al 3 para la importancia: ")
            while not self.tarea_vm.validar_importancia(importancia):
                importancia = self.solicitar_input_int("Nivel de importancia incoherente (rango de 1 a 3): ")
            exito, mensaje = self.tarea_vm.actualizar_importancia(username, nombre_tarea, importancia)
            self.mostrar_mensaje(mensaje)
        
        elif opcion == 3:
            categoria = self.solicitar_input_int("Ingrese un valor del 1 al 3 para la categoría: ")
            while not self.tarea_vm.validar_categoria(categoria):
                categoria = self.solicitar_input_int("Categoría inválida (rango de 1 a 3): ")
            exito, mensaje = self.tarea_vm.actualizar_categoria(username, nombre_tarea, categoria)
            self.mostrar_mensaje(mensaje)
        
        elif opcion == 4:
            tiempo = self.solicitar_input_int("¿Cuál es el nuevo tiempo límite (En días)?: ")
            while not self.tarea_vm.validar_tiempo(tiempo):
                tiempo = self.solicitar_input_int("Ingrese números mayores a 0: ")
            exito, mensaje = self.tarea_vm.actualizar_tiempo(username, nombre_tarea, tiempo)
            self.mostrar_mensaje(mensaje)
        
        elif opcion == 5:
            exito, mensaje = self.tarea_vm.marcar_completada(username, nombre_tarea)
            self.mostrar_mensaje(mensaje)
        
        else:
            self.mostrar_mensaje("Opción no válida")
    
    def eliminar_tarea(self):
        '''Flujo para eliminar una tarea'''
        username = self.usuario_vm.obtener_usuario_actual()
        if not username:
            self.mostrar_mensaje("Debe iniciar sesión primero")
            return
        
        nombre_tarea = self.solicitar_input("Ingrese el nombre de la tarea: ")
        exito, mensaje = self.tarea_vm.eliminar_tarea(username, nombre_tarea)
        self.mostrar_mensaje(mensaje)
    
    def leer_tareas(self):
        '''Flujo para listar todas las tareas'''
        username = self.usuario_vm.obtener_usuario_actual()
        if not username:
            self.mostrar_mensaje("Debe iniciar sesión primero")
            return
        
        tareas = self.tarea_vm.obtener_tareas(username)
        
        if tareas:
            self.mostrar_mensaje("\\n=== TAREAS ===")
            for nombre, datos in tareas.items():
                self.mostrar_mensaje(f"\\nTarea: {nombre}")
                self.mostrar_mensaje(f"  Importancia: {datos.get('importancia de la Tarea', 'N/A')}")
                self.mostrar_mensaje(f"  Categoría: {datos.get('Categoria', 'N/A')}")
                self.mostrar_mensaje(f"  Tiempo: {datos.get('Tiempo', 'N/A')} días")
                self.mostrar_mensaje(f"  Estado: {'Completada' if datos.get('Estado', False) else 'Pendiente'}")
        else:
            self.mostrar_mensaje("No hay tareas registradas.")
    
    def marcar_completada(self):
        '''Flujo para marcar una tarea como completada'''
        username = self.usuario_vm.obtener_usuario_actual()
        if not username:
            self.mostrar_mensaje("Debe iniciar sesión primero")
            return
        
        nombre_tarea = self.solicitar_input("Ingrese el nombre de la tarea: ")
        exito, mensaje = self.tarea_vm.marcar_completada(username, nombre_tarea)
        self.mostrar_mensaje(mensaje)
    
    def menu_principal(self):
        '''Menú principal de la aplicación'''
        while True:
            self.mostrar_mensaje("\\n=== GESTOR DE TAREAS ===")
            self.mostrar_mensaje("1. Crear usuario")
            self.mostrar_mensaje("2. Iniciar sesión")
            self.mostrar_mensaje("3. Agregar tarea")
            self.mostrar_mensaje("4. Actualizar tarea")
            self.mostrar_mensaje("5. Eliminar tarea")
            self.mostrar_mensaje("6. Ver tareas")
            self.mostrar_mensaje("7. Marcar tarea como completada")
            self.mostrar_mensaje("8. Salir")
            
            opcion = self.solicitar_input_int("\\nSeleccione una opción: ")
            
            if opcion == 1:
                self.crear_usuario()
            elif opcion == 2:
                self.login()
            elif opcion == 3:
                self.agregar_tarea()
            elif opcion == 4:
                self.actualizar_tarea()
            elif opcion == 5:
                self.eliminar_tarea()
            elif opcion == 6:
                self.leer_tareas()
            elif opcion == 7:
                self.marcar_completada()
            elif opcion == 8:
                self.mostrar_mensaje("¡Hasta luego!")
                break
            else:
                self.mostrar_mensaje("Opción no válida")