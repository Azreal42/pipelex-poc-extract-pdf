# :rocket: Welcome to the Pipelex Cookbook!

Start your Pipelex journey by following this quickstart guide below and checking out our samples.

> :books: Check out [Pipelex Repository](https://github.com/Pipelex/pipelex) and [Pipelex Documentation](https://github.com/Pipelex/pipelex/blob/dev/doc/Documentation.md) for more information.

## Clone the Repository

```bash
git clone https://github.com/Pipelex/pipelex-cookbook.git
cd pipelex-cookbook
```

## Prepare your virtual environment

Example using uv:

```bash
uv venv --python 3.11
source .venv/bin/activate
uv sync --extra dev
```

This will install the Pipelex python library and its dependencies using poetry.

## Set up environment variables

```bash
cp .env.example .env
```

Enter your API keys into your `.env` file. The `OPENAI_API_KEY` is enough to get you started, but some pipelines require models from other providers.

## Run Hello World

```bash
python cookbook/quick_start/hello_world.py
```
