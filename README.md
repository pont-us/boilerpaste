boilerpaste: insert text blocks into files
==========================================

boilerpaste is a tool to insert and update blocks of boilerplate
text in files. It's mainly intended for managing license text
block in source code files.

Usage
-----

`boilerpaste.py [--line <number>] <boilerplate-file> <source-file> ...`

All arguments are names of text files.

The boilerplate file contains a chunk of text to be inserted into
each source file, possibly after removing a previous, corresponding
chunk of boilerplate text.

The first and last lines of the boilerplate file define the **delimiter
lines** which are used to mark the chunk in the source files.

If the `--line` option is given, the boilerplate will be inserted
before the given line number.

If the `--line` option is not given, each source file is scanned for the
delimiter lines. If they are found, the text between them is removed and
replaced with the text in the boilerplate file. Files are modified in
place.

If `--line` is not given and no delimiter lines are found in a source
code file, the boilerplate will be inserted after the first empty line.
If there are no delimiter lines and no empty lines, the file will not be
modified, and a warning will be printed.

License
-------

Copyright 2016 Pontus Lurcock (pont at talvi dot net).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program. If not, see <http://www.gnu.org/licenses/>.
