import random

def main():
    while 1:
        menu = input('0.Exit\n 1.연산자\n 2.BMI\n 3.Grade\n 4.AutoGrade\n 5.주사위\n '
                     '6.랜덤숫자\n 7.수강생\n 8.가위바위보\n 9.소수\n 10.년도\n 11.숫자맞추기\n')
        if menu == '0':
            break
        elif menu == '1': # 계산기
            # 객체생성
            calc = Quiz01Calculator(int(input('첫번째 수')), int(input('두번째 수')), input('연산자'))
            print('*' * 30)
            print(f'{calc.num1} {calc.op} {calc.num2} = {calc.res()}')

        elif menu == '2': #BMI
            bmi = Quiz02Bmi(input('이름'), int(input('키')), int(input('몸무게')))
            print(f'{bmi.name}님의 BMI는 {bmi.getBmi()}입니다.')

        elif menu == '3': #Grade
            grade = Quiz03Grade(input('이름'), int(input('국어')), int(input('영어')), int(input('수학')))
            print('*' * 30)
            print(f'{grade.name}님의 총점: {grade.sum()} 평균: {grade.avg()}으로 {grade.pas()}입니다.')
        elif menu == '4':
            for i in ['국어', '영어', '수학']:
                print(i)
            #grade = Quiz03Grade(input('이름'), int(input('국어')), int(input('영어')), int(input('수학')))
            print('*' * 30)
            print(f'{grade.name}님의 총점: {grade.sum()} 평균: {grade.avg()}으로 {grade.pas()}입니다.')
        elif menu == '5':
            q5 = Quiz05Dice()
            print(f'결과: {Quiz05Dice.cast()}')
        elif menu == '6':
            pass
        elif menu == '7':
            q7 = Quiz07RandomChoice()
            print(f'결과: {q7.chooseMember()}')
        elif menu == '8':
            q8 = Quiz08Rps(int(input('가위: 1 바위: 2 보: 3')))
            print(f'결과: com {q8.com}로 {q8.game()}')
        elif menu == '9':
            q9 = Quiz09GetPrime(int(input('startnum')), int(input('endnum')))
            print(f'결과: {q9.getPrime()}')
        elif menu == '10':
            q10 = Quiz10LeapYear(int(input('년도 입력')))
            print(f'입력한 년도는 {q10.leapYear()}')
        elif menu == '11':
            q11 = Quiz11NumberGolf()
            print(f'결과: {q11.game()}')

class Quiz01Calculator:
    def __init__(self, num1, num2, op):
        self.num1 = num1
        self.num2 = num2
        self.op = op

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def did(self):
        return self.num1 / self.num2

    def res(self):
        if self.op == "+":
            return f'{self.add()}'
        elif self.op == "-":
            return f'{self.sub()}'
        elif self.op == "*":
            return f'{self.mul()}'
        elif self.op == "/":
            return f'{self.did()}'


class Quiz02Bmi:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def getBmi(self):
        b = self.weight / (self.height * self.height) * 10000
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
        return res


class Quiz03Grade:

    def __init__(self, name, korscore, engscore, mathscore):
        self.name = name
        self.korscore = korscore
        self.engscore = engscore
        self.mathscore = mathscore

    def sum(self):
        return self.korscore + self.engscore + self.mathscore

    def avg(self):
        return self.sum() / 3

    def pas(self):
        if self.avg() > 80:
            return f'합격'
        else:
            return f'불합격'


class Quiz04GradeAuto(object):
    def __init__(self, name, korscore, engscore, mathscore):
        self.name = name
        self.korscore = korscore
        self.engscore = engscore
        self.mathscore = mathscore

    def sum(self):
        return self.korscore + self.engscore + self.mathscore

    def avg(self):
        return self.sum() / 3

    def getGrade(self):
        pass

    def pas(self):
        if self.avg() > 80:
            return f'합격'
        else:
            return f'불합격'


def myRandom(start, end):
    return random.randint(start, end)


class Quiz05Dice(object):

    @staticmethod
    def cast():
        return myRandom(1, 6)


class Quiz06RandomGenerator(object):
    pass


class Quiz07RandomChoice(object):
    def __init__(self):
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                       "권혜민", "서성민", "조현국", "김한슬", "김진영",
                       '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                       '최민서', '한성수', '김윤섭', '김승현',
                       "강 민", "최건일", "유재혁", "김아름", "장원종"]

    def chooseMember(self):
        ran = myRandom(0, 23)
        return self.members[ran]


class Quiz08Rps(object):

    def __init__(self, user):
        self.user = user
        self.com = myRandom(1, 3)

    def game(self):
        score = self.user - self.com
        if score == 0:
            res = '비겼습니다.'
        elif score == 1 or score == -2:
            res = '이겼습니다.'
        else:
            res = '졌습니다.'
        return res


class Quiz09GetPrime(object):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def getPrime(self):
        count = 0
        for i in range(self.num1, self.num2+1):
            for j in range(1, i+1):
                if i % j == 0:
                    count += 1
        if count <= 2:
            return i


class Quiz10LeapYear(object):
    def __init__(self, year):
        self.year = year

    def leapYear(self):
        if self.year % 4 == 0 and self.year % 10 != 0 or self.year % 400 == 0 :
            res = '윤년입니다.'
        else:
            res = '평년입니다.'
        return res


class Quiz11NumberGolf(object):

    def __init__(self):
        self.comNum = myRandom(1, 100)

    def game(self):
        while 1:
            userNum = int(input('숫자입력'))
            if userNum == self.comNum:
                return '정답입니다.'
            elif userNum > self.comNum:
                print('더 작은 수를 입력하세요')
            elif userNum < self.comNum:
                print('더 큰 수를 입력하세요')
            else:
                print('잘못 입력하셨습니다.')


class Quiz12Lotto(object):
    def __init__(self):
        pass


class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass


class Quiz14Gugudan(object): # 책받침구구단
    def __init__(self):
        pass



if __name__ == '__main__':
    main()


