import logging
import threading


class Hook(object):
    """Emacs-style hook, allows arbitrary functions to be run at specific times.

    When the hook is `run`, every function attached to the hook is executed.
    Exceptions will not interrupt subsequent functions.

    """

    def __init__(self):
        self._lock = threading.Lock()
        self._functions = []

    def add(self, function_):
        """Add a function to the hook.

        The function will be called whenever the hook is run.

        """
        with self._lock:
            self._functions.append(function_)

    def remove(self, function_):
        """Remove a function from the hook. See `add`.

        Will not raise an error if the function is absent.

        """
        with self._lock:
            try:
                self._functions.remove(function_)
            except AttributeError:
                pass

    def run(self, *args, **kwargs):
        """Run all functions attached to the hook.

        Provide ``args`` or ``kwargs`` to run the functions with arguments.

        Errors will be logged, but otherwise ignored.

        """
        with self._lock:
            functions_copy = self._functions
        for func in functions_copy:
            try:
                func(*args, **kwargs)
            except Exception:
                logging.exception("Error running hooked function")
