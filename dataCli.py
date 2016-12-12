import json

class clientes:
    clientes = []

    def readCli(self):
        with open('data/clientes.json','r') as file:
            clientes = json.load(file)
            self.clientes = clientes['results']

    def getCliente(self):
        cliente = []
        for row in self.clientes:
            cli = row['nombre']
            if cli not in cliente:
                cliente.append(cli)
        return cliente



