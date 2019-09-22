import os

import yaml

FILE_PATH = os.path.abspath(__file__)
PROFILE_PATH = os.path.dirname(FILE_PATH)
PROJECT_PATH = os.path.dirname(PROFILE_PATH)


def data_analyze(filename, key):
    with open(PROJECT_PATH + "{}data{}{}".format(os.sep, os.sep, filename), "r", encoding="utf-8")as f:
        case_data = yaml.full_load(f)[key]
        data_list = list()
        for i in case_data.values():
            data_list.append(i)

    return data_list


if __name__ == '__main__':
    print(FILE_PATH)
    print(PROFILE_PATH)
    print(PROJECT_PATH)
    print(data_analyze("data.yaml", "testlogin"))
