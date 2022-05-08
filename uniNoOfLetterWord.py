#A = "aaaabbbbb"
A = "ccffaaddecee"
def uniLetterWord(A):
    mapLetters = {}
    noLetters = []
    for Letter in A:
        if Letter in mapLetters:
            mapLetters[Letter] += 1
        else:
            mapLetters[Letter] = 1
    print(mapLetters)

    noLetters = sorted(list(mapLetters.values()))
    print(noLetters)
    counter = 0

    while len(noLetters) > 0:
        frequency = noLetters[-1]
        del noLetters[-1]

        if len(noLetters) == 0:
            return counter

        if noLetters[-1] == frequency:
            if frequency > 1:
                noLetters.append(frequency - 1)
            counter += 1
        noLetters = sorted(noLetters)
    return counter








print(uniLetterWord(A))