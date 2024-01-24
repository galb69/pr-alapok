def main():
    nyitva_kezdet = 8
    zaro = 16

    ora = int(input("Hány óra van most? "))

    if nyitva_kezdet <= ora < zaro:
        print("A bolt nyitva van. Ennyi órád van még odaérni:", zaro - ora)
    else:
        print("A bolt zárva van.")

if __name__ == "__main__":
    main()
