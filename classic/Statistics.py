from scipy.stats import chisquare

SPANISH_LETTER_FREQUENCY = {"a": 12.53, "b": 1.42, "c": 4.68, "d": 5.86, "e": 13.68, "f": 0.69, "g": 1.01, "h": 0.7,
                            "i": 6.25, "j": 0.44, "k": 0.02, "l": 4.97, "m": 3.15, "n": 6.71, "ñ": 0.31, "o": 8.68,
                            "p": 2.51, "q": 0.88, "r": 6.87, "s": 7.98, "t": 4.63, "u": 3.93, "v": 0.90, "w": 0.01,
                            "x": 0.22, "y": 0.90, "z": 0.52}

ENGLISH_LETTER_FREQUENCY = {"a": 8.2, "b": 1.5, "c": 2.8, "d": 4.3, "e": 13, "f": 2.2, "g": 2, "h": 6.1, "i": 7,
                            "j": 0.15, "k": 0.77, "l": 4, "m": 2.4, "n": 6.7, "o": 7.5, "p": 1.9, "q": 0.095, "r": 6,
                            "s": 6.3, "t": 9.1, "u": 2.8, "v": 0.98, "w": 2.4, "x": 0.15, "y": 2, "z": 0.074}


def new_alphabet():
    return {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
            "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "ñ": 0, "o": 0,
            "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0,
            "x": 0, "y": 0, "z": 0}


def absolute_frequency_histogram(text):
    text_frequency = new_alphabet()
    real_length = 0
    for i in range(len(text)):
        actual_character = text[i]
        if actual_character in text_frequency:
            real_length += 1
            text_frequency[actual_character] += 1
    return text_frequency, real_length


def relative_frequency_histogram(text):
    absolute, length = absolute_frequency_histogram(text)
    for key in absolute.keys():
        absolute[key] = (absolute[key] / length) * 100
    return absolute, length

def xi(text):
    absolute, length = absolute_frequency_histogram(text)
    valor = list(absolute.values())
    valor2 = list(SPANISH_LETTER_FREQUENCY.values())
    for i in range(len(valor2)):
        valor2[i] *= length
    return chisquare(valor, valor2)
