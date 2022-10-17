# warp10
### python-powered SPA server
Or something like that

## > info

This project is under heavy development right now, and is by no means stable. With that said, this project is fairly small and should be easily modified to your needs.

## > learn

Look in [example](#/example).


## > structure

Most abstraction is based off the `Pipe` class.

```
Pipe
 +- __init__(pipeline)
 |
 +- async .broadcast(clients, packet)
 |
 +- async .on_connect(), async .on_message(), async .on_disconnect()
 |
 +- Element
     +- async .set(value)

Packet
 +- __init__()
 |
 +- .write(cssclass, value)
 |
 +- .remove(cssclass)
 | 
 +- .append(cssclass, value)
 |
 +- .insert(cssclass, value, indices)
 |
 +- CustomPacket
     +- __init__(name, tag, value)
     |
     +- @classmethod .from_toml() -> CustomPacket
     |
     +- __call__(val)
```