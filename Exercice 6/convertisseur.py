class Convertisseur :
    TAUX_EUR_DH = 10.9

    @staticmethod
    def vers_dh(euros:float) -> float :
        return euros * Convertisseur.TAUX_EUR_DH
    
    @staticmethod
    def vers_eur(dirhams:float) -> float :
        return dirhams / Convertisseur.TAUX_EUR_DH

    @classmethod
    def mettre_a_jour_taux(cls, nv_taux : float) :
        cls.TAUX_EUR_DH = nv_taux

    