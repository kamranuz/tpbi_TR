# !/usr/bin/env python3

import sys

sys.path.append('../app')
from hello import main

def test_hello(capsys):
	main()
	stdout, stderr = capsys.readouterr()
	assert stdout == 'Hello world from dev\n'

