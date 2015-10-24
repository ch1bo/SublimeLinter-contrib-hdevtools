#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Sebastian Nagel
# Copyright (c) 2015 Sebastian Nagel
#
# License: MIT
#

"""This module exports the Hdevtools plugin class."""

from SublimeLinter.lint import Linter


class Hdevtools(Linter):

    """Provides an interface to hdevtools."""

    syntax = ('haskell', 'haskell-sublimehaskell', 'literate haskell')
    cmd = 'hdevtools check'
    version_args = '--numeric-version'
    version_requirement = '>= 0.1.2.1'
    regex = (
        r'.+:(?P<line>\d+):'
        r'(?P<col>\d+):\s*'
        r'(?:(?P<warning>Warning:)|(?P<error>(Error:)?))\s*'
        r'(?P<message>[^\n]+)'
    )
    multiline = True
    tempfile_suffix = '-'
