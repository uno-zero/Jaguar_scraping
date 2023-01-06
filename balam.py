import requests
import colorama
import signal
from bs4 import BeautifulSoup
from colorama import Fore, Style

def opcion_1():
	while True:
		print("")
		query= input("º	Nota: ")
		print("")
		def search(query):
		  url = f"https://google.com/search?q={query}"
		  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
		  response = requests.get(url, headers=headers)
		  soup = BeautifulSoup(response.text, 'html.parser')
		  results = soup.find_all('div', class_='g')
		  return results

		dorks = [
		  f"site:medium.com {query}",
		  f"inurl:gitbook.io {query}",
		  f"inurl:github.io {query}"
		]

		for dork in dorks:
		  results = search(dork)
		  print(f"Results for dork '{dork}':")
		  for result in results:
			   link = result.find('a')
			   print(Fore.GREEN + link.get('href') + Style.RESET_ALL)
def opcion_2():
	while True:
		print("")
		query= input("º	Codigo: ")
		print("")
		def search(query):
		  url = f"https://google.com/search?q={query}"
		  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
		  response = requests.get(url, headers=headers)
		  soup = BeautifulSoup(response.text, 'html.parser')
		  results = soup.find_all('div', class_='g')
		  return results

		dorks = [
		  f"inurl:medium.com {query}",
		  f"inurl:github.com {query}",
		  f"inurl:searchcode.com {query}"  
		]

		for dork in dorks:
		  results = search(dork)
		  print(f"Results for dork '{dork}':")
		  for result in results:
			   link = result.find('a')
			   print(Fore.GREEN + link.get('href') + Style.RESET_ALL)
def opcion_3():
	  # Código para la opción 3
		 print("333")


print("")
banner = "\033[1;32m	  ▄▄▄▄    ▄▄▄       ██▓    ▄▄▄       ███▄ ▄███▓                   \033[0m\n" \
		 "\033[1;32m	▓█████▄ ▒████▄    ▓██▒   ▒████▄    ▓██▒▀█▀ ██▒                    \033[0m\n" \
		 "\033[1;32m	▒██▒ ▄██▒██  ▀█▄  ▒██░   ▒██  ▀█▄  ▓██    ▓██░                    \033[0m\n" \
		 "\033[1;32m	▒██░█▀  ░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██ ▒██    ▒██                     \033[0m\n" \
		 "\033[1;32m	░▓█  ▀█▓ ▓█   ▓██▒░██████▒▓█   ▓██▒▒██▒   ░██▒                    \033[0m\n" \
		 "\033[1;32m	░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ░  ░                    \033[0m\n" \
		 "\033[1;32m	▒░▒   ░   ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░░  ░      ░                    \033[0m\n" \
		 "\033[1;32m	 ░    ░   ░   ▒     ░ ░    ░   ▒   ░      ░                       \033[0m\n" \
		 "\033[1;32m	░            ░  ░    ░  ░     ░  ░       ░                        \033[0m\n" \
		 "\033[1;32m      ░                                                   By:unozero  \033[0m"
		 
print(banner)
	 
def show_menu():
  print("1. ")
  print("2. Salir")
  return input("Selecciona una opción: ")
  
def show_menu():
  print("")
  print(colorama.Fore.BLUE + "1. Buscar Notas" + colorama.Style.RESET_ALL)
  print(colorama.Fore.GREEN + "2. Buscar codigo" + colorama.Style.RESET_ALL)
  print("3. Salir")
  print("")
  return input("Selecciona una opción: ")

def salir(signum, frame):
  exit()

signal.signal(signal.SIGINT, salir)

while True:
  option = show_menu()
  if option == "1":
    opcion_1()
  elif option == "2":
    opcion_2()
  elif option == "3":
    break
  else:
    print("Opcion invalida")
    print("")
    
#
