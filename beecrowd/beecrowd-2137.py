while True:
    try:
        n = int(input())
        records = []

        for _ in range(n):
            records.append(input())

        for record in sorted(records):
            print(record)

    except EOFError:
        break
