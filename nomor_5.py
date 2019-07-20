def evenSum(n):
    start = 0
    next = 1
    sumEven = 0
    for i in range(n):
        current = start + next
        start = next
        next = current
        if current % 2 == 0 and current < n:
            sumEven += current
    return sumEven 

def oddSum(n):
    start = 0
    next = 1
    sumOdd = 0
    for i in range(n):
        current = start + next
        start = next
        next = current
        if current % 2 != 0 and current < n:
            sumOdd += current
    return sumOdd 

print(evenSum(100))
print(evenSum(1000))
print(oddSum(100))
print(oddSum(1000))
