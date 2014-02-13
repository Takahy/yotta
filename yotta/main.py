# standard library modules, , ,
import argparse
import logging
import sys

# subcommand modules, , add subcommands, internal
from . import version
from . import link

def logLevelFromVerbosity(v):
    return max(1, logging.ERROR - v * (logging.ERROR-logging.NOTSET) / 5)

def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    parser.add_argument('-v', '--verbose', dest='verbosity', action='count', default=0)

    version_parser = subparser.add_parser('version', description='bump the module version')
    version.addOptions(version_parser)
    version_parser.set_defaults(command=version.execCommand)

    link_parser = subparser.add_parser('link', description='symlink a module')
    link.addOptions(link_parser)
    link_parser.set_defaults(command=link.execCommand)

    args = parser.parse_args()
    
    logging.basicConfig(
        level=logLevelFromVerbosity(args.verbosity),
        format='%(message)s'
    )

    status = args.command(args)

    sys.exit(status or 0)
