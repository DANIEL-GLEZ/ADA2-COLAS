class Cola:
    def __init__(self):
        self.clientes = []

    def agregar(self, cliente):
        self.clientes.append(cliente)

    def atender(self):
        return self.clientes.pop(0) if self.clientes else "No hay clientes en espera."

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
            print(f"Atendiendo a: {self.colas[servicio].atender()}")
        else:
            print(f"No existe la cola del servicio {servicio}.")

    def ejecutar(self):
        print("Comandos: 'C <servicio>' para nuevo cliente, 'A <servicio>' para atender, 'salir' para finalizar.")
        while True:
            entrada = input(">> ").strip().lower()
            if entrada == 'salir':
                break
            try:
                accion, servicio = entrada.split()
                if accion == 'c':
                    self.llegada_cliente(servicio)
                elif accion == 'a':
                    self.atender_cliente(servicio)
                else:
                    print("Comando no reconocido.")
            except ValueError:
                print("Entrada no válida.")

sistema = SistemaSeguros()
sistema.ejecutar()
