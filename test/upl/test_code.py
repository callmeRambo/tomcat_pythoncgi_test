from Model1 import model
class test_code():
    def __init__(self):
        self.result = 0
    def get_result(self):
        test = model()
        test_result = test.get_result()
        self.result = test_result
        return self.result

    
