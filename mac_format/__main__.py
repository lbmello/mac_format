
import sys


from .mac_formater import MacFormater


if __name__ == "__main__":
    if len(sys.argv) > 1:
        mac_arg = sys.argv[1]
        
        MacFormater(mac_address_input = mac_arg)  
    
    else:
        mac_input = input("Type the MAC address: ")

        MacFormater(mac_address_input = mac_input)