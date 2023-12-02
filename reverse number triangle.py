def nNumberTriangle(n: int) -> None:
     for i in range(n+1):
         for j in range(n-i):
             print(j+1,end=" ")
         print()
