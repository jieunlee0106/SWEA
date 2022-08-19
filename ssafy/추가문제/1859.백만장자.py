T = int(input())
for t in range(T):
    day = int(input())
    price = list(map(int, input().split()))
    my_coin = 0
    stack = []
    max_price = max(price)
    max_price_index = price.index(max_price)
    if max_price_index != 0:
        for i in range(len(price)):
            for p in price[:max_price_index]:
                my_coin += max_price - p
                price.remove(p)
            price.remove(max_price)
            if price:
                max_price = max(price)
                max_price_index = price.index(max_price)
            if not price:
                break
    print(f'#{t+1}', my_coin)
