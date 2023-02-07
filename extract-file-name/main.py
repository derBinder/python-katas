# https://www.codewars.com/kata/597770e98b4b340e5b000071/train/python

class FileNameExtractor:
    @staticmethod
    def extract_file_name(dirty_file_name):
        file = '_'.join(dirty_file_name.split('_')[1:])
        file = '.'.join(file.split('.')[:-1])
        return file
        