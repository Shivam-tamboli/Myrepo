#Functuion catching

import time
from functools import lru_cache


@lru_cache(maxsize = 2)
def some_work(n):
    time.sleep(n)
    return n 


if __name__=='__main__':
    print("Now runnig some work")
    some_work(2)
    print("DONE.... CALLING AGAIN")
    some_work(2)
    print("called again")