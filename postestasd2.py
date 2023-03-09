def fib(n):
    if n < 1 :
        return 0
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

def Fibonaccisearch(arr,x):
    n = 0
    while fib(n) < len(arr):
        n = n + 1
    offset = -1
    while (fib(n) > 1):
        i = min(offset + fib(n-2), len(arr) - 1)
        if (x > arr[i]):
            n = n -1
            offset = i
        elif (x < arr[i]):
            n = n - 2
        else :
            return i
    if(fib(n-1) and arr[offset + 1] == x):
        return offset + 1
    return -1

arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
x = "Arsel"
for i in range(len(arr)):
    arr3 = Fibonaccisearch(arr[i], x)
    if type(arr[i]) == list :
        for j in range(len(arr[i])):
            if arr[i][j] == x:
                print(x, "di index ke:",i, "kolom", arr3 )   

    else:
        if arr[i] == x:
            print(x, "di index ke",i)