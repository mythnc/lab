from datetime import datetime
from pytz import timezone


def get_local_time(zone: str) -> datetime:
    utcnow = timezone('UTC').localize(datetime.utcnow())
    return utcnow.astimezone(timezone(zone)).replace(tzinfo=None)


if __name__ == "__main__":
    print(type(get_local_time('Asia/Tokyo')))