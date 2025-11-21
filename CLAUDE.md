# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projekt-Übersicht

**Hotel Dakota Food Concept 2025** - Ein umfassendes Restaurant-Konzept für das Hotel Dakota in Meiringen (Berner Oberland), inspiriert vom Restaurant Rosatsch im Engadin.

**Technologie-Stack:**
- Vanilla HTML5, CSS3, JavaScript (ES6)
- jsPDF für PDF-Generierung (CDN)
- Browser LocalStorage für Datenpersistierung
- Keine Build-Tools, kein Backend, keine Frameworks

**Philosophie:** "Alpine Berner Küche - Regional, Nachvollziehbar, Ehrlich"
- 90% Schweizer Produkte, 70% aus dem Berner Oberland
- Transparente Lieferantenkette
- Traditionelle Gerichte mit modernen Techniken
- Zugängliche Preisgestaltung (nicht elitär)

---

## ⚠️ KRITISCHES STATUS-UPDATE (03.11.2025)

**PROJEKT-STATUS: ON HOLD - WARTEND AUF KLÄRUNG**

### Situation
- **Datum:** 03. November 2025, vormittags
- **Ereignis:** Hotelbesitzer heute morgen verstorben
- **Konsequenz:** Alle Turnaround-Pläne und Investitionsentscheidungen auf unbestimmte Zeit verschoben

### Aktuelle Lage des Restaurants
- **Performance:** 1.6 Essen/Tag (8 Essen in 5 Tagen)
- **Soll-Performance:** 25-30 Essen/Tag (laut ursprünglichem Konzept)
- **Qualität:** 70-80% Convenience/Tiefkühlware
- **Team:** Unmotiviert, toxische Kultur
- **Equipment:** Massive Mängel (CHF 13.000-22.000 Investitionsbedarf)

### Marcel's Position
- **Anstellung:** Küchenchef, seit 1 Woche (seit ~27. Oktober 2025)
- **Rolle:** Neu im Team, kein etabliertes Vertrauensverhältnis
- **Arbeit investiert:** Komplettes Konzept erstellt, 3-Optionen-Turnaround-Plan entwickelt
- **Geplantes Meeting:** Mittwoch-Kadermeeting wurde gecancelt/verschoben

### Drei entwickelte Optionen (00_MEETING_MITTWOCH)

**Option 1: Soft-Relaunch**
- Kosten: CHF 15.000 / Timeline: 2 Wochen
- Ziel: 5-8 Essen/Tag → 10-15 nach 3 Monaten
- Erfolgswahrscheinlichkeit: 60%

**Option 2: Hard-Reset (WAR EMPFOHLEN)**
- Kosten: CHF 45.000 / Timeline: 6 Wochen
- Ziel: 15-20 Essen/Tag → 20-25 nach 3 Monaten
- Erfolgswahrscheinlichkeit: 75%
- ROI: 200-320% nach 18 Monaten

**Option 3: Aufgeben**
- Kosten: CHF 0-5.000 / Timeline: 2 Wochen
- Restaurant nur noch für Hotelgäste
- Erfolgswahrscheinlichkeit: 90% (aber kein Upside)

**Status aller Optionen:** NICHT UMSETZBAR bis neue Eigentümerverhältnisse geklärt sind

### Unbekannte Faktoren
- Wer erbt das Hotel? (Familie, Verkauf, Schließung?)
- Timeline für Klärung: 2-8 Wochen (rechtliche Prozesse)
- Wird neuer Eigentümer Restaurant weiterführen wollen?
- Werden Investitionen genehmigt werden?
- Bleibt Marcel im Hotel? (Arbeitsvertrag läuft weiter, aber Zukunft unklar)

### Dokumentation & Backup
- ✅ Komplettes Projekt auf private Festplatte gesichert
- ✅ Alle Konzepte, Menüs, Kalkulationen dokumentiert
- ✅ Turnaround-Plan in 00_MEETING_MITTWOCH vollständig ausgearbeitet
- ✅ Projekt ist "schlüsselfertig" und könnte bei anderen Hotels eingesetzt werden

### Nächste Schritte (Warten & Beobachten)
1. **Kurzfristig (1-7 Tage):**
   - Stabiler Basis-Betrieb aufrechterhalten
   - Informationen sammeln über neue Eigentümersituation
   - Team stabilisieren in unsicherer Zeit
   - Keine großen Änderungen initiieren

2. **Mittelfristig (2-4 Wochen):**
   - Klarheit über Hoteleigentum abwarten
   - Falls keine Perspektive: Alternative Job-Optionen prüfen
   - Projekt-Konzept ist wiederverwendbar für andere Hotels in Region

3. **Bei Klärung der Situation:**
   - **Szenario A:** Neue Eigentümer wollen investieren → Option 2 präsentieren
   - **Szenario B:** Neue Eigentümer wollen Status Quo → Option 1 oder Exit
   - **Szenario C:** Hotel wird verkauft/geschlossen → Exit, Konzept mitnehmen

### Referenz-Dokumente für Turnaround (bereit, sobald grünes Licht)
- `00_MEETING_MITTWOCH/01_IST_ANALYSE_TURNAROUND.md` - Schonungslose Bestandsaufnahme
- `00_MEETING_MITTWOCH/02_3_OPTIONEN_PLAN.md` - Drei Szenarien durchgerechnet
- `00_MEETING_MITTWOCH/03_EQUIPMENT_MANGELLISTE.md` - Was fehlt + Kosten
- `00_MEETING_MITTWOCH/04_SOFORTMASSNAHMEN.md` - Erste Woche Aktionen
- `00_MEETING_MITTWOCH/05_MEETING_PRESENTATION.md` - 35-Min Präsentation
- `00_MEETING_MITTWOCH/06_FAQ_KRITISCHE_FRAGEN.md` - 26 Fragen mit Antworten
- `00_MEETING_MITTWOCH/KADERMEETING_KOMPLETT.html` - Vollständige Meeting-Vorbereitung

**Status dieser Dokumente:** Vollständig vorbereitet, nicht präsentiert, wartend auf Gelegenheit

---

## Development Commands

### Anwendung starten
```bash
# Hauptanwendung (Offerten-Generator)
open dakota-offerten-generator.html

# Oder einfach Doppelklick auf die HTML-Datei
```

### Dokumentation bearbeiten
```bash
# Markdown-Dateien mit beliebigem Editor öffnen
code README.md
code 01_KONZEPTE/DAKOTA_FOOD_KONZEPT_2025_FINAL.md
code 02_MENUEKARTEN/ABENDKARTE_DAKOTA_2025.md
```

### Excel-Kalkulationen aktualisieren
```bash
# Excel-Dateien in 07_WARENWIRTSCHAFT/Kalkulation/
open "07_WARENWIRTSCHAFT/Kalkulation/MENU_KALKULATION_DAKOTA_2025_DESIGNED.xlsx"
```

**Wichtig:** Es gibt keine Build-, Test- oder Deployment-Commands. Alle Änderungen werden direkt in den Dateien gemacht und sind sofort wirksam.

## Code-Architektur

### Dakota Offerten Generator (`dakota-offerten-generator.html`)

**Single-File-Architecture:** Die gesamte Anwendung (HTML, CSS, JavaScript, Daten) ist in einer 2.525-Zeilen-Datei enthalten.

**Datenmodell (eingebettet):**
```javascript
const menuDatabase = {
    vorspeisen: [...],  // Appetizers mit Preis, Beschreibung, Badges
    hauptgerichte: [...], // Main courses
    desserts: [...],     // Desserts
    getraenke: [...],   // Beverage packages
    extras: [...]       // Additional services
};
```

**Badges-System:**
- 🌿 = Vegetarisch
- ⭐ = Signature Dish
- 💎 = Premium
- 🎨 = Creative/Innovative

**Kern-Komponenten:**

1. **Event-Handler (`initializeEventListeners`)** - Verwaltet alle UI-Interaktionen
2. **Price Calculator (`updatePreisAnzeige`)** - Berechnet Live-Preise pro Person + Total
3. **PDF Generator (`generatePDF`)** - Erstellt professionelle Offerten mit jsPDF
4. **LocalStorage Manager (`saveAngebot`, `loadAngebote`)** - Browser-basierte Persistierung
5. **Admin Panel** - CRUD-Operationen für Menü-Items (toggle mit Passwort-Konzept)

**Datenpersistierung:**
- Alle Offerten werden im Browser LocalStorage gespeichert
- Keine Cloud-Synchronisation
- Daten bleiben pro Browser/Gerät lokal

### Multi-Konzept Restaurant-Design

Das Projekt implementiert drei verschiedene Service-Konzepte:

1. **LUNCH (12:00-14:00)** - "Wanderer & Business"
   - Schneller Service (45 Min)
   - Preisbereich: CHF 24-38
   - Zielgruppe: Touristen, Geschäftsleute

2. **DINNER (18:30-21:30)** - "Alpine Fine Dining"
   - Erlebnis (90-120 Min)
   - Preisbereich: CHF 38-58
   - Zielgruppe: Genießer, besondere Anlässe

3. **APRÈS (15:00-18:00)** - "Brettljause & Bar"
   - Sharing Boards, Social Atmosphere
   - Getränkefokus mit Snacks

## Dateistruktur-Logik

**Nummeriertes Verzeichnissystem (01-10):**
```
01_KONZEPTE/         → Kern-Konzeptdokumente
02_MENUEKARTEN/      → Alle Menükarten (Abend, Mittag, Silvester, Weihnachten)
03_LIEFERANTEN/      → Supplier-Netzwerk
04_PACKAGES/         → Angebots-Packages
05_CHECKLISTEN/      → Implementierungs-Checklisten
06_REZEPTE/          → Rezepturen (Vorspeisen, Hauptgerichte, Desserts, Saucen)
07_WARENWIRTSCHAFT/  → Kalkulation, Inventar, Bestellungen
08_TEAM/             → Dienstpläne, Schulungen
09_DOKUMENTATION/    → Fotos, Präsentationen, Social Media
10_ARCHIV/           → Archivierte Dateien
```

**Versionierung:**
- Keine Git-Versionskontrolle
- Manuelle Versionierung über Dateinamen (`_2025`, `_FINAL`, `_UPDATE`)

## Wichtige Konventionen

### Naming Conventions

**Dateien & Verzeichnisse:** UPPERCASE mit Unterstrichen
```
DAKOTA_FOOD_KONZEPT_2025_FINAL.md
ABENDKARTE_DAKOTA_2025.md
02_MENUEKARTEN/
```

**JavaScript-Variablen:** camelCase
```javascript
selectedVorspeise
currentAnzahlPersonen
updatePreisAnzeige()
```

**CSS-Klassen:** kebab-case
```css
.menu-grid
.admin-panel
.price-display
```

### Preisstrategie

**Ziel Food Cost:** 28-35%

**Preisbereiche:**
- Vorspeisen (Abend): CHF 20-28
- Hauptgerichte (Abend): CHF 38-58
- Desserts: CHF 16-22
- 4-Gang-Menü: CHF 95
- 6-Gang-Degustation: CHF 145

**Kalkulations-Logik:**
- Wareneinsatz wird in Excel detailliert berechnet
- Siehe: `07_WARENWIRTSCHAFT/Kalkulation/MENU_KALKULATION_DAKOTA_2025_DESIGNED.xlsx`
- Break-Even nach 1,6 Monaten geplant
- Umsatzziel: CHF 87.000/Monat

### Code-Patterns im Offerten-Generator

**Admin-Panel Toggle:**
```javascript
// Admin-Bereich ist standardmäßig ausgeblendet
// Toggle mit Konzept für Passwort-Schutz
```

**Responsive Grid:**
```css
.menu-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1rem;
}
```

**PDF-Generierung:**
- Professional Layout mit Hotel-Branding
- Automatische Preisberechnung
- Detaillierte Auflistung aller Positionen
- Kontaktinformationen Footer

## Wichtige Referenzen

### Primäre Dokumentation

1. **README.md** - Projekt-Übersicht, Philosophie, nächste Schritte
2. **README_OFFERTEN_GENERATOR.md** - Vollständiges User-Manual für die Web-App (349 Zeilen)
3. **DAKOTA_FOOD_KONZEPT_2025_FINAL.md** - Kern Food Concept (429 Zeilen)

### Konzept-Dokumente

4. **ROSATSCH_INSPIRATION.md** - Inspirations-Quelle aus dem Engadin
5. **CHECKLISTE_UMSETZUNG_DAKOTA.md** - 6-Phasen Implementierungsplan (11 Wochen)
6. **LIEFERANTEN_NETZWERK_BERNER_OBERLAND.md** - Vollständiges Lieferanten-Verzeichnis

### Menü-Dokumentation

7. **ABENDKARTE_DAKOTA_2025.md** - Abendkarte mit 14 voll entwickelten Gerichten
8. **MITTAGSKARTE_DAKOTA_2025.md** - Mittagskarte mit 10 Gerichten
9. **Spezial-Menüs:** Weihnachten, Silvester, Winter-Klassiker (Dez-Feb)

### Business-Dokumente

10. **KALKULATION_ALLE_MENUES_DAKOTA_2025.csv** - Alle Menü-Kostenkalkulationen
11. **MENU_KALKULATION_DAKOTA_2025_DESIGNED.xlsx** - Excel-Kostenmodell

## Implementierungs-Status

**Aktuelle Phase:** Phase 1-2 von 6 (Vorbereitung & Lieferanten-Setup)

**11-Wochen Rollout-Plan:**
- Woche 1-2: Lieferanten-Verträge, Team-Rekrutierung
- Woche 3-4: Menü-Testing, Rezeptur-Finalisierung
- Woche 5-6: Team-Training, Soft Opening
- Woche 7-8: Marketing-Launch, Social Media
- Woche 9-10: Optimierung basierend auf Feedback
- Woche 11: Review & Finalisierung

**Offene Aufgaben:**
- Lieferanten-Verhandlungen abschließen
- Team-Schulungen durchführen
- Marketing-Materialien erstellen
- Soft-Opening planen

## Technische Limitationen

**Bekannte Einschränkungen:**
- Keine Multi-User-Unterstützung
- Keine Cloud-Synchronisation (LocalStorage only)
- Keine automatischen Updates
- Skalierung limitiert durch eingebettetes Datenmodell
- Browser-Kompatibilität erfordert ES6-Support

**Warum diese Architektur sinnvoll ist:**
- Keine Server-Kosten
- Funktioniert offline nach erstem CDN-Load
- Einfach zu deployen (Email/USB)
- Keine Wartungskomplexität
- Portabel und unabhängig

## Änderungen vornehmen

### Dokumentation aktualisieren
1. Markdown-Datei in entsprechendem Verzeichnis öffnen
2. Direkt bearbeiten
3. Speichern - fertig

### Web-App anpassen
1. `dakota-offerten-generator.html` in Text-Editor öffnen
2. JavaScript/CSS/HTML direkt bearbeiten
3. Im Browser öffnen und testen
4. Speichern und kopieren für Deployment

### Menü-Items hinzufügen/ändern
1. Im `menuDatabase` JavaScript-Objekt bearbeiten (ca. Zeile 200-800)
2. Struktur beibehalten:
```javascript
{
    name: "Gericht-Name",
    preis: 45,
    beschreibung: "Detaillierte Beschreibung",
    badges: ["🌿", "⭐"]  // Optional
}
```

### Kalkulationen aktualisieren
1. Excel-Datei öffnen: `07_WARENWIRTSCHAFT/Kalkulation/MENU_KALKULATION_DAKOTA_2025_DESIGNED.xlsx`
2. Preise/Mengen anpassen
3. Food Cost automatisch berechnen lassen
4. Bei Bedarf CSV exportieren für Archivierung

## Lieferanten-Netzwerk

**Hauptlieferanten (8 Partner):**
- Meat & More (Fleisch, Wildbret)
- Käserei Reichenbach (Käse)
- Gemüsegarten Berner Oberland (Gemüse)
- Fischhandel Bern (Fisch)
- Bäckerei Imboden Meiringen (Brot)
- Getränke Fuchs AG (Wein, Spirituosen)
- Too Good To Go (Nachhaltigkeits-Partner)

**Beschaffungs-Prinzip:** 90% Schweiz, 70% Berner Oberland, 100% nachvollziehbar

## Support & Kontakt

Bei Fragen zur Anwendung oder zum Konzept:
- Siehe README_OFFERTEN_GENERATOR.md für detaillierte Anleitung
- Siehe CHECKLISTE_UMSETZUNG_DAKOTA.md für Implementierungs-Steps
- Lieferanten-Kontakte in LIEFERANTEN_NETZWERK_BERNER_OBERLAND.md
