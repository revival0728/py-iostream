class ostream:
    def __init__(self, ofile):
        self.__ofile = ofile

    def write(self, *args) -> None:
        for var in args:
            self.__ofile.write(str(var))

    def writelist(self, *args) -> None:
        for var in args:
            buf = ''
            for i in var:
                buf += str(i) + ' '
            buf = buf[:-1]
            self.__ofile.write(buf)

    def writetuple(self, *args) -> None:
        for var in args:
            buf = ''
            for i in var:
                buf += str(i) + ' '
            buf = buf[:-1]
            self.__ofile.write(buf)

    def print(self, *args) -> None:
        buf = ''
        for var in args:
            buf += str(var) + ' '
        buf = buf[:-1] + '\n'
        self.__ofile.write(buf)

    def printlist(self, *args) -> None:
        buf = ''
        for var in args:
            for i in var:
                buf += str(i) + ' '
        buf = buf[:-1] + '\n'
        self.__ofile.write(buf)

    def printtuple(self, *args) -> None:
        buf = ''
        for var in args:
            for i in var:
                buf += str(i) + ' '
        buf = buf[:-1] + '\n'
        self.__ofile.write(buf)