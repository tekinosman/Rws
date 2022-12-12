# Rws

**Rws** is an experimental social platform for reading, writing, and sharing thoughts and news.

*Leggi questo README in [Italiano](README.it_IT.md).*

## Prerequisites

* Python 3.6+ (if not sure you can check with `python3 --version`)

* [FastAPI](https://github.com/tiangolo/fastapi) - The web framework

* [aioredis](https://github.com/aio-libs/aioredis) - For accessing the Redis db asynchronously

* [async_lru](https://github.com/aio-libs/async_lru) - For async function caching

## Usage

1. Run `git clone https://github.com/osmanjtekin/Rws.git` in your CLI.

2. `cd` to the Rws directory.

3. Run `uvicorn bootstrap:app` or `uvicorn bootstrap:app --reload` if you want to reload the server after code changes. Default host and port are `127.0.0.1` and `8000` respectively, but you can append `--host <host_address>` or `--port <port_number>` for custom values.

## Technologies

* [FastAPI](https://github.com/tiangolo/fastapi)

* [Redis](https://redis.io)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Preview (homepage)
![preview](https://raw.githubusercontent.com/tekinosman/Rws/main/misc/preview.png)
