import typing
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
        print(Fore.YELLOW + msg, *args, **kwargs)

    @staticmethod
    def error(msg, *args, **kwargs):
        print(Fore.RED, msg, *args, **kwargs)

    @staticmethod
    def _assert(statement: bool):
        assert statement

    @staticmethod
    def table(iterable: typing.Union[list, tuple, set, dict], seperator: str = "*", *args, **kwargs):
        print(f"Array({len(iterable)})")
        print(seperator*10)
        if not isinstance(iterable, dict):
            for num, item in enumerate(iterable):
                if isinstance(item, dict):
                    for sets in item.items():
                        for key, value in sets:
                            print(
                                f'{Fore.LIGHTMAGENTA_EX}{key}{Fore.RESET}: {Fore.LIGHTRED_EX}"{value}"')
                if isinstance(item, int) or isinstance(item, float):
                    print(
                        f"{Fore.LIGHTMAGENTA_EX}{num}{Fore.RESET}: {item}")
                else:
                    print(
                        f'{Fore.LIGHTMAGENTA_EX}{num}{Fore.RESET}: {Fore.LIGHTRED_EX}"{item}"')
        if isinstance(iterable, dict):
            for sets in iterable.items():
                for key, value in sets:
                    print(
                        f'{Fore.LIGHTMAGENTA_EX}{key}{Fore.RESET}: {Fore.LIGHTRED_EX}"{value}"')
        print(
            f"{Fore.MAGENTA}length{Fore.RESET}: {Fore.LIGHTMAGENTA_EX}{len(iterable)}{Fore.RESET}", *args, **kwargs)
        print(seperator*10)
