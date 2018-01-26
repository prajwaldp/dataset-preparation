import csv
from dataset_preparation.file_handler import FileHandler
from dataset_preparation.dataframe_handler import DataframeHandler
from importlib import import_module


def prepare(path, save_path):
    file_handler_module = FileHandler(path).handler()
    file_handler_class = __get_class(file_handler_module)
    file_handler = getattr(import_module(file_handler_module), file_handler_class)

    df = file_handler(path).get_dataframe()
    processed_df = DataframeHandler(df).process()

    processed_df.to_csv(save_path, quoting=csv.QUOTE_NONNUMERIC)

    print(processed_df.head())



def __get_class(import_path):

    klass = import_path.split('.')[-1]
    return ''.join(map(lambda x: x.title(), klass.split('_')))
