import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[1;31mO site Pudim está inacessível no momento.\033[m')
else:
    print('\033[1;92mVai um Pudimzin?\033[m')