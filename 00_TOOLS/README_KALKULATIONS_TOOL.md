# Dakota Kalkulations-Tool

**Professional Food Cost Management System**

Version 1.0 | Erstellt am 18. November 2025

---

## 📋 Übersicht

Das Dakota Kalkulations-Tool ist eine professionelle, browserbasierte Anwendung zur Verwaltung von Lebensmitteln, Rezepten und Kalkulationen für die Gastronomie.

### Features

- ✅ **Lebensmittel-Datenbank** mit Kategorien, Preisen, Verlustfaktoren
- ✅ **Rezept-Verwaltung** mit Zutaten-Verknüpfung
- ✅ **Automatische Kalkulation** mit Rüst- und Garverlust
- ✅ **Rezept-Skalierung** (1-1000 Personen)
- ✅ **Einkaufslisten-Generator** nach Kategorien gruppiert
- ✅ **Food Cost Berechnung** mit Farbindikatoren
- ✅ **Offline-fähig** - IndexedDB lokale Speicherung
- ✅ **Responsive Design** - funktioniert auf allen Geräten
- ✅ **Dakota Branding** - professionelles Design

---

## 🚀 Quick Start

### 1. Tool öffnen

Einfach die Datei `dakota-kalkulations-tool.html` im Browser öffnen:
- **Doppelklick** auf die Datei
- Oder: **Rechtsklick → Öffnen mit → Browser wählen**

### 2. Beispiel-Daten laden

Beim ersten Start wird gefragt, ob Beispiel-Daten geladen werden sollen:
- ✅ **Ja** → 5 Beispiel-Lebensmittel werden hinzugefügt
- ❌ **Nein** → Leer starten und selbst eingeben

### 3. Erste Schritte

1. **Tab "Lebensmittel"** → Neue Lebensmittel hinzufügen
2. **Tab "Rezepte"** → Rezept erstellen mit Zutaten
3. **Tab "Kalkulation"** → Rezept auswählen und kalkulieren
4. **Tab "Einkaufsliste"** → Mehrere Rezepte wählen und Liste generieren

---

## 📚 Bedienungsanleitung

### 🥕 LEBENSMITTEL-DATENBANK

#### Gastro-Datenbank importieren (180 Produkte)

**NEU:** Sie können die vorgefertigte Gastro-Datenbank mit 180 Produkten aus dem Berner Oberland mit einem Klick importieren!

1. Button **"📥 Gastro-Datenbank (180 Produkte)"** klicken
2. Bestätigungs-Dialog erscheint mit Übersicht:
   - 180 Produkte aus Berner Oberland
   - Fleisch, Fisch, Käse, Gemüse, Gewürze, etc.
   - Mit realistischen Preisen (CHF)
   - Mit Verlustfaktoren (Rüst-/Garverlust)
   - Mit lokalen Lieferanten
3. **"OK"** klicken zum Starten
4. Progress-Bar zeigt Fortschritt (ca. 5-10 Sekunden)
5. Fertig! Alle 180 Produkte sind jetzt in der Datenbank

**Wichtig:**
- Der Import fügt Produkte hinzu (löscht keine bestehenden)
- Bei Bedarf können Sie nach dem Import Duplikate manuell löschen
- Die Datei `dakota-gastro-produkte-datenbank.json` muss im selben Verzeichnis wie das Tool liegen

**Enthaltene Lieferanten:**
- H&R Gastro AG (Interlaken)
- Metzgerei Christian Nussbaum (Meiringen)
- Alpkäserei Engstlenalp
- Käserei Meiringen
- Bio-Hof Hasliberg
- Forellenzucht Reichenbach
- Obstgarten Brienz
- Transgourmet Moosseedorf

#### Lebensmittel manuell hinzufügen

1. Button **"➕ Neues Lebensmittel"** klicken
2. Formular ausfüllen:
   - **Name** (Pflicht): z.B. "Rindsfilet"
   - **Kategorie** (Pflicht): z.B. "Fleisch"
   - **Preis pro Einheit** (Pflicht): z.B. 65.00 (CHF/kg)
   - **Einheit** (Pflicht): kg, L oder Stk
   - **Rüstverlust**: z.B. 5% (optional)
   - **Garverlust**: z.B. 25% (optional)
   - **Lieferant**: z.B. "Metzgerei Trachsel" (optional)
   - **Bemerkungen**: Zusatzinfos (optional)
3. **"💾 Speichern"** klicken

#### Verlustfaktoren verstehen

**Rüstverlust:**
- Verlust beim Vorbereiten (Schälen, Putzen, Trimmen)
- Beispiel: Kartoffeln 15% (Schalen)
- Berechnung: Brutto-Menge = Netto-Menge / (1 - Rüstverlust/100)

**Garverlust:**
- Gewichtsverlust beim Kochen/Braten
- Beispiel: Rindsfilet 25% (Wasser, Fett)
- Wird zusätzlich zum Rüstverlust angewendet

#### Suchen & Filtern

- **Suchfeld**: Name, Kategorie oder Lieferant eingeben
- **Dropdown**: Nach spezifischer Kategorie filtern

#### Lebensmittel bearbeiten/löschen

- **Stift-Icon (✏️)**: Bearbeiten
- **Mülleimer-Icon (🗑️)**: Löschen (mit Bestätigung)

---

### 📖 REZEPT-DATENBANK

#### Neues Rezept erstellen

1. Button **"➕ Neues Rezept"** klicken
2. **Rezept-Details** eingeben:
   - Name: z.B. "Älplermagronen"
   - Kategorie: Vorspeise, Hauptgang, etc.
   - Portionen: z.B. 1 (für 1 Person)
   - Verkaufspreis: CHF pro Portion
   - Beschreibung (optional)

3. **Zutaten hinzufügen**:
   - Button **"➕ Zutat hinzufügen"** klicken
   - Lebensmittel aus Dropdown wählen
   - Menge eingeben (z.B. 200)
   - Einheit wählen (g, ml, Stk)
   - Weitere Zutaten hinzufügen
   - Zutat löschen mit 🗑️-Button

4. **"💾 Rezept speichern"** klicken

#### Rezept-Tabelle verstehen

Die Tabelle zeigt:
- **Wareneinsatz**: Automatisch berechnet (inkl. Verluste!)
- **Food Cost**: In % mit Farbindikator
  - 🟢 **< 30%**: Excellent (grün)
  - 🟡 **30-35%**: Good (gelb)
  - 🔴 **> 35%**: Warning (rot)

#### Rezept anzeigen/bearbeiten/löschen

- **Auge-Icon (👁️)**: Details anzeigen
- **Stift-Icon (✏️)**: Bearbeiten
- **Mülleimer-Icon (🗑️)**: Löschen

---

### 💰 KALKULATION

#### Rezept kalkulieren

1. **Rezept auswählen** aus Dropdown
2. **Anzahl Personen** eingeben (1-1000)
3. **Verkaufspreis** anpassen (optional)
4. → Automatische Berechnung!

#### Kalkulations-Details

Die Tabelle zeigt für jede Zutat:
- **Netto-Menge**: Für X Personen skaliert
- **Rüstverlust**: Angewendeter Prozentsatz
- **Garverlust**: Angewendeter Prozentsatz
- **Brutto-Menge**: Benötigte Einkaufsmenge (inkl. Verluste!)
- **Wareneinsatz**: Kosten dieser Zutat

#### Ergebnis-Box

Zeigt:
- **Wareneinsatz Total**: Summe aller Zutaten
- **Verkaufspreis Total**: Für alle Personen
- **Food Cost %**: Wareneinsatz / Verkaufspreis
- **Deckungsbeitrag**: Verkaufspreis - Wareneinsatz

#### Aktionen

- **📄 Als PDF exportieren**: Kalkulation als PDF speichern (kommt bald)
- **💾 Kalkulation speichern**: Im LocalStorage speichern

---

### 🛒 EINKAUFSLISTE

#### Einkaufsliste generieren

1. **Rezepte auswählen**: Checkboxen aktivieren (mehrere möglich!)
2. Button **"✨ Einkaufsliste generieren"** klicken
3. → Liste wird nach **Kategorien gruppiert** angezeigt

#### Was zeigt die Liste?

- **Nach Kategorie sortiert**: Fleisch, Gemüse, Käse, etc.
- **Zusammengefasste Mengen**: Gleiche Zutaten werden summiert
- **Lieferant**: Für jeden Artikel angezeigt

**Beispiel:**
```
KÄSE
- Alpkäse: 180g (Alpkäserei Engstlenalp)
- Parmesan: 45g (-)

GEMÜSE
- Kartoffeln: 350g (Bio-Hof Hasliberg)
- Zwiebeln: 85g (Bio-Hof Hasliberg)
```

#### Aktionen

- **📄 Als PDF exportieren**: Liste als PDF (kommt bald)
- **🖨️ Drucken**: Browser-Druckdialog öffnen

---

## ⚙️ Technische Details

### Technologie

- **HTML5** + **CSS3** + **JavaScript ES6**
- **IndexedDB** für lokale Datenbank
- **Google Fonts**: Playfair Display, Lato
- **jsPDF** für PDF-Export (CDN)
- **Single-File-Architecture**: Alles in einer Datei!

### Browser-Kompatibilität

Funktioniert in:
- ✅ Chrome / Edge (empfohlen)
- ✅ Firefox
- ✅ Safari
- ❌ Internet Explorer (nicht unterstützt)

**Mindest-Version:** Chrome 60+, Firefox 55+, Safari 11+

### Datenspeicherung

- **Datenbank**: IndexedDB `DakotaKalkulationDB`
- **Stores**:
  - `lebensmittel`: Alle Lebensmittel-Stammdaten
  - `rezepte`: Alle Rezepte mit Zutaten
- **Speicherort**: Lokal im Browser
- **Größe**: Unbegrenzt (nur durch Browser-Speicher limitiert)

### Daten-Export/Import

**Export:**
- Browser-DevTools → Application → IndexedDB → Daten kopieren
- Oder: LocalStorage Backup-Funktion (kommt bald)

**Import:**
- CSV-Import-Funktion (geplant)
- JSON-Import über Browser-Konsole (fortgeschritten)

---

## 📊 Kalkulationslogik

### Preis-Berechnung mit Verlust

```
Beispiel: Rindsfilet (CHF 65/kg, 5% Rüst, 25% Garverl ust)

Netto-Menge: 180g (gewünschte Portion)

Schritt 1: Rüstverlust
Brutto nach Rüsten = 180g / (1 - 0.05) = 189.5g

Schritt 2: Garverlust
Brutto nach Garen = 189.5g / (1 - 0.25) = 252.7g

→ Einkaufsmenge: 253g
→ Wareneinsatz: 0.253kg × CHF 65 = CHF 16.45
```

### Food Cost Ziele

- **Excellent**: < 30%
- **Good**: 30-35%
- **Warning**: > 35%

**Formel:**
```
Food Cost % = (Wareneinsatz / Verkaufspreis) × 100
```

### Skalierung

**Faktor-Berechnung:**
```
Faktor = Ziel-Portionen / Original-Portionen

Neue Menge = Original-Menge × Faktor
```

**Beispiel:**
- Rezept: 1 Portion, 180g Rindsfilet
- Ziel: 50 Portionen
- Faktor: 50 / 1 = 50
- Neue Menge: 180g × 50 = 9000g = 9kg

---

## 🎨 Design-Elemente

### Farben (Dakota Branding)

- **Gold**: #dba765 (Primär-Akzent)
- **Dark**: #32373c (Text, Header)
- **Light**: #f5f5f5 (Hintergrund)
- **Success**: #28a745 (< 30% Food Cost)
- **Warning**: #ffc107 (30-35% Food Cost)
- **Danger**: #dc3545 (> 35% Food Cost)

### Icons

- 🥕 Lebensmittel
- 📖 Rezepte
- 💰 Kalkulation
- 🛒 Einkaufsliste
- ✏️ Bearbeiten
- 🗑️ Löschen
- 👁️ Anzeigen
- 💾 Speichern
- 📄 PDF

---

## 🔧 Troubleshooting

### Problem: Datenbank lädt nicht

**Lösung:**
- Browser-Cache leeren
- IndexedDB in DevTools löschen
- Seite neu laden

### Problem: Rezept zeigt keinen Wareneinsatz

**Mögliche Ursachen:**
1. Lebensmittel wurde gelöscht → Rezept bearbeiten, Zutat neu wählen
2. Preis = 0 → Lebensmittel bearbeiten, Preis eingeben

### Problem: Food Cost zu hoch

**Optimierungs-Tipps:**
1. Verlustfaktoren prüfen (zu hoch gesetzt?)
2. Günstigere Lieferanten suchen
3. Portionsgröße anpassen
4. Verkaufspreis erhöhen

### Problem: Beispiel-Daten erscheinen nicht

**Lösung:**
- F5 drücken (Seite neu laden)
- Oder: Lebensmittel manuell hinzufügen

---

## 📈 Best Practices

### Lebensmittel-Datenbank

1. **Konsistente Einheiten**: Preise immer pro kg/L, Mengen in g/ml
2. **Realistische Verluste**: Aus Erfahrung oder Fachliteratur
3. **Lieferanten pflegen**: Für Einkaufslisten wichtig
4. **Kategorien nutzen**: Erleichtert Suche und Filter

### Rezepte

1. **Standard-Portionen**: 1 Person als Basis (einfacher zu skalieren)
2. **Alle Zutaten**: Auch Gewürze, Öl etc. erfassen
3. **Beschreibung**: Kurze Notizen zu Besonderheiten
4. **Verkaufspreis**: Immer aktuell halten

### Kalkulation

1. **Regelmäßig überprüfen**: Preise ändern sich!
2. **Food Cost tracken**: Monatlicher Durchschnitt
3. **Saisonalität**: Im Winter andere Preise als Sommer
4. **Portionsgrößen**: Bei Events oft kleiner (Degustation)

---

## 🛠️ Geplante Features

### Version 1.1 (Q1 2026)

- [ ] PDF-Export für Kalkulationen
- [ ] PDF-Export für Einkaufslisten
- [ ] CSV-Import für Lebensmittel
- [ ] Backup/Restore-Funktion
- [ ] Druck-Optimierung

### Version 1.2 (Q2 2026)

- [ ] Lieferanten-Verwaltung
- [ ] Preishistorie
- [ ] Menü-Zusammenstellung (mehrere Gänge)
- [ ] Kostenstellen-Tracking
- [ ] Statistik-Dashboard

### Version 2.0 (Q3 2026)

- [ ] Cloud-Synchronisation
- [ ] Multi-User-Support
- [ ] Mobile App (iOS/Android)
- [ ] API-Integration (Lieferanten)
- [ ] Barcode-Scanner

---

## 💡 Tipps & Tricks

### Schnell-Suche

- **Suchfeld nutzen**: Schneller als Scrollen
- **Filter kombinieren**: Suchfeld + Kategorie-Dropdown

### Batch-Eingabe

- Mehrere ähnliche Lebensmittel hintereinander eingeben
- Copy-Paste für wiederkehrende Lieferanten

### Einkaufsliste optimieren

- Rezepte mit gleichen Zutaten zusammen wählen
- Nach Lieferant sortieren (geplant)

### Food Cost senken

1. Verluste minimieren (bessere Vorbereitung)
2. Saisonale Produkte nutzen
3. Größere Mengen einkaufen (Rabatt)
4. Alternative Zutaten testen

---

## 📞 Support & Feedback

### Dokumentation

- Diese README-Datei
- CLAUDE.md (technische Details)
- Inline-Hilfe im Tool (Tooltips)

### Fragen?

Kontaktiere den Entwickler oder erstelle ein Issue im Projekt-Repository.

---

## 📄 Lizenz & Credits

**Entwickelt für:** Hotel Dakota, Meiringen
**Entwickler:** Marcel Gärtner (mit Claude Code)
**Version:** 1.0
**Datum:** 18. November 2025

**Verwendete Libraries:**
- [jsPDF](https://github.com/parallax/jsPDF) - MIT License
- [Google Fonts](https://fonts.google.com/) - Open Font License

---

## 🎉 Los geht's!

Öffne `dakota-kalkulations-tool.html` und starte mit der Kalkulation!

**Viel Erfolg mit dem Dakota Kalkulations-Tool! 🚀**
