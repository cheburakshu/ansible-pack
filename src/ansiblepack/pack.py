import logging
import pathlib

import ansiblepack.utils.generate

log = logging.getLogger(__name__)


def pack(opts):
    """Package ansible modules into zip files."""
    dest_dir = pathlib.Path(opts.dest).joinpath(opts.name)
    ansiblepack.utils.generate.Packer.pack(
        dest_dir=dest_dir,
        modules=opts.modules,
        pattern=opts.pattern,
    )
    log.info("Package created at %s", dest_dir)
