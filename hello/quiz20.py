import random


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


    def quiz24zip(self) -> str: return None

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27(self) -> str: return None

    def quiz28(self) -> str: return None

    def quiz29(self) -> str: return None
