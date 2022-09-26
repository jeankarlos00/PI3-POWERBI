from turtle import title
from bs4 import BeautifulSoup
import requests
from csv import writer
from datetime import date, datetime

# Cidades
# Brasilia
# Goiania
# Florianopolis
# Fortaleza
# Luziania
# Uberlandia


url = 'https://www.gasoradar.com.br/'
cidades = 'Uberlandia'
tipos_combustivel = ['1', '2', '3', '4', '5']
nome_tipos_combustivel = ['Gasolina Comum', 'Gasolina Aditivada', 'Etanol', 'Diesel S10', 'GNV']

with open('dados.csv', '+a', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        #header = ['Posto', 'Endereço', 'Estado', 'Preço', 'Tipo', 'Data', 'Hora']
        #thewriter.writerow(header)

        for i, tipoComb in enumerate(tipos_combustivel):

            url = '{0}search?q={1}&fuel_id={2}&search=true'.format(url, cidades, tipoComb)
            page = requests.get(url)

            soup = BeautifulSoup(page.content, 'html.parser')
            lists = soup.find_all('div', class_="card p-4 mb-4")

            for list in lists:
                posto = list.find('h4').text
                if ("avaliações" in list.find('p').text):
                    enderecos = list.find('p').find_next('p')
                    estado = list.find('p').find_next('p').find_next('p').text
                else:
                    enderecos = list.find('p')
                    estado = list.find('p').find_next('p').text
                preco = list.find('h4').find_next('h4').text
                endereco = enderecos.get_text(separator=" ").strip()
                
                info = [posto, endereco, estado, preco, nome_tipos_combustivel[i], date.today(), datetime.now().strftime("%H:%M:%S")]
                thewriter.writerow(info)