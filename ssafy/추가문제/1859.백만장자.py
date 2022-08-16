T = int(input())

for t in range(T):
    day = int(input())
    price = list(map(int, input().split()))
    my_coin = 0
    max_price = max(price)
    m_p_i = price.index(max_price)
    while m_p_i != day or :
        for i in range(m_p_i):
            my_coin += max_price - price[i]
        price = price[m_p_i + 1:]
        m_p_i = max(price)
    print(my_coin)