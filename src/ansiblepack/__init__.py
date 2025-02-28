import argparse
import logging

import ansiblepack.utils.generate

log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(name)-17s][%(levelname)-8s:%(lineno)-4d][%(processName)s:%(process)d] %(message)s",
)


def pack(modules=None, pattern=None):
    """Package ansible modules into zip files."""
    ansiblepack.utils.generate.Packer.pack(modules=modules, pattern=pattern)


def cli():
    parser = argparse.ArgumentParser(
        description="Ansible Module Packager: A CLI tool for creating self-contained, distributable Ansible modules"
    )
    parser.add_argument(
        "-m",
        "--modules",
        type=lambda x: x.split(","),
        help="Comma-separated list of modules",
        default=None,
    )
    parser.add_argument(
        "-p",
        "--pattern",
        type=str,
        help="Glob pattern to match the module name",
        default=None,
    )
    args = parser.parse_args()
    pack(modules=args.modules, pattern=args.pattern)


if __name__ == "__main__":
    pack(pattern="*.builtin.ping")
