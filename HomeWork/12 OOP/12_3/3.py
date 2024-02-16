class MyDict(dict):

    def get(self, key, default=None):
        super().get(key,default)
        return dict.get(self,key) or 0



my_dict = MyDict({'x': 2, 'y': 22})
print(my_dict.get('z'), my_dict.get('y'), my_dict.get('x'))
