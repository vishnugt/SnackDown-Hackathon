for testcase in range(int(raw_input())):
    n, k = map(int, raw_input().split())
    scores = list(map(int, raw_input().split()))
    scores.sort(reverse=True)
    numPeopleCleared = 0
    iterator = 0
    while iterator < k and iterator < n:
        if iterator != n-1 and scores[iterator] == scores[iterator+1]:
            numPeopleCleared+=1
            scores.remove(scores[iterator])
            continue
        iterator+=1
        numPeopleCleared+=1
    print(numPeopleCleared)
