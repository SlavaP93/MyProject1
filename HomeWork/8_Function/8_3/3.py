def create_dict(deta):
    template = dict()
    if isinstance(deta, dict):
        return deta
    if isinstance(deta, (int, float,str)):
        template[deta]=deta
    return template


def data_preparation(old_list):
    new_list = []
    for i_ind,i_element in enumerate(old_list):
        new_list.append(create_dict(i_element))
    return new_list


data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
print(data_preparation(data))
