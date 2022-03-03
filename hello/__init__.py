from hello.domains import Member
from hello.models import Quiz01Calculator, Quiz02Bmi, Quiz03Grade, Quiz05Dice, Quiz07RandomChoice, Quiz08Rps, \
    Quiz09GetPrime, Quiz10LeapYear, Quiz11NumberGolf, Quiz13Bank

if __name__ == '__main__':
    while 1:
        menu = input('0.Exit\n 1.연산자\n 2.BMI\n 3.Grade\n 4.AutoGrade\n 5.주사위\n '
                     '6.랜덤숫자\n 7.수강생\n 8.가위바위보\n 9.소수\n 10.년도\n 11.숫자맞추기\n '
                     '13.은행')
        if menu == '0':
            break
        elif menu == '1': # 계산기
            # 객체생성
            calc = Quiz01Calculator(int(input('첫번째 수')), int(input('두번째 수')), input('연산자'))
            print('*' * 30)
            print(f'{calc.num1} {calc.op} {calc.num2} = {calc.res()}')

        elif menu == '2': #BMI
            member = Member()
            q2 = Quiz02Bmi()
            member.name = input('이름: ')
            member.height = float(input('키: '))
            member.weight = float(input('몸무게: '))
            res = q2.getBmi(member)
            print(f'{member.name}님의 BMI는 {res}입니다.')

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
            print(f'{q8.game()}')
        elif menu == '9':
            q9 = Quiz09GetPrime(int(input('startnum')), int(input('endnum')))
            res = q9.getPrime()
            print(f'결과: {res}')
        elif menu == '10':
            q10 = Quiz10LeapYear(int(input('년도 입력')))
            print(f'입력한 년도는 {q10.leapYear()}')
        elif menu == '11':
            q11 = Quiz11NumberGolf()
            print(f'결과: {q11.game()}')
        elif menu == '1':
            q13 = Quiz13Bank()