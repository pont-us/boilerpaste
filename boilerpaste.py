#!/usr/bin/env python3

# Copyright 2016 Pontus Lurcock

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Insert boilerplate licence text into source code files."""

import argparse

template_start = "# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = >"
template_end =   "# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = <"

def paste(sourcefile, boilerplate):
    with open(sourcefile) as fh:
        lines = fh.readlines()
    start_line = -1
    end_line = -1
    include_delimiters = False
    for i in range(len(lines)):
        line = lines[i].strip()
        if template_start == line:
            start_line = i
        if start_line > -1 and template_end == line:
            end_line = i
            break
    if start_line == -1 or end_line == -1:
        include_delimiters = True
        for i in range(len(lines)):
            line = lines[i].strip()
            if line == "":
                start_line = i
                end_line = start_line + 1
                break
    if start_line == -1 or end_line == -1:
        print("Skipping %s: nowhere to put licence." % sourcefile)
    with open(sourcefile, "w") as fh:
        i = 0
        while i<len(lines):
            line = lines[i]
            fh.write(line)
            if i == start_line:
                if include_delimiters: fh.write(template_start + "\n")
                fh.write(boilerplate)
                if include_delimiters: fh.write(template_end + "\n\n")
                i = end_line
            else:
                i += 1

def main():
    parser = argparse.ArgumentParser(description="Insert boilerplate licence text into source code files.")
    parser.add_argument("licence", metavar="licence-file", type=str, nargs=1,
                   help="a licence text file")
    parser.add_argument("sourcefiles", metavar="source-file",
                        type=str, nargs="+",
                        help="a source code file")
    args = parser.parse_args()

    with open(args.licence[0]) as fh:
        boilerplate = fh.read()
    for filename in args.sourcefiles:
        paste(filename, boilerplate)

if __name__ == "__main__":
    main()