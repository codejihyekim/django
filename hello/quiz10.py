
import random
from hello import Member
from hello.domains import my100, myRandom, members

class Quiz10:

    def quiz10bubble(self) -> str:
        arr = []
        for i in range(0, 10):
            a = my100()
            if a not in arr:
                arr.append(a)
        for i in range(0, len(arr)):
            for j in range(0, len(arr)-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f'버블정렬: {arr}')


    def quiz11insertion(self) -> str: return None

    def quiz12selection(self) -> str: return None

    def quiz13quick(self) -> str: return None

    def quiz14merge(self) -> str: return None

    def quiz15magic(self) -> str: return None

    def quiz16zigzag(self) -> str: return None

    def quiz17prime(self):
        num = random.sample(range(1, 10), 2)
        num.sort()
        res = ''
        for i in range(num[0], num[1]+1):
            count = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    count += 1
            if count <= 2:
                res += str(i) + ' '
        print(res)
        if res == '':
            print(f'{num[0]}과 {num[1]} 사이에는 소수가 없습니다.')


    def quiz18golf(self):
        comNum = myRandom(1, 100)
        while 1:
            userNum = myRandom(1, 100)
            if userNum == comNum:
                print('정답입니다.')
                return
            elif userNum > comNum:
                print('더 작은 수를 입력하세요')
            elif userNum < comNum:
                print('더 큰 수를 입력하세요')
            else:
                print('잘못 입력하셨습니다.')

    def quiz19booking(self) -> str: return None