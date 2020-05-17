import os

from httpx import AsyncClient

class Github(AsyncClient):
    """docstring for Github"""
    def __init__(self, user, token):
        self.user = user
        self.token = token

        super().__init__(
            base_url=os.getenv('GITHUB_BASE_URL'),
            auth=(self.user, self.token)
        )

    async def repos(self):
        return await self.get("/user/repos")

    async def transfer(self, repo, target):
        return await self.post(
            f"/repos/{self.user}/{repo}/transfer",
            json={"new_owner": target}
        )

    async def starred_repos(self, per_page=30):
        return await self.get(f"/user/starred?per_page={per_page}")

    async def star_repo(self, owner, repo):
        return await self.put(f"/user/starred/{owner}/{repo}")

    async def followers(self, per_page=30):
        return await self.get(f"/user/followers?per_page={per_page}")

    async def following(self, per_page=30):
        return await self.get(f"/user/following?per_page={per_page}")

    async def follow_user(self, username):
        return await self.put(f"/user/following/{username}")
