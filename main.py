# main.py

from colony import Colony
from colonist import Colonist

def main():
    print("=== Mars Colony ===")
    print("Starting colony simulation...\n")
    
    colony = Colony("Ares Base")
    
    for i in range(10):
        colony.show_status()
        colony.next_day()
    
    colonist = Colonist("Przemek")
    
if __name__ == "__main__":
    main()