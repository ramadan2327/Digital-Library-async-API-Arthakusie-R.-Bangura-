import asyncio
from typing import Dict

# Simulated library database
books: Dict[str, bool] = {
    "math_book": True  # True = available, False = borrowed
}

# Lock to handle concurrent access safely
lock = asyncio.Lock()


async def borrow_book(user: str, book: str) -> str:
    async with lock:
        print(f"{user} is trying to borrow {book}...")
        await asyncio.sleep(1)  # Simulate processing delay

        if books.get(book, False):
            books[book] = False
            return f"{user} successfully borrowed {book}"
        else:
            return f"{book} is not available for {user}"


async def return_book(user: str, book: str) -> str:
    async with lock:
        print(f"{user} is returning {book}...")
        await asyncio.sleep(1)  # Simulate processing delay

        books[book] = True
        return f"{user} returned {book}"


async def main() -> None:
    # Simulate multiple users accessing the system concurrently
    tasks = [
        borrow_book("Bob", "math_book"),
        return_book("Alice", "math_book"),
        borrow_book("Charlie", "math_book"),
    ]

    results = await asyncio.gather(*tasks)

    print("\n--- Results ---")
    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())