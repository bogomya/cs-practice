def continuousBackpack(capacity: int, items: (int, int)):
    result = 0
    orderedItems = sorted(items, key=lambda item: item[0]/item[1], reverse = True)
    for i, [price, amount] in enumerate(orderedItems):
        part = min(capacity, amount)
        result += round(part/amount * price, 3)
        capacity = capacity - part
        if capacity <= 0:
            break
    return result


def main():
    items = []
    n, capacity = map(lambda i: int(i), input().split(" "))
    for i in range(n):
        price, amount = map(lambda i: int(i), input().split(" "))
        items.append(( price, amount))
    print(continuousBackpack(capacity, items))

if __name__ == "__main__":
    main()
