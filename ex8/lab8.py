def num_different_permutations(word):
    return _helper_num_per(list(word), 0)


def _helper_num_per(word_ls, ind):
    if not word_ls:
        return 1
    elif ind == len(word_ls) - 1:
        print(word_ls,ind)
        return 1
    count = 0
    for i in range(ind, len(word_ls)):

        word_ls[ind], word_ls[i] = word_ls[i], word_ls[ind]
        count += _helper_num_per(word_ls, ind + 1)
        word_ls[ind], word_ls[i] = word_ls[i], word_ls[ind]

    return count
print(num_different_permutations("abb"))