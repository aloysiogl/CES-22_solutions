#!/usr/bin/python3
import abc


#####################################################################
# This example is a file tree structure using the pattern Composite #
#####################################################################


class IComposite:
    """This composite prints hte path"""

    @abc.abstractmethod
    def printFiles(self):
        pass


class File(IComposite):
    """This is a file (leaf)"""

    def __init__(self, name):
        self.name = name

    def printFiles(self):
        print(self.name + '\n', end='')


class Folder(IComposite):
    """This is the folder (the composite)"""

    def __init__(self, name, files):
        self.name = name
        self.files = files

    def printFiles(self):
        print('\\' + self.name + '\n', end='')
        for file in self.files:
            file.printFiles()
        print('\\' + "end" + self.name + '\n', end='')


# Test
if __name__ == '__main__':
    # Creating files
    file1 = File("file1")
    file2 = File("file2")
    file3 = File("file3")
    filesList1 = [file1, file2]
    folder1 = Folder("folder1", filesList1)
    filesList2 = [folder1, file3]
    folder2 = Folder("folder2", filesList2)

    # Printing files
    folder2.printFiles()
