import math
A = [1,5,3,4,3,4,1,2,3,4,6,2]

def flagPeaks(A):
    peaks = [0] * len(A)
    next_peak = len(A)
    peaks[len(A) - 1] = next_peak
    for i in range(len(A) -2,0,-1):
        if A[i-1]<A[i] and A[i+1]<A[i]:
            next_peak = i
        peaks[i] = next_peak
    peaks[0] = next_peak
    print(peaks)

    current_guess = 0
    next_guess = 0
    while can_place_flags(peaks, next_guess):
        current_guess = next_guess
        next_guess += 1
    return current_guess

def can_place_flags(peaks, flags_to_place):
    current_position = 1 - flags_to_place
    for i in range(flags_to_place):
        if current_position + flags_to_place > len(peaks) - 1:
            return False
        current_position = peaks[current_position + flags_to_place]
    return current_position < len(peaks)


def flagPeaks1(A):
    N = len(A)
    peaks = []
    for i in range(1,N-1):
        if A[i-1] < A[i] and A[i+1] < A[i]:
            peaks.append(i)
    if len(peaks) <= 1:
        return len(peaks)
    print(peaks)
    maxFlags = int(math.ceil(math.sqrt(peaks[len(peaks) - 1] - peaks[0])))
    print(maxFlags)
    peaksSize = len(peaks)

    for flag in range(maxFlags,1,-1):
        startIndex = 0
        endIndex = peaksSize - 1

        startFlag = peaks[startIndex]
        endFlag = peaks[endIndex]
        flagsPlaced = 2
        while startIndex < endIndex:
            startIndex += 1
            endIndex -= 1

            if peaks[startIndex] >= startFlag + flag:
                if peaks[startIndex] <= endFlag - flag:
                    flagsPlaced += 1
                    startFlag = peaks[startIndex]

            if peaks[endIndex] >= startFlag + flag:
                if peaks[endIndex] <= endFlag - flag:
                    flagsPlaced += 1
                    endFlag = peaks[endIndex]

            if flagsPlaced == flag:
                return flag
    return 0

print(flagPeaks(A))
print(flagPeaks1(A))