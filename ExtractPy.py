class ExtractPy():
    def load_dict(self,file_name):
        list = []
        with open(file_name,'r') as f:
            content = f.read().splitlines()
            print content
        for n in content:
            list.append(n)
        return list
    def process(self, transform, params):
        if transform is not None:
            list_dict =[]
            list = self.load_dict(params['dict'])
            seperator = params['seperator'] if params.has_key('seperator') else ','
            print list
            for l in list:
                list_dict.extend([x for x in l.split(seperator)])
            print list_dict
            for dict_element in list_dict:
                if dict_element in transform:
                    return list_dict[0]
        else:
            return None



edx = ExtractPy()
edx.process('abc',{'dict':'dict.txt'})