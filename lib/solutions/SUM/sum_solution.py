
class SumSolution:
    def compute(self, x, y=None):
        # If the first arg is iterable (list/tuple), unpack it
        if y is None and hasattr(x, '__iter__'):
            x, y = x
        return x + y

