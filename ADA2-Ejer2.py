class Cola:
    def __init__(self):
        self.clientes = []

    def agregar(self, cliente):
        self.clientes.append(cliente)

    def atender(self):
        return self.clientes.pop(0) if self.clientes else None

    def estado(self):
        return self.clientes

class SistemaSeguros:
    def __init__(self):
        self.colas = {}

    def llegada_cliente(self, servicio):
        if servicio not in self.colas:
            self.colas[servicio] = Cola()
        numero = f"{servicio}-{len(self.colas[servicio].clientes) + 1}"
        self.colas[servicio].agregar(numero)
        print(f"Cliente agregado: {numero}")

    def atender_cliente(self, servicio):
        if servicio in self.colas:
            cliente_atendido = self.colas[servicio].atender()
            if cliente_atendido:
                print(f"Atendiendo a: {cliente_atendido}")
            else:
                print("No hay clientes en espera.")
            self.mostrar_estado(servicio)
        else:
            print(f"No existe la cola del servicio {servicio}.")

    def mostrar_estado(self, servicio=None):
        print("Estado de las colas:")
        if servicio:
            if servicio in self.colas:
                print(f"Servicio {servicio}: {self.colas[servicio].estado()}")
            else:
                print(f"No existe la cola del servicio {servicio}.")
        else:
            for servicio, cola in self.colas.items():
                print(f"Servicio {servicio}: {cola.estado()}")

    def ejecutar(self):
        print("Comandos: 'C <servicio>' para nuevo cliente, 'A <servicio>' para atender, 'E' para mostrar estado, 'salir' para finalizar.")
        while True:
            entrada = input(">> ").strip().lower()
            if entrada == 'salir':
                break
            try:
                if entrada.startswith('c'):
                    _, servicio = entrada.split()
                    self.llegada_cliente(servicio)
                elif entrada.startswith('a'):
                    _, servicio = entrada.split()
                    self.atender_cliente(servicio)
                elif entrada == 'e':
                    self.mostrar_estado()
                else:
                    print("Comando no reconocido.")
            except ValueError:
                print("Entrada no válida.")

sistema = SistemaSeguros()
sistema.ejecutar()
