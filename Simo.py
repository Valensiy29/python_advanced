import threading


counter = 1

class Sem(threading.Thread):
    def __init__(self,semo: threading.Semaphore):
        super().__init__()
        self.sem = semo

    def worker_1(self):
        global counter
        with self.sem:
            while counter < 1000:
                counter += 1
                print('worker_1 add 1 penis')

    # def worker_2(self):
    #     global counter
    #     with self.sem:
    #         while counter > -1000:
    #             counter -= 1
    #             print('worker_1 remove 1 penis')

def main():
    semaphore = threading.Semaphore()
    counters = []
    for _ in range(2):
        work = Sem(semaphore)
        work.start()
        counters.append(work)

    for work in counters:
        work.join()



if __name__ == '__main__':
    main()