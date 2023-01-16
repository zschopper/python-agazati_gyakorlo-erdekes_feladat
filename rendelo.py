class Rendelo:
    # kakaós: “K”
    # nutellás: “N”
    # mákos: “M”
    # lekváros: “L”
    # garfield: “G”

    palacsinta_kodok = "KNMLG"
    palancsinta_nevek = ['kakaós', 'nutellás', 'mákos', 'lekváros', 'garfield']

    def __init__(self) -> None:
        self.lista = []

    # 1/A. feladat:
    def betukeres(self, szo, betu):
        i = 0
        db = 0
        while i < len(szo):
            if betu in szo[i]:
                db += 1
            i += 1
        return db

    # 1/B. feladat:
    def szohossz(self, szo, min, max):
        return min <= len(str(szo)) <= max

    # 2. feladat:
    def beker(self):
        rend = ""
        while not rend:
            rend = input("Kérem a rendelést: ").upper()
            if not self.szohossz(rend, 1, 20):
                print("Érvénytelen rendelés (túl rövid vagy túl hosszú)!")
                rend = ""
            else:
                for betu in rend:
                    if not self.betukeres(Rendelo.palacsinta_kodok, betu):
                        print("Érvénytelen rendelés (érvénytelen palacsintakód)!")
                        rend = ""
        return rend

    # 3. feladat:
    def feltolt(self, db):
        self.lista = []
        while len(self.lista) < db:
            rend = self.beker()
            self.lista.append(rend)
        return self.lista

    # 4/A. feladat
    def garfield_db(self):
        db = 0
        i = 0
        while i < len(self.lista):
            db += self.betukeres(self.lista[i], 'G')
            i += 1
        return db

    # 4/B. feladat
    def tanyerok(self):
        rendelesek = "".join(self.lista)
        i = 0
        tanyer_kell = 0
        while i < len(Rendelo.palacsinta_kodok):
            betu = Rendelo.palacsinta_kodok[i]
            db = self.betukeres(rendelesek, betu)
            if db > 0:
                # print(">>", f"{Rendelo.palancsinta_nevek[i]}:", db)
                tanyer_kell += 1
            i += 1
        return tanyer_kell
