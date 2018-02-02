import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

number_of_pages = 41
url = 'https://osu.ppy.sh/p/pp/?m=0&s=3&o=1&f=&page='
playcounts = []
pps = []
accuracy = []
ss = []
def get_html(url):
    r = requests.get(url).text
    return r

def playcount_parse():
    for i in range(number_of_pages):
        soup = BeautifulSoup(get_html(url+str(i)), 'lxml')
        playcount = soup.findAll('td')
        for user in range(3,len(playcount),8):
            pc = str(playcount[user])
            playcounts.append(pc[10:pc.find('(') - 1].replace(',',''))


def pp_parse():
    for i in range(number_of_pages):
        soup = BeautifulSoup(get_html(url + str(i)), 'lxml')
        pp = soup.findAll('td')
        for user in range(4, len(pp), 8):
            pepe = str(pp[user])
            pps.append(pepe[36:pepe.find('pp')].replace(',',''))

def accuracy_parse():
    for i in range(number_of_pages):
        soup = BeautifulSoup(get_html(url + str(i)), 'lxml')
        acc = soup.findAll('td')
        for user in range(2, len(acc), 8):
            accur = str(acc[user])
            accuracy.append(accur[4:accur.find('%')])

def ss_parse():
    for i in range(number_of_pages):
        soup = BeautifulSoup(get_html(url + str(i)), 'lxml')
        ss_count = soup.findAll('td')
        for user in range(5, len(ss_count), 8):
            ss1 = str(ss_count[user])
            ss.append(ss1[19:ss1.find('</')])

ss_parse()
# playcount_parse()
pp_parse()
# playcount_parse()
x = [float(a) for a in pps]
y = [int(b) for b in ss]
plt.scatter(x, y, s=20)
plt.title("Зависимость ss от pp")
plt.xlabel("PP")
plt.ylabel("SS")
plt.show()
