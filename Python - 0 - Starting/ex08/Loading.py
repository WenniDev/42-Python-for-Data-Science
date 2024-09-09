from datetime import datetime
from time import time
import shutil
import sys


class Loading():
    """
    Loading()
    """
    def __init__(self, total) -> None:
        """
        __init__(self, total) -> None
        """
        self.total = total
        self.start_time = time()

    def get_elapsed_time(self) -> float:
        """
        elapsed_time() -> float
        """
        return time() - self.start_time

    def get_remaining_time(self, n: int) -> float:
        """
        get_remaining_time(n: int) -> float
        """
        remaining_time = self.get_elapsed_time()
        if n == 0:
            return 0
        return remaining_time * (self.total - n) / n

    def get_terminal_column(self) -> float:
        """
        get_terminal_column() -> int
        """
        size = shutil.get_terminal_size()
        return size.columns

    def update(self, n: int) -> None:
        """
        update(n: int, total: int) -> None
        """

        frac = n / self.total
        percentage = ("{0:.0f}").format(100 * (n / float(self.total))).rjust(3)

        elapsed_time = datetime.fromtimestamp(self.get_elapsed_time())\
            .strftime("%M:%S")
        remaining_time = datetime.fromtimestamp(self.get_remaining_time(n))\
            .strftime("%M:%S")

        rate = n / self.get_elapsed_time()

        line = (f"""\r{percentage}%|| {n}/{self.total}\
 [{elapsed_time}<{remaining_time}, {rate:.2f}it/s]""")

        bar_len = self.get_terminal_column() - len(line) + 1
        bar = "█" * int(bar_len * frac) + \
            (" " * int(bar_len - int(bar_len * frac)))

        sys.stdout.write(f"""\r{percentage}%|{bar}| {n}/{self.total}\
 [{elapsed_time}<{remaining_time}, {rate:.2f}it/s]""")
        sys.stdout.flush()
        return None


def ft_tqdm(lst: range) -> None:
    """
    ft_tqdm(lst: range) -> None
    """
    total = len(lst)

    loading = Loading(total)

    loading.update(0)
    for i, item in enumerate(lst):
        loading.update(i + 1)
        yield item

    sys.stdout.write('\n')
    return None
