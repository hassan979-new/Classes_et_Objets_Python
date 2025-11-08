from article import Article

a1 = Article("001", "Clavier DELL",24.99,10)
a2 = Article("002", "Sourie DELL",59.99,30)
a3 = Article("003", "Camera web",199.99,5)

articles = [a1,a2,a3]

for article in articles :
    print(article)

total = sum(a.valeur_stock() for a in articles)
print(f"Valeur d’inventaire : {total:.2f} €")
