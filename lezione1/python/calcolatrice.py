print(
    """Benvenuto al programma calcolatrice!
    Funzioni disponibili:
    -Per effettuare un'Addizione, seleziona 1
    -Per effettuare una Sottrazione, seleziona 2
    -Per effettuare una Moltiplicazione, seleziona 3
    -Per effettuare una Divisone, seleziona 4
    -Per uscire dal programma puoi digitare 5"""
)

scelta = str(input("Inserisci il numero corrispondente all'operazione scelta:"))

if scelta == "1":
    print("\nHai scelto: Addizione\n")
    a = float(input("Inserisci il Primo Numero: "))
    b = float(input("Inserisci il Secondo Numero: "))
    print("Il risultato della Somma e': " + str(a + b))
elif scelta == "2":
    print("\nHai Scelto: Sottrazione\n")
    a = float(input("Inserisci il Primo Numero: "))
    b = float(input("Inserisci il Secondo Numero: "))
    print("Il risultato della Sottrazione e': " + str(a - b))
elif scelta == "3":
    print("\nHai scelto: Moltiplicazione\n")
    a = float(input("Inserisci il Primo Numero: "))
    b = float(input("Inserisci il Secondo Numero: "))
    print("Il risultato della Moltiplicazione e': " + str(a * b))
elif scelta == "4":
    print("\nHai scelto: Divisione\n")
    a = float(input("Inserisci il Primo Numero: "))
    b = float(input("Inserisci il Secondo Numero: "))
    print("Il risultato della Divisione e': " + str(a / b))
elif scelta == "5":
    print("L'applicazione verra' ora chiusa!")

print("Grazie e arrivederci!")
