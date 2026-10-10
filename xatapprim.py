import requests as r
from bs4 import BeautifulSoup

print("scraping craulin")

try:
    resultado = r.get("https://uol.com.br/start/esport")

except:
    print("seu pc foi hackeado pague 10000 pesos agentinos para ter seu pc de volta nessa chave pix: 458.364.604-92")
else:
    resposta = resultado.text
    soup = BeautifulSoup(resposta, "html.parser")

    print(soup.title.string)


    lista = ["Free fire", "Neymar" , "corinthians"]


    for paragrafo in soup.find_all("body"):
        for palavra in lista:
            for paragrafo_str in paragrafo.stripped_strings:
                if palavra.upper() in str(paragrafo_str).upper():
                    print(f"NOTICIA: {paragrafo_str}")