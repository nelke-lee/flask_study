def main():
    print('Hello, world!')

def exercise0401():
    print('04-14 번')
    x = 0xF0 | 0x0F # x -> 0xFF
    print(x)

def exercise0402():
    print('04-15 번')
    a = '{0} {1}'.format('Mario', 48)
    b = '{name} {age}'.format(name = 'Luigi', age = 35)
    print(a)
    print(b)

def exercise0501():
    print('05-04 번')
    a = 1,2,3,4,5
    print(a , type(a))
    a = 1,
    print(a , type(a))
    a = (1,2,3,4,5)
    print(a , type(a))
    a = [1,2,3,4,5]
    print(a , type(a))


def exercise0502():
    print('05-06 번')
    #a = (1,2,3)
    #a[0] = 7
    #print(a[0])

    b = [1,2,3]
    b[0] = 7
    print(b[0])

if __name__ == '__main__':
    main()
    exercise0401()
    exercise0402()
    exercise0501()
    exercise0502()
