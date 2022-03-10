import random
import urllib.request


from bs4 import BeautifulSoup
from urllib.request import urlopen


class Quiz20:

    def quiz20list(self) -> str:
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))
        print(list1[0], list1[-1], list1[-2], list1[1:3])
        list2 = ['math', 'english']
        print(list2[0])
        print(list2[0][1])
        list3 = [1, '2', [1, 2, 3]]
        print(list3)
        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)
        print(2*list4)
        list4.append(list5)
        print(list4)
        list4[-2:] = []
        print(list4)
        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)
        print(c[0][1])
        c[0][1] = 10
        print(c)
        a =range(10)
        print(a)
        print(sum(a))
        b = [2, 10, 0, -2]
        print(sorted(b))
        b.index(0)
        len(b)
        print(b.index(0), len(b))


    def quiz21tuple(self) -> str:
        a = (1, 2)
        print(a, type(a))
        a = (1, 2)
        b = (0,(1, 4))
        print(a + b)


    def quiz22dict(self) -> str:
        a = {"class":['deep learning', 'machine learning'], "num_students":[40, 20]}
        print(a)
        print(type(a))
        print(a["class"])
        a['grade'] = ['A', 'B', 'C']
        print(a)
        print(a.keys())
        print(list(a.keys()))
        print(a.values())
        print(a.items())
        print(a.get('class'))
        print("class" in a)



    def quiz23listcom(self) -> str:
        print('--------- legacy ---------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)

        print('--------- comprehension ---------')
        a2 = [i for i in range(5)]
        print(a2)


    def quiz24zip(self) -> str:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml') # html.parser vs lxml
        '''
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        #print(''.join(i for i in artists))
        # print(soup.prettify())
        # print(type(artists)
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i for i in titles]
        print('\n'.join(i.get_text().strip() for i in titles))
        '''
        for i, j in enumerate(['artist', 'title']):
            print('\n\n\n'.join(i for i in [i for i in self.find(soup, j)]))
            print('*'*100)
        # a = [i for i in self.find(soup, 'artist')]
        # a = [i for i in self.find(soup, 'title')]
        '''
        self.find(soup, 'p', 'class', 'artist')
        print('*'*100)
        self.find(soup, 'p', 'class', 'title')
        '''

    @staticmethod
    def find(soup, a) -> str:
        ag = soup.find_all('p', {'class': a})
        ag = [i.get_text() for i in ag]
        # print('\n'.join(i.get_text().strip() for i in ag))
        return ag


    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0 '}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers = headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        songs = soup.find_all('div', {'class':'ellipsis rank01'})
        songs = [i for i in songs]
        print('\n'.join(i.get_text().strip() for i in songs))

    def quiz28(self) -> str:
        a = [i if i == 0 or i == 0 else i for i in range()]
        b = [i if i == 0 or i == 0 else i for i in []]
        c = [(i, j) for i, j in enumerate([])]
        d = ''.join(i for i in [])
        return None

    def quiz29(self) -> str: return None
