import argparse
import os
import sys
import importlib



nl = os.linesep

Parser = argparse.ArgumentParser(description="This will decide which file to compile.")

Parser.add_argument("Filename", metavar="filename", help="Filename of the file that you want to compile", type=str)
args = Parser.parse_args()
targetFile = args.Filename

if os.path.isdir(targetFile) and targetFile.lower().endsWith(".ks"):
    with open(targetFile, "w") as YamalCompiler:  
        print(YamalCompiler.read())     
else:
    class InvalidFile_ERR(Exception):
        def __init__(self, message=f"{nl}|File invalid{nl}|{nl}|Please enter a valid .ks file/path to .ks file"):
            self.message = message
            super().__init__(self.message)
    raise InvalidFile_ERR()
    sys.exit()