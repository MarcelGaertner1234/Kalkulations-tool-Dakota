#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dakota Kalkulations-Daten Extraktion v2
=========================================
Robustes Parsing der CSV mit vereinfachter Logik.

Autor: Claude Code
Datum: 2025-11-18
"""

import csv
import json
from collections import defaultdict
from decimal import Decimal

# Standard-Verlustfaktoren
RUESTVERLUST = {
    "Kartoffeln": 15, "Zwiebeln": 10, "Randen": 20, "Kürbis Hokkaido": 25,
    "Sellerie": 20, "Federkohl": 15, "Spinat": 20, "Rucola": 10,
    "Rindsfilet": 5, "Entrecôte": 5, "Kalbfleisch": 10, "Schweinefleisch": 10,
    "Forelle": 30, "Felchen": 35, "Äpfel": 15, "Feigen": 5, "Zitrone": 10,
}

GARVERLUST = {
    "Rindsfilet": 25, "Entrecôte": 25, "Dry-Aged Entrecôte": 30,
    "Kalbfleisch": 25, "Kalbsleber": 20, "Schweinefleisch": 30,
    "Schweinsbäckli": 20, "Rehfleisch": 25, "Forelle": 15, "Felchen": 15,
    "Kartoffeln": 5, "Kürbis Hokkaido": 10, "Spinat": 30, "Federkohl": 20,
}

# Kategorie-Mapping (gekürzt für Übersicht)
KATEGORIEN = {
    # Fleisch
    **{k: "Fleisch" for k in ["Rindsfilet", "Entrecôte", "Dry-Aged Entrecôte", "Kalbfleisch",
                               "Kalbsleber", "Schweinefleisch", "Schweinsbäckli", "Rehfleisch"]},
    # Fisch
    **{k: "Fisch & Meeresfrüchte" for k in ["Forelle", "Forelle geräuchert", "Felchen", "Seeteufel", "Jakobsmuschel"]},
    # Käse
    **{k: "Käse" for k in ["Alpkäse", "Parmesan", "Burrata", "Fontina-Käse", "Gorgonzola",
                            "Belper Knolle geräuchert", "Ziegenkäse geräuchert"]},
    # Milchprodukte
    **{k: "Milchprodukte" for k in ["Rahm", "Butter", "Eier", "Eigelb", "Milch", "Mayonnaise"]},
    # Gemüse
    **{k: "Gemüse" for k in ["Kartoffeln", "Randen", "Kürbis Hokkaido", "Zwiebeln", "Schalotten",
                              "Sellerie", "Federkohl", "Spinat", "Rucola", "Champignons", "Meerrettich"]},
    # Pilze
    **{k: "Pilze" for k in ["Steinpilze", "Steinpilze getrocknet", "Morcheln getrocknet"]},
    # Teigwaren
    **{k: "Teigwaren & Getreide" for k in ["Macaroni", "Blätterteig", "Mehl", "Paniermehl",
                                             "Linguine", "Carnaroli Reis"]},
    # Gewürze
    **{k: "Gewürze & Kräuter" for k in ["Salz & Pfeffer", "Gewürze", "Gewürze & Kräuter",
                                         "Dill frisch", "Thymian", "Trüffelöl", "Fleur de Sel"]},
    # Öle
    **{k: "Öle & Essig" for k in ["Olivenöl", "Olivenöl extra virgin", "Frittieröl", "Balsamico Aceto"]},
    # Früchte
    **{k: "Früchte" for k in ["Äpfel", "Feigen frisch", "Zitrone", "Quitten", "Apfelmus"]},
    # Premium
    **{k: "Premium-Zutaten" for k in ["Foie Gras", "Gänseleber", "Schwarzer Trüffel", "Safran",
                                       "Tonkabohne", "Vanille", "Yuzu-Saft"]},
    # Alkohol
    **{k: "Alkohol (Kochen)" for k in ["Weißwein", "Portwein", "Cognac", "Amaretto"]},
    # Sonstige
    **{k: "Sonstige" for k in ["Gemüsebouillon", "Kalbsfond", "Zucker", "Honig", "Walnüsse",
                                 "Hummerschalen", "Microgreens", "Brioche", "Shortbread"]},
}


def auto_kategorisieren(name):
    """Auto-Kategorisierung mit Keywords."""
    n = name.lower()
    if any(k in n for k in ["fleisch", "rind", "kalb", "schwein", "reh"]): return "Fleisch"
    if any(k in n for k in ["fisch", "muschel"]): return "Fisch & Meeresfrüchte"
    if "käse" in n or "parmesan" in n: return "Käse"
    if any(k in n for k in ["rahm", "butter", "ei"]): return "Milchprodukte"
    if any(k in n for k in ["kartoffel", "zwiebel", "kohl"]): return "Gemüse"
    if "pilz" in n or "morchel" in n: return "Pilze"
    if "gewürz" in n or "kräuter" in n: return "Gewürze & Kräuter"
    if "öl" in n or "essig" in n: return "Öle & Essig"
    if any(k in n for k in ["apfel", "feige", "zitrone"]): return "Früchte"
    return "Sonstige"


def extract_kategorie_from_gang(gang):
    """Gang → Kategorie."""
    g = gang.lower()
    if "vorspeise" in g: return "Vorspeise"
    if "suppe" in g: return "Suppe"
    if "hauptgang" in g: return "Hauptgang"
    if "dessert" in g: return "Dessert"
    if "amuse" in g: return "Amuse-Bouche"
    if "zwischengang" in g or "fischgang" in g: return "Zwischengang"
    return "Sonstiges"


def safe_float(value):
    """Sicheres Konvertieren zu Float."""
    if not value or value.strip() == "": return 0.0
    try:
        return float(value.replace('%', '').replace(',', '.'))
    except:
        return 0.0


def parse_csv_robust(csv_path):
    """Robustes CSV-Parsing mit vereinfachter Logik."""
    lebensmittel_dict = {}
    rezepte = []
    menues = []

    current_menu_typ = None
    current_menu = None
    current_rezept = None
    current_zutaten = []

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row_num, row in enumerate(reader, start=2):
            menu_typ = row.get('Menü-Typ', '').strip()
            gericht = row.get('Gericht', '').strip()
            gang = row.get('Gang', '').strip()
            zutat_name = row.get('Zutat', '').strip()

            # DEBUG: Print row 5-10 (should show Alpkäse)
            if 5 <= row_num <= 10:
                print(f"Row {row_num}: Menu={menu_typ!r}, Gericht={gericht!r}, Gang={gang!r}, Zutat={zutat_name!r}")

            # Menü-Typ tracken (bleibt gleich bis neues Menü kommt)
            if menu_typ:
                current_menu_typ = menu_typ

            # Menü-Header (Komplett, Gesamt)
            if gericht == "Komplett" and gang == "Gesamt":
                # Vorheriges Menü speichern
                if current_menu:
                    menues.append(current_menu)

                current_menu = {
                    'name': current_menu_typ,
                    'verkaufspreis': safe_float(row.get('Verkaufspreis CHF', '')),
                    'wareneinsatz_total': safe_float(row.get('Wareneinsatz Total CHF', '')),
                    'food_cost_prozent': row.get('Food Cost %', '').replace('%', '').strip(),
                    'gerichte': []
                }
                continue

            # Neues Gericht (Gericht + Gang gefüllt, Zutat leer)
            if gericht and gang and not zutat_name:
                # Debug
                print(f"   🔍 Neues Gericht gefunden: {gericht} ({gang})")

                # Vorheriges Rezept speichern
                if current_rezept and current_zutaten:
                    current_rezept['zutaten'] = current_zutaten
                    current_rezept['wareneinsatz_total'] = sum(z['wareneinsatz'] for z in current_zutaten)
                    rezepte.append(current_rezept)
                    if current_menu:
                        current_menu['gerichte'].append(current_rezept)
                    print(f"      ✓ Rezept gespeichert: {current_rezept['name']} mit {len(current_zutaten)} Zutaten")

                current_rezept = {
                    'id': len(rezepte) + 1,
                    'menu_typ': current_menu_typ,
                    'name': gericht,
                    'gang': gang,
                    'kategorie': extract_kategorie_from_gang(gang),
                    'portionen': 1  # Standard: 1 Person
                }
                current_zutaten = []
                continue

            # Subtotal oder TOTAL-Zeile (im Zutat-Feld!)
            if zutat_name and ("Subtotal" in zutat_name or "TOTAL" in zutat_name):
                if current_rezept and current_zutaten:
                    current_rezept['zutaten'] = current_zutaten
                    current_rezept['wareneinsatz_total'] = sum(z['wareneinsatz'] for z in current_zutaten)
                    rezepte.append(current_rezept)
                    if current_menu:
                        current_menu['gerichte'].append(current_rezept)
                    current_rezept = None
                    current_zutaten = []
                continue

            # Zutat-Zeile (Zutat gefüllt, Menge > 0, current_rezept existiert)
            if zutat_name and current_rezept:
                menge = safe_float(row.get('Menge', ''))
                if menge == 0:
                    print(f"      ⚠ Zutat {zutat_name} hat Menge 0, überspringe")
                    continue

                einheit = row.get('Einheit', '').strip()
                preis_pro_einheit = safe_float(row.get('Preis pro Einheit CHF', ''))
                wareneinsatz = safe_float(row.get('Wareneinsatz CHF', ''))
                lieferant = row.get('Lieferant', '').strip()
                bemerkungen = row.get('Bemerkungen', '').strip()

                print(f"      + Zutat: {zutat_name} ({menge}{einheit})")

                # Lebensmittel-Stammdaten
                if zutat_name not in lebensmittel_dict:
                    lebensmittel_dict[zutat_name] = {
                        'id': len(lebensmittel_dict) + 1,
                        'name': zutat_name,
                        'kategorie': KATEGORIEN.get(zutat_name, auto_kategorisieren(zutat_name)),
                        'preis_pro_einheit': preis_pro_einheit,
                        'einheit': einheit,
                        'lieferant': lieferant if lieferant else None,
                        'ruestverlust_prozent': RUESTVERLUST.get(zutat_name, 0),
                        'garverlust_prozent': GARVERLUST.get(zutat_name, 0),
                        'bemerkungen': None
                    }

                # Zutat zum Rezept
                current_zutaten.append({
                    'zutat': zutat_name,
                    'menge': menge,
                    'einheit': einheit,
                    'wareneinsatz': wareneinsatz,
                    'bemerkungen': bemerkungen if bemerkungen else None
                })
            elif zutat_name and not current_rezept:
                print(f"      ⚠ Zutat {zutat_name} gefunden, aber kein current_rezept!")

    # Letztes Menü speichern
    if current_menu:
        menues.append(current_menu)

    # Letztes Rezept (falls nicht schon gespeichert)
    if current_rezept and current_zutaten:
        current_rezept['zutaten'] = current_zutaten
        current_rezept['wareneinsatz_total'] = sum(z['wareneinsatz'] for z in current_zutaten)
        rezepte.append(current_rezept)

    return lebensmittel_dict, rezepte, menues


def generate_stats(lebensmittel, rezepte, menues):
    """Statistiken generieren."""
    kategorien = defaultdict(int)
    for lm in lebensmittel.values():
        kategorien[lm['kategorie']] += 1

    lieferanten = set(lm['lieferant'] for lm in lebensmittel.values() if lm['lieferant'])

    rezept_kategorien = defaultdict(int)
    for r in rezepte:
        rezept_kategorien[r['kategorie']] += 1

    return {
        'anzahl_lebensmittel': len(lebensmittel),
        'anzahl_rezepte': len(rezepte),
        'anzahl_menues': len(menues),
        'kategorien_lebensmittel': dict(kategorien),
        'kategorien_rezepte': dict(rezept_kategorien),
        'anzahl_lieferanten': len(lieferanten),
        'lieferanten': sorted(list(lieferanten))
    }


def main():
    print("=" * 70)
    print("DAKOTA KALKULATIONS-DATEN EXTRAKTION V2")
    print("=" * 70)
    print()

    csv_path = "/Users/marcelgaertner/Desktop/Projekte/dekota/07_WARENWIRTSCHAFT/Kalkulation/KALKULATION_ALLE_MENUES_DAKOTA_2025.csv"
    output_dir = "/Users/marcelgaertner/Desktop/Projekte/dekota/00_TOOLS"

    print("📖 Lese CSV-Datei...")
    lebensmittel, rezepte, menues = parse_csv_robust(csv_path)

    stats = generate_stats(lebensmittel, rezepte, menues)

    print(f"✅ {stats['anzahl_lebensmittel']} Lebensmittel extrahiert")
    print(f"✅ {stats['anzahl_rezepte']} Rezepte strukturiert")
    print(f"✅ {stats['anzahl_menues']} Menüs erkannt")
    print(f"✅ {stats['anzahl_lieferanten']} Lieferanten gefunden")
    print()

    print("📊 Lebensmittel-Kategorien:")
    for kat, anzahl in sorted(stats['kategorien_lebensmittel'].items(), key=lambda x: -x[1]):
        print(f"   - {kat:25s}: {anzahl:3d} Items")
    print()

    print("📊 Rezept-Kategorien:")
    for kat, anzahl in sorted(stats['kategorien_rezepte'].items()):
        print(f"   - {kat:25s}: {anzahl:3d} Gerichte")
    print()

    # JSON-Export
    files_created = []

    # 1. Lebensmittel
    lm_path = f"{output_dir}/dakota-lebensmittel-stammdaten.json"
    with open(lm_path, 'w', encoding='utf-8') as f:
        json.dump({
            'meta': {'titel': 'Dakota Lebensmittel-Stammdaten', 'version': '1.0', 'datum': '2025-11-18'},
            'lebensmittel': list(lebensmittel.values())
        }, f, ensure_ascii=False, indent=2)
    files_created.append(lm_path)

    # 2. Rezepte
    rz_path = f"{output_dir}/dakota-rezepte.json"
    with open(rz_path, 'w', encoding='utf-8') as f:
        json.dump({
            'meta': {'titel': 'Dakota Rezepte', 'version': '1.0', 'datum': '2025-11-18'},
            'rezepte': rezepte
        }, f, ensure_ascii=False, indent=2)
    files_created.append(rz_path)

    # 3. Menüs
    mn_path = f"{output_dir}/dakota-menues.json"
    with open(mn_path, 'w', encoding='utf-8') as f:
        json.dump({
            'meta': {'titel': 'Dakota Menüs', 'version': '1.0', 'datum': '2025-11-18'},
            'menues': menues
        }, f, ensure_ascii=False, indent=2)
    files_created.append(mn_path)

    # 4. Statistik
    st_path = f"{output_dir}/dakota-daten-statistik.json"
    with open(st_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    files_created.append(st_path)

    print("💾 JSON-Dateien erstellt:")
    for fp in files_created:
        print(f"   - {fp.split('/')[-1]}")
    print()

    print("=" * 70)
    print("✅ EXTRAKTION ERFOLGREICH ABGESCHLOSSEN")
    print("=" * 70)
    print()
    print("📋 Nächste Schritte:")
    print("   1. JSON-Dateien prüfen")
    print("   2. Web-App entwickeln (dakota-kalkulations-tool.html)")
    print("   3. IndexedDB-Import implementieren")
    print()


if __name__ == "__main__":
    main()
