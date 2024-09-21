import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.realitica.com' 
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

with open('nekretnine.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['vrsta', 'područje', 'lokacija', 'broj_spavaćih_soba', 'broj_kupila', 
                     'cijena', 'stambena_površina', 'zemljište', 'parking_mjesta', 
                     'od_mora', 'novogradnja', 'klima', 'naslov', 'opis', 
                     'web_stranica', 'oglasio', 'mobilni', 'broj_id_oglasa', 
                     'zadnja_promjena', 'slike', 'link'])

    for nekretnina in soup.find_all('div', class_='thumb_div'):
        link = nekretnina.find('a')['href']  
        vrsta = nekretnina.find('div', class_='vrsta').text.strip()  

        writer.writerow([
            vrsta,
            'default_područje',
            'default_lokacija',
            2, 
            1,  
            100000.0,  
            50,  
            30, 
            1, 
            500, 
            True,  
            True,  
            'default_naslov',
            'default_opis',
            url,
            'default_oglasio',
            'default_mobilni',
            123456,  
            '2024-09-21',  
            '[]',  
            link
        ])

print('Podaci su sacuvani u nekretnine.csv')

