#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Sebastian Nagel
# Copyright (c) 2015
#
# License: MIT
#

"""This module exports the Hdevtools plugin class."""

from SublimeLinter.lint import Linter, util


class Hdevtools(Linter):

    """Provides an interface to hdevtools."""

    syntax = ('haskell', 'haskell-sublimehaskell', 'literate haskell')
    cmd = 'hdevtools check'
    # version_args = '--numeric-version'
    # version_re = r'(?P<version>\d+\.\d+\.\d+\.\d+)'
    # version_requirement = '>= 0.1.0.8'
    regex = (
        r'^.+:(?P<line>\d+):'
        r'(?P<col>\d+):\s*'
        r'(?:(?P<warning>Warning:)|(?P<error>(Error:)?))\s*'
        # r'(?:(?P<warning>Warning)|(?P<error>(Error)?)):\s*'
        r'(?P<message>[\s\S]+)$'
    )
    multiline = True
    tempfile_suffix = '-'
    # error_stream = util.STREAM_BOTH
    # selectors = {}
    # word_re = None
    # defaults = {}
    # inline_settings = None
    # inline_overrides = None
    # comment_re = None

