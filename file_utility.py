class FileUtility:
    @staticmethod
    def extract_file_names(argv):
        file_names = []

        index = 2;
        while index < len(argv):
            current_file_name = argv[index]
            file_names.append(current_file_name)

            index += 1

        return file_names