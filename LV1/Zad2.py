while True:
    try:
        ocjena=float(input("Upišite ocjenu u intervalu [0.0,1.0]: "))
        while ocjena>1 or ocjena<0:    
            ocjena=float(input("Upisana ocjena nije u intervalu [0.0, 1.0], molimo vas upišite ponovno: "))
        if ocjena>=0.9:
            print("A")
            break
        elif ocjena>=0.8:
            print("B")
            break
        elif ocjena>=0.7:
            print("C")
            break
        elif ocjena>=0.6:
            print("D")
            break
        else:
            print("F")
            break
    except ValueError:
        print('Niste upisali broj')
