class ColaTarjetas:
    def __init__(self):
        """Inicializa una cola vacía para almacenar tarjetas de apoyo"""
        self.tarjetas = []

    def encolar(self, persona):
        self.tarjetas.append(persona)
        return f"Persona '{persona}' agregada a la cola"

    def desencolar(self):
        if self.esta_vacia():
            return "No hay personas en la cola"
        return self.tarjetas.pop(0)

    def esta_vacia(self):
        """Verifica si la cola está vacía"""
        return len(self.tarjetas) == 0

    def mostrar_cola(self):
        """Retorna la lista de personas en la cola"""
        if self.esta_vacia():
            return []
        return self.tarjetas.copy()

    def obtener_tamano(self):
        """Retorna el número de elementos en la cola"""
        return len(self.tarjetas)

    def eliminar_por_indice(self, indice):
        if 0 <= indice < len(self.tarjetas):
            eliminado = self.tarjetas.pop(indice)
            return f"Persona '{eliminado}' eliminada de la cola"
        return "Índice inválido" 