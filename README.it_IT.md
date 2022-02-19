# Rws

> **Rws.** è una piattaforma sociale per leggere, scrivere e condividere pensieri e notizie.
> Questo progetto si trova nella fase iniziale di sviluppo.

## Prerequisiti

* Python 3.6+ (se non ne sei sicuro puoi verificare con `python3 --version`)

* [FastAPI](https://github.com/tiangolo/fastapi) - Il web framework

* [aioredis](https://github.com/aio-libs/aioredis) - Per accedere al db Redis in modo asincrono

* [async_lru](https://github.com/aio-libs/async_lru) - Per il caching asincrono delle funzioni

## Da dove iniziare

1. Esegui `git clone https://github.com/osmanjtekin/Rws.git` nella CLI.

2. `cd` nella cartella Rws.

3. Esegui `uvicorn bootstrap:app` o `uvicorn bootstrap:app --reload` se vuoi ricaricare il server dopo ogni modifica del codice. L'host e la porta predefinita sono rispettivamente `127.0.0.1` e `8000`, ma puoi appendere `--host <host_address>` o `--port <port_number>` per valori personalizzati.

## Tecnologie

* [FastAPI](https://github.com/tiangolo/fastapi)

* [Redis](https://redis.io)

## Licenza

Questo progetto è rilasciato sotto licenza MIT - vedi il file [LICENSE](LICENSE) per dettagli.

## Anteprima approssimativa (homepage)
![preview](https://raw.githubusercontent.com/tekinosman/Rws/main/misc/preview.png)
