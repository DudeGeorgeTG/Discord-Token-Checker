import aiohttp
import asyncio

async def check_token(session, token):
    try:
        async with session.get(
            "https://canary.discord.com/api/v10/users/@me",
            headers={"Authorization": token}
        ) as response:
            if response.status in [200, 204, 201]:
                data = await response.json()
                user_id = data.get("id")
                username = data.get("username")
                print(f"Valid Token: {user_id} | {username}")
                return token
    except Exception as e:
        print(f"Error checking token: {e}")
    return None

async def main():
    valid_tokens = []
    
    try:
        with open("tokens.txt", "r") as f:
            tokens = [line.strip() for line in f.readlines() if line.strip()]
    except FileNotFoundError:
        print("tokens.txt not found!")
        return
    
    connector = aiohttp.TCPConnector(limit_per_host=10) 
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [check_token(session, token) for token in tokens]
        results = await asyncio.gather(*tasks)
        valid_tokens = [token for token in results if token is not None]
    
    if valid_tokens:
        with open("valid.txt", "w") as f:
            f.write("\n".join(valid_tokens))
        print(f"\nSaved {len(valid_tokens)} valid tokens to valid.txt")
    else:
        print("\nNo valid tokens found.")

if __name__ == "__main__":
    asyncio.run(main())
