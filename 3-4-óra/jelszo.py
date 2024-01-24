def main():
    helyes_felhasznalonev = "bori99"
    helyes_jelszo = "Szivecske<3"

    while True:
        felhasznalonev = input("Adja meg a felhasználónevét! ").strip()
        jelszo = input("Adja meg a jelszavát! ")

        if felhasznalonev == helyes_felhasznalonev and jelszo == helyes_jelszo:
            print("Belépés engedélyezve.")
            break
        else:
            print("Belépés megtagadva.")

if __name__ == "__main__":
    main()
