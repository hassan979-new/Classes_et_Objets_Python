
# 🧮 Patrons de conception

## 📘 Description

Ce document regroupe plusieurs projets Python illustrant des concepts fondamentaux de la programmation orientée objet, appliqués à des cas concrets de gestion, de conversion, de géométrie et de journalisation :

- Encapsulation : protection des données internes via attributs privés et propriétés contrôlées

- Attributs de classe vs d’instance : distinction entre données partagées et spécifiques à chaque objet

- Méthodes statiques et de classe : logique indépendante ou liée à la classe elle-même

- Surcharge de méthodes spéciales (__str__, __enter__, __exit__) : personnalisation du comportement des objets

- Gestion de contexte (with) : ouverture et fermeture automatique de ressources

- Agrégation d’objets : manipulation de collections d’instances (ex. carnet de contacts)

- Validation et robustesse : contrôle des valeurs et gestion des erreurs

- Calculs dynamiques : propriétés calculées à partir des attributs internes

- Modularité et séparation des responsabilités : organisation claire des classes et des fichiers

## 📂 Project Structure
````
projets/
├── Exercice 1/
│   ├── compteur_page.py
│   └── test.py
├── Exercice 2/
│   ├── article.py
│   └── enventaire.py
├── Exercice 3/
│   ├── contact.py
│   ├── carnet.py
│   └── test.py
├── Exercice 4/
│   ├── cercle.py
│   └── test_cercle.py
├── Exercice 5/
│   ├── journal.py
│   └── test.py
├── Exercice 6/
│   ├── convertisseur.py
│   └── test.py
└── README.md
````


## ⚙️ Features

### **1.** CompteurPage – Suivi des visites web
Classe CompteurPage
- Attribut de classe : TOTAL_VISITES (compteur global)

- Attributs d’instance : url, visites_par_page

Méthodes :

- enregistrer_lecture() : incrémente les visites de la page

- afficher_stats() : retourne une chaîne formatée avec les statistiques

### **2.** Article – Gestion d’inventaire
Classe Article
- Attributs : reference, designation, prix_ht, stock

Méthodes :

- valeur_stock() : calcule la valeur totale du stock

- __str__() : retourne une représentation textuelle formatée

### **3.** Carnet – Gestion de contacts
Classe Contact
- Attributs : nom, telephone, email

Méthode :

- initiale() : retourne la première lettre du nom (majuscule)

Classe Carnet
- Attribut privé : __contacts (liste de contacts)

Méthodes :

- ajouter(Contact) : ajoute un contact

- recherche(fragment) : retourne les contacts dont le nom contient le fragment

- afficher_tous() : affiche tous les contacts du carnet

### **4.** Cercle – Encapsulation géométrique
Classe Cercle
- Attribut privé : __rayon

Propriétés :

- rayon (getter/setter) : contrôle la validité du rayon

- perimetre : retourne 2𝜋𝑟

- surface : retourne 𝜋𝑟²
### **5.** JournalTaches – Journalisation avec contexte
Classe JournalTaches
- Attribut : fichier

Méthodes spéciales :

- __enter__() : ouvre le fichier en mode ajout

- __exit__() : ferme le fichier

Méthodes :

- enregistrer(tache) : ajoute une ligne horodatée

- lire() : affiche les entrées du journal en ordre inverse
### **6.** Convertisseur – Conversion EUR/DH
Classe Convertisseur
- Attribut de classe : TAUX_EUR_DH

Méthodes statiques :

- vers_dh(euros) : convertit en dirhams

- vers_eur(dirhams) : convertit en euros

Méthode de classe :

- mettre_a_jour_taux(nv_taux) : modifie le taux global
## 🖥️ Example Execution


### Compteur de visites de pages :
- <img width="480" height="504" alt="image" src="https://github.com/user-attachments/assets/fabe1dc3-2bae-472b-ad60-b010dcfcfa15" />
### Gestion d’inventaire d’articles : 
- <img width="480" height="504" alt="image" src="https://github.com/user-attachments/assets/ad346686-2d08-4246-bb31-00f2e12cc525" />
### Carnet d’adresses minimal :
- <img width="480" height="504" alt="image" src="https://github.com/user-attachments/assets/434c9abe-87b5-4751-8c1d-3d208ff00d43" />
### Calculatrice géométrique pour cercles :
- <img width="480" height="504" alt="image" src="https://github.com/user-attachments/assets/65492850-d6f0-4b4e-a972-78f7f7ac9f58" />
### Journal de tâches avec gestion de contexte :
- <img width="480" height="504" alt="image" src="https://github.com/user-attachments/assets/b31bf202-05d5-4520-b091-511a9256dd3e" />
- <img width="480" height="504" alt="image" src="https://github.com/user-attachments/assets/44906bd1-fe38-499f-9a49-046c30bac25b" />
### Convertisseur de devises :
- <img width="480" height="504" alt="image" src="https://github.com/user-attachments/assets/bd718201-bb7a-4fb6-bbc3-9a36d57fb6a3" />
## 💡 Concepts Practiced

- Attributs de classe vs d’instance

- Encapsulation et validation via propriétés

- Méthodes statiques et de classe

- Gestion de fichiers avec contexte (with)

- Recherche dans des collections d’objets

- Affichage personnalisé avec __str__
## 🧑‍💻 Author

- 👤 Agouram Hassan
- 🏫 Programmation orientée objet : Python
- 🎓 Instructor	Mr.LACHGAR
- 📅 08	novembre 2025
