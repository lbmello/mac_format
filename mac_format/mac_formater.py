

class MacFormater:

    def __init__(self, mac_address_input):
        self.mac = self.mac_filter(mac_address_input)


    def mac_filter(self, mac_address):
        patterns = ['-', '_', 
                    '.', ' ', 
                    ',', ':',
                    '_', ' ']

        mac_filtered = mac_address

        for pattern in patterns:
            mac_filtered = mac_filtered.replace(pattern, '')

        return mac_filtered
        

    def dois_pontos_M(self):
        formated_mac = ''

        local_mac = self.mac.upper()

        for letter in range(0, len(local_mac), 2):
            formated_mac = formated_mac + (local_mac[letter] + local_mac[letter+1] + ':')

        return f"| : | | M | : {formated_mac[0:-1]}"


    def dois_pontos_m(self):
        formated_mac = ''

        local_mac = self.mac.lower()

        for letter in range(0, len(local_mac), 2):
            formated_mac = formated_mac + (local_mac[letter] + local_mac[letter+1] + ':')

        return f"| : | | m | : {formated_mac[0:-1]}"


    def traco_M(self):
        formated_mac = ''

        local_mac = self.mac.upper()

        for letter in range(0, len(local_mac), 2):
            formated_mac = formated_mac + (local_mac[letter] + local_mac[letter+1] + '-')

        return f"| - | | M | : {formated_mac[0:-1]}"


    def traco_m(self):
        formated_mac = ''

        local_mac = self.mac.lower()

        for letter in range(0, len(local_mac), 2):
            formated_mac = formated_mac + (local_mac[letter] + local_mac[letter+1] + '-')

        return f"| - | | m | : {formated_mac[0:-1]}"


    def ponto_M(self):
        formated_mac = ''

        local_mac = self.mac.upper()

        for letter in range(0, len(local_mac), 2):
            formated_mac = formated_mac + (local_mac[letter] + local_mac[letter+1] + '.')

        return f"| . | | M | : {formated_mac[0:-1]}"


    def ponto_m(self):
        formated_mac = ''

        local_mac = self.mac.lower()

        for letter in range(0, len(local_mac), 2):
            formated_mac = formated_mac + (local_mac[letter] + local_mac[letter+1] + '.')

        return f"| . | | m | : {formated_mac[0:-1]}"


    def espaco_M(self):
        formated_mac = ''

        local_mac = self.mac.upper()

        for letter in range(0, len(local_mac), 2):
            formated_mac = formated_mac + (local_mac[letter] + local_mac[letter+1] + ' ')

        return f"|   | | M | : {formated_mac[0:-1]}"


    def espaco_m(self):
        formated_mac = ''

        local_mac = self.mac.lower()

        for letter in range(0, len(local_mac), 2):
            formated_mac = formated_mac + (local_mac[letter] + local_mac[letter+1] + ' ')

        return f"|   | | m | : {formated_mac[0:-1]}"


    def virgula_M(self):
        formated_mac = ''

        local_mac = self.mac.upper()

        for letter in range(0, len(local_mac), 2):
            formated_mac = formated_mac + (local_mac[letter] + local_mac[letter+1] + ',')

        return f"| , | | M | : {formated_mac[0:-1]}"


    def virgula_m(self):
        formated_mac = ''

        local_mac = self.mac.lower()

        for letter in range(0, len(local_mac), 2):
            formated_mac = formated_mac + (local_mac[letter] + local_mac[letter+1] + ',')

        return f"| , | | m | : {formated_mac[0:-1]}"


    def nada_M(self):
        formated_mac = ''

        local_mac = self.mac.upper()

        return f"| N | | M | : {local_mac}"


    def nada_m(self):
        formated_mac = ''

        local_mac = self.mac.lower()

        return f"| N | | M | : {local_mac}"


    def print_all(self):
        print(self.dois_pontos_M())
        print(self.dois_pontos_m())
        print(self.traco_M())
        print(self.traco_m())
        print(self.ponto_M())
        print(self.ponto_m())
        print(self.virgula_M())
        print(self.virgula_m())
        print(self.espaco_M())
        print(self.espaco_m())
        print(self.nada_M())
        print(self.nada_m())
