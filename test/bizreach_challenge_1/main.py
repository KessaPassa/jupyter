import sys


def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    # for i, v in enumerate(argv):
    #     print("argv[{0}]: {1}".format(i, v))

    num = argv[0]

    # 一文字ずつ出せるように文字列にしてlistに格納
    num_list = []
    for n in str(num):
        num_list.append(n)

    # 小さい順にソート
    num_list.sort()

    # 0が先頭にあるとダメなので、0以外が先頭になるまでループ
    index = 1
    while True:
        # 先頭が0だったら要素数の近い順に入れ替えて判定する
        if num_list[0] == '0':
            tmp = num_list[0]
            num_list[0] = num_list[index]
            num_list[index] = tmp
            index = index + 1

        else:
            break

    # listに一文字ずつ入れているのを一列の文字列に直し、数値に変換する
    result = int("".join(num_list))
    print(result)


if __name__ == '__main__':
    main(sys.argv[1:])
