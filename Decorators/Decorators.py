# creating a decorator
# creating a function that needs to be passed into the decorator
# testing the decorator

import time


def fonction_vitesse(fonc):
    def wrapper():
        print("Commencer...")
        time.sleep(1.5)
        a = time.time()
        fonc()
        b = time.time()
        print("Terminer la fonction...")
        time.sleep(.5)
        print("Terminé")
        time.sleep(.2)
        print(f"Vitesse de la fonction {b - a}")
        return 0
    return wrapper


@fonction_vitesse
def mon_fonction() -> int:
    for i in range(2000):
        b: int = int(i / 3)
        for c in range(b):
            time.sleep(0.01)
            return c


mon_fonction()
