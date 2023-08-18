import importlib
import sys
import glob
from pathlib import Path
sys.path.append('./modules')


class MyApplication:
    # We are going to receive a list of plugins as parameter
    def __init__(self):
        self.modules_dir = "modules"
        modules_tmp = glob.glob(f'{self.modules_dir}/*.py')
        self.modules = []
        for module in modules_tmp:
            module_path = Path(module)
            module_name = module_path.stem
            self.modules.append(module_name)

    def new_object(self, module_name):
        if module_name in self.modules:
            return importlib.import_module(module_name, self.modules_dir).Plugin()


    def run(self):
        print("Starting my application")
        print("-" * 10)
        print("This is my core system")
        print("-" * 10)

        objects = {}
        counter = 0
        for plugin in self.modules:
            objects.update({f"{plugin}_{counter}": self.new_object(plugin)})
            counter += 1
        for plugin in self.modules:
            objects.update({f"{plugin}_{counter}": self.new_object(plugin)})
            counter += 1

        for name, obj in objects.items():
            print(name, obj)

        print("-" * 10)
        print("Ending my application")
        print()
