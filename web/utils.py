"""
Module with utils functions
"""
from importlib import import_module
import importlib
import pkgutil

def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    Attributes:
        package: {package} -- Python package where all modules will be imported
        recursive: {bool} -- recursive import or not (default: `True`)

    Returns:
        dict[str, types.ModuleType]: all imported submodules
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for _, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))

    return results

def all_subclasses(cls):
    """
    Recursively get all subclasses of class

    Returns:
        [set]: all subclasses path
    """
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)])

def load_class(module_path):
    """
    Load the expected class using the module path str value

    Returns:
        class: the expected class to load
    """

    # retrieve module and expected class
    modules = module_path.split('.')
    module_name = '.'.join(modules[:-1])
    class_name = modules[-1]

    # load module and get class
    module = import_module(module_name)
    expected_class = getattr(module, class_name)

    return expected_class
