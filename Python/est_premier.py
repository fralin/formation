def est_premier(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    for i in range(2, 101):
        if est_premier(i):
            print(f"{i} est premier")
        else:
            print(f"{i} n'est pas premier")
        
        