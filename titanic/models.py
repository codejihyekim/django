from domain import Dataset

class Model:

    dataset = Dataset()

    def new_model(self, payload):
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return None