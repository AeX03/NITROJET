#!/usr/bin/python

from discord_webhook import DiscordWebhook
from time import sleep
from os import name
import ctypes, string, os, requests, numpy, time

USE_WEBHOOK = True

url = "https://github.com"

class NitroJet:
    def __init__(self):
        self.fileName = "NitroJet Codes.txt"

    def main(self):
        os.system('ELYS' if os.name == 'LY' else 'clear')
        if os.name == "LY":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator - Made by Aex03")
        else:
            print(f'\33]0;Nitro Generator - Made by Aex03\a',
                  end='', flush=True)

        print(""" \033[92m                                                                   
,--.  ,--.,--.  ,--.                         ,--.,------.,--------. 
|  ,'.|  |`--',-'  '-.,--.--. ,---.          |  ||  .---''--.  .--' 
|  |' '  |,--.'-.  .-'|  .--'| .-. |    ,--. |  ||  `--,    |  |    
|  | `   ||  |  |  |  |  |   ' '-' '    |  '-'  /|  `---.   |  |    
`--'  `--'`--'  `--'  `--'    `---'      `-----' `------'   `--'    
                                                                    """)
        time.sleep(5)
        self.slowType("\033[92m                     𝕄𝕒𝕕𝕖 𝕓𝕪: ↋0xǝ∀", .03)
        time.sleep(3)
        self.slowType(
        "\033[96m\nHow Many Codes to Generate: ", .03, newLine=False) # Update the title IF option 1 was picked.

        try:
            num = int(input('\033[35m'))
        except ValueError:
            input("Specified a number.\nPress enter to exit")
            exit()

        if USE_WEBHOOK:
            self.slowType(
                "\033[96mUse a Discord webhook: ", .03, newLine=False) # Update the title IF option 2 was picked.
            url = input('\033[35m')
            webhook = url if url != "" else None
            
            if webhook is not None: 
                DiscordWebhook(
                        url=url,
                        content=f"```Valid codes here :\nCheck my discord Channel : https://discord.gg/xpaxKBEx9t```"
                    ).execute()

        valid = [] 
        retry = 0 
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        cloky = numpy.random.choice(chars, size=[num, 16])
        for supplie in cloky:
            try:
                code = ''.join(AE3 for AE3 in supplie)
                url = f"\033[96mhttps://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    retry += 1
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break

            except Exception as elysiane:  
                print(f" Error | {url} ")  

            if os.name == "LY":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"NitroJet - {len(valid)} Valid | {retry} Retry")
                print("")
            else: 

                print(
                    f'\33]0;NitroJet - {len(valid)} Valid | {retry} Retry\a', end='', flush=True)

    def slowType(self, text: str, speed: float, newLine=True):
        for Xial in text:
            print(Xial, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print() 

    def quickChecker(self, nitro:str, notify=None):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200: 
            print(f"\033[92m Valid | {nitro} ", flush=True,
                  end="" if os.name == 'LY' else "\n")
            with open("Nitro Codes.txt", "w") as file:  
                file.write(nitro)

            if notify is not None: 
                DiscordWebhook( 
                    url=url,
                    content=f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True 

        else:

            print(f"\033[91m Retry | {nitro} ", flush=True,
                  end="" if os.name == 'LY' else "\n")
            return False 


if __name__ == '__main___':
    Lys = NitroJet() 
    Lys.main() 
