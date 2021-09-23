class Task:
    def __init__(self, time, func, *args, **kwargs):
        self.time = time
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        if self.time > 0:
            self.time -= 1
            return self.func (*self.args, **self.kwargs)
        else:
            return -1
