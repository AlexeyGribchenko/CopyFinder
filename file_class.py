import os


class FileSystem(object):

    def __init__(self):
        self.__file_dict = dict()

    def find_duplicates(self, root_path) -> dict[str, str] or None:

        try:
            current_objects = os.listdir(root_path)
        except PermissionError as e:
            print(e)
            return

        while len(current_objects) > 0:  # define type of objects

            cur_object_name = current_objects.pop(0)
            cur_object_path = os.path.join(root_path, cur_object_name)

            dir_dict = dict()

            if os.path.isdir(cur_object_path):
                dir_dict[cur_object_name] = cur_object_path
            else:
                cur_object_size = str(os.path.getsize(cur_object_path))
                cur_object_key = cur_object_name + "_" + cur_object_size

                if cur_object_key not in self.__file_dict.keys():
                    self.__file_dict[cur_object_key] = [cur_object_path]
                else:
                    self.__file_dict[cur_object_key].append(cur_object_path)

            for directory in dir_dict.keys():
                self.find_duplicates(dir_dict[directory])

        return self.__file_dict

    def write_duplicates_into_file(self, args) -> None:

        root_path = args[0]
        save_path = args[1] if len(args) > 1 else os.getcwd()
        filename  = args[2] if len(args) > 2 else "duplicates"

        dictionary = self.find_duplicates(root_path)

        try:
            f = open(os.path.join(save_path, f'{filename}.txt'), 'w', encoding='utf-8')
        except PermissionError as e:
            print(e)
            return

        for key in dictionary.keys():
            if len(dictionary[key]) > 1:
                for path in dictionary[key]:
                    f.write("{:35} || {}\n".format(key, path))
                f.write("=" * 200 + '\n')

        f.close()
        print("Duplicates saved in " + save_path + "\\.", end=" ")
