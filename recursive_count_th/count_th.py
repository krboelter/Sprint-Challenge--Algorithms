'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    w = list(word)
    test = w.pop(0)
    count = 0

    if len(w) <= 1:
        return count

    if test == 't' and w[0] == 'h':
        print(w)
        count += 1
        return count_th(w)
    else:
        return count_th(w)

        

print(count_th('thTHtH'))
