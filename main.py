import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

playcounts = []
pps = []
accuracy = []
ss = []

class Parse:
    def __init__(self, number_of_pages, country):
        self.number_of_pages = number_of_pages 
        self.country = country
        self.url = 'https://osu.ppy.sh/rankings/osu/performance?country={}&page='.format(country)

    def get_html(self, url):
        r = requests.get(self.url).text
        return r

    def playcount(self):
        for i in range(1, self.number_of_pages + 1):
            soup = BeautifulSoup(self.get_html(self.url + str(i)), 'html.parser')
            playcount = soup.findAll('td')
            for user in range(3,len(playcount),8):
                pc = "".join(playcount[user].text.replace(',', '').split())
                playcounts.append(pc)
            print("Page "+str(i)+" of "+str(self.number_of_pages)+" for playcount")

    def pp(self):
        for i in range(1, self.number_of_pages + 1):
            soup = BeautifulSoup(self.get_html(self.url + str(i)), 'html.parser')
            pp = soup.findAll('td')
            for user in range(4, len(pp), 8):
                pepe = "".join(pp[user].text.replace(',', '').split())
                pps.append(pepe)
            print("Page "+str(i)+" of "+str(self.number_of_pages)+" for PP")

    def accuracy(self):
        for i in range(1, self.number_of_pages + 1):
            soup = BeautifulSoup(self.get_html(self.url + str(i)), 'html.parser')
            acc = soup.findAll('td')
            for user in range(2, len(acc), 8):
                accur  = "".join(acc[user].text.replace(',', '').split())
                accuracy.append(accur)
            print("Page "+str(i)+" of "+str(self.number_of_pages)+" for Accuracy")

    def ss(self):
        for i in range(1, self.number_of_pages + 1):
            soup = BeautifulSoup(self.get_html(self.url + str(i)), 'html.parser')
            ss_count = soup.findAll('td')
            for user in range(5, len(ss_count), 8):
                ss1 = "".join(ss_count[user].text.replace(',', '').split())
                ss.append(ss1)
            print("Page "+str(i)+" of "+str(self.number_of_pages)+" for SS")



def main():
    parse = Parse(5, '')
    parse.pp()
    parse.playcount()
    x = [int(a) for a in playcounts]
    y = [int(b) for b in pps]
    plt.scatter(x, y, s=20)
    plt.title("PP(PC) OVERALL")
    plt.xlabel("PC")
    plt.ylabel('PP')
    plt.show()

if __name__ == '__main__':
    main()
