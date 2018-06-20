Cats = "Fluffy, Mr Whiskers, Lazy Tom, Meow McMeowface"
Cats = Cats.split(",")
enumerate(Cats)
for Names,a in enumerate(Cats):
    Cats[Names] = Cats[Names].strip()
    print (Cats)
