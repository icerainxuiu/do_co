import json


class GenJsonData(object):

    def __init__(self, num, dict_data, change_dict):
        self.num = num

        self.dict_data = dict_data
        self.change_dict = change_dict
        self.gen_num = (i for i in range(self.num))
        self.key_list = list(self.dict_data.keys())
        self.index_change_key = self.key_list.index(self.change_dict)

    def generator_json_data_for_feature(self):
        data = self.__next__()
        with open("./d_data.json", "a+") as f:
            json.dump(data, f)

    def __next__(self):
        data_list = []
        for num in self.gen_num:
            save_data = dict()
            for key in self.key_list:
                if key == self.key_list[self.index_change_key]:
                    save_data[key] = "".join("{}".format(self.dict_data[key][:-1]) + str(num))
                else:
                    save_data[key] = self.dict_data[key]
            data_list.append(save_data)
        return data_list

    def __iter__(self):
        return self


if __name__ == '__main__':
    json_data = {"1": "1",
                 "2": "2"}
    json_data1 = "1"
    ob1 = GenJsonData(10000, json_data, json_data1)
    ob1.generator_json_data_for_feature()