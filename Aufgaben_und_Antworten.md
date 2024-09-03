# jobRad-coding-challenge-DevEx

## Rahmenbedingungen:
- [x] Bitte die Aufgabe selbstständig und allein lösen, natürlich darf dabei Literatur und / oder das Internet benutzt 
werden. 
- [x] Bitte teile uns deine Bearbeitungszeit mit:
```
Der erste Commit war gegen 15 Uhr, während der letzte bedeutende Commit kurz vor 24 Uhr desselben Tages stattfand. Somit 
vergingen insgesamt etwa 9 Stunden vom ersten bis zum letzten Commit. Natürlich habe ich mich in dieser Zeit nicht 
ununterbrochen mit dem Projekt beschäftigt. Ich habe gearbeitet, war beim Sport und habe auch einige Hausarbeiten erledigt.

Grob geschätzt kann man die Aufwände folgendermaßen einteilen:

- Vorbereitung des Git-Repositories, des virtuellen Umfelds, der Ordner- und Dateistruktur - 15 Minuten.
- Implementierung der ersten Basisversion der Funktion „merge_intervals“ - 25 Minuten.
- Hinzufügen von Kommentaren und Docstrings - 10 Minuten.
- Schreiben der Tests - 20 Minuten.
- Hinzufügen von Validitätsprüfungen für die Eingabedaten - 10 Minuten.
- Hinzufügen von Skripten für den Start auf verschiedenen Plattformen - 60 Minuten.
- Hinzufügen der README.md - 20 Minuten.
- Implementierung verschiedener Eingabemethoden + Kommentare - 40 Minuten.
- Änderung der main-Funktion für die Arbeit mit verschiedenen Eingabeoptionen - 10 Minuten.
- Hinzufügen von Tests - 15 Minuten.
- Testen auf verschiedenen Plattformen und entsprechende Anpassungen - 10 Minuten.

Insgesamt habe ich etwa 4 Stunden reine Arbeitszeit aufgewendet (dazu gehören auch die Suche nach Lösungen, Googeln, 
Debuggen und Testen).
```

- [x] Die Lösung hätten wir gerne als GitHub Repository.
- [x] Die Programmiersprache ist frei wählbar, wobei eine ‘gewöhnliche’ Sprache bevorzugt wäre.
- [x] Das Resultat muss von uns gebaut und ausgeführt werden können. Bitte entsprechende Build-Scripte oder Makefiles 
bereitstellen.
- [x] Eigene Annahmen und wichtige Implementierungsdetails bitte klar kommentieren.
- [x] Eventuelle sinnvolle Zwischenergebnisse dürfen gern als separater Git commit vorliegen.
- [x] Genauso wichtig wie das lauffähige Programm ist die Dokumentation (readme und code comments) der Lösungsidee 
und der einzelnen Programmteile und Tests.

Das Hauptziel ist es, dass wir erleben, wie Du Software in einem professionellen Umfeld entwickelst. Die gesamte 
Bearbeitungsdauer sollte max. 1-2 Tage sein.

---
## Aufgabe:
Implementiere eine Funktion MERGE die eine Liste von Intervallen entgegennimmt und als Ergebnis wiederum eine Liste von 
Intervallen zurückgibt. Im Ergebnis sollen alle sich überlappenden Intervalle gemerged sein. Alle nicht überlappenden 
Intervalle bleiben unberührt.

**Beispiel**: Input: [25,30] [2,19] [14, 23] [4,8] Output: [2,23] [25,30]

---
## Fragen
- Wie ist die Laufzeit deines Programms?
```
Die Laufzeit des Programms wird hauptsächlich durch den Algorithmus zum Zusammenführen 
von Intervallen bestimmt. Die größte Rechenkomplexität entsteht durch das Sortieren der Intervalle, 
was eine Zeit von O(n log n) benötigt, wobei n die Anzahl der Intervalle ist. 
Nach dem Sortieren durchläuft der Algorithmus die Liste der Intervalle einmal, 
was eine lineare Komplexität von O(n) hat. Daher beträgt die gesamte Laufzeit des Algorithmus 
O(n log n) aufgrund des Sortierschritts. Das bedeutet, dass die Laufzeit logarithmisch mit der 
Anzahl der Intervalle steigt.
```
- Wie kann die Robustheit sichergestellt werden, vor allem auch mit Hinblick auf sehr große Eingaben?
```
Um die Robustheit des Programms bei der Verarbeitung großer Datenmengen zu gewährleisten, 
können folgende Maßnahmen ergriffen werden:

1. Ausnahmebehandlung: Die Implementierung von Fehlerbehandlungen hilft, 
Programmabstürze zu vermeiden und ermöglicht es, Fehler während der Ausführung korrekt zu melden.
Z.B.:
- Fehlerbehandlung beim Dateilesen
- Protokollierung
- Benutzeroberfläche zur Fehlerbehandlung

2. Speicheroptimierung:
Z.B.:
- Effiziente Datenstrukturen (schon implementiert mit tuples) 
- Lazy Loading von Daten (mit Generatoren oder Iteratoren)
- Verwendung von In-Place-Algorithmen

3. Leistungstests: 
Regelmäßige Durchführung von Leistungstests und Stresstests hilft dabei, 
Engpässe und potenzielle Fehler bei der Verarbeitung großer Datenmengen zu identifizieren.

```
- Wie verhält sich der Speicherverbrauch deines Programms?
```
Der Speicherverbrauch des Programms hängt von der Anzahl und Größe der verarbeiteten Intervalle ab. 
Da jedes Intervall als Tupel im Speicher gehalten wird, hängt der Hauptteil 
des Speicherverbrauchs linear von der Anzahl der Intervalle ab. Zusätzlicher Speicher wird 
auch für die Datenstrukturen benötigt, wie die Liste für das Sortieren und die Liste 
für das Speichern der Ergebnisse der Zusammenführung. Im schlimmsten Fall, 
wenn die Intervalle sich nicht überschneiden, kann der Speicherbedarf für die Ergebnisse 
vergleichbar mit den Eingabedaten sein und den gesamten Speicherverbrauch verdoppeln.
```
---
## Fazit
Je nach der spezifischen Situation und den Anforderungen an Leistung, Zuverlässigkeit und 
Speichernutzung kann es sinnvoll sein, eine andere Programmiersprache zu wählen.

Z.B.:
- für Anwendungen, die extrem schnelle Datenverarbeitung erfordern, wie Echtzeitsysteme oder Datenanalyse großer 
Volumen, könnte ein Wechsel zu Sprachen wie C oder C++ sinnvoll sein.
- Programme, die eine präzise Kontrolle über den Speicherverbrauch benötigen, profitieren von Sprachen wie C, C++ 
oder Rust.