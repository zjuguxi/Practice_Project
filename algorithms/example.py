class Sort:
    def __init__(self):
        self.time = 0 # 类变量

class Bubble(Sort):
    # def __init__(self):
    #     self.time = 0 # 类变量

    def sort(self,n):
        self.time = n

    def get_time(self):
        print(self.time)

bubble = Bubble()