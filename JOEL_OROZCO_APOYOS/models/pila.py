class PilaApoyos:
    def __init__(self):
        """Inicializa una pila vacía para almacenar apoyos"""
        self.apoyos = []

    def empilar(self, apoyo):
        self.apoyos.append(apoyo)
        return f"Apoyo '{apoyo}' agregado al historial"

    def desempilar(self):
        if self.esta_vacia():
            return "No hay apoyos en el historial"
        return self.apoyos.pop()

    def esta_vacia(self):
        """Verifica si la pila está vacía"""
        return len(self.apoyos) == 0

    def mostrar_pila(self):
        """Retorna la lista de apoyos en la pila"""
        if self.esta_vacia():
            return []
        return self.apoyos.copy()

    def obtener_tamano(self):
        """Retorna el número de elementos en la pila"""
        return len(self.apoyos)

    def eliminar_por_indice(self, indice):
        if 0 <= indice < len(self.apoyos):
            eliminado = self.apoyos.pop(indice)
            return f"Apoyo '{eliminado}' eliminado del historial"
        return "Índice inválido" 