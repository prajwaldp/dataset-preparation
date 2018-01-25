import magic


class FileHandler:


    HANDLERS = {
        'text/plain': 'text'
    }


    def __init__(self, path):
        self.path = path
        self.filetype = magic.from_file(path, mime=True)


    def handler(self):
        return 'dataset_preparation.file_handler.{}'.format(self.__class__.HANDLERS[self.filetype])
