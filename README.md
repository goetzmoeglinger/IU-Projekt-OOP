Installationsanleitung
Die Datei „Dashboard.py“ sowie die Installationsanleitung ist auf GitHub in folgendem Verzeichnis abgelegt: https://github.com/goetzmoeglinger/IU-Projekt-OOP. Um das Python Programm ausführen zu können müssen die Bibliotheken „tkinter“, „datetime“ und „os“ installiert sein. Dies ist beispielsweise sowohl in der Jupyter als auch der Thonny Umgebung bereits der Fall.

Beim ersten Start ist das Dashboard bis auf die Fortschrittsbalken noch leer, falls die Datei „kurse.txt“ nicht mitinstalliert wurde. Die Balken zeigen die verstrichene bzw. noch übrige Zeit im jeweiligen Semester an. Start war der 1. August 2025. Es werden die Rahmen für sechs Semester angezeigt, was der Regel- und meiner Zielstudienzeit entspricht.

Um einen Kurs hinzuzufügen, ECTS-Punkte oder Noten einzutragen klicken Sie auf den Button „Kurs(e) hinzufügen oder ändern“. Es öffnet sich ein Wordpad Editor mit den Daten eines Musterkurses (11, Musterkurs, 5, 1.0). In Anlehnung an diesen werden die Kurse wie folgt, mit Komma und Leerzeichen getrennt, in den Editor eingetragen:
•	11: die erste Ziffer steht für das Semester, die zweite für einen von x Kursen, bzw. Modulen des jeweiligen Semesters.
•	Musterkurs: Platzhalter für den Namen des Kurses
•	5: (Platzhalter für die) Anzahl der ECTS-Punkte
•	1.0: (Platzhalter für die) Note. Dabei ist folgende Codierung zu beachten:
•	0 (inaktiv): wenn noch keine Anmeldung für den Kurs erfolgt ist (wird auf dem Dashboard in grauer Schrift wiedergegeben).
•	0.0 (aktiv): wenn eine Anmeldung bereits erfolgt ist, aber noch keine Prüfung abgelegt wurde (wird auf dem Dashboard in grüner Schrift wiedergegeben).
•	0.00 (eingereicht): wenn eine Prüfung abgelegt und zur Beurteilung eingereicht wurde (wird auf dem Dashboard in roter Schrift wiedergegeben).
•	X.X (abgeschlossen): die erhaltene Note für den, damit abgeschlossenen, Kurs (wird auf dem Dashboard in schwarzer Schrift wiedergegeben).

Nach dem Speichern und Schließen der Datei wird nach einem Klick auf „Neu laden“ das Dashboard aktualisiert und die Kurse entsprechend der Codierung angezeigt, sowie die Durchschnittsnote aus den bereits bestandenen Kursen und die entsprechend erreichte ECTS-Punktzahl berechnet. Die Gesamtpunktzahl von 180 ist als Vorgabe für eine Bachelor-Studiengang bereits voreingestellt.
Viel Erfolg 😊!
