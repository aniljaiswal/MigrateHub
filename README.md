# MigrateHub

Transfer your Github repositories, starred repos and followers to another user.

## Get Started

Requirements:

Python 3.8+ & `pipenv`

Create a .env file in project root.

```bash
cp .env.sample .env
```

Create a Github Personal access token for both users & update the values in
`.env` file.

Install dependencies:
```bash
pip3 install pipenv
pipenv install
```

Open async python3 REPL:
```bash
pipenv shell
python3 -m asyncio
```

In python terminal:

By default, the script is `dry run` and will only print responses.

```python
from migrate_bh import main
await main.account_transfer() # Pass `False` to start actual migration.
```

## TODO:
- [ ] Add CLI command based setup
- [ ] Add tests
- [ ] Add documentation
- [ ] Refactor codebase

## Contributing
Fork and send PRs

## Need help?
Raise an issue
