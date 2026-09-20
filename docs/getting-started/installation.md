# Installation

Pytdbot needs **Python 3.10+**, a Telegram [API key](https://my.telegram.org/apps), and TDLib.

## Recommended

Install Pytdbot with a pre-built TDLib (`tdjson`):

```bash
pip install --upgrade pytdbot[tdjson]
```

For faster JSON parsing, also install [orjson](https://github.com/ijl/orjson) or [ujson](https://github.com/ultrajson/ultrajson).

## Without a pre-built TDLib

If that extra fails, install the library alone:

```bash
pip install pytdbot
```

Then [build TDLib from source](https://github.com/tdlib/td#building) and pass the library path:

```python
client = Client(..., lib_path="/path/to/libtdjson.so")
```

## Development version

```bash
pip install --pre pytdbot
```

## Optional extras

| Extra | Install | What it is |
| --- | --- | --- |
| `tdjson` | `pip install pytdbot[tdjson]` | Pre-built TDLib |
| `nats` | `pip install pytdbot[nats]` | [TDLib Server](../guides/tdlib-server.md) via NATS |
| `docs` | `pip install pytdbot[docs]` | This site (`properdocs serve`) |

Next: [Quick start](quickstart.md).
