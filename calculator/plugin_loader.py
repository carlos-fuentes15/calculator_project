"""Plugin loader for calculator plugins."""
import os
import importlib.util
import pathlib

PLUGINS_DIR = os.path.join(os.path.dirname(__file__), "plugins")


def load_plugins():
    """Dynamically load all plugins in the plugins directory."""
    plugins = []
    plugin_path = pathlib.Path(PLUGINS_DIR)

    for plugin_file in plugin_path.glob("*.py"):
        if plugin_file.name == "__init__.py":
            continue

        spec = importlib.util.spec_from_file_location(
            plugin_file.stem, plugin_file
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            plugins.append(module)
    return plugins
