import threading,time

class loopcalss:
    def __init__(self) -> None:
        self.flag = True

    def test1 (self)->None:
        for i in range(10):
            print(f'test1 : {i}')
            time.sleep(1)
    def loopfuc(self):
        while self.flag:
            print(f'action: {self.flag}')
            time.sleep(1)

action = loopcalss()
t1 = threading.Thread(target=action.test1)
t = threading.Thread(target=action.loopfuc)
t1.start()
t.start()
t1.join()

time.sleep(5)
# print('aaaa')
action.flag = False
