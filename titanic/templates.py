from context.domains import Dataset
from context.models import Model
from models import TitanicModel
from icecream import ic
import matplotlib.pyplot as plt
'''
데이터 시각화
앤티티(개체)를 차트로 표현하는 것 

모든 feature 를 다 그려야 하지만, 시간 관계상 
survived, pclass, sex, embarked 의 4개만 그리겠습니다. 
템플릿 메소드 패턴으로 구성하시오 
'''


class TitanicTemplates(object):
    dataset = Dataset()
    model = Model()

    def __init__(self, fname):
        self.entity = self.model.new_model(fname)
        this = self.entity
        ic(f'트레인의 타입: {type(this)}')
        ic(f'트레인의 컬럼: {this.columns}')
        ic(f'트레인의 상위5행: {this.head()}')
        ic(f'트레인의 하위5행: {this.tail()}')

    def visualize(self) -> None:
        this = self.entity
        self.survived_nominal(this)
        self.pclass_ordinal(this)
        self.sex_nominal(this)
        self.embarked_nominal(this)

    @staticmethod
    def survived_nominal(this) -> None:
        plt.show()

    @staticmethod
    def pclass_ordinal(this) -> None:
        plt.show()

    @staticmethod
    def sex_nominal(this) -> None:
        plt.show()

    @staticmethod
    def embarked_nominal(this) -> None:
        plt.show()

