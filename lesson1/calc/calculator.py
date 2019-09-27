def sum(m, n):
    if n < 0:
        for i in range(abs(n)):
            m = m - 1
    else:
        for i in range(n):
            m = m + 1
        return m


def div(m, n):
    if n == 0:
        raise Exception('Cant divide by 0')
    n_a = abs(n)
    m_a = abs(m)
    div = 0
    while m_a >= n_a:
        m_a = m_a - n_a
        div = div + 1
    if (m > 0 and n > 0) or (m < 0 and n < 0):
        return div
    else:
        return -1 * div


print(sum(3, 5))
print(div(3, -1))
print(div(-3, 1))
print(div(-3, -1))
print(div(3, 0))
