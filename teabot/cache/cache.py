from collections import OrderedDict

class LRUCache:
    def __init__(self, function, max_size, on_expiration):
        self.function = function
        self.cache = OrderedDict()

    def __call__(self, *args):
        if args in self.cache:
            self.cache.move_to_end(args)
            return self.cache[args]
        result = self.function(*args)
        self.cache[args] = result
        if len(self.cache) > self.max_size:
            _, value = self.cache.popitem(0)
            if on_expiration is not None:
                on_expiration(value)
        return result

def cached(max_size, *, on_expiration=None):
    def decorator(function):
        lru = LRUCache(function, max_size, on_expiration)
        return lru
    
    return decorator

