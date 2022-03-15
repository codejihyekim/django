

from titanic.views import TitanicView

if __name__ == '__main__':

    view = TitanicView()
    while 1:
        menu = input('1.전처리')
        if menu == '1':
            print('### 1.전처리 ###')
            view.preprocess('test.csv', 'train.csv')
            break
        else:
            break
