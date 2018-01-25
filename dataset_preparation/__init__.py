from dataset_preparation.file_handler import FileHandler
from importlib import import_module


def prepare(path):
    file_handler_module = FileHandler(path).handler()
    file_handler_class = get_class(file_handler_module)
    file_handler = getattr(import_module(file_handler_module), file_handler_class)

    return file_handler(path).get_dataframe().head()



def get_class(import_path):

    klass = import_path.split('.')[-1]
    return ''.join(map(lambda x: x.title(), klass.split('_')))
