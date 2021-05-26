import cmath

def fft(p):
    """Calculates the FFT of a polynomial in coefficient representation."""
    deg = len(p)
    if p == []:
        return []
    elif deg == 1:
        return p
    even, odd = fft(p[::2]) * 2, fft(p[1::2]) * 2
    w = cmath.exp(2j * cmath.pi / deg)
    return [even[i] + w**i * odd[i] for i in range(deg)]

def ifft(p):
    return [i / len(p) for i in ifft_helper(p)]

def ifft_helper(p):
    """Calculates the IFFT of a set of complex exponentials."""
    deg = len(p)
    if p == []:
        return []
    elif deg == 1:
        return p
    even, odd = ifft_helper(p[::2]) * 2, ifft_helper(p[1::2]) * 2
    w = cmath.exp(-2j * cmath.pi / deg)
    return [even[i] + w**i * odd[i] for i in range(deg)]

def poly_mul(p1, p2):
    p1_pad = p1 + [0] * len(p1)
    p2_pad = p2 + [0] * len(p2)
    return ifft([i * j for i, j in zip(fft(p1_pad), fft(p2_pad))])
