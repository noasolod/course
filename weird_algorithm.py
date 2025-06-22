n = int(input("please enter an integer between 1 and 10**6: "))
track_results = [n]
while n != 1:
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = int(n * 3 + 1)
    track_results.append(n)
print(track_results)