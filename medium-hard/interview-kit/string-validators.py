if __name__ == '__main__':
    s = input()
    print(s.isalnum())
    print(any(list(map(lambda t: t.isalpha(), list(s)))))
    print(any(list(map(lambda t: t.isdigit(), list(s)))))
    print(any(list(map(lambda t: t.islower(), list(s)))))
    print(any(list(map(lambda t: t.isupper(), list(s)))))