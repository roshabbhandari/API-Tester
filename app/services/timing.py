from time import perf_counter


class Timer:
    def __enter__(self):
        self.started = perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed_ms = (perf_counter() - self.started) * 1000
