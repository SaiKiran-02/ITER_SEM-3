import math

def functionGrowth():
    n = 16
    print(f"log N\t\t\t\t\t\tN\t\t\tN log N\t\t\t\t\t\tN^2\t\t\tN^3\t\t\t\t\t2^N")
    while (n!=2**12):
        print(f"{math.log(n,10)}\t\t\t{n}\t\t\t{n*math.log(n,10)}\t\t\t{n**2}\t\t\t{n**3}\t\t\t\t{2**n}")
        n = n*2

functionGrowth()
