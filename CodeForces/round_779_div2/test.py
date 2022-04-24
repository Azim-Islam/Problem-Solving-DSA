def turn_to_2d(string, M, N):
    arr = [[] for i in range(M)]
    for index, value in enumerate(string):
        arr[index%M].append(value)
    return arr


#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


def main():
    for _ in range(int(input().rstrip())):
        N, M = map(int, input().rstrip().split())
        string = input().rstrip()
        string = list(string)
        string += list(" "*(N*M-len(string)))

        string = turn_to_2d(string, M, N)

        for q in range(M):
            Q, K = input().split()
            K = int(K)
            if Q == "U":
                tmp_arr = [0]*N
                for i in range(N):
                    tmp_arr[(i-(K%N))] = string[q][i]
                string[q] = tmp_arr
            else:
                tmp_arr = [0]*N
                for i in range(N):
                    tmp_arr[(i+K)%N] = string[q][i]
                string[q] = tmp_arr

        ans = []
        for i in range(N):
            for j in range(M):
                ans.append(string[j][i])
        print("".join(ans))


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()