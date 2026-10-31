"""Assignment 1: Division Algorithm

Find integers q and r such that a = b*q + r and 0 <= r < |b|.
"""

def division_algorithm(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero.")

    q = a // b
    r = a - b * q

    # Adjust to keep the remainder non-negative.
    if r < 0:
        if b > 0:
            q -= 1
            r += b
        else:
            q += 1
            r -= b

    return q, r


if __name__ == "__main__":
    print("DIVISION ALGORITHM")
    try:
        a = int(input("Enter dividend (a): "))
        b = int(input("Enter divisor (b): "))
        q, r = division_algorithm(a, b)
        print("Quotient:", q)
        print("Remainder:", r)
        print(f"Verification: {a} = ({b} * {q}) + {r}")
    except ValueError as error:
        print("Error:", error)
