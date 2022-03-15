from context.domains import Dataset
from context.models import Model
from models import TitanicModel
from icecream import ic




class TitanicTemplates(object):
    def __init__(self, train_fname, test_fname):
        self.model = Model()
        self.dataset = Dataset()
        self.titanicModel = TitanicModel(train_fname, test_fname)
