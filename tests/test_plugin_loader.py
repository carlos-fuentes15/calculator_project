"""Unit tests for plugin_loader.py."""

import types
from calculator.plugin_loader import load_plugins


def test_load_plugins_success(tmp_path, monkeypatch):
    """Test plugins load successfully from a given directory."""
    plugin_code = "def square(x): return x * x"
    plugin_file = tmp_path / "square.py"
    plugin_file.write_text(plugin_code)

    monkeypatch.setattr("calculator.plugin_loader.PLUGINS_DIR", str(tmp_path))
    plugins = load_plugins()
    assert isinstance(plugins, list)
    assert any(isinstance(p, types.ModuleType) for p in plugins)


def test_load_plugins_with_invalid_file(tmp_path, monkeypatch):
    """Test that non-Python files are ignored during plugin loading."""
    (tmp_path / "README.txt").write_text("This should be ignored")

    monkeypatch.setattr("calculator.plugin_loader.PLUGINS_DIR", str(tmp_path))
    plugins = load_plugins()
    assert isinstance(plugins, list)
    assert len(plugins) == 0
