from datetime import datetime
from time import time


def print_time(time):
    print(f"Seconds since January 1, 1970: {time:,.4f} \
          or {time:.2e} in scientific notation")
    print(datetime.fromtimestamp(time).strftime('%b %d %Y'))


print_time(time())
print_time(datetime(2022, 10, 21).timestamp())
