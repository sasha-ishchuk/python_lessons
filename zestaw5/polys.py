# poly1(x) + poly2(x)
def add_poly(poly1, poly2):
    m, n = len(poly1), len(poly2)
    size = max(m, n)
    poly_sum = [0 for _ in range(size)]

    for i in range(0, m, 1):
        poly_sum[i] = poly1[i]

    for i in range(n):
        poly_sum[i] += poly2[i]

    return poly_sum


# poly1(x) - poly2(x)
def sub_poly(poly1, poly2):
    m, n = len(poly1), len(poly2)
    size = max(m, n)
    poly_sub = [0 for _ in range(size)]

    for i in range(0, m, 1):
        poly_sub[i] = poly1[i]

    for i in range(n):
        poly_sub[i] -= poly2[i]

    return poly_sub


# poly1(x) * poly2(x)
def mul_poly(poly1, poly2):
    m, n = len(poly1), len(poly2)
    prod = [0] * (m + n - 1)

    for i in range(m):
        for j in range(n):
            prod[i + j] += poly1[i] * poly2[j]

    return prod


# bool, [0], [0,0], itp.
def is_zero(poly):
    return sum(poly) == 0


# bool, porównywanie poly1(x) == poly2(x)
def eq_poly(poly1, poly2):
    m, n = len(poly1), len(poly2)

    if m != n:
        return False
    else:
        for i in range(0, m, 1):
            if poly1[i] != poly2[i]:
                return False

    return True


# poly(x0), algorytm Hornera
def eval_poly(poly, x0):
    n = len(poly)
    poly.reverse()
    result = poly[0]

    for i in range(1, n):
        result = result * x0 + poly[i]

    return result


# poly1(poly2(x)), trudne!
def combine_poly(poly1, poly2):
    poly_combined = [0]
    n = len(poly1)
    help_poly = poly2
    for i in range(0, n, 1):
        if poly1[i] != 0:
            if i == 0:
                poly_combined[i] = poly1[i]
            else:
                powered_poly2 = pow_poly(help_poly, i)
                mul_poly2 = combine_poly_mul(powered_poly2, poly1[i])
                poly_combined = add_poly(poly_combined, mul_poly2)
    return poly_combined


# poly(x) * n, help function
def combine_poly_mul(poly, n):
    poly_m = [0 for _ in range(len(poly))]
    if n == 1:
        return poly
    for i in range(0, len(poly), 1):
        poly_m[i] = poly[i] * n
    return poly_m


# poly(x) ** n
def pow_poly(poly, n):
    if n == 1:
        return poly
    powered_poly = poly
    for i in range(1, n):
        powered_poly = mul_poly(powered_poly, poly)
    return powered_poly


# pochodna wielomianu
def diff_poly(poly):
    return [poly[i] * i for i in range(1, len(poly))]


if __name__ == '__main__':
    print(add_poly([0, 1], [0, 0, 1]))
    print(sub_poly([0, 1], [0, 0, 1]))
    print(mul_poly([0, 1], [0, 0, 1]))
    print(is_zero([0, 1]))
    print(eq_poly([0, 1], [0, 0, 1]))
    print(eval_poly([0, 0, 1], 5))
    print(combine_poly([0, 1], [0, 0, 1]))  # [0, 0, 1]
    print(str(combine_poly([1, 1], [0, 0, 1])))  # [1, 0, 1]
    print(combine_poly([1, 1, 1], [3, 0, 1]))  # [13, 0, 7, 0, 1]
    print(combine_poly([4, 3, 1, 8], [1, 0, 1]))  # [16, 0, 29, 0, 25, 0, 8]
    print(pow_poly([0, 0, 1], 2))
    print(diff_poly([0, 0, 1]))
