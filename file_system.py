import os


class FileSystem(object):

    def __init__(self):
        self.__file_dict = dict()

    def __find_duplicates(self, root_path) -> dict[str, list[str]] or None:

        try:
            objects = os.listdir(root_path)
        except PermissionError as e:
            print(e)
            return

        while len(objects) > 0:  # define type of objects

            object_name = objects.pop(0)
            object_path = os.path.join(root_path, object_name)

            dir_dict = dict()

            if os.path.isdir(object_path):
                dir_dict[object_name] = object_path
            else:
                object_size = str(os.path.getsize(object_path))
                object_key = (object_name, object_size)

                if object_key not in self.__file_dict.keys():
                    self.__file_dict[object_key] = [object_path]
                else:
                    self.__file_dict[object_key].append(object_path)

            for directory in dir_dict.keys():
                self.__find_duplicates(dir_dict[directory])

        return self.__file_dict

    def write_duplicates_into_file(self, root_path, save_path=os.getcwd(), filename='duplicates') -> None:

        self.__find_duplicates(root_path)

        try:
            f = open(os.path.join(save_path, f'{filename}.txt'), 'w', encoding='utf-8')
        except PermissionError as e:
            print(e)
            return

        for key in self.__file_dict.keys():
            if len(self.__file_dict[key]) > 1:
                for path in self.__file_dict[key]:
                    f.write("{:35} || {}\n".format(key[0], path))
                f.write("=" * 200 + '\n')

        f.close()
        print("Duplicates saved in " + save_path + "\\.", end=" ")
