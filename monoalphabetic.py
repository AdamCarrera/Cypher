
cipher_text = "mgzoowirw iay aiok kavl fask fvy kavl cuis haui vp"

print("The cipher text is: ", cipher_text)


def replace_given_alphabet(cipher):
    in_tab = 'zrcalk'
    out_tab = 'agmory'

    transtab = str.maketrans(in_tab, out_tab.upper())
    return cipher.translate(transtab)


def common_frequencies(cipher):
    """
    This function evaluates the letter frequency in the cipher text
    and sorts it
    :param cipher: cipher text, string
    :return: sorted_freq, list of tuples
    """
    alpha_freq = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25
    }
    # print("Computing letter frequencies:")
    for letter in alpha_freq:
        # update alpha_freq with the letter's frequency
        alpha_freq[letter] = cipher.count(letter)

    sorted_freq = sorted(alpha_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq


def assign(cipher, frequency_tuple):
    """
    maps the given string to the frequency list
    replaces said characters in the cipher accordingly
    :param cipher: cipher text
    :param frequency_tuple: frequency tuple from common frequencies
    :return: translated cipher
    """
    # replace common frequencies with the letter e
    outtab = input('enter string to replace: ')
    length = len(outtab)
    user_in = []
    for x in range(26):
        user_in.append(frequency_tuple[x][0])
    intab = ''.join(user_in[0:length])
    transtab = str.maketrans(intab, outtab.upper())
    return cipher.translate(transtab)


k = replace_given_alphabet(cipher_text)
print("Replace given alphabet")
h = common_frequencies(k)
print(k)
j = assign(k, h)
print(j)

#nulbdiethjcs




