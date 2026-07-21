# main.py

from colony import Colony
from colonist import Colonist

def main():
    print("=== Mars Colony ===")
    print("Starting colony simulation...\n")
    
    colony = Colony("Ares Base")
    
    przemek = Colonist("Przemek", 39, 100, "Supervisor")
    ewa = Colonist("Ewa", 29, 100, "Hot Chick (Very Hot)" )
    
    colony.add_colonist(przemek)
    colony.add_colonist(ewa)
    
    for i in range(10):
        colony.show_status()
        colony.next_day()
    
    print("Colonists")
    colony.show_colonists()
    
if __name__ == "__main__":
    main()