import urllib.request
import urllib.error

print(f' EXERCÍCIO 114 '.center(40))
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no momento!')
else:
    print('Consegui acessar o site pudim com sucesso!')
