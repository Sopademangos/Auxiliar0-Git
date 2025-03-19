class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
<<<<<<< HEAD
                print(f"[X] {tarea.obtenerNombre()}" )
                print(f"[ ] {tarea.obtenerNombre()}" )
=======
                print(f"La tarea {tarea.obtenerNombre()} está lista")
>>>>>>> 84e20d8b91c03c5216d462520f0528af9d43f8e7
