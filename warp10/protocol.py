import json
import toml


class Packet:
    def __init__(self):
        self.changes = []

    def dump(self):
        return json.dumps(self.changes)

    def _add_change(self, cssclass: str, content: str, method: str, *args):
        self.changes.append([cssclass, method, content, *args])
        return self

    def append(self, cssclass: str, content: str):
        return self._add_change(cssclass, content, "append")

    def remove(self, cssclass):
        return self._add_change(cssclass, None, "remove")

    def write(self, cssclass, content):
        return self._add_change(cssclass, content, "write")

    def insert(self, cssclass, content, indices: tuple):
        return self._add_change(cssclass, content, "insert", indices)


class CustomPacket(Packet):
    def __init__(self, name, tag, value, **kwargs):
        super().__init__()
        self.tag = tag
        self.value = value
        self.name = name
        if kwargs:
            print("[WARN] Got unexpected kwargs", kwargs)

    def __call__(self, val):
        self.changes = []
        content = (self.value % val) if not isinstance(val, list) else ("".join([self.value % v for v in val]))
        self.write(self.tag, content)
        return self

    def __repr__(self):
        return f"<{self.name} tag={self.tag} value={self.value}>"

    __str__ = __repr__

    @classmethod
    def from_toml(cls, filename, name):
        with open(filename, "r") as file:
            content = toml.loads(file.read())
        return cls(name, **(content[name]))
