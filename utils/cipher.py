def ceaser_cipher(s: str, key: int) -> str:
    """

    :param s: String given for ciphering
    :param key: how many simbols should be shifted
    :return: ciphered string
    """
    chars = [chr((ord(let) + key) % 0x110000) for let in s]
    return "".join(chars)


def decipher(s: str, key: int) -> str:
    """
    Function deciphered any string by given key
    :param s: ciphered string
    :param key: how many simbols was shifted
    :return: deciphered string
    """
    chars = (chr((ord(let) - key) % 0x110000) for let in s)
    return ''.join(chars)


if __name__ == '__main__':
    print(chr(0x10ffff))
    text = input("input text")
    k = int(input("input key"))
    text = ceaser_cipher(text, k)
    print(text)
    text = decipher(text, k)
    print(text)
