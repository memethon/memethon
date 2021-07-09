import logging
import sys
import traceback

log = logging.getLogger(__name__)


class console(object):
    log = print
    trace = traceback.print_exc()

    @staticmethod
    def clear():
        sys.stdout.flush()

    @staticmethod
    def debug(msg, *args, **kwargs):
        log.debug(msg, *args, **kwargs)

    @staticmethod
    def warn(msg, *args, **kwargs):
        log.warning(msg, *args, **kwargs)

    @staticmethod
    def error(msg, *args, **kwargs):
        log.error(msg, *args, **kwargs)

    @staticmethod
    def _assert(statement: bool):
        assert statement
