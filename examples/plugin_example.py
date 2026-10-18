from pyutility.registry import GreetingPlugin, Plugin, PluginMeta


class FarewellPlugin(Plugin):
    """Plugin that returns a farewell message."""

    def run(self) -> str:
        return "Goodbye from the plugin!"


def main() -> None:
    print("=== PyUtility Plugin Example ===")

    # Display all registered plugins
    print("\nRegistered plugins:")
    for plugin_name in PluginMeta.registry:
        print(f"- {plugin_name}")

    # Execute the greeting plugin
    greeting = GreetingPlugin()
    print("\nGreeting:", greeting.run())

    # Execute the farewell plugin
    farewell = FarewellPlugin()
    print("Farewell:", farewell.run())


if __name__ == "__main__":
    main()
