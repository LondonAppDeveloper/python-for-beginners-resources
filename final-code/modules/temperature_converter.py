def c_to_f(c):
    """Convert celcius to fahrenheit and return result."""
    f = (c * 1.8) + 32

    return f


def f_to_c(f):
    """Convert fahrenheit to celcius."""
    c = (f - 32) / 1.8

    return c