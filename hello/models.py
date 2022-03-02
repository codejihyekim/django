class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def did(self):
        return self.num1 / self.num2

    def opcode(self):
        if opcode == "+":
            return f'{calc.num1} + {calc.num2} = {calc.add()}'
        elif opcode == "-":
            return f'{calc.num1} - {calc.num2} = {calc.sub()}'
        elif opcode == "*":
            return f'{calc.num1} * {calc.num2} = {calc.mul()}'
        elif opcode == "/":
            return f'{calc.num1} / {calc.num2} = {calc.did()}'

class Bmi:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
    def bmi(self):
        bmires = self.weight / (self.height * self.height) * 10000
        if bmires < 18.5:
            return f'저체충'
        elif bmires < 22.9:
            return f'정상'
        elif bmires < 24.9:
            return f'과체중'
        elif bmires < 29.9:
            return f'경도비만'
        elif bmires < 34.9:
            return f'중도비만'
        else:
            return f'고도비만'

class Grade:
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

if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1.연산자 2.BMI 3.Grade')
        if menu == '0':
            break
        elif menu == '1':
            num1 = int(input('첫번째 수'))
            num2 = int(input('두번째 수'))
            opcode = input('연산자')
            # 객체생성
            calc = Calculator(num1, num2)
            print('*' * 30)
            print(calc.opcode())

        elif menu == '2':
            name = input('이름')
            height = int(input('키'))
            weight = int(input('몸무게'))
            bmi = Bmi(name, height, weight)
            print('*' * 30)
            print(f'{bmi.name}님의 BMI는 {bmi.bmi()}입니다.')

        elif menu == '3':
            for i in ['국어', '영어', '수학']:
                print()

            name = input('이름')
            korscore = int(input('국어'))
            engscore = int(input('영어'))
            mathscore = int(input('수학'))
            grade = Grade(name, korscore, engscore, mathscore)
            print('*' * 30)
            print(f'{grade.name}님의 총점: {grade.sum()} 평균: {grade.avg()}으로 {grade.pas()}입니다.')



