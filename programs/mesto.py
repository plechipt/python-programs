# Skript pro generovani nahodneho jmena mesta
# Copyright © 2020, Jakub Šenkýř, SPŠ Trutnov

import random

# vyber samohlasek pro konstrukci jmena
# (zakomentujte radky, ktere nevyhovuji)
samohlasky = [
    'a','e','i','o','u','y',
    'ä','ë','ö','ü',
    'â','ô',
    ]

# vyber souhlasek pro konstrukci jmena
# (zakomentujte radky, ktere nevyhovuji)
souhlasky = [
    'h','ch','k','r','d','t','n',
    'c','j',
    'b','f','l','m','p','s','v','z',
    ]

# vyber dvojitych samohlasek pro konstrukci jmena
# (podle potreby upravte)
dvoj_samohlasky = [
    'au', 'ou', 'ea', 'eu',
    ]

# vyber dvojitych souhlasek pro konstrukci jmena
# (podle potreby upravte)
dvoj_souhlasky = [
    'th', 'tn', 'ng', 'zh',
    ]

# kolik jmen se bude generovat
for i in range(10):
    a = samohlasky + dvoj_samohlasky
    b = souhlasky + dvoj_souhlasky

    # nahodny zacatek jmena
    jmeno = random.choice(a + b)
    # zadany rozsah delky jmena
    # (pred poslednim prodlouzenim)
    delka = random.randint(5, 8)
    
    # pripadne prohozeni, aby se zabranilo opakovani
    if jmeno in a:
        a, b = b, a

    # generovani zbytku jmena
    while len(jmeno) < delka:
        jmeno += random.choice(a)
        jmeno += random.choice(b)
        
        # pripadne vyrazeni dvojitych samohlasek
        # (pokud uz ve jmene nejaka je)
        if any(dvoj_samohlaska in jmeno for dvoj_samohlaska in dvoj_samohlasky):
            a = [hlaska for hlaska in a if hlaska not in dvoj_samohlasky]
            b = [hlaska for hlaska in b if hlaska not in dvoj_samohlasky]
        # pripadne vyrazeni dvojitych souhlasek
        # (pokud uz ve jmene nejaka je)
        if any(dvoj_souhlaska in jmeno for dvoj_souhlaska in dvoj_souhlasky):
            a = [hlaska for hlaska in a if hlaska not in dvoj_souhlasky]
            b = [hlaska for hlaska in b if hlaska not in dvoj_souhlasky]
    else:
        # prvni pismeno velke
        print(jmeno.capitalize())
