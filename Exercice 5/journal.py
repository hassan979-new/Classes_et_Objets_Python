from datetime import datetime

class JournalTaches :
    def __init__(self):
        self.fichier = None

    def __enter__(self) :
        self.fichier =  open("journal.txt","a",encoding="UTF-8")
        return self
        
    def enregistrer(self, tache : str) :
        date = datetime.now().isoformat()
        self.fichier.write(f"{date} - {tache}\n")

    def __exit__(self,exc_type, exc, tb) :
        if self.fichier :
            self.fichier.close()

    def lire(self) :
        with open("journal.txt","r",encoding="UTF-8") as f :
            lines = f.readlines()
            for line in reversed(lines) :
                print(line.strip())


        
