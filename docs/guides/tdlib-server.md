# TDLib Server

Scale with [TDLib Server](https://github.com/pytdbot/tdlib-server): one TDLib process, many Pytdbot workers over NATS.

```bash
pip install pytdbot[nats]
```

Pass `nats_url=` (and optional `instance_id=`) on [`Client`](client.md). `no_updates=True` if this process only sends requests.
