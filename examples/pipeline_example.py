from pyutility.pipeline import chunk_items, filter_items, map_items


def main() -> None:
    numbers = [10, 15, 20, 25, 30, 35, 40]

    # 1. Map: multiply each number by 2
    doubled = list(map_items(numbers, lambda value: value * 2))
    print("Original numbers:", numbers)
    print("Doubled numbers:", doubled)

    # 2. Filter: select numbers greater than 20
    filtered = list(filter_items(numbers, lambda value: value > 20))
    print("\nNumbers greater than 20:", filtered)

    # 3. Chunk: divide numbers into groups of 3
    chunks = list(chunk_items(numbers, 3))
    print("\nNumbers divided into chunks:")
    for index, chunk in enumerate(chunks, start=1):
        print(f"Chunk {index}: {chunk}")


if __name__ == "__main__":
    main()
