import pandas as pd

df = pd.read_csv(r'e:\Mihajlo\Test\Urban Air Quality and Health Impact Dataset.csv')

print(df.columns)

kolona = 'tempmax'  

max_vrednost = df[kolona].max()
min_vrednost = df[kolona].min()

prosecna_vrednost = df[kolona].mean()

procenat_razlika = ((max_vrednost - prosecna_vrednost) / prosecna_vrednost) * 100

df[kolona] = (df[kolona] - min_vrednost) / (max_vrednost - min_vrednost)

df.to_csv('azurirani_podaci.csv', index=False)

print(f'Maks: {max_vrednost}, Min: {min_vrednost}, Prosek: {prosecna_vrednost}, Procenat razlika: {procenat_razlika:.2f}%')

numericke_kolone = df.select_dtypes(include=['float64', 'int64'])  
korelacije = numericke_kolone.corr()
najveca_pozitivna = korelacije.max().max()
najveca_negativna = korelacije.min().min()

print(f'Najveca pozitivna korelacija: {najveca_pozitivna}, Najveca negativna korelacija: {najveca_negativna}')




