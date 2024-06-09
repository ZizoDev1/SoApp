from surrealdb import Surreal


async def ISDB(username, password, email, firstname, lastname):
    """Example of how to use the SurrealDB client."""
    async with Surreal("http://localhost:8000") as db:
        await db.signin({"user": "rootor", "pass": "aroot"})
        await db.use("pythonsdk", "userinfo")
        # In SurrealQL you can do a direct insert
        # and the table will be created if it doesn't exist
        await db.query("""
        INSERT INTO person {
            username : '{username}',
            password : '{password}',
            email    : '{email}',
            firstname: '{firstname}',
            lastname : '{lastname}'
        };
        """.format(username=username, password=password, email=email, firstname=firstname, lastname=lastname))
