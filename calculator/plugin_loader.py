

import os
import importlib.util

def load_plugins(plugin_dir="calculator/plugins"):
    commands = {}
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            file_path = os.path.join(plugin_dir, filename)
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "register"):
                new_cmds = module.register()
                commands.update(new_cmds)
    return commands
