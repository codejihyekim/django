import random

from hello import Member
from hello.domains import my100, myRandom, members


class Quiz00:
    def quiz00calculator(self) -> float:
        a = my100()
        b = my100()
        o = ['+', '-', '*', '/', '%']
        ran = o[myRandom(0, 4)]
        if ran == '+': res = self.add(a, b)
        elif ran == '-': res = self.sub(a, b)
        elif ran == '*': res = self.mul(a, b)
        elif ran == '/': res = self.div(a, b)
        elif ran == '%': res = self.mod(a, b)
        print(f'{res}')

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b


    def quiz01bmi(self):
        this = Member()
        this.name = members()[myRandom(0, 23)]
        this.height = myRandom(1, 500)
        this.weight = myRandom(1, 500)
        b = this.weight / (this.height * this.height) * 10000
        if b >= 35:
            res = '고도비만'
        elif b >= 30:
            res = '중도비만'
        elif b >= 25:
            res = '경도비만'
        elif b >= 23:
            res = '과체중'
        elif b >= 18.5:
            res = '정상'
        else:
            res = '저체중'
        print(f'{this.name}님의 BMI는 {res}입니다.')

    def quiz02dice(self):
        print(myRandom(1, 6))

    def quiz03rps(self):
        user = myRandom(0, 2)
        com = myRandom(0, 2)
        rps = ['가위', '바위', '보']
        score = user - com
        if score == 0:
            res = f' com:{rps[com]} user:{rps[user]}으로 비겼습니다.'
        elif score == 1 or score == -2:
            res = f' com:{rps[com]} user:{rps[user]}으로 이겼습니다.'
        else:
            res = f' com:{rps[com]} user:{rps[user]}으로 졌습니다.'
        print(f'{res}')

    def quiz04leap(self):
        year = myRandom(1, 10000)
        if year % 4 == 0 and year % 10 != 0 or year % 400 == 0 :
            res = '윤년입니다.'
        else:
            res = '평년입니다.'
        print(f'{year}년도는 {res}')

    def quiz05grade(self):
        kor = myRandom(1, 100)
        eng = myRandom(1, 100)
        math = myRandom(1, 100)
        sum = self.sum(kor, eng, math)
        avg = self.avg(kor, eng, math)
        pas = self.pas(kor, eng, math)
        print(f' 국어:{kor} 영어:{eng} 수학:{math} 총점:{sum} 평균:{avg} {pas}')

    def sum(self, kor, eng, math):
        return kor + eng + math

    def avg(self, kor, eng, math):
        return self.sum(kor, eng, math) / 3

    def pas(self, kor, eng, math):
        if self.avg(kor, eng, math) > 80:
            res = '합격'
        else:
            res = '불합격'
        return res

    def quiz06memberChoice(self):
        ran = members()[myRandom(1, 23)]
        print(ran)

    def quiz07lotto(self):
        a = random.sample(range(1, 46), 6)
        a.sort()
        print(a)

    def quiz08bank(self): # 이름, 입금, 출금만 구현
        total =0
        while 1:
            menu = int(input('0.Exit 1.예금 2.출금 3.잔금'))
            money = myRandom(1, 10000)
            if menu == 0:
                return f'종료'
            elif menu == 1:
                total = self.save(money, total)
            elif menu == 2:
                total = self.pay(money, total)
            elif menu == 3:
                print(f'현재 잔금은 {total}입니다.')

    def save(self, money, total):
        total += money
        print(f'{money}를 예금하였습니다.')
        return total
    def pay(self, money, total):
        if total < money:
            print(f'잔고가 없습니다.')
        else:
            total -= money
            print(f'{money}를 출금하였습니다.')
        return total

    def quiz09gugudan(self): # 책받침구구단
        res = ''
        for i in range(2, 9, 4):
            for j in range(1, 10):
                for k in range(i, i+4):
                    res += f'{k}*{j}={k*j}'+'\t'
                res += '\n'
            res += '\n'
        print(res)

