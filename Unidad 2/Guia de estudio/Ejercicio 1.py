class Estudiante:
    def __init__(self, nombre, promedio):
        self.__nombre = nombre
        self.__promedio = promedio
        self.estado = self.__evaluar_estado()

    def __evaluar_estado(self):
        return self.__promedio >= 4.0

    def actualizar_promedio(self, nuevo_promedio):
        if 0.0 <= nuevo_promedio <= 7.0:
            self.__promedio = nuevo_promedio
            self.estado = self.__evaluar_estado()
        else:
            raise ValueError("El promedio debe estar entre 0.0 y 7.0.")

    def __str__(self):
        estado_str = "Aprobado" if self.estado else "Reprobado"
        return f"Estudiante: {self.__nombre}, Promedio: {self.__promedio:.2f}, Estado: {estado_str}"

estudiante1 = Estudiante("Ana", 4.5)
estudiante2 = Estudiante("Luis", 5.8)
estudiante3 = Estudiante("Carla", 7.0)

estudiantes = [estudiante1, estudiante2, estudiante3]

print("Estado inicial de los estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

print("\nActualizando promedios...")
estudiante2.actualizar_promedio(6.5)

print("\nEstado actualizado de los estudiantes:")
for estudiante in estudiantes:
    print(estudiante)
