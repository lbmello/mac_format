
import sys


from .mac_formater import MacFormater


if __name__ == "__main__":
    if len(sys.argv) > 1:
        mac_arg = sys.argv[1]
        
        MacFormater(mac_address_input = mac_arg).print_all()  
    
    else:
        mac_input = input("Digite o endereço MAC: ")

        MacFormater(mac_address_input = mac_input).print_all()