persoon = {"naam": "Kleintjes", "voornaam": "Karel", "leeftijd": 18}

print(persoon["naam"]) # resultaat: Kleintjes

# problemen - ik wil een value opvragen van een key die niet bestaat
# print(persoon["woonplaats"]) --> KeyError: 'woonplaats'
# oplossing 1
if "woonplaats" in persoon:
    print(persoon["woonplaats"])


# oplossing 2
print(persoon.get("woonplaats","niet gekend")) # resultaat = niet gekend   
# naam_variabele.get("key", wat is de key niet aanwezig is )

# hoe voeg ik items toe
persoon["woonplaats"] = "kerkstraat 3"
# sintax: naam_variabele["nieuweKey"] = nieuwe waarde
print(persoon.get("woonplaats","niet gekend")) # resultaat = kerkstraat 3
    
# binnen het OO (object geörienteerd programmeren heet dit een "object")