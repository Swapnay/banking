import pathlib


class PathUtil:

    @staticmethod
    def get_empyreal_path():
        return pathlib.Path(__file__).parents[1]
