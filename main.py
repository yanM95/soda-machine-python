# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 18:44:39 2022

@author: yannis_montreer
"""
from soda_machine import SodaMachine

def main():

    soda_machine = SodaMachine.get_instance()
    soda_machine.display_items()

    while True:
        try:
            user_selection =  int(input("Order number from machine button : "))
        except ValueError:
            print("\nNo such soda")
            continue # keep asking
        if user_selection not in range(1, len(soda_machine.items)+1) :
            print("\nNo such soda")
            continue
        else :
            break # go out of while loop
    item = soda_machine.items[user_selection-1]
    while soda_machine.money_inserted < item.price :
        left = item.price - soda_machine.money_inserted
        print(f"\nPrice of {item.name} is {item.price} NOK\nPlease insert {left:.0f} NOK.")
        while True:
            try:
                money_to_insert = float(input("Money put into slot: "))
                soda_machine.insert_money(money_to_insert)
            except ValueError:
                continue
            else:
                break
    print(f"\n  Giving \"{item.name}\" out.")
    print(f"  Returning {soda_machine.money_inserted - item.price:.0f} NOK to customer.\n")
    item.inventory -= 1
    soda_machine.money_inserted = 0
    
    if item.inventory != 0 :        
        main()

    return 0
    
    
if __name__ == "__main__":
    import sys
    sys.exit(main())
