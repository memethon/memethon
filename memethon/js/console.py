import typing
from ..utils.bg_colors import BackgroundColors
import sys
import traceback
from colorama import Fore


class console:
    log = print
    trace = traceback.print_exc

    @staticmethod
    def clear():
        sys.stdout.flush()

    @staticmethod
    def warn(msg, *args, **kwargs):
        print(BackgroundColors.WARNING + msg, *args, **kwargs)

    @staticmethod
    def error(msg, *args, **kwargs):
        print(BackgroundColors.ERROR, msg, *args, **kwargs)

    @staticmethod
    def _assert(statement: bool):
        assert statement

    @staticmethod
    def table(iterable: typing.Union[list, tuple], seperator: str = "*", *args, **kwargs):
        print(f"Array({len(iterable)})")
        print(seperator*10)
        for num, item in enumerate(iterable):
            if isinstance(item, int) or isinstance(item, float):
                print(
                    f"{Fore.LIGHTMAGENTA_EX}{num}{Fore.RESET}: {item}")
            else:
                print(
                    f'{Fore.LIGHTMAGENTA_EX}{num}{Fore.RESET}: {Fore.LIGHTRED_EX}"{item}"')
        print(f"{Fore.MAGENTA}length{Fore.RESET}: {Fore.LIGHTMAGENTA_EX}{len(iterable)}{Fore.RESET}", *args, **kwargs)
        print(seperator*10)
