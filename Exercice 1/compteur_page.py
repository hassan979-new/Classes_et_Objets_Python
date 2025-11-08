class CompteurPage :
    TOTAL_VISITES = 0

    def __init__(self, url:str):
        self.url = url
        self.visites_par_page = 0
        CompteurPage.TOTAL_VISITES +=1


    def enregistrer_lecture(self) :
        self.visites_par_page += 1
    
    def afficher_stats(self) -> str :
        return f"Page {self.url} — visites globales : {CompteurPage.TOTAL_VISITES} — visites par page : {self.visites_par_page}"