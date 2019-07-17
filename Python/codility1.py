N = 4

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    binary = bin(N).format(6)
    counts = {}
    maxx = 0
    count_no = 0
    for idx, i in enumerate(binary):
        if i == '1':
            try:
                j = idx+1
                count = 0
                while binary[j] == '0':
                    count += 1
                    j += 1
                counts['count_no_{}'.format(count_no)] = count
                print(counts.keys(), counts.items())
                maxx = max(counts.values())
                count_no += 1
            except:
                pass
    print(maxx)
    return maxx


solution(N)
print(bin(N).format(10))
