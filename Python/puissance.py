def calc_puissance(x: int, y: int) -> int:
    value = 1
    for _ in range(y):
        value *=x
    return value

if __name__ == "__main__":
    for i in range(21):
        print(f"2^{i}\t = {calc_puissance(2,i):8}")
        

    