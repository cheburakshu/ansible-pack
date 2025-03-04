# noqa: INP001
def module(mod_name, **params):
    path = __salt__["cp.cache_file"](f"salt://{mod_name}.zip")  # noqa: F821
    return __utils__["ansiblepack.run"](mod_name, path, params)  # noqa: F821
