import tkinter as tk
from tkinter import ttk
from datetime import date
import os


# Status 
# schwarz: Kurs abgeschlossen, 
# grün: angemeldet aber noch nicht bewertet (Note: 0.0), 
# grau: Kurs inaktiv (Note: 0)
class Status:
    @staticmethod
    def farbe(note):
        if note == "0":
            return "grey" 
        elif note == "0.0":
            return "green"
        elif note != "0.0":
            return "black"
     
# Dateimanager zum öffnen und bearbeiten der Module
class DateiManager:
    @staticmethod
    def datei_oeffnen():
        if not os.path.exists("kurse.txt"):
            with open("kurse.txt", "w", encoding="utf-8") as f:
                f.write("11, Musterkurs, 5, 1.0")
        else:
             os.system("notepad kurse.txt")

# Klasse Semester
class Semester:
    def __init__(self, master, nummer, x, y):
        self.nummer = nummer

        # Nummer für den Semesterstart:
        # Rückgabe 8: Semester startet im August
        # Rückgabe 2: Semester startet im Februar
        def start_monat(nummer):
            return 8 if nummer % 2 == 1 else 2

        # Berechnung der verstrichenen Zeit für die Progressbar
        def berechne_fortschritt():
            heute = date.today()
            if heute < semester_start:
                return 0
            elif heute > semester_ende:
                return 100
            else:
                gesamt_tage = (semester_ende - semester_start).days
                vergangene_tage = (heute - semester_start).days
                return (vergangene_tage / gesamt_tage) * 100
        
        # Rahmen und Titel für die Semester-Objekte
        self.rahmen = tk.LabelFrame(master, labelanchor="sw", text=f"  {str(self.nummer)}. SEMESTER  ",
                                    bg="white", fg="grey", font=("Helvetica", 12), bd=1, relief="solid")
        self.rahmen.place(x=x, y=y, width=300, height=250)

        # Berechung der relevanten Datumsanzeigen
        if self.nummer == 1: y1, y2, semester_start, semester_ende = 2024, 2025, date(2024, 8, 1), date(2025, 1, 31)
        elif self.nummer == 2: y1, y2, semester_start, semester_ende = 2025, 2025, date(2025, 2, 1), date(2025, 7, 31)
        elif self.nummer == 3: y1, y2, semester_start, semester_ende = 2025, 2026, date(2025, 8, 1), date(2026, 1, 31)
        elif self.nummer == 4: y1, y2, semester_start, semester_ende = 2026, 2026, date(2026, 2, 1), date(2026, 7, 31)
        elif self.nummer == 5: y1, y2, semester_start, semester_ende = 2026, 2027, date(2026, 8, 1), date(2027, 1, 31)
        elif self.nummer == 6: y1, y2, semester_start, semester_ende = 2027, 2027, date(2027, 2, 1), date(2027, 7, 31)

        # Anzeige des jeweilien Semester-Zeitraumes
        label_date = tk.Label(self.rahmen, bg="white", text = (
                        f"{date(2024, start_monat(self.nummer), 1).strftime('%b')} {y1 - 2000} - "
                        f"{date(2024, start_monat(self.nummer + 1) - 1, 1).strftime('%b')} {y2 - 2000}"
                        ))
        label_date.pack(padx=3, pady=3)

        # Progressbar anzeigen
        fortschritt = berechne_fortschritt()
        progressbar = ttk.Progressbar(self.rahmen, length=200)
        progressbar['value'] = fortschritt
        progressbar.pack(pady=0)

        # Trennungslinie
        label_hr = tk.Label(self.rahmen, bg="white", text=("_________________________________________________"))
        label_hr.pack(pady=0)
        
        # Ausgabe der Kurse mit Punkten und Note im jeweiligen Semester-Objekt
        try:
            with open("kurse.txt", "r", encoding="utf-8") as file:
                for zeile in file:
                    kurs_liste = zeile.strip().split(", ")
                    if kurs_liste[0].startswith(str(self.nummer)):
                        kurs_str = (f"{kurs_liste[1]}  |  {kurs_liste[2]}  |  {kurs_liste[3]}") 
                        label_kurs = tk.Label(self.rahmen, bg="white", fg=Status.farbe(kurs_liste[3]), text=(kurs_str), font=("Helvetica", 10))
                        label_kurs.pack()
        except FileNotFoundError:
            DateiManager.datei_oeffnen()
        except ValueError:
            pass

################################################################  Class Semester Ende ################################################################

# Auslesen der kurse.txt und Umwandlung der ausgelesenen Strings in Listen um die Noten wiederum in Listen ablegen zu können
def noten_auslesen():
    noten = []
    try:
        with open("kurse.txt", "r", encoding="utf-8") as file:
            for zeile in file:
                kurs_liste = zeile.strip().split(", ")
                if float(kurs_liste[3]) > 0:
                    noten.append(float(kurs_liste[3]))
    except FileNotFoundError:
        DateiManager.datei_oeffnen()
    except ValueError:
        pass
    return noten

# Auslesen der kurse.txt und Umwandlung der ausgelesenen Strings in Listen um die Noten wiederum in Listen ablegen zu können
def punkte_auslesen():
    punkte = []
    try:
        with open("kurse.txt", "r", encoding="utf-8") as file:
            for zeile in file:
                kurs_liste = zeile.strip().split(", ")
                if float(kurs_liste[3]) > 0:
                    punkte.append(int(kurs_liste[2]))
    except FileNotFoundError:
        DateiManager.datei_oeffnen()
    except ValueError:
        pass
    return punkte

def start_gui():
    global dashboard
    dashboard = tk.Tk()
    dashboard.geometry("1100x800")
    dashboard.title("Dashboard")

    # Funktion für die Invertierung der Button
    def button_hover(button, bg, fg):
        def handler(event):
            button.config(bg=bg, fg=fg)
        return handler

    # Neustart-Button Definition
    def neustart():
        dashboard.destroy()
        start_gui()

    # Funktion zum Berechnen der Durchschnittsnote
    def note_berechnen():
        noten = noten_auslesen()
        try:
            note = round(sum(noten)/len(noten), 2)
        except ZeroDivisionError:
            pass
        return note
   
    # Funktion zum Berechnen der Durchschnittsnote und Punkte anzeigen
    def punkte_berechnen():
        punkte = punkte_auslesen()
        punkte_summe = sum(punkte)
        return punkte_summe 

    # Semester Objekte
    Semester(dashboard, 1, 50, 50)
    Semester(dashboard, 2, 400, 50)
    Semester(dashboard, 3, 750, 50)
    Semester(dashboard, 4, 50, 350)
    Semester(dashboard, 5, 400, 350)
    Semester(dashboard, 6, 750, 350)

    # Kurse-Hinzufügen-oder-ändern-Button
    button_kurse_hinzufügen = tk.Button(dashboard, text="Kurs(e) hinzufügen oder ändern", command=DateiManager.datei_oeffnen,
                    cursor="hand2", bg="green", fg="white", bd=1, font=("Helvetica", 12), relief="solid")
    button_kurse_hinzufügen.place(x=425, y=650, width=250, height=60)
    button_kurse_hinzufügen.bind("<Enter>", button_hover(button_kurse_hinzufügen, bg="lightgrey", fg="black"))
    button_kurse_hinzufügen.bind("<Leave>", button_hover(button_kurse_hinzufügen, bg="green", fg="white"))

    # Neustart-Button anzeigen
    button_neu_laden = tk.Button(dashboard, text="Neu laden", command=neustart, 
                    cursor="hand2", bg="green", fg="white", bd=1, font=("Helvetica", 12), relief="solid")
    button_neu_laden.place(x=425, y=720, width=250, height=30)
    button_neu_laden.bind("<Enter>", button_hover(button_neu_laden, bg="lightgrey", fg="black"))
    button_neu_laden.bind("<Leave>", button_hover(button_neu_laden, bg="green", fg="white"))
        
    # Durchschnittsnote anzeigen
    label_note = tk.Label(dashboard, bg="white", text=f"Ø-Note\n{note_berechnen()}", relief="solid", bd=1, font=("Helvetica", 12))
    label_note.place(x=125, y=650, width=150, height=100)

    # Punkte anzeigen
    label_punkte = tk.Label(dashboard, bg="white", relief="solid", bd=1, text=f"ECTS-Punkte\n{punkte_berechnen()}/180", font=("Helvetica", 12))
    label_punkte.place(x=850, y=650, width=150, height=100)

    dashboard.mainloop()

start_gui()
