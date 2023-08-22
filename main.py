from file_class import FileSystem
import sys


if __name__ == '__main__':

    file_system = FileSystem()
    file_system.write_duplicates_into_file(sys.argv[1])
