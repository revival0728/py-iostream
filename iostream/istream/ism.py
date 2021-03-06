class istream:
    def __init__(self, ifile):
        self.__buffer = ''
        self.__ifile = ifile

    def __clear_spcecial_char(self, string) -> str:
        string = string.replace('\n', '')
        string = string.replace('\r', '')
        return string

    def __buffer_strip_front(self):
        while self.__buffer[0] in ('\r', ' ', '\n'):
            self.__buffer = self.__buffer[1:]

    def __read_buffer(self):
        while self.__buffer.replace(' ', '').replace('\n', '') == '':
            self.__buffer += self.__ifile.readline().replace('\r', '')

    def readline(self) -> str:
        return self.__clear_spcecial_char(self.__ifile.readline())

    def readchar(self) -> str:
        self.__read_buffer()
        self.__buffer_strip_front()
        buf = self.__buffer[0]
        self.__buffer = self.__buffer[1:]
        return buf

    def read(self, to_type=str):
        self.__read_buffer()
        buf = self.__buffer
        buf.strip()
        if not ' ' in buf:
            self.__buffer = self.__buffer.replace(buf, '', 1)
            return to_type(buf.strip())
        else:
            buf = buf.split()
            self.__buffer = self.__buffer.replace(buf[0], '', 1)
            return to_type(buf[0].strip())

    def readlist(self, to_type=str) -> list:
        self.__read_buffer()
        self.__buffer_strip_front()
        buf = self.__buffer.split('\n')[0]
        self.__buffer = self.__buffer.replace(buf, '', 1)
        if not ' ' in buf.strip():
            return [to_type(buf.strip())]
        else:
            buf = buf.strip().split()
            for i in range(len(buf)):
                buf[i] = to_type(buf[i])
            return buf

    def readtuple(self, to_type=str) -> tuple:
        return tuple(self.readlist(to_type))