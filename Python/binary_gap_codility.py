# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

N = 32


def solution(N):
    # write your code in Python 3.6
    N = [int(x) for x in bin(N)[2:]]
    print(N)
    i_count = 0
    counts = {i_count:0}
    for inx, i in enumerate(N):
        if i == 1:
            i_count = i_count + 1
            count_num = 0
            try:
                print(N[inx+1])
                while N[inx+1] == 0:
                    count_num += 1
                    print(count_num)
                    inx += 1
                if i == 1:
                    counts[i_count] = count_num
            except IndexError:
                break
    print(counts)
    return max(counts.values())

solution(N)
