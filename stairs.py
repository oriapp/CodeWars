def solve():
    for i in range(1, int(input())+1):
        print(f"{' ' * (i - 1)} {'-' * i}")
    print(chr_counter("ass"))


if __name__ == "__main__":
    solve()
