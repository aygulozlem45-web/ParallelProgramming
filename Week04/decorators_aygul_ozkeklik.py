import time
import sys
import functools

class Performance:
    def __init__(self):
        self.counter = 0        
        self.total_time = 0.0  
        self.total_mem = 0.0    

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()

            self.counter += 1
            self.total_time += (end - start)
            self.total_mem += sys.getsizeof(result)

            return result
        return wrapper

performance = Performance()
