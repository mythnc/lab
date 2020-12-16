import logging
import traceback

logging.basicConfig()


def main():
    try:
        1/0
    except Exception:
        # print(traceback.format_exc())
        # logging.exception("exception logging")
        logging.error("error logging", exc_info=True)
    


if __name__ == "__main__":
    main()