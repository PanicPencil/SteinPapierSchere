import tkinter as tk
import random

# Punktestand Variablen
spieler_punkte = 0
computer_punkte = 0


# Funktion zur Bestimmung des Ergebnisses
def spiele_spiel(spieler_wahl):
    global spieler_punkte, computer_punkte
    optionen = ["Stein", "Papier", "Schere"]
    computer_wahl = random.choice(optionen)

    if spieler_wahl == computer_wahl:
        ergebnis_text.set(f"Unentschieden! Computer wählte auch {computer_wahl}.")
    elif (spieler_wahl == "Stein" and computer_wahl == "Schere") or \
            (spieler_wahl == "Schere" and computer_wahl == "Papier") or \
            (spieler_wahl == "Papier" and computer_wahl == "Stein"):
        spieler_punkte += 1
        ergebnis_text.set(f"Du hast gewonnen! Computer wählte {computer_wahl}.")
    else:
        computer_punkte += 1
        ergebnis_text.set(f"Computer hat gewonnen! Computer wählte {computer_wahl}.")

    # Punktestand aktualisieren
    punktestand_text.set(f"Spieler: {spieler_punkte}  Computer: {computer_punkte}")


# Hauptfenster erstellen
fenster = tk.Tk()
fenster.title("Stein, Papier, Schere")

# Begrüßung und Regeln anzeigen
begruesung_text = "Willkommen zu Stein, Papier, Schere!\n\nDie Regeln sind einfach:\n" \
                  "Stein schlägt Schere, Schere schlägt Papier, Papier schlägt Stein.\n"
begruesung_label = tk.Label(fenster, text=begruesung_text, font=("Arial", 12), justify="left")
begruesung_label.pack(pady=10)

# Label für den Punktestand
punktestand_text = tk.StringVar()
punktestand_text.set("Spieler: 0  Computer: 0")
punktestand_label = tk.Label(fenster, textvariable=punktestand_text, font=("Arial", 14))
punktestand_label.pack(pady=10)

# Label für das Ergebnis
ergebnis_text = tk.StringVar()
ergebnis_label = tk.Label(fenster, textvariable=ergebnis_text, font=("Arial", 14))
ergebnis_label.pack(pady=20)

# Buttons für die Auswahl
button_stein = tk.Button(fenster, text="🗿 Stein", width=15, command=lambda: spiele_spiel("Stein"))
button_stein.pack(pady=10)

button_papier = tk.Button(fenster, text="📄 Papier", width=15, command=lambda: spiele_spiel("Papier"))
button_papier.pack(pady=10)

button_schere = tk.Button(fenster, text="✂ Schere", width=15, command=lambda: spiele_spiel("Schere"))
button_schere.pack(pady=10)

# Hauptschleife des Fensters starten
fenster.mainloop()