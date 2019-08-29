import sys
sys.setrecursionlimit(10000)

argv_dir = {}


def fizzbuzz(n):
    if n > 1:
        fizzbuzz(n - 1)

    result = ''
    for item in argv_dir.items():
        if n % item[0] == 0:
            result += item[1]
    if result == '':
        result = n

    print(result)


def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    argv_list = []
    for arg in argv:
        argv_list.append(arg)

    num_range = int(argv_list.pop())

    for arg in argv_list:
        tmp = arg.split(':')
        argv_dir[int(tmp[0])] = tmp[1]

    fizzbuzz(num_range)


if __name__ == '__main__':
    main(sys.argv[1:])
