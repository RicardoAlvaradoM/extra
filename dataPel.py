import json

class peliculas:
    pelic = []
    def readPel(self):
        with open('data/peliculas.json','r') as file:
            pelic = json.load(file)
            self.pelic = pelic['results']
    def getPelicula(self):
        pel = []
        for row in self.pelic:
            pe = row['titulo']
            if pe not in pel:
                pel.append(pe)
        return pel