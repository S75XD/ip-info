import requests,json,os,colorama
from colorama import Fore
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clear()
print('''
██╗██████╗░░░░░░░██╗███╗░░██╗███████╗░█████╗░
██║██╔══██╗░░░░░░██║████╗░██║██╔════╝██╔══██╗
██║██████╔╝█████╗██║██╔██╗██║█████╗░░██║░░██║
██║██╔═══╝░╚════╝██║██║╚████║██╔══╝░░██║░░██║
██║██║░░░░░░░░░░░██║██║░╚███║██║░░░░░╚█████╔╝
╚═╝╚═╝░░░░░░░░░░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
	By SaLeH | insta @8_uvw''')

colorama.init(autoreset=True)
red=Fore.RED
yellow=Fore.YELLOW
blue=Fore.BLUE
green=Fore.GREEN
cyan=Fore.CYAN
white=Fore.WHITE

r1 = requests.get("https://pastebin.com/raw/aEekKFhV").text
print(f"\n{yellow}{r1}\n")
r = requests.Session()

try:
	ip = input(f'[!] Enter the {red}ip {white}:').strip()

	url = f'https://ipinfo.io/{ip}/geo'

	req = r.get(url).json()

	city = (req['city'])
	region = (req['region'])
	country = (req['country'])
	loc = (req['loc'])
	org = (req['org'])
	timezone = (req['timezone'])

	print(f"{red}="*25)
	print(f'[+] ip : {ip}\n[+] city : {city} \n[+] region : {region}\n[+] country : {country}\n[+] loc : {loc}\n[+] org : {org}\n[+] timezone : {timezone}\n[+] By SaLeH & insta @8_uvw')
	print(f"{red}="*25)

except:
	print(f"{yellow}[-] this ip ? {ip} :/")
	exit()

user = input(f"[!] Do you want to send information to telegram [y/n]:").strip()

if user =='y':
	ID = input("[-] Enter Your id :").strip()
	token = input("[-] Enter Your Token :").strip()
	print(f"{red}="*25)
	tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=[*] ip : {ip}\n[*] city : {city} \n[*] region : {region}\n[*] country : {country}\n[*] loc : {loc}\n[*] org : {org}\n[*] timezone : {timezone}\n[*] By SaLeH insta @8_uvw''')
										
	reqte = requests.post(tlg)
	print(f"{green}[+] Done Goodbye :)")
	exit()

elif user =='n':
	print(f"{green}[+] Done Goodbye :)")
	exit()