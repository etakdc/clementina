import os
import magic


class Directory:
    def __init__(self, input_dir):
        self.root = input_dir
        self._filtered_files = []

    def filter_files(self, magic_signature):
        """
        This method filters the files of the input_dir using magic module
        :param input_dir: root directory
        :param magic_signature: an output string of the magic module used to filter
        :return: a filtered directory
        """
        for dirs, subdirs, files in os.walk(self.root):
            for file in files:
                with magic.Magic() as m:
                    database_file = os.path.join(os.path.abspath(dirs), file)
                    file_signature = m.id_filename(database_file)
                    if magic_signature in file_signature:
                        self._filtered_files.append(database_file)

    def __len__(self):
        return len(self._filtered_files)

    def __getitem__(self, position):
        return self._filtered_files[position]
