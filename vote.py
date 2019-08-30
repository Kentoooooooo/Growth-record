#メイン関数
def main():
    M, N, K, a = get_data()
    
    groups = [0] * (M+1)
    groups[0] = N

    for i in range(K):
        get_vote(groups, a[i])
        
    max_indexes = get_max_index(groups)
    
    for index in max_indexes:
        print(index)


#標準入力の読み込み
def get_data():
    input_line = input()
    colomns = input_line.split(' ')
    M = int(colomns[0])
    N = int(colomns[1])
    K = int(colomns[2])
    a = [int(input()) for i in range(K)]
    return M, N, K, a


#演説後の支持者の移動
def get_vote(groups, i):
    for n in range(len(groups)):
        if n == i:
            continue
        else:
            if groups[n] > 0:
                groups[i] += 1
                groups[n] -= 1


# 最大値を持つリストの要素を取得
def get_max_index(groups):
    temp = groups[1:]
    max_val = max(temp)
    max_list = []
    for i, values in enumerate(temp):
        if values == max_val:
            max_list.append(i+1)
    return max_list


if __name__ == '__main__':
    main()
