import abc


class AbstractBlastDatabase:
    fasta_suffix = ".fsa"

    def __init__(self, database_dir):
        __metaclass__ = abc.ABCMeta
        self.database_dir = database_dir

    @abc.abstractmethod
    def get_database_names(self):
        pass

    @abc.abstractmethod
    def get_path(self, database_name):
        pass

    def get_database_paths(self):
        return [self.get_path(x) for x in self.get_database_names()]