
from threading import Timer

class PeriodicTimer(object):
    """
        Periodic timer wrapper class for the threading.Timer class
    """
    def __init__(self, interval, func, *args, **kwargs):
        self._timer     = None
        self.function   = func
        self.interval   = interval
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False