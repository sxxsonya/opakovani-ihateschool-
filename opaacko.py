cisla = [3, 5, 8, 1, 2, 4, 6, 7]

def seradit_cisla(cisla, sestupne=False):
    serazena_cisla=sorted(cisla,reverse=sestupne)
    return serazena_cisla 

def vyber_poradi():
    volba = input("Chces seradit cisla vzestupne (A) nebo sestupne (B)?").upper()
    return volba == "B"

sestupne = vyber_poradi()
print("cisla serazena:", seradit_cisla(cisla, sestupne))