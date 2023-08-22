import os


class Directory(object):

    def __init__(self, name, path):
        self.name = name
        self.path = path


class FileSystem(object):

    def __init__(self):
        self.__file_dict = dict()

    def find_duplicates(self, root_path):

        try:
            current_objects = os.listdir(root_path)
        except PermissionError as e:
            print(e)
            return

        while len(current_objects) > 0:  # define type of objects

            cur_object = current_objects.pop(0)
            cur_object_path = os.path.join(root_path, cur_object)

            dir_array = []

            if os.path.isdir(cur_object_path):
                dir_array.append(Directory(cur_object, cur_object_path))
            else:
                if cur_object not in self.__file_dict.keys():
                    self.__file_dict[cur_object] = [cur_object_path]
                else:
                    self.__file_dict[cur_object].append(cur_object_path)

            for directory in dir_array:
                self.find_duplicates(directory.path)

        return self.__file_dict

    def write_duplicates_into_file(self, root_path):

        dictionary = self.find_duplicates(root_path)

        try:
            f = open(os.path.join(root_path, 'duplicates.txt'), 'w', encoding='utf-8')
        except PermissionError:
            f = open(os.path.join(os.getcwd(), 'duplicates.txt'), 'w', encoding='utf-8')

        for key in dictionary.keys():
            if len(dictionary[key]) > 1:
                for path in dictionary[key]:
                    f.write("{:35} || {}\n".format(key, path))
                f.write("=" * 200 + '\n')

        f.close()
