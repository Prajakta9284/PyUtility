from typing import Any


class PluginMeta(type):
    """Automatically register plugin subclasses."""

    registry: dict[str, type[Any]] = {}

    def __new__(mcs, name: str, bases: tuple[type, ...], namespace: dict[str, Any]):
        cls = super().__new__(mcs, name, bases, namespace)

        if namespace.get("register_plugin", True):
            PluginMeta.registry[name] = cls

        return cls


class Plugin(metaclass=PluginMeta):
    register_plugin = False

    def run(self) -> str:
        raise NotImplementedError


class GreetingPlugin(Plugin):
    def run(self) -> str:
        return "Hello from the plugin!"
