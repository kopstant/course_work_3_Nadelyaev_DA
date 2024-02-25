from src import config
from utils.functions import load_operations
from utils.functions import withdraw_operations


def main():
    print(withdraw_operations(load_operations(config.PATH_JSON_DATA), 5))


main()