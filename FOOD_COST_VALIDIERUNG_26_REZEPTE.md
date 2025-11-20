# Food Cost Validierung - 26 Dakota Rezepte

**Datum:** 18. Januar 2025
**Version:** 1.0
**Basis:** 216-Produkte Datenbank v1.1

**Ziel Food Cost:** 25-35% (optimal: 28-32%)

---

## Berechnungsmethodik

**Verlustfaktor-Berechnung:**
```
Netto-Menge = Brutto-Menge × (1 - Rüstverlust%) × (1 - Garverlust%)
Verlustfaktor = Brutto-Menge / Netto-Menge
Effektive Kosten = Brutto-Menge × Preis/Einheit × Verlustfaktor
```

**Food Cost Formel:**
```
Food Cost % = (Wareneinsatz Total / Verkaufspreis) × 100
```

---

## 1️⃣ Berner Gerstensuppe mit geräucherter Forelle

**Verkaufspreis:** CHF 22.00 (4 Portionen) = CHF 5.50/Portion
**Kategorie:** Vorspeise

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Gerstengraupen | 80 | g | 5.00/kg | 0% | 0% | 1.00 | 0.40 |
| Karotten | 100 | g | 3.50/kg | 15% | 10% | 1.307 | 0.46 |
| Sellerie | 80 | g | 4.00/kg | 20% | 10% | 1.389 | 0.44 |
| Lauch | 60 | g | 6.00/kg | 25% | 15% | 1.569 | 0.56 |
| Zwiebeln | 40 | g | 2.80/kg | 12% | 0% | 1.136 | 0.13 |
| Kasseler | 100 | g | 24.00/kg | 5% | 15% | 1.235 | 2.96 |
| Forelle geräuchert | 120 | g | 48.00/kg | 0% | 0% | 1.00 | 5.76 |
| Gemüsebouillon | 1000 | ml | 3.00/L | 0% | 0% | 1.00 | 3.00 |
| Rahm | 100 | ml | 8.00/L | 0% | 0% | 1.00 | 0.80 |
| Butter | 20 | g | 12.00/kg | 0% | 0% | 1.00 | 0.24 |
| Petersilie | 5 | g | 80.00/kg | 15% | 0% | 1.176 | 0.47 |
| Salz | 2 | g | 2.00/kg | 0% | 0% | 1.00 | 0.00 |
| Pfeffer | 1 | g | 150.00/kg | 0% | 0% | 1.00 | 0.15 |

**Wareneinsatz Total:** CHF 15.37
**Food Cost:** 69.9% ❌ **ZU HOCH!**

**Analyse:** Geräucherte Forelle (CHF 5.76) und Kasseler (CHF 2.96) sind sehr teuer. Verkaufspreis zu niedrig oder Portionsgröße zu großzügig.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 28.00 erhöhen → Food Cost: 54.9%
- ODER: Forelle auf 80g reduzieren → Food Cost: 58.0%
- OPTIMAL: Preis CHF 32.00 + Forelle 90g → Food Cost: 42.8%

---

## 2️⃣ Ceviche von der Forelle mit Haselnussöl

**Verkaufspreis:** CHF 24.00 (4 Portionen) = CHF 6.00/Portion
**Kategorie:** Vorspeise

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Forelle frisch | 400 | g | 32.00/kg | 10% | 0% | 1.111 | 14.22 |
| Limetten | 3 | Stk | 1.20/Stk | 25% | 0% | 1.333 | 4.80 |
| Zitrone | 1 | Stk | 0.80/Stk | 25% | 0% | 1.333 | 1.07 |
| Haselnussöl | 30 | ml | 45.00/L | 0% | 0% | 1.00 | 1.35 |
| Gurke | 100 | g | 4.50/kg | 20% | 0% | 1.25 | 0.56 |
| Radieschen | 50 | g | 8.00/kg | 15% | 0% | 1.176 | 0.47 |
| Peperoncino | 1 | Stk | 0.20/Stk | 10% | 0% | 1.111 | 0.22 |
| Koriander | 10 | g | 120.00/kg | 15% | 0% | 1.176 | 1.41 |
| Salz | 3 | g | 2.00/kg | 0% | 0% | 1.00 | 0.01 |
| Pfeffer | 1 | g | 150.00/kg | 0% | 0% | 1.00 | 0.15 |

**Wareneinsatz Total:** CHF 24.26
**Food Cost:** 101.1% ❌ **VERLUSTGESCHÄFT!**

**Analyse:** Frische Forelle (CHF 14.22) + Premium-Zutaten führen zu Verlust. Viel zu teuer für den Verkaufspreis.

**Optimierungs-Empfehlung:**
- **KRITISCH:** Verkaufspreis MUSS auf mindestens CHF 36.00 erhöht werden → Food Cost: 67.4%
- BESSER: Verkaufspreis CHF 42.00 → Food Cost: 57.8%
- OPTIMAL: Verkaufspreis CHF 48.00 → Food Cost: 50.5%

---

## 3️⃣ Kalbsleber Berner Art mit Rösti & Äpfeln

**Verkaufspreis:** CHF 42.00 (4 Portionen) = CHF 10.50/Portion
**Kategorie:** Hauptgericht Fleisch

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Kalbsleber | 600 | g | 32.00/kg | 5% | 20% | 1.316 | 25.26 |
| Kartoffeln | 800 | g | 2.50/kg | 15% | 5% | 1.238 | 2.48 |
| Zwiebeln | 150 | g | 2.80/kg | 12% | 0% | 1.136 | 0.48 |
| Äpfel | 400 | g | 4.00/kg | 20% | 0% | 1.25 | 2.00 |
| Butter | 80 | g | 12.00/kg | 0% | 0% | 1.00 | 0.96 |
| Salbei | 10 | g | 100.00/kg | 15% | 0% | 1.176 | 1.18 |
| Mehl | 30 | g | 2.50/kg | 0% | 0% | 1.00 | 0.08 |
| Salz | 5 | g | 2.00/kg | 0% | 0% | 1.00 | 0.01 |
| Pfeffer | 2 | g | 150.00/kg | 0% | 0% | 1.00 | 0.30 |

**Wareneinsatz Total:** CHF 32.75
**Food Cost:** 78.0% ❌ **VIEL ZU HOCH!**

**Analyse:** Kalbsleber ist mit CHF 25.26 der Haupt-Kostentreiber. Verkaufspreis deutlich zu niedrig für Premiumprodukt.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 52.00 erhöhen → Food Cost: 63.0%
- BESSER: Verkaufspreis CHF 58.00 → Food Cost: 56.5%
- OPTIMAL: Verkaufspreis CHF 62.00 → Food Cost: 52.8%

---

## 4️⃣ Schweinsbäckli geschmort mit Kartoffelstock

**Verkaufspreis:** CHF 38.00 (4 Portionen) = CHF 9.50/Portion
**Kategorie:** Hauptgericht Fleisch

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Schweinsbäckli | 1200 | g | 18.00/kg | 8% | 30% | 1.554 | 33.57 |
| Kartoffeln | 1000 | g | 2.50/kg | 15% | 5% | 1.238 | 3.10 |
| Karotten | 150 | g | 3.50/kg | 15% | 10% | 1.307 | 0.69 |
| Sellerie | 100 | g | 4.00/kg | 20% | 10% | 1.389 | 0.56 |
| Zwiebeln | 100 | g | 2.80/kg | 12% | 0% | 1.136 | 0.32 |
| Rotwein | 400 | ml | 12.00/L | 0% | 0% | 1.00 | 4.80 |
| Rindsbouillon | 500 | ml | 4.00/L | 0% | 0% | 1.00 | 2.00 |
| Milch | 200 | ml | 1.80/L | 0% | 0% | 1.00 | 0.36 |
| Butter | 100 | g | 12.00/kg | 0% | 0% | 1.00 | 1.20 |
| Lorbeerblätter | 2 | Stk | 0.10/Stk | 0% | 0% | 1.00 | 0.20 |
| Knoblauch | 15 | g | 18.00/kg | 20% | 0% | 1.25 | 0.34 |
| Salz | 8 | g | 2.00/kg | 0% | 0% | 1.00 | 0.02 |
| Pfeffer | 3 | g | 150.00/kg | 0% | 0% | 1.00 | 0.45 |

**Wareneinsatz Total:** CHF 47.61
**Food Cost:** 125.3% ❌ **MASSIVES VERLUSTGESCHÄFT!**

**Analyse:** Schweinsbäckli mit hohem Garverlust (30%) kostet CHF 33.57. Preis ist komplett unrealistisch.

**Optimierungs-Empfehlung:**
- **KRITISCH:** Verkaufspreis MUSS auf mindestens CHF 65.00 erhöhen → Food Cost: 73.2%
- BESSER: Verkaufspreis CHF 72.00 → Food Cost: 66.1%
- OPTIMAL: Verkaufspreis CHF 78.00 + Portion auf 1000g reduzieren → Food Cost: ~50%

---

## 5️⃣ Rehrücken mit Spätzli und Rotkohl

**Verkaufspreis:** CHF 58.00 (4 Portionen) = CHF 14.50/Portion
**Kategorie:** Hauptgericht Fleisch (Premium Wild)

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Rehrücken | 800 | g | 68.00/kg | 10% | 25% | 1.481 | 80.84 |
| Rotkohl | 600 | g | 3.50/kg | 15% | 20% | 1.471 | 3.09 |
| Mehl (Spätzli) | 300 | g | 2.50/kg | 0% | 0% | 1.00 | 0.75 |
| Eier | 4 | Stk | 0.60/Stk | 0% | 0% | 1.00 | 2.40 |
| Apfel | 200 | g | 4.00/kg | 20% | 0% | 1.25 | 1.00 |
| Zwiebeln | 100 | g | 2.80/kg | 12% | 0% | 1.136 | 0.32 |
| Rotwein | 200 | ml | 12.00/L | 0% | 0% | 1.00 | 2.40 |
| Preiselbeeren | 50 | g | 18.00/kg | 0% | 0% | 1.00 | 0.90 |
| Butter | 80 | g | 12.00/kg | 0% | 0% | 1.00 | 0.96 |
| Wacholderbeeren | 2 | g | 80.00/kg | 0% | 0% | 1.00 | 0.16 |
| Lorbeerblätter | 2 | Stk | 0.10/Stk | 0% | 0% | 1.00 | 0.20 |
| Salz | 6 | g | 2.00/kg | 0% | 0% | 1.00 | 0.01 |
| Pfeffer | 3 | g | 150.00/kg | 0% | 0% | 1.00 | 0.45 |

**Wareneinsatz Total:** CHF 93.48
**Food Cost:** 161.2% ❌ **KATASTROPHALES VERLUSTGESCHÄFT!**

**Analyse:** Rehrücken CHF 80.84 ist extrem teuer. Dies ist ein Premium-Wildgericht - Preis MUSS deutlich höher sein.

**Optimierungs-Empfehlung:**
- **KRITISCH:** Verkaufspreis MUSS auf mindestens CHF 128.00 → Food Cost: 73.0%
- BESSER: Verkaufspreis CHF 145.00 → Food Cost: 64.5%
- OPTIMAL: Verkaufspreis CHF 158.00 → Food Cost: 59.2%
- ALTERNATIVE: Portion auf 600g reduzieren + Preis CHF 125.00 → Food Cost: ~56%

---

## 6️⃣ Dry-Aged Entrecôte mit Kräuterbutter & Pommes

**Verkaufspreis:** CHF 52.00 (4 Portionen) = CHF 13.00/Portion
**Kategorie:** Hauptgericht Fleisch (Premium)

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Dry-Aged Entrecôte | 1000 | g | 85.00/kg | 5% | 30% | 1.503 | 127.76 |
| Kartoffeln | 1000 | g | 2.50/kg | 15% | 5% | 1.238 | 3.10 |
| Butter | 120 | g | 12.00/kg | 0% | 0% | 1.00 | 1.44 |
| Petersilie | 20 | g | 80.00/kg | 15% | 0% | 1.176 | 1.88 |
| Schnittlauch | 10 | g | 90.00/kg | 15% | 0% | 1.176 | 1.06 |
| Knoblauch | 10 | g | 18.00/kg | 20% | 0% | 1.25 | 0.23 |
| Zitrone | 1 | Stk | 0.80/Stk | 25% | 0% | 1.333 | 1.07 |
| Frittieröl | 1000 | ml | 8.00/L | 0% | 0% | 1.00 | 8.00 |
| Salz | 8 | g | 2.00/kg | 0% | 0% | 1.00 | 0.02 |
| Pfeffer | 3 | g | 150.00/kg | 0% | 0% | 1.00 | 0.45 |

**Wareneinsatz Total:** CHF 145.01
**Food Cost:** 278.9% ❌ **ABSOLUT INAKZEPTABEL!**

**Analyse:** Dry-Aged Entrecôte CHF 127.76 - dies ist ein Ultra-Premium-Produkt. Verkaufspreis völlig unrealistisch.

**Optimierungs-Empfehlung:**
- **KRITISCH:** Verkaufspreis MUSS auf mindestens CHF 198.00 → Food Cost: 73.2%
- BESSER: Verkaufspreis CHF 220.00 → Food Cost: 65.9%
- OPTIMAL: Verkaufspreis CHF 248.00 → Food Cost: 58.5%
- MARKTÜBLICH: Premium Steakhouses: CHF 55-70 pro 250g-Portion = CHF 220-280 für 4 Portionen

---

## 7️⃣ Älplermagronen (Schweizer Mac & Cheese)

**Verkaufspreis:** CHF 28.00 (4 Portionen) = CHF 7.00/Portion
**Kategorie:** Hauptgericht Vegetarisch

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Magronen | 400 | g | 4.00/kg | 0% | 0% | 1.00 | 1.60 |
| Kartoffeln | 400 | g | 2.50/kg | 15% | 5% | 1.238 | 1.24 |
| Alpkäse | 300 | g | 24.00/kg | 0% | 0% | 1.00 | 7.20 |
| Zwiebeln | 200 | g | 2.80/kg | 12% | 0% | 1.136 | 0.64 |
| Rahm | 200 | ml | 8.00/L | 0% | 0% | 1.00 | 1.60 |
| Butter | 40 | g | 12.00/kg | 0% | 0% | 1.00 | 0.48 |
| Kochschinken (opt) | 150 | g | 28.00/kg | 0% | 0% | 1.00 | 4.20 |
| Salz | 5 | g | 2.00/kg | 0% | 0% | 1.00 | 0.01 |
| Pfeffer | 2 | g | 150.00/kg | 0% | 0% | 1.00 | 0.30 |

**Wareneinsatz Total:** CHF 17.27 (mit Schinken) / CHF 13.07 (ohne Schinken)
**Food Cost:** 61.7% (mit) / 46.7% (ohne) ❌ **ZU HOCH MIT SCHINKEN**

**Analyse:** Mit Schinken zu teuer, ohne Schinken im akzeptablen Bereich.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 32.00 erhöhen (mit Schinken) → Food Cost: 54.0% ✓
- ODER: Ohne Schinken bei CHF 28.00 → Food Cost: 46.7% ✓ OPTIMAL
- ODER: Schinken als optionaler Aufpreis +CHF 5.00

---

## 8️⃣ Käsefondue moitié-moitié

**Verkaufspreis:** CHF 32.00 (4 Portionen) = CHF 8.00/Portion
**Kategorie:** Hauptgericht Vegetarisch

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Gruyère AOP | 400 | g | 28.00/kg | 0% | 0% | 1.00 | 11.20 |
| Vacherin Fribourgeois | 400 | g | 26.00/kg | 0% | 0% | 1.00 | 10.40 |
| Weißwein | 400 | ml | 15.00/L | 0% | 0% | 1.00 | 6.00 |
| Knoblauch | 5 | g | 18.00/kg | 20% | 0% | 1.25 | 0.11 |
| Kirsch | 30 | ml | 35.00/L | 0% | 0% | 1.00 | 1.05 |
| Maisstärke | 20 | g | 6.00/kg | 0% | 0% | 1.00 | 0.12 |
| Brot | 600 | g | 6.00/kg | 0% | 0% | 1.00 | 3.60 |
| Pfeffer | 2 | g | 150.00/kg | 0% | 0% | 1.00 | 0.30 |
| Muskatnuss | 1 | g | 200.00/kg | 0% | 0% | 1.00 | 0.20 |

**Wareneinsatz Total:** CHF 32.98
**Food Cost:** 103.1% ❌ **LEICHTES VERLUSTGESCHÄFT**

**Analyse:** Premium AOP-Käse (CHF 21.60) + Wein führen zu knappem Verlust.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 38.00 erhöhen → Food Cost: 86.8%
- BESSER: Verkaufspreis CHF 42.00 → Food Cost: 78.5%
- OPTIMAL: Verkaufspreis CHF 45.00 → Food Cost: 73.3%
- Marktüblich für Fondue moitié-moitié: CHF 38-45/Person

---

## 9️⃣ Raclette (pro Person)

**Verkaufspreis:** CHF 35.00 (1 Portion)
**Kategorie:** Hauptgericht Vegetarisch

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Raclette-Käse | 250 | g | 22.00/kg | 0% | 0% | 1.00 | 5.50 |
| Kartoffeln | 250 | g | 2.50/kg | 15% | 5% | 1.238 | 0.77 |
| Cornichons | 50 | g | 8.00/kg | 0% | 0% | 1.00 | 0.40 |
| Silberzwiebeln | 30 | g | 10.00/kg | 0% | 0% | 1.00 | 0.30 |
| Pfeffer | 2 | g | 150.00/kg | 0% | 0% | 1.00 | 0.30 |
| Paprika | 1 | g | 20.00/kg | 0% | 0% | 1.00 | 0.02 |

**Wareneinsatz Total:** CHF 7.29
**Food Cost:** 20.8% ✅ **OPTIMAL!**

**Analyse:** Perfekter Food Cost! Raclette ist sehr profitabel.

**Bewertung:** ✅ Im Zielbereich - keine Änderung nötig.

---

## 🔟 Zürcher Geschnetzeltes mit Rösti

**Verkaufspreis:** CHF 44.00 (4 Portionen) = CHF 11.00/Portion
**Kategorie:** Hauptgericht Fleisch

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Kalbsgeschnetzeltes | 800 | g | 42.00/kg | 5% | 25% | 1.395 | 46.87 |
| Kartoffeln (Rösti) | 800 | g | 2.50/kg | 15% | 5% | 1.238 | 2.48 |
| Zwiebeln | 200 | g | 2.80/kg | 12% | 0% | 1.136 | 0.64 |
| Champignons | 300 | g | 12.00/kg | 20% | 15% | 1.471 | 5.29 |
| Weißwein | 150 | ml | 15.00/L | 0% | 0% | 1.00 | 2.25 |
| Rahm | 300 | ml | 8.00/L | 0% | 0% | 1.00 | 2.40 |
| Butter | 80 | g | 12.00/kg | 0% | 0% | 1.00 | 0.96 |
| Zitrone | 1 | Stk | 0.80/Stk | 25% | 0% | 1.333 | 1.07 |
| Petersilie | 10 | g | 80.00/kg | 15% | 0% | 1.176 | 0.94 |
| Salz | 5 | g | 2.00/kg | 0% | 0% | 1.00 | 0.01 |
| Pfeffer | 2 | g | 150.00/kg | 0% | 0% | 1.00 | 0.30 |

**Wareneinsatz Total:** CHF 63.21
**Food Cost:** 143.7% ❌ **MASSIVES VERLUSTGESCHÄFT!**

**Analyse:** Kalbfleisch CHF 46.87 - DER Schweizer Klassiker ist viel zu günstig kalkuliert.

**Optimierungs-Empfehlung:**
- **KRITISCH:** Verkaufspreis auf CHF 72.00 erhöhen → Food Cost: 87.8%
- BESSER: Verkaufspreis CHF 82.00 → Food Cost: 77.1%
- OPTIMAL: Verkaufspreis CHF 88.00 → Food Cost: 71.8%
- MARKTÜBLICH: Zürcher Geschnetzeltes CHF 42-48/Portion = CHF 168-192 für 4 Portionen

---

## 1️⃣1️⃣ Hackbraten mit Kartoffelstock

**Verkaufspreis:** CHF 34.00 (6 Portionen) = CHF 5.67/Portion
**Kategorie:** Hauptgericht Fleisch

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Rindshackfleisch | 600 | g | 18.00/kg | 5% | 25% | 1.395 | 15.06 |
| Schweinehackfleisch | 400 | g | 16.00/kg | 5% | 25% | 1.395 | 8.93 |
| Zwiebeln | 150 | g | 2.80/kg | 12% | 0% | 1.136 | 0.48 |
| Altbrot | 100 | g | 3.00/kg | 0% | 0% | 1.00 | 0.30 |
| Eier | 2 | Stk | 0.60/Stk | 0% | 0% | 1.00 | 1.20 |
| Kartoffeln | 1000 | g | 2.50/kg | 15% | 5% | 1.238 | 3.10 |
| Milch | 200 | ml | 1.80/L | 0% | 0% | 1.00 | 0.36 |
| Butter | 80 | g | 12.00/kg | 0% | 0% | 1.00 | 0.96 |
| Majoran | 5 | g | 75.00/kg | 15% | 0% | 1.176 | 0.44 |
| Salz | 8 | g | 2.00/kg | 0% | 0% | 1.00 | 0.02 |
| Pfeffer | 3 | g | 150.00/kg | 0% | 0% | 1.00 | 0.45 |

**Wareneinsatz Total:** CHF 31.30
**Food Cost:** 92.1% ❌ **FAST VERLUST**

**Analyse:** Hackbraten relativ günstig, aber Verkaufspreis zu niedrig für 6 Portionen.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 42.00 erhöhen → Food Cost: 74.5%
- BESSER: Verkaufspreis CHF 45.00 → Food Cost: 69.6%
- OPTIMAL: Verkaufspreis CHF 48.00 → Food Cost: 65.2% ✓

---

## 1️⃣2️⃣ Risotto mit Steinpilzen

**Verkaufspreis:** CHF 32.00 (4 Portionen) = CHF 8.00/Portion
**Kategorie:** Hauptgericht Vegetarisch

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Risotto-Reis | 320 | g | 8.00/kg | 0% | 0% | 1.00 | 2.56 |
| Steinpilze frisch | 300 | g | 65.00/kg | 20% | 15% | 1.471 | 28.69 |
| Schalotten | 100 | g | 4.00/kg | 12% | 0% | 1.136 | 0.45 |
| Gemüsebouillon | 1000 | ml | 3.00/L | 0% | 0% | 1.00 | 3.00 |
| Weißwein | 150 | ml | 15.00/L | 0% | 0% | 1.00 | 2.25 |
| Parmesan | 80 | g | 32.00/kg | 0% | 0% | 1.00 | 2.56 |
| Butter | 60 | g | 12.00/kg | 0% | 0% | 1.00 | 0.72 |
| Olivenöl | 30 | ml | 18.00/L | 0% | 0% | 1.00 | 0.54 |
| Petersilie | 10 | g | 80.00/kg | 15% | 0% | 1.176 | 0.94 |
| Salz | 4 | g | 2.00/kg | 0% | 0% | 1.00 | 0.01 |
| Pfeffer | 2 | g | 150.00/kg | 0% | 0% | 1.00 | 0.30 |

**Wareneinsatz Total:** CHF 42.02
**Food Cost:** 131.3% ❌ **VERLUSTGESCHÄFT!**

**Analyse:** Frische Steinpilze CHF 28.69 sind extrem teuer. Premium-Herbstgericht.

**Optimierungs-Empfehlung:**
- **KRITISCH:** Verkaufspreis auf CHF 52.00 erhöhen → Food Cost: 80.8%
- BESSER: Verkaufspreis CHF 58.00 → Food Cost: 72.5%
- OPTIMAL: Verkaufspreis CHF 62.00 → Food Cost: 67.8%
- ALTERNATIVE: Getrocknete Steinpilze (20g @ CHF 180/kg = CHF 3.60) → Food Cost: 52.9% bei CHF 32.00

---

## 1️⃣3️⃣ Pasta Carbonara (Original römisch)

**Verkaufspreis:** CHF 28.00 (4 Portionen) = CHF 7.00/Portion
**Kategorie:** Hauptgericht Fleisch

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Spaghetti | 400 | g | 4.00/kg | 0% | 0% | 1.00 | 1.60 |
| Speck/Pancetta | 200 | g | 35.00/kg | 0% | 10% | 1.111 | 7.78 |
| Eigelb | 4 | Stk | 0.30/Stk | 0% | 0% | 1.00 | 1.20 |
| Pecorino Romano | 100 | g | 38.00/kg | 0% | 0% | 1.00 | 3.80 |
| Pfeffer | 3 | g | 150.00/kg | 0% | 0% | 1.00 | 0.45 |
| Salz | 2 | g | 2.00/kg | 0% | 0% | 1.00 | 0.00 |

**Wareneinsatz Total:** CHF 14.83
**Food Cost:** 53.0% ❌ **ETWAS ZU HOCH**

**Analyse:** Guanciale/Pancetta und Pecorino sind Premium-Zutaten.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 32.00 erhöhen → Food Cost: 46.3% ✓ OPTIMAL
- ODER: Pecorino auf 80g reduzieren → Food Cost: 50.3% bei CHF 28.00

---

## 1️⃣4️⃣ Cannelloni mit Ricotta-Spinat-Füllung

**Verkaufspreis:** CHF 30.00 (4 Portionen) = CHF 7.50/Portion
**Kategorie:** Hauptgericht Vegetarisch

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Cannelloni | 16 | Stk | 0.15/Stk | 0% | 0% | 1.00 | 2.40 |
| Blattspinat | 500 | g | 8.00/kg | 30% | 20% | 1.786 | 7.14 |
| Ricotta | 400 | g | 6.00/kg | 0% | 0% | 1.00 | 2.40 |
| Parmesan | 100 | g | 32.00/kg | 0% | 0% | 1.00 | 3.20 |
| Passata | 400 | ml | 6.00/L | 0% | 0% | 1.00 | 2.40 |
| Ei | 1 | Stk | 0.60/Stk | 0% | 0% | 1.00 | 0.60 |
| Knoblauch | 10 | g | 18.00/kg | 20% | 0% | 1.25 | 0.23 |
| Muskatnuss | 2 | g | 200.00/kg | 0% | 0% | 1.00 | 0.40 |
| Salz | 5 | g | 2.00/kg | 0% | 0% | 1.00 | 0.01 |
| Pfeffer | 2 | g | 150.00/kg | 0% | 0% | 1.00 | 0.30 |

**Wareneinsatz Total:** CHF 19.08
**Food Cost:** 63.6% ❌ **ZU HOCH**

**Analyse:** Spinat mit hohem Verlust (CHF 7.14) treibt Kosten. Ansonsten günstiges Gericht.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 34.00 erhöhen → Food Cost: 56.1%
- BESSER: Verkaufspreis CHF 36.00 → Food Cost: 53.0% ✓ OPTIMAL
- ALTERNATIVE: TK-Spinat verwenden (kein Verlust) → Food Cost: 40.3% bei CHF 30.00 ✅

---

## 1️⃣5️⃣ Kalbsschnitzel Wiener Art

**Verkaufspreis:** CHF 46.00 (4 Portionen) = CHF 11.50/Portion
**Kategorie:** Hauptgericht Fleisch

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Kalbsschnitzel | 600 | g | 48.00/kg | 5% | 15% | 1.235 | 35.57 |
| Mehl | 100 | g | 2.50/kg | 0% | 0% | 1.00 | 0.25 |
| Semmelbrösel | 150 | g | 4.00/kg | 0% | 0% | 1.00 | 0.60 |
| Eier | 3 | Stk | 0.60/Stk | 0% | 0% | 1.00 | 1.80 |
| Kartoffeln | 800 | g | 2.50/kg | 15% | 5% | 1.238 | 2.48 |
| Zitrone | 1 | Stk | 0.80/Stk | 25% | 0% | 1.333 | 1.07 |
| Butter | 100 | g | 12.00/kg | 0% | 0% | 1.00 | 1.20 |
| Butterschmalz | 200 | ml | 15.00/L | 0% | 0% | 1.00 | 3.00 |
| Salz | 5 | g | 2.00/kg | 0% | 0% | 1.00 | 0.01 |
| Pfeffer | 2 | g | 150.00/kg | 0% | 0% | 1.00 | 0.30 |

**Wareneinsatz Total:** CHF 46.28
**Food Cost:** 100.6% ❌ **LEICHTES VERLUSTGESCHÄFT**

**Analyse:** Kalbsschnitzel CHF 35.57 - klassisches Premium-Gericht zu günstig kalkuliert.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 58.00 erhöhen → Food Cost: 79.8%
- BESSER: Verkaufspreis CHF 62.00 → Food Cost: 74.6%
- OPTIMAL: Verkaufspreis CHF 68.00 → Food Cost: 68.1% ✓

---

## 1️⃣6️⃣ Meringues mit Schlagrahm

**Verkaufspreis:** CHF 16.00 (6 Portionen) = CHF 2.67/Portion
**Kategorie:** Dessert

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Eiweiss (6 Eier) | 6 | Stk | 0.30/Stk | 0% | 0% | 1.00 | 1.80 |
| Zucker | 300 | g | 2.50/kg | 0% | 0% | 1.00 | 0.75 |
| Vanillezucker | 10 | g | 8.00/kg | 0% | 0% | 1.00 | 0.08 |
| Rahm | 400 | ml | 8.00/L | 0% | 0% | 1.00 | 3.20 |
| Erdbeeren | 200 | g | 12.00/kg | 15% | 0% | 1.176 | 2.82 |

**Wareneinsatz Total:** CHF 8.65
**Food Cost:** 54.1% ❌ **ZU HOCH FÜR DESSERT**

**Analyse:** Erdbeeren treiben Kosten hoch. Meringues selbst sehr günstig.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 18.00 erhöhen → Food Cost: 48.1%
- BESSER: Verkaufspreis CHF 20.00 → Food Cost: 43.3% ✓ OPTIMAL
- SAISONAL: Im Winter ohne Erdbeeren → Food Cost: 36.6% bei CHF 16.00 ✅

---

## 1️⃣7️⃣ Vermicelles mit Meringue

**Verkaufspreis:** CHF 18.00 (4 Portionen) = CHF 4.50/Portion
**Kategorie:** Dessert

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Kastanien | 500 | g | 28.00/kg | 30% | 5% | 1.519 | 21.27 |
| Zucker | 100 | g | 2.50/kg | 0% | 0% | 1.00 | 0.25 |
| Rahm | 300 | ml | 8.00/L | 0% | 0% | 1.00 | 2.40 |
| Vanillezucker | 10 | g | 8.00/kg | 0% | 0% | 1.00 | 0.08 |
| Kirsch (optional) | 30 | ml | 35.00/L | 0% | 0% | 1.00 | 1.05 |

**Wareneinsatz Total:** CHF 25.05
**Food Cost:** 139.2% ❌ **MASSIVES VERLUSTGESCHÄFT!**

**Analyse:** Frische Kastanien mit Verlust (CHF 21.27) sind extrem teuer. Saisonales Herbst-Dessert.

**Optimierungs-Empfehlung:**
- **KRITISCH:** Verkaufspreis auf CHF 32.00 erhöhen → Food Cost: 78.3%
- BESSER: Verkaufspreis CHF 36.00 → Food Cost: 69.6%
- OPTIMAL: Verkaufspreis CHF 38.00 → Food Cost: 65.9%
- ALTERNATIVE: Kastanienpüree (Konserve) verwenden → Food Cost: ~35% bei CHF 18.00 ✅

---

## 1️⃣8️⃣ Crème Brûlée mit Vanille

**Verkaufspreis:** CHF 14.00 (6 Portionen) = CHF 2.33/Portion
**Kategorie:** Dessert

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Rahm | 500 | ml | 8.00/L | 0% | 0% | 1.00 | 4.00 |
| Eigelb (6 Eier) | 6 | Stk | 0.30/Stk | 0% | 0% | 1.00 | 1.80 |
| Zucker | 100 | g | 2.50/kg | 0% | 0% | 1.00 | 0.25 |
| Vanillezucker | 20 | g | 8.00/kg | 0% | 0% | 1.00 | 0.16 |
| Zucker (Karamell) | 60 | g | 2.50/kg | 0% | 0% | 1.00 | 0.15 |

**Wareneinsatz Total:** CHF 6.36
**Food Cost:** 45.4% ❌ **ETWAS ZU HOCH**

**Analyse:** Elegantes Dessert mit gutem Food Cost, aber knapp über Ziel.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 16.00 erhöhen → Food Cost: 39.8% ✓ OPTIMAL
- ALTERNATIVE: Bei CHF 14.00 akzeptabel (48% noch vertretbar für Dessert)

---

## 1️⃣9️⃣ Schweizer Schokoladenmousse

**Verkaufspreis:** CHF 15.00 (6 Portionen) = CHF 2.50/Portion
**Kategorie:** Dessert

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Zartbitter-Schokolade | 200 | g | 18.00/kg | 0% | 0% | 1.00 | 3.60 |
| Eier | 4 | Stk | 0.60/Stk | 0% | 0% | 1.00 | 2.40 |
| Rahm | 300 | ml | 8.00/L | 0% | 0% | 1.00 | 2.40 |
| Zucker | 50 | g | 2.50/kg | 0% | 0% | 1.00 | 0.13 |
| Butter | 30 | g | 12.00/kg | 0% | 0% | 1.00 | 0.36 |

**Wareneinsatz Total:** CHF 8.89
**Food Cost:** 59.3% ❌ **ZU HOCH**

**Analyse:** Schokoladen-Mousse mit gutem Verhältnis, aber über Ziel.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 18.00 erhöhen → Food Cost: 49.4%
- BESSER: Verkaufspreis CHF 20.00 → Food Cost: 44.5% ✓ OPTIMAL

---

## 2️⃣0️⃣ Apfelstrudel mit Vanillesauce

**Verkaufspreis:** CHF 12.00 (8 Portionen) = CHF 1.50/Portion
**Kategorie:** Dessert

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Mehl | 250 | g | 2.50/kg | 0% | 0% | 1.00 | 0.63 |
| Äpfel | 1000 | g | 4.00/kg | 20% | 0% | 1.25 | 5.00 |
| Semmelbrösel | 80 | g | 4.00/kg | 0% | 0% | 1.00 | 0.32 |
| Zucker | 120 | g | 2.50/kg | 0% | 0% | 1.00 | 0.30 |
| Rosinen | 80 | g | 12.00/kg | 0% | 0% | 1.00 | 0.96 |
| Butter | 100 | g | 12.00/kg | 0% | 0% | 1.00 | 1.20 |
| Zimt | 5 | g | 35.00/kg | 0% | 0% | 1.00 | 0.18 |
| Milch (Sauce) | 400 | ml | 1.80/L | 0% | 0% | 1.00 | 0.72 |
| Eigelb (3) | 3 | Stk | 0.30/Stk | 0% | 0% | 1.00 | 0.90 |
| Vanillezucker | 20 | g | 8.00/kg | 0% | 0% | 1.00 | 0.16 |

**Wareneinsatz Total:** CHF 10.37
**Food Cost:** 86.4% ❌ **VIEL ZU HOCH**

**Analyse:** Apfelstrudel mit Vanillesauce - sehr arbeitsintensiv, aber zu günstig.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 16.00 erhöhen → Food Cost: 64.8%
- BESSER: Verkaufspreis CHF 18.00 → Food Cost: 57.6%
- OPTIMAL: Verkaufspreis CHF 20.00 → Food Cost: 51.9% ✓

---

## 2️⃣1️⃣-2️⃣4️⃣ Beilagen (Rösti, Kartoffelstock, Spätzli, Salat)

**Rösti:** CHF 8.00 → Wareneinsatz CHF 2.29 → **Food Cost: 28.6% ✅ PERFEKT**

**Kartoffelstock:** CHF 6.00 → Wareneinsatz CHF 3.46 → **Food Cost: 57.7% ❌** → Preis auf CHF 8.00 → **43.3% ✅**

**Spätzli:** CHF 7.00 → Wareneinsatz CHF 2.01 → **Food Cost: 28.7% ✅ PERFEKT**

**Salat:** CHF 6.00 → Wareneinsatz CHF 2.35 → **Food Cost: 39.2% ✅ GUT**

---

## 2️⃣5️⃣ Toblerone-Mousse

**Verkaufspreis:** CHF 16.00 (6 Portionen) = CHF 2.67/Portion
**Kategorie:** Dessert

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Toblerone | 200 | g | 32.00/kg | 0% | 0% | 1.00 | 6.40 |
| Eier | 3 | Stk | 0.60/Stk | 0% | 0% | 1.00 | 1.80 |
| Rahm | 300 | ml | 8.00/L | 0% | 0% | 1.00 | 2.40 |
| Zucker | 40 | g | 2.50/kg | 0% | 0% | 1.00 | 0.10 |

**Wareneinsatz Total:** CHF 10.70
**Food Cost:** 66.9% ❌ **ZU HOCH**

**Analyse:** Toblerone als Swiss Icon ist teuer, aber Marketing-Wert hoch.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 20.00 erhöhen → Food Cost: 53.5%
- OPTIMAL: Verkaufspreis CHF 22.00 → Food Cost: 48.6% ✓

---

## 2️⃣6️⃣ Pizzoccheri (Buchweizennudeln)

**Verkaufspreis:** CHF 30.00 (4 Portionen) = CHF 7.50/Portion
**Kategorie:** Hauptgericht Vegetarisch

| Zutat | Menge | Einheit | Preis/Einheit | Rüst% | Gar% | Verlust-Faktor | Kosten CHF |
|-------|-------|---------|---------------|-------|------|----------------|------------|
| Pizzoccheri | 400 | g | 8.00/kg | 0% | 0% | 1.00 | 3.20 |
| Wirsing | 300 | g | 4.00/kg | 20% | 20% | 1.563 | 1.88 |
| Kartoffeln | 300 | g | 2.50/kg | 15% | 5% | 1.238 | 0.93 |
| Valtellina Casera | 200 | g | 26.00/kg | 0% | 0% | 1.00 | 5.20 |
| Parmesan | 100 | g | 32.00/kg | 0% | 0% | 1.00 | 3.20 |
| Butter | 120 | g | 12.00/kg | 0% | 0% | 1.00 | 1.44 |
| Knoblauch | 15 | g | 18.00/kg | 20% | 0% | 1.25 | 0.34 |
| Salbei | 10 | g | 100.00/kg | 15% | 0% | 1.176 | 1.18 |
| Salz | 5 | g | 2.00/kg | 0% | 0% | 1.00 | 0.01 |
| Pfeffer | 2 | g | 150.00/kg | 0% | 0% | 1.00 | 0.30 |

**Wareneinsatz Total:** CHF 17.68
**Food Cost:** 58.9% ❌ **ETWAS ZU HOCH**

**Analyse:** Authentisches Graubündner Gericht mit zwei Käsesorten.

**Optimierungs-Empfehlung:**
- Verkaufspreis auf CHF 34.00 erhöhen → Food Cost: 52.0%
- OPTIMAL: Verkaufspreis CHF 36.00 → Food Cost: 49.1% ✓

---

## 📊 ZUSAMMENFASSUNG FOOD COST VALIDIERUNG

### Food Cost Übersicht (26 Rezepte)

| # | Rezept | VK CHF | WE CHF | FC% | Status | Empfehlung |
|---|--------|--------|--------|-----|--------|------------|
| 1 | Berner Gerstensuppe | 22.00 | 15.37 | 69.9% | ❌ | → CHF 32.00 |
| 2 | Ceviche Forelle | 24.00 | 24.26 | 101.1% | ❌ | → CHF 48.00 |
| 3 | Kalbsleber Rösti | 42.00 | 32.75 | 78.0% | ❌ | → CHF 62.00 |
| 4 | Schweinsbäckli | 38.00 | 47.61 | 125.3% | ❌ | → CHF 78.00 |
| 5 | Rehrücken | 58.00 | 93.48 | 161.2% | ❌ | → CHF 158.00 |
| 6 | Dry-Aged Entrecôte | 52.00 | 145.01 | 278.9% | ❌ | → CHF 248.00 |
| 7 | Älplermagronen | 28.00 | 13.07 | 46.7% | ✅ | OK (ohne Schinken) |
| 8 | Fondue moitié-moitié | 32.00 | 32.98 | 103.1% | ❌ | → CHF 45.00 |
| 9 | Raclette | 35.00 | 7.29 | 20.8% | ✅ | **PERFEKT!** |
| 10 | Geschnetzeltes | 44.00 | 63.21 | 143.7% | ❌ | → CHF 88.00 |
| 11 | Hackbraten | 34.00 | 31.30 | 92.1% | ❌ | → CHF 48.00 |
| 12 | Risotto Steinpilze | 32.00 | 42.02 | 131.3% | ❌ | → CHF 62.00 |
| 13 | Carbonara | 28.00 | 14.83 | 53.0% | ⚠️ | → CHF 32.00 |
| 14 | Cannelloni | 30.00 | 19.08 | 63.6% | ❌ | → CHF 36.00 |
| 15 | Kalbsschnitzel | 46.00 | 46.28 | 100.6% | ❌ | → CHF 68.00 |
| 16 | Meringues | 16.00 | 8.65 | 54.1% | ⚠️ | → CHF 20.00 |
| 17 | Vermicelles | 18.00 | 25.05 | 139.2% | ❌ | → CHF 38.00 |
| 18 | Crème Brûlée | 14.00 | 6.36 | 45.4% | ✅ | OK |
| 19 | Schokomousse | 15.00 | 8.89 | 59.3% | ❌ | → CHF 20.00 |
| 20 | Apfelstrudel | 12.00 | 10.37 | 86.4% | ❌ | → CHF 20.00 |
| 21 | Rösti (Beilage) | 8.00 | 2.29 | 28.6% | ✅ | **PERFEKT!** |
| 22 | Kartoffelstock | 6.00 | 3.46 | 57.7% | ❌ | → CHF 8.00 |
| 23 | Spätzli (Beilage) | 7.00 | 2.01 | 28.7% | ✅ | **PERFEKT!** |
| 24 | Salat (Beilage) | 6.00 | 2.35 | 39.2% | ✅ | GUT |
| 25 | Toblerone-Mousse | 16.00 | 10.70 | 66.9% | ❌ | → CHF 22.00 |
| 26 | Pizzoccheri | 30.00 | 17.68 | 58.9% | ❌ | → CHF 36.00 |

---

### 🎯 KRITISCHE ERKENNTNISSE

**✅ Im Zielbereich (25-35%):** 3 Rezepte (11.5%)
- Raclette: 20.8% ⭐
- Rösti: 28.6% ⭐
- Spätzli: 28.7% ⭐

**⚠️ Grenzwertig (36-50%):** 3 Rezepte (11.5%)
- Salat: 39.2%
- Crème Brûlée: 45.4%
- Älplermagronen: 46.7%

**❌ Zu hoch (>50%):** 20 Rezepte (76.9%)
- Davon VERLUSTGESCHÄFTE (>100%): 9 Rezepte
- Katastrophal (>150%): 2 Rezepte (Rehrücken, Entrecôte)

---

### 💰 UMSATZ-IMPACT BEI ANPASSUNG

**Aktuell kalkuliert:**
- Durchschnittlicher VK: CHF 26.38
- Durchschnittlicher FC: 82.4% ❌

**Nach Optimierung:**
- Durchschnittlicher VK: CHF 40.12 (+52%)
- Durchschnittlicher FC: 54.2% ⚠️
- **Ziel-FC 30%:** VK müsste CHF 48.50 sein (+84%)

---

### ⚠️ HANDLUNGSEMPFEHLUNGEN

**1. SOFORTMASSNAHMEN (Kritisch):**
- **Dry-Aged Entrecôte:** CHF 52 → CHF 248 (+377%)
- **Rehrücken Wild:** CHF 58 → CHF 158 (+172%)
- **Schweinsbäckli:** CHF 38 → CHF 78 (+105%)
- **Vermicelles:** CHF 18 → CHF 38 (+111%)

**2. STRATEGISCHE ENTSCHEIDUNGEN:**
- Premium-Fleischgerichte (Kalb, Wild, Dry-Aged) MÜSSEN deutlich teurer verkauft werden
- Alternative: Portionsgrößen reduzieren
- Convenience-Produkte nutzen (TK-Spinat, Kastanienpüree, getrocknete Pilze)

**3. MARKTPOSITIONIERUNG:**
- Aktuelle Preise suggerieren "Budget-Restaurant"
- Food Concept suggeriert "Alpine Fine Dining"
- **KONFLIKT:** Preise und Konzept passen nicht zusammen!

---

**Status:** ⚠️ **FOOD COST VALIDIERUNG KOMPLETT - MASSIVE PREISANPASSUNGEN NÖTIG!**
