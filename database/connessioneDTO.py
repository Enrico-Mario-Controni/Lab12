import dataclasses


@dataclasses.dataclass
class Connessione():
    id:int
    id_rifugio1:int
    id_rifugio2:int
    distanza:float
    difficolta:str
    durata:float
    anno:int

    def __str__(self):
        return (f"{self.id}, {self.id_rifugio1}, {self.id_rifugio2},"
                f" {self.distanza}, {self.difficolta}, {self.durata}, {self.anno}")

    def __hash__(self):
        return hash(self.id)
