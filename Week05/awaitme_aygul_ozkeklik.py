import asyncio
import awaitme  

def test_basic():
    @awaitme.awaitme
    def add(x: int, y: int) -> int:
        return x + y

    @awaitme.awaitme
    def capitalize(s: str) -> str:
        return s.capitalize()

    async def run_tests():
        assert await add(2, 3) == 5
        assert await capitalize("aygül") == "Aygül"

    asyncio.run(run_tests())

if __name__ == "__main__":
    test_basic()
    print("Everything passed ✅")
