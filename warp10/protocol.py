import json


class Packet:
    def __init__(self):
        self.changes = []

    def __str__(self):
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

    def insert(self, cssclass, content, index: int):
        return self._add_change(cssclass, content, "insert", index)
