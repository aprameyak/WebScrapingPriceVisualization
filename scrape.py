#imports
import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import matplotlib.pyplot as plt

#enviornment fields
PRODUCT1URL = ""
PRODUCT2URL = ""
CSVPATH = ""

#webscraping function
def soup(url):
    r = requests.get(url) 
    soup = BeautifulSoup(r.text, 'html.parser')
    prices = soup.find_all(string="$")
    parent = prices[0].parent
    strong = parent.find("strong")
    str = strong.string
    return str

#data visualization function
def plot():
    df = pd.read_csv(r''+CSVPATH)
    data = df[['Price1','Price2']]
    df = pd.DataFrame(data, columns=['Price1','Price2'])
    df.plot(x="Price1", y='Price2',
        kind="line", figsize=(10, 10))
    plt.show()

#main logic function 
def main():
    f = open(r''+CSVPATH, "a")
    f.write("\n")
    f.write(soup(PRODUCT1URL))
    f.write(',')
    f.write(soup(PRODUCT2URL = ""))
    f.close()
    plot()

#executed code   
main()
