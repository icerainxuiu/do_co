def generator_num_for_file(total, data_dict, change_key, file):

    gen_num = (i for i in range(total))

    key_list = list(data_dict.keys())
    index_change_key = key_list.index(change_key)

    for num in gen_num:
        with open("./test.{}".format(file), 'a+') as f:
            for key in key_list:
                if key == key_list[index_change_key]:

                    f.write("{}{},".format(data_dict[key], num))
                else:
                    f.write("{},".format(data_dict[key]))
            f.write("\n")


if __name__ == '__main__':
    json_data = {"1": 1,
                 "2": 2}
    generator_num_for_file(10, json_data, "1", "csv")
