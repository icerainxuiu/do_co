import pytest
import yaml

with open("./data.yaml", 'r', encoding='utf-8')as f1, open('./data1.yaml', 'w', encoding='utf-8') as f2:
    data = yaml.full_load(f1)
    print(data)
    yaml.dump(data, stream=f2, allow_unicode=True)

@pytest.mark.parametrize()
def ssdsds():
    pass