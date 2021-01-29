import argparse
import os
import sys
from Colors import bcolors
import progress

nl = os.linesep

Parser = argparse.ArgumentParser(description="This will decide which file to compile.")

Parser.add_argument("Filename", metavar="filename", help="Filename of the file that you want to compile", type=str)
args = Parser.parse_args()
targetFile = args.Filename
file_name, file_ext = os.path.splitext(targetFile)

if """os.path.isdir(targetFile)""" and file_ext == ".briz":
    with open(targetFile, "r+") as YamalCompiler:  
        breezContent = YamalCompiler.read
            
else:
    class InvalidFile_ERR(Exception):
        def __init__(self, message=f"{nl}|File invalid{nl}|{nl}|Please enter a valid path to .briz file"):
            self.message = message
            super().__init__(self.message)
    raise InvalidFile_ERR()
    sys.exit()
