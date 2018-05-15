import os
import shutil


def remove(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


directory = os.path.abspath(os.path.dirname(__file__))
output_directory = os.path.join(directory, "output")
files = [os.path.join(output_directory, x) for x in os.listdir(output_directory) if not x.startswith(".git")]
map(remove, files)
