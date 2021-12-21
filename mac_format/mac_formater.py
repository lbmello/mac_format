
# TODO: Translate the string format methods.
# TODO: Add the documentation to the string format methods.


class MacFormater:

    def __init__(self, mac_address_input):
        self.mac_inputed = mac_address_input
        self.mac = self.mac_filter()


    def mac_filter(self):
        """Remove some possible delimiters."""

        patterns = ['-', '_', 
                    '.', ' ', 
                    ',', ':',
                    '_', ' ']

        mac_filtered = self.mac_inputed

        for pattern in patterns:
            mac_filtered = mac_filtered.replace(pattern, '')

        return mac_filtered


    def mac_generator(self):
        """Run all formating methods and return a list."""

        mac_list = [
            self.dois_pontos_M(),
            self.dois_pontos_m(),
            self.traco_M(),
            self.traco_m(),
            self.ponto_M(),
            self.ponto_m(),
            self.virgula_M(),
            self.virgula_m(),
            self.espaco_M(),
            self.espaco_m(),
            self.nada_M(),
            self.nada_m()
        ]

        return mac_list

        
    def print_all(self):
        """Simply run mac_generator and print all the results."""

        macs = self.mac_generator()

        for mac in macs:
            print(mac)


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

