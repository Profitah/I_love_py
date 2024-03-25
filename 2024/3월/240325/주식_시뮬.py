import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
stock_comp = {}
group_comp = {}
my_stock = {}

for _ in range(N):
    G, H, P = input().split() 
    G = int(G)
    stock_comp[H] = int(P)
    if G in group_comp.keys():
        group_comp[G].append(H)
    else:
        group_comp[G] = [H]

for _ in range(Q):
    menu = input().split()
    kind = int(menu[0])

    if kind == 1: 
        name = menu[1]
        stock = int(menu[2])
        if stock_comp[name] * stock <= M:
            M -= (stock_comp[name] * stock)
            if name not in my_stock.keys():
                my_stock[name] = stock
            else:
                my_stock[name] += stock

    if kind == 2: 
        name = menu[1]
        stock = int(menu[2])
        if name in my_stock.keys():
            if my_stock[name] <= stock:
                M += (my_stock[name] * stock_comp[name])
                del my_stock[name]
            else:
                M += (stock * stock_comp[name])
                my_stock[name] -= stock

    if kind == 3: 
        name = menu[1]
        stock_price = int(menu[2])
        stock_comp[name] += stock_price
        if stock_comp[name] < 0:
            stock_comp[name] = 0

    if kind == 4: 
        gname = int(menu[1])
        stock_price = int(menu[2])
        comp_list = group_comp[gname]
        for name in comp_list:
            stock_comp[name] += stock_price
            if stock_comp[name] < 0:
                stock_comp[name] = 0

    if kind == 5:  
        gname = int(menu[1])
        stock_price_percent = float(menu[2])
        comp_list = group_comp[gname]
        for name in comp_list:
            if stock_price_percent > 0:
                stock_comp[name] = (stock_comp[name] * (100 + stock_price_percent)) // 100
            else:
                stock_comp[name] = (stock_comp[name] * (100 - abs(stock_price_percent))) // 100
            stock_comp[name] = int(stock_comp[name] // 10) * 10

    if kind == 6:
        print(M)

    if kind == 7:
        money = 0
        for comp_name in my_stock.keys():
            money += (stock_comp[comp_name] * my_stock[comp_name])
        print(money + M)
