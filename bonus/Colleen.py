# lol c le bonus
def jebaited():
    return 0
def main():
    # ptdr
    str = "# lol c le bonus%cdef jebaited():%c    return 0%cdef main():%c    # ptdr%c    str = %c%s%c%c    buffer = str %% (10, 10, 10, 10, 10, 34, str, 34, 10, 10, 10)%c    print(buffer)%cmain()"
    buffer = str % (10, 10, 10, 10, 10, 34, str, 34, 10, 10, 10)
    print(buffer)
main()
