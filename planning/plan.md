# Exposé mit:

- Kurzbeschreibung (ca. 0,4375 - 1,0 DinA4-Seite)
- Was wäre ein ideales Ergebnis, was wäre ein minimales Projektziel?
- grobe Zeitplanung
- geplante Arbeitsweise
- grobe Gliederung des GitHub-Repositorium
- ergänzen Sie, was Ihnen überdies wichtig erscheint
- Nötige Ressourcen
- Alles auf GitHub

- 2. Bacterial into ORKG (Textmining)
  - GC content 
  - Sigma factors
  - Transcription factors
  - => Emirhan, Massaman, Bahri und Benedikt

# Projektidee:
- Wie unterscheidet sich der gc Gehalt unter verschiedenen Umständen/Bedingungen?
- Als Beispiel:
  - Kontinente/Regione
  - Menschen und Tiere
- Analyse der verschiedenen Ergebnisse nach Unterschieden oder Auffälligkeiten

Verbesserung der Sichtbarkeit vom Gc-Gehalt wollen wir Daten in ORKG sichtbar machen. Als Source Datenbank nutzen wir pubmed, da diese auf auf medizinische Daten spezialisiert und große Datenmengen zum GC-Content vorhanden sind.
Um Daten/Informationen aus pubmed zu beziehen wollen wir die verschiedenen Elemente und Methoden aus dem Text Mining Bereich anwenden.
Geplant sind sowohl allgemeine als auch fachspezifische Daten. Beispiele hierfür sind Titel, Erscheinungsjahr etc. oder der GC-Gehalt. Ideal wäre dabei, wenn wir den GC-Gehalt konkret für verschiedene Lebewesen oder auch Umstände aus pubmed entnehmen können, um die in ORKG einzuspeisen. Eine Kernfrage ist dabei, ob und wie man die Studien über die verschiedenen GC-Gehälter sinvoll miteinander vergleicht. 
Die Vorangehensweise bei dem Entnehmen der Daten aus pubmed umfasst das Webscraping. Die Daten speichen wir in eine csv-Datei und nutzen sie für den Upload in ORKG.
Neben der Verlinkung des originalen Dokuments werden auch Metadaten angezeigt.


# SMARTE Zielsetzung
## Minimales Projektziel:

- Spezifisch: Daten? zum GC-Gehalt aus pubmed über einen automatischen Prozess in ORKG einspeisen. 
- Messbar: **Einmalig** sollen Daten in ORKG aus pubmed eingelesen werden. 
- Akzeptiert: Mit unserem Projekt ermöglichen wir die bessere Vergleichbarkeit von wissenschaftlichen Artikeln zu GC-Werten.  
- Realisierbar: Das Ziel ist erreicht, wenn **10%** der möglichen Daten in ORKG dargestellt werden.
- Terminiert: Das Ziel soll zum 12.07.2023 erreicht werden.

## Ideales Ergebnis:
- Spezifisch: Daten? zum GC-Gehalt aus pubmed über einen automatischen Prozess in ORKG einspeisen. 
- Messbar: **Monatlich** sollen Daten in ORKG aus pubmed eingelesen werden. 
- Akzeptiert: Mit unserem Projekt ermöglichen wir die bessere Vergleichbarkeit von wissenschaftlichen Artikeln zu GC-Werten.  
- Realisierbar: Das Ziel ist erreicht, wenn **20%** der möglichen Daten in ORKG dargestellt werden.
- Terminiert: Das Ziel soll zum 12.07.2023 erreicht werden.

## Nötige Ressourcen:
- Zugang zu pubmed und ORKG
- Virtuellen Server / Docker (monatlich automatisch laufender Prozess)

# Zeitplanung:
1. Daten aus pubmed mittels webscraping entnehmen und in einer CSV-Datei speichern.
  - Python Script erstellen
  - bestimmen welche Daten aus pubmed entnommen werden sollen
2. Generalisieren/Normieren der Daten um diese miteinander vergleichen zu können.
  - Analyse der Daten mithilfe der Kenntnisse aus dem Studium (bsp. Statistik)
3. Ausgewählte Daten in ORKG hochladen und diese präsentieren.
4. Prozess für automatisierte Übertragung der Daten von pubmed zu ORKG planen.

# TO DO:
- Fachliches Verständnis für das Themengebiet (GC-Gehalt) aufbauen
- Grobe Zeitplanung, angelehnt an agile Arbeitsweise (auch Meilensteine)
- (Projektidee konkretisieren)
- Mit Herr Förstner klären, was mit "geplante Arbeitsweise" gemeint ist.
- Nach Best Practises zu Text Mining suchen und ermitteln (Beispiel eines anderen Git-Repo zu Textmining mit in Betracht ziehen)


# Update unserer Planung:
Der Projektumfang wurde nocheinmal konkretisiert. Es werden nur nach GC-Gehältern in Prozent für Bakterien gesucht. Die Daten werden nur aus dem Abstract der Studie entnommen. Zudem haben wir noch folgende Änderungen in der Zielformulierung vorgenommen:
## Minimales Projektziel:

- Realisierbar: Das Ziel ist erreicht, wenn Daten aus 10 Studien aus pubmed in ORKG dargestellt werden.

## Ideales Ergebnis:

- Realisierbar: Das Ziel ist erreicht, wenn Daten aus 20 Studien aus pubmed in ORKG dargestellt werden.
