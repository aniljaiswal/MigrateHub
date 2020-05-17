import os
import asyncio
from .github import Github

async def transfer_account(dry_run=True):
    repositories = []
    source = os.getenv('SOURCE_USER')
    source_token = os.getenv('SOURCE_TOKEN')
    target = os.getenv('TARGET_USER')
    target_token = os.getenv('TARGET_TOKEN')
    await transfer_repo(source, source_token, target, dry_run)
    await transfer_starred(source, source_token, target, target_token, dry_run)
    await transfer_network(source, source_token, target, target_token, dry_run)

async def transfer_repo(source, source_token, target, dry_run=True):
    async with Github(source, source_token) as client:
        response = await client.repos()
        repositories = list(map(lambda x: x['name'], response.json()))

        if dry_run:
            for repo in repositories:
                print(repo)
        else:
            for repo in repositories:
                response = await client.transfer('demo', target)
                print(response.json())

async def transfer_starred(source, source_token, target, target_token, dry_run=True):
    async with Github(source, source_token) as client:
        starred = []
        response = await client.starred_repos(per_page=100)
        starred = response.json()
        repositories = [tuple(repo["full_name"].split("/")) for repo in starred]

        if dry_run:
            for owner, repo in repositories:
                print(f"{owner}: {repo}")
        else:
            async with Github(target, target_token) as client:
                for owner, repo in repositories:
                    response = await client.star_repo(owner, repo)
                    print(response)

async def transfer_network(source, source_token, target, target_token, dry_run=True):
    async with Github(source, source_token) as client:
        response = await client.followers(per_page=100)
        followers = [user["login"] for user in response.json()]

        response = await client.following(per_page=100)
        following = [user["login"] for user in response.json()]

        if dry_run:
            for user in followers + following:
                print(user)
        else:
            async with Github(target, target_token) as client:
                for user in followers + following:
                    response = await client.follow_user(user)
                    print(response)

