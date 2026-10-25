#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

otazky = [
    {
        "cislo": 1,
        "text": "Postavení mezinárodního práva v právním systému ČR je upraveno v Ústavě.",
        "typ": "ano_ne",
        "moznosti": ["Ano", "Ne"],
        "spravna": 0,
    },
    {
        "cislo": 2,
        "text": "Zastupitelstva obcí a krajů představují suverenitu územní samosprávy.",
        "typ": "ano_ne",
        "moznosti": ["Ano", "Ne"],
        "spravna": 1,
    },
    {
        "cislo": 3,
        "text": "Přístup k včasným a úplným informacím o životním prostředí je základní lidské právo.",
        "typ": "ano_ne",
        "moznosti": ["Ano", "Ne"],
        "spravna": 1,
    },
    {
        "cislo": 4,
        "text": "Do obecné soudní soustavy patří",
        "typ": "abcd",
        "moznosti": [
            "Okresní, krajské, vrchní a Nejvyšší soud",
            "Evropský soud pro lidská práva, Evropský soudní dvůr, Ústavní soud",
            "Arbitrážní a rozhodčí orgány",
            "Státní orgány",
        ],
        "spravna": 0,
    },
    {
        "cislo": 5,
        "text": "Úmluva o přístupu k informacím, účasti veřejnosti na rozhodování a přístupu k právní ochraně v záležitostech životního prostředí je též známa jako",
        "typ": "abcd",
        "moznosti": [
            "Aarhuská úmluva",
            "Kjótský protokol k Rámcové úmluvě OSN o změně klimatu",
            "Kyjevská úmluva",
            "Římská úmluva",
        ],
        "spravna": 0,
    },
    {
        "cislo": 6,
        "text": "Součástí ústavního pořádku je též Listina základních práv a svobod, která má podústavní právní sílu.",
        "typ": "ano_ne",
        "moznosti": ["Ano", "Ne"],
        "spravna": 1,
    },
    {
        "cislo": 7,
        "text": "Stanovit, co je trestným činem, je vyhrazeno i podzákonnému právnímu předpisu.",
        "typ": "ano_ne",
        "moznosti": ["Ano", "Ne"],
        "spravna": 1,
    },
    {
        "cislo": 8,
        "text": "Trestní odpovědnost je definována",
        "typ": "abcd",
        "moznosti": [
            "obecné části trestního zákoníku",
            "zvláštní části trestního zákoníku",
            "obecné části trestního řádu",
            "zvláštní části trestního řádu",
        ],
        "spravna": 0,
    },
    {
        "cislo": 9,
        "text": "Správní rozhodnutí nemusí",
        "typ": "abcd",
        "moznosti": [
            "být písemné",
            "obsahovat výrok",
            "obsahovat poučení o opravných prostředcích",
            "být odůvodněno, pokud žádosti občana zcela vyhovuje",
        ],
        "spravna": 1,
    },
    {
        "cislo": 10,
        "text": "Zdrojem veškeré moci v České republice",
        "typ": "abcd",
        "moznosti": [
            "je parlament",
            "je prezident",
            "je prezident a vláda",
            "jsou občané",
        ],
        "spravna": 3,
    },
    {
        "cislo": 11,
        "text": "Princip právního státu svěřuje ochranu základních práv a svobod do rukou moci soudní.",
        "typ": "ano_ne",
        "moznosti": ["Ano", "Ne"],
        "spravna": 0,
    },
    {
        "cislo": 12,
        "text": "Trestní stíhání upravuje Trestní zákoník.",
        "typ": "ano_ne",
        "moznosti": ["Ano", "Ne"],
        "spravna": 1,
    },
    {
        "cislo": 13,
        "text": "K odpovědnosti za přestupek postačuje zavinění z nedbalosti, ledaže zákon stanoví výslovně, že vyžaduje zavinění úmyslné.",
        "typ": "ano_ne",
        "moznosti": ["Ano", "Ne"],
        "spravna": 0,
    },
    {
        "cislo": 14,
        "text": "Zákon o svobodném přístupu k informacím (zákon č. 106)",
        "typ": "abcd",
        "moznosti": [
            "upravuje pouze povinnosti úřadů a práva občanů",
            "podléhá autonomnímu výkladu pojmu stát dle evropského práva",
            "vstoupí v platnost v roce 2026",
            "zavazuje pouze orgány samosprávy",
        ],
        "spravna": 1,
    },
    {
        "cislo": 15,
        "text": "Zákonná opatření senátu mají stejnou právní sílu jako",
        "typ": "abcd",
        "moznosti": [
            "amnestijní rozhodnutí prezidenta",
            "zákony",
            "ústavní zákony",
            "prováděcí právní předpisy",
        ],
        "spravna": 1,
    },
    {
        "cislo": 16,
        "text": "O vině a trestu za trestné činy mohou v České republice rozhodovat výlučně civilní soudy.",
        "typ": "ano_ne",
        "moznosti": ["Ano", "Ne"],
        "spravna": 1,
    },
    {
        "cislo": 17,
        "text": "Trestní odpovědnost právnických osob není v České republice součástí právní úpravy.",
        "typ": "ano_ne",
        "moznosti": ["Ano", "Ne"],
        "spravna": 1,
    },
    {
        "cislo": 18,
        "text": "V ústavní stížnosti lze argumentovat porušením lidských práv či základních svobod",
        "typ": "abcd",
        "moznosti": [
            "ve sporu",
            "soudním rozhodnutím",
            "zákonem",
            "jiným občanem",
        ],
        "spravna": 2,
    },
    {
        "cislo": 19,
        "text": "Státní zastupitelství je v trestním řízení",
        "typ": "abcd",
        "moznosti": [
            "zástupcem oběti trestného činu",
            "zástupcem majetkových zájmů státu",
            "zástupcem poškozeného",
            "zástupcem veřejnosti",
        ],
        "spravna": 3,
    },
    {
        "cislo": 20,
        "text": "Odvolací lhůta proti správnímu rozhodnutí činí",
        "typ": "abcd",
        "moznosti": [
            "5 dnů",
            "15 dnů",
            "30 dnů",
            "ve složitých případech až 60 dnů",
        ],
        "spravna": 1,
    },
]


def clear_line():
    print()


def zobraz_otazku(otazka):
    print("=" * 60)
    print(f"  Otázka {otazka['cislo']} / {len(otazky)}")
    print("=" * 60)
    print(f"\n  {otazka['text']}\n")

    if otazka["typ"] == "ano_ne":
        print("  1) Ano")
        print("  2) Ne")
        print()
        while True:
            volba = input("  Tvoje odpověď (1 nebo 2): ").strip()
            if volba in ["1", "2"]:
                return int(volba) - 1
            print("  ⚠️  Zadej 1 nebo 2.")
    else:
        pismena = ["a", "b", "c", "d"]
        for i, moznost in enumerate(otazka["moznosti"]):
            print(f"  {pismena[i]}) {moznost}")
        print()
        while True:
            volba = input("  Tvoje odpověď (a/b/c/d): ").strip().lower()
            if volba in pismena:
                return pismena.index(volba)
            print("  ⚠️  Zadej a, b, c nebo d.")


def spust_kviz():
    print("\n" + "=" * 60)
    print("       KVÍZ – PRÁVO A PRÁVNÍ SYSTÉM ČR")
    print("=" * 60)
    print("\n  Vítej v kvízu! Odpověz na 20 otázek.\n")
    input("  Stiskni Enter pro začátek...")

    skore = 0
    spatne = []

    for otazka in otazky:
        clear_line()
        odpoved = zobraz_otazku(otazka)
        spravna = otazka["spravna"]

        if odpoved == spravna:
            print("\n  ✅  Správně!\n")
            skore += 1
        else:
            spravna_text = otazka["moznosti"][spravna]
            print(f"\n  ❌  Špatně! Správná odpověď: {spravna_text}\n")
            spatne.append(otazka)

        input("  Stiskni Enter pro další otázku...")

    # Výsledky
    print("\n" + "=" * 60)
    print("                   VÝSLEDKY")
    print("=" * 60)
    print(f"\n  Skóre: {skore} / {len(otazky)}")
    procenta = round(skore / len(otazky) * 100)
    print(f"  Úspěšnost: {procenta} %\n")

    if procenta == 100:
        print("  🏆  Perfektní výsledek! Výborně!")
    elif procenta >= 75:
        print("  👍  Dobrý výsledek!")
    elif procenta >= 50:
        print("  📚  Ujde to, ale ještě si zopakuj látku.")
    else:
        print("  📖  Je potřeba více studia. Nevzdávej to!")

    if spatne:
        print("\n" + "-" * 60)
        print("  Otázky, kde jsi chyboval(a):")
        print("-" * 60)
        for o in spatne:
            print(f"\n  Otázka {o['cislo']}: {o['text']}")
            print(f"  ✅ Správná odpověď: {o['moznosti'][o['spravna']]}")

    print("\n" + "=" * 60)
    print("  Konec kvízu. Díky za účast!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    try:
        spust_kviz()
    except KeyboardInterrupt:
        print("\n\n  Kvíz přerušen. Na shledanou!")
        sys.exit(0)