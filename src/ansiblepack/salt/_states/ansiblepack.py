# noqa: INP001


"""
Run ansible modules as state modules via a salt proxy.

.. code-block:: yaml

    my_state:
      ansiblepack.module:
        - mod_name: ansible.builtin.ping
        - params:
            data: hello

"""

import json
import logging

__proxyenabled__ = ["ansiblepack"]
log = logging.getLogger(__name__)


def module(name, mod_name, params):
    """
    Run ansible modules statefully.

    :param name: State Id
    :param mod_name: Name of the ansible module to be run.
    :param params: Parameters for the ansible module
    :return: A standard Salt changes dictionary
    """
    # setup return structure
    ret = {
        "name": name,
        "changes": {},
        "result": False,
        "comment": "",
    }

    # TODO: Run in check mode
    # if __opts__["test"]:
    #     Set check module flag for the ansible module.

    mod_ret = __salt__["ansiblepack.module"](mod_name=mod_name, **params)  # noqa: F821

    changed = mod_ret.pop("changed", None)
    if changed:
        diff = mod_ret.pop("diff", {})
        ret["changes"] = diff

    failed = mod_ret.pop("failed", False)
    if failed:
        ret["comment"] = mod_ret.pop("msg", None)
        ret["result"] = False
    else:
        ret["comment"] = json.dumps(mod_ret)
        ret["result"] = True

    return ret
