from MongoDB import *
from SurrealDB import *
from SqLite import *
from signup import *
import asyncio

async def main():
    for i in userall:
        await ISDB(i[0], i[1], i[2], i[3], i[4])


if __name__ == "__main__":
    asyncio.run(main())