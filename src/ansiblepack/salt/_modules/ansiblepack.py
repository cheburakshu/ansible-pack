# noqa: INP001
def module(mod_name, saltenv="base", **params):
    path = __salt__["cp.cache_file"](f"salt://{mod_name}.zip")  # noqa: F821
    if not path:
        return f"Unable to find {mod_name} in {saltenv}."
    return __utils__["ansiblepack.run"](mod_name, path, params)  # noqa: F821
