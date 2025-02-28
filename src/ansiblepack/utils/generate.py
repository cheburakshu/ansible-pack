import fnmatch
import functools
import logging
import pathlib

import ansiblecall

import ansiblepack
from ansiblepack.utils.process import Parallel

log = logging.getLogger(__name__)


class Packer(Parallel):
    def __init__(self, func):
        self.func = func

    @classmethod
    def pack(cls, modules=None, pattern=None):
        mods = list(ansiblecall.refresh_modules())
        pack_mods = set()
        if modules:
            pack_mods = set(modules) & set(mods)
        if pattern:
            for mod in mods:
                if fnmatch.fnmatch(mod, pattern):
                    pack_mods.add(mod)
        if not pack_mods and not (modules or pattern):
            pack_mods = mods
        cache_dir = pathlib.Path(ansiblepack.__file__).parent.joinpath("modules")
        cache_dir.mkdir(parents=True, exist_ok=True)
        funcs = [functools.partial(ansiblecall.cache, mod_name=mod, dest=cache_dir) for mod in pack_mods]
        tasks = [cls(func=func) for func in funcs]
        cls.start(tasks=tasks)

    def run(self):
        """
        Package ansible modules as zip files
        """
        return self.func()
