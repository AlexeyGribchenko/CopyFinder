from file_system import FileSystem
import sys
import time

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("Not enough arguments. At least one required. Try --help option.")
    elif sys.argv[1] == "--help":
        print("Script takes 3 positional arguments:\n"
              "\t- path to the directory to be checked\n"
              "\t- (optional) path to the directory the final file to be saved | else current working directory\n"
              "\t- (optional) name of the saving file without extension | else \"duplicates\"\n"
              "As a result of this script you receive a txt file with a list of duplicated files.\n")
    else:
        start = time.time()

        file_system = FileSystem()
        file_system.write_duplicates_into_file(*sys.argv[1:])

        end = time.time()
        print("Execution time: {:.3f} sec".format((end - start)))
