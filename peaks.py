A = [1,2,3,4,3,4,1,2,3,4,6,2]

def peakBlocks(A):
    N = len(A)

    if N < 3:
        return 0

    peaks = []
    for i in range(1,N-1):
        if A[i-1] < A[i] and A[i+1] < A[i]:
            peaks.append(i)

    peakSize = len(peaks)

    if peakSize == 0:
        return 0

    for blocklength in range(3,(N//2)+1):
        if N % blocklength != 0:
            continue

        currentPeak = 0
        ok = True

        for blockStart in range(0,N,blocklength):
            foundPeak = False
            while(currentPeak < peakSize):
                if peaks[currentPeak] < blockStart+blocklength:
                    foundPeak = True
                    currentPeak += 1
                elif peaks[currentPeak] >= blockStart+blocklength:
                    break

            if not foundPeak:
                ok = False
                break

        if ok:
            return N//blocklength

    return 1







print(peakBlocks(A))