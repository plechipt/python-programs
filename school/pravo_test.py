import random

questions = [

("Co znamená retroaktivita právní normy?",
 ["Je běžná v rodinném právu",
  "Je Ústavou ČR připuštěna jen v trestním právu",
  "Znamená její zpětnou účinnost"], 2),

("Co platí o interpretaci právního předpisu?",
 ["Není právně upravena",
  "Bývá pravidelnou součástí aplikace práva",
  "Má pevná pravidla zákonem"], 1),

("Právo tvořené státem:",
 ["Je vždy psané",
  "Může být objektivní i subjektivní",
  "Nemá restriktivní funkci"], 1),

("Platná právní norma:",
 ["Je účinná",
  "Je publikována zákonem stanoveným způsobem",
  "Je publikována na webu Parlamentu"], 1),

("Prameny práva:",
 ["Neexistovaly před rokem 1945",
  "Vznikají vždy podle pravidel",
  "Dělí se na formální a materiální"], 2),

("Prezident ČR:",
 ["Lze ho zadržet",
  "Nelze ho zadržet",
  "Lze ho stíhat za přestupek"], 1),

("Senát Parlamentu ČR:",
 ["Je volen většinovým systémem",
  "Může být rozpuštěn ÚS",
  "Nemůže soudit prezidenta"], 0),

("Evropský soud pro lidská práva:",
 ["Je orgán EU",
  "Není zřízen",
  "Je orgán Rady Evropy"], 2),

("Suverén v ČR:",
 ["Prezident",
  "Parlament",
  "Lid"], 2),

("Lidská práva:",
 ["Jsou nezcizitelná",
  "Zanikají nevyužitím",
  "Jsou jen přes ÚS"], 0),

("Není členem EU:",
 ["Německo",
  "Lucembursko",
  "Lichtenštejnsko"], 2),

("Rada EU:",
 ["Je poradní orgán",
  "Je rozhodovací orgán států",
  "Je přímo volená"], 1),

("Mezi orgány EU nepatří:",
 ["Evropský soudní dvůr",
  "Soudní dvůr EU",
  "Evropská centrální banka"], 0),

("Princip nadřazenosti práva EU:",
 ["Má přednost právo státu",
  "Má přednost právo EU",
  "Starší norma má vždy přednost"], 1),

("Evropský parlament:",
 ["Má stejný počet poslanců",
  "Je dvoukomorový",
  "Má různý počet poslanců podle států"], 2),

("Územní samospráva:",
 ["Okresy",
  "Obce",
  "Krajské úřady"], 1),

("Smíšený model správy:",
 ["Jen stát vykonává správu",
  "Obce a kraje vykonávají i státní správu",
  "Jen obce vykonávají stát"], 1),

("Opatření obecné povahy:",
 ["Je forma činnosti veřejné správy",
  "Je obecně závazný zákon",
  "Vydává ho kdokoliv"], 0),

("Správní rozhodnutí:",
 ["Je ústní",
  "Zavazuje všechny",
  "Má zásadně písemnou formu"], 2),

("Odvolání proti rozhodnutí:",
 ["Podává se u orgánu, který rozhodl",
  "U nadřízeného orgánu",
  "Do 30 dnů"], 0),

("Přestupek spáchá:",
 ["Jen právnická osoba",
  "Jen člověk",
  "Jen podnikatel"], 1),

("Blokové řízení:",
 ["Není správní řízení",
  "Pro všechny přestupky",
  "Ukládá pokutu na místě"], 2),

("Tzv. jiného správního deliktu se může dopustit:",
 ["Jen právnická osoba",
  "Právnická osoba",
  "Jen fyzická osoba"], 1),

("O přestupcích se vede:",
 ["Trestní řízení",
  "Správní řízení svého druhu",
  "Občanské soudní řízení"], 1),

("Osoba mladší 15-ti let:",
 ["Není odpovědna za přestupky",
  "Odpovídá v plném rozsahu",
  "Odpovídá částečně"], 0),

("Úprava trestných činů a trestů:",
 ["Je vyhrazena zákonu",
  "Je v Listině práv",
  "Je dána soudy"], 0),

("Trestný čin:",
 ["Je protiprávní jednání definované zákonem",
  "Je forma přestupku",
  "Vyžaduje vždy vysokou nebezpečnost"], 0),

("Trestně způsobilé osoby:",
 ["Jen právnické osoby",
  "Všechny osoby",
  "Fyzické osoby starší 15 let"], 2),

("Objekt trestného činu (zanedbání správy majetku):",
 ["Lidská důstojnost",
  "Majetek",
  "Zdraví"], 1),

("Pro vznik trestní odpovědnosti je třeba:",
 ["Úmysl",
  "Hrubá nedbalost",
  "Provinění"], 0),

("Podnikatelem je:",
 ["Každá firma",
  "Osoba vykonávající činnost samostatně",
  "Jen ten s oprávněním"], 1),

("Podmínka živnosti:",
 ["Věk 15 let",
  "Svéprávnost",
  "Základní vzdělání"], 1),

("Živnostenské oprávnění:",
 ["Vzniká ohlášením",
  "Je převoditelné",
  "Zaniká po 3 letech"], 0),

("Povinnost živnostníka:",
 ["Dávat peníze na charitu",
  "Mít osobu mluvící česky",
  "Zaměstnávat ZP"], 1),

("Kyotský protokol reguluje:",
 ["Emise skleníkových plynů",
  "Ochranu tradičního zemědělství",
  "Kácení lesů"], 0),

("Obecné užívání lesa:",
 ["Umožňuje každému volný vstup do lesa",
  "Zakazuje sběr plodů",
  "Umožňuje vjezd motorových vozidel"], 0),

("Aarhuská úmluva – nepatří:",
 ["Účast cizích států na rozhodování",
  "Právo na informace",
  "Přístup k soudní ochraně"], 0),

("Princip předběžné opatrnosti:",
 ["Nejezdit auty",
  "Nerealizovat žádné záměry",
  "Nepovolit při nejistotě dopadu"], 2),

("SEA je upravena:",
 ["Zákon o informacích",
  "Zákon o ekologické újmě",
  "Zákon o posuzování vlivů na ŽP"], 2),
]

random.shuffle(questions)
score = 0

for q, options, correct in questions:
    print("\n" + q)
    for i, opt in enumerate(options):
        print(f"{i+1}. {opt}")
    
    try:
        answer = int(input("Tvoje odpověď (1-3): ")) - 1
        if answer == correct:
            print("✅ Správně!")
            score += 1
        else:
            print(f"❌ Špatně. Správná odpověď: {options[correct]}")
    except:
        print("Neplatný vstup.")

print(f"\nVýsledek: {score}/{len(questions)}")