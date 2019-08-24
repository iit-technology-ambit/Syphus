from threading import Thread


def make_async(f):
    """Decorate a function to allow running async tasks in threads."""
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper
