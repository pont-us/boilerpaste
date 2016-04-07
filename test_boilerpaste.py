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

import os
import unittest
import tempfile
from boilerpaste import paste

boilerplate = """START
new line one
new line two
END"""

bp_lines = [x + "\n" for x in boilerplate.split("\n")]

class BoilerpasteTest(unittest.TestCase):

    def readfile(self, filename):
        with open(filename, "rb") as fh:
            filecontents = fh.read()
        return filecontents

    def maketmpfile(self, string):
        f = tempfile.NamedTemporaryFile(delete=False)
        f.write(string)
        f.close()
        return f

    def test_paste_replace(self):
        # replacing an existing block
        f = self.maketmpfile(b"""1
2
3
START
old line one
old line two
old line three
END
4
5
""")
        paste(f.name, bp_lines, None)
        self.assertEqual(self.readfile(f.name), b"""1
2
3
START
new line one
new line two
END
4
5
""")
        os.remove(f.name)

    def test_paste_insert_blank(self):
        # inserting at a blank line
        f = self.maketmpfile(b"1\n2\n\n3\n4\n")
        paste(f.name, bp_lines, None)
        self.assertEqual(self.readfile(f.name), b"""1
2

START
new line one
new line two
END
3
4
""")
        os.remove(f.name)

    def test_paste_insert_position(self):
        # inserting at a specified line
        f = self.maketmpfile(b"1\n2\n3\n")
        paste(f.name, bp_lines, 1)
        result = b"START\nnew line one\nnew line two\nEND\n1\n2\n3\n"
        self.assertEqual(self.readfile(f.name), result)
        os.remove(f.name)

if __name__=="__main__":
    unittest.main()
