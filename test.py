if __name__ == '__main__':
    a = bin(6.6)
    b = bin(6)
    print(type(b))
    c = int(a, 2)-int(b, 2)
    print(a == b)
