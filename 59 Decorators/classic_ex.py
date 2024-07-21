import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("function took:", time.time()-before, "seconds")

    return wrapper

@timer
def run():
    time.sleep(5)

run()