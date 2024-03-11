brSati=float(input("Broj radnih sati: "))
satnica=float(input("Satnica: "))



def total_euro(brSati,satnica):
    return brSati*satnica

print("Korisnik je zaradio ", total_euro(brSati,satnica), " eura!")
