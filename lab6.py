def only_integers(func):
    def wrapper(*args, **kwargs):
        for v in list(args) + list(kwargs.values()):
            if not (isinstance(v, int) and not isinstance(v, bool)):
                raise TypeError("Усі аргументи мають бути цілими числами")
        return func(*args, **kwargs)
    return wrapper
