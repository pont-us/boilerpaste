#!/usr/bin/env python3

# Copyright 2016 Pontus Lurcock
#
# This file is part of boilerpaste.
#
# boilerpaste is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# boilerpaste is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with boilerpaste. If not, see <http://www.gnu.org/licenses/>.

"""Insert boilerplate license text into source code files."""

import argparse

def paste(sourcefile, bp_lines, insert_line):

    with open(sourcefile) as fh:
        lines = fh.readlines()
    start_line = -1
    end_line = -1

    template_start = bp_lines[0].strip()
    template_end = bp_lines[-1].strip()
    insert = False

    if insert_line:
        # Use explicitly specified location
        start_line = insert_line - 1
        end_line = insert_line
        insert = True

    else:
        # No explicit location given.
        # Try to find the delimiter lines.
        for i in range(len(lines)):
            line = lines[i].strip()
            if template_start == line:
                start_line = i
            if start_line > -1 and template_end == line:
                end_line = i + 1
                break
    
        # If no delimiters are found, insert the
        # boilerplate text after the first empty line.
        if start_line == -1 or end_line == -1:
            for i in range(len(lines)):
                line = lines[i].strip()
                if line == "":
                    start_line = i + 1
                    end_line = start_line + 1
                    break
            insert = True
    
    if start_line == -1 or end_line == -1:
        print("Skipping %s: nowhere to put license." % sourcefile)
        return

    with open(sourcefile, "w") as fh:
        i = 0
        while i<len(lines):
            line = lines[i]
            if i == start_line:
                for bp_line in bp_lines:
                    fh.write(bp_line)
                i = end_line
                if insert:
                    fh.write(line)
            else:
                fh.write(line)
                i += 1

def main():
    parser = argparse.ArgumentParser(description =
        "Insert boilerplate license text into source code files.")
    parser.add_argument('--line', metavar = "line-number",
                        type=int, default=None,
                        help="Insert boilerplate before this line number")
    parser.add_argument("license", metavar = "license-file",
                        type = str, nargs = 1,
                        help="a license text file")
    parser.add_argument("sourcefiles", metavar = "source-file",
                        type = str, nargs = "+",
                        help = "a source code file")
    args = parser.parse_args()

    with open(args.license[0]) as fh:
        bp_lines = fh.readlines()
    for filename in args.sourcefiles:
        paste(filename, bp_lines, args.line)

if __name__ == "__main__":
    main()
