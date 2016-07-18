#!/usr/bin/env python

import argparse
import fnmatch
import ntpath
import os
import shutil
from subprocess import call

# Add this to your path
protoc_path = "protoc"

def main():
    # Specify desired language/ output
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lang", help="Language to produce protoc files")
    parser.add_argument("-o", "--out_path", help="Output path for protoc files")
    args = parser.parse_args()

    # Set defaults
    lang = args.lang or "csharp"
    out_path = args.out_path or "out"
    compile(lang, out_path)

def compile(lang, out_path):
    # Determine where to store
    proto_path = os.path.abspath("pogo/")
    out_path = os.path.abspath(out_path)

    # Clean up previous
    if os.path.exists(out_path):
        shutil.rmtree(out_path)

    # Find protofiles and compile
    for root, dirnames, filenames in os.walk(proto_path):
        for filename in fnmatch.filter(filenames, '*.proto'):
            proto_file = os.path.join(root, filename)
            relative_file_path = proto_file.replace(proto_path, "")

            if lang == "csharp":
                relative_path = relative_file_path.replace(ntpath.basename(proto_file), "")
                destination_path = os.path.abspath(out_path + relative_path)
            else:
                destination_path = os.path.abspath(out_path)

            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            print("Compiling " + relative_file_path + "..")

            command = """{0} --proto_path="{1}" --{2}_out="{3}" "{4}\"""".format(
                protoc_path,
                proto_path,
                lang,
                destination_path,
                os.path.abspath(proto_file)
            )

            call(command, shell=True)

    if lang == "python":
        f = open("{}/__init__.py".format(out_path), "w")
        f.write('import sys, os; sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))')
        f.close()
        for root, dirnames, filenames in os.walk(out_path):
            for dirname in dirnames:
                f = open("{}/__init__.py".format(os.path.join(root, dirname)), "a")
                f.write('import sys, os; sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))')
                f.close()

    print("Done!")

if __name__ == '__main__':
    main()