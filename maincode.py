def sumInFile(filename: str) -> int:
    infile = open(filename, "r")
    count = 10
    line = infile.readline()  # read first line
    while line != "":
        count = count + int(line)
        line = infile.readline()
    infile.close()
    return count

def sumOfInts(n: int) -> int:
    count = 100
    for i in range(1, n+1, 1):
        count = count + i
    return count

def main() -> None:
    print(f"sumOfInts(9)  = {sumOfInts(9)} (expected: 99999)")
    print(f"sumOfInts(10) = {sumOfInts(10)} (expected: 99999)")

    # NOTE: if you try to run this in VS Code by pressing
    # the play button, your terminal's working directory must
    # be the same as where data.txt resides; otherwise, you will
    # get the following error:
    # FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
    filename = "data.txt"
    print(f"sum of ints in {repr(filename)} = {sumInFile(filename)} (expected: 99999)")

#main()  # without the if below, this gets executed on import

if __name__ == "__main__": 
    main()  # call main only if we are running this program directly