
from urllib.parse import urljoin
import requests


class MacFormater:

    def __init__(self, mac_address_input):
        self.mac_raw = mac_address_input
        
        # This is the section of chars to remove from original mac 
        self.possible_patterns = [
            '-', '_',
            '.', ' ',
            ',', ':',
            '_', ' ']
        
        self.mac = self.mac_raw_filter()

        # This is the final chars to delimit new macs
        self.final_delimiters = [
            '',  ':',
            '-', '_',
            '.', ' ',
        ]

        self.final_macs = self.format_final_macs(self.final_delimiters)
        

        # Print the final results
        for mac in self.final_macs:
            for key, value in mac.items():
                print(f"| {key} |: {value}")

        print('------------------------------')
        print(f"The vendor of {self.mac} is: {self.mac_vendor()}")
        

    def mac_raw_filter(self):
        """Remove any possible delimiters."""

        mac_filtered = self.mac_raw

        for pattern in self.possible_patterns:
            mac_filtered = mac_filtered.replace(pattern, '')

        return mac_filtered


    def format_final_macs(self, delimiter):
        """Create the final mac by each final_delimiters."""
        
        macs = list()

        for d in delimiter:       
            formated_mac = ''

            upper_mac = self.mac.upper()
            for letter in range(0, len(self.mac), 2):
                formated_mac = formated_mac + (upper_mac[letter] + upper_mac[letter+1] + d)

            macs.append(
                {
                    f"{d} | M": f"{formated_mac[0:-1]}"
                })

            formated_mac = ''
            lower_mac = self.mac.lower()
            for letter in range(0, len(self.mac), 2):
                formated_mac = formated_mac + (lower_mac[letter] + lower_mac[letter+1] + d)
                
            macs.append(
                {
                    f"{d} | m": f"{formated_mac[0:-1]}"
                })
        
        return macs


    def mac_vendor(self):
        """Check the mac vendor."""

        base_url = "https://api.macvendors.com/"
        final_url = urljoin(base_url, f"/{self.mac}/")

        try:
            response = requests.get(final_url)

            if response.status_code == 200:
                return response.text
        except:
            return "Mac Vendor not available!"

