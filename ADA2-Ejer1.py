class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, valor):
        self.elementos.append(valor)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamano(self):
        return len(self.elementos)

    def mostrar_cola(self):
        return self.elementos 

def combinar_colas(cola1, cola2):
    cola_resultado = Cola()

    while not cola1.esta_vacia() and not cola2.esta_vacia():
        valor1 = cola1.desencolar()
        valor2 = cola2.desencolar()
        suma = valor1 + valor2
        cola_resultado.encolar(suma)

    return cola_resultado

cola_a = Cola()
cola_b = Cola()

cola_a.encolar(3)
cola_a.encolar(4)
cola_a.encolar(2)
cola_a.encolar(8)
cola_a.encolar(12)

cola_b.encolar(6)
cola_b.encolar(2)
cola_b.encolar(9)
cola_b.encolar(11)
cola_b.encolar(3)

print("Cola A antes de la combinación:", cola_a.mostrar_cola())
print("Cola B antes de la combinación:", cola_b.mostrar_cola())

cola_resultado = combinar_colas(cola_a, cola_b)

print("Cola A después de la combinación:", cola_a.mostrar_cola())
print("Cola B después de la combinación:", cola_b.mostrar_cola())

print("Elementos de la Cola Resultado:")
while not cola_resultado.esta_vacia():
    print(cola_resultado.desencolar())
