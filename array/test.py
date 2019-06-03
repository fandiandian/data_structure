def foo1(n):
    import time
    l1, l2 = list(range(100000)), list(range(100000))
    start = time.time()
    for i in range(n):
        l1.insert(0, i)
    end1 = time.time()
    l2.reverse()
    for i in range(n):
        l2.insert(len(l2), i)
    l2.reverse()
    end2 = time.time()
    t1 = (end1 - start) / n
    t2 = (end2 - end1) / n
    return t1, t2


if __name__ == "__main__":
    print(foo1(1))
