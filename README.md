SublimeLinter-contrib-hdevtools
================================

[![Build Status](https://travis-ci.org/ch1bo/SublimeLinter-contrib-hdevtools.svg?branch=master)](https://travis-ci.org/ch1bo/SublimeLinter-contrib-hdevtools.svg?branch=master)

This linter plugin for [SublimeLinter][docs] provides an interface to [hdevtools](https://github.com/schell/hdevtools) ([Hackage](http://hackage.haskell.org/package/hdevtools), [Stackage](https://www.stackage.org/package/hdevtools)). It will be used to typecheck files with Haskell syntax (`haskell`, `haskell-sublimehaskell`, `literate haskell`).

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `hdevtools` is installed on your system using [stack](https://github.com/commercialhaskell/stack):

`stack install hdevtools`

or via [cabal-install](https://github.com/haskell/cabal/tree/master/cabal-install):

`cabal update`

`cabal install hdevtools`

**Note:** This plugin requires `hdevtools` 0.1.2.1 or later.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `hdevtools`. Among the entries you should see `SublimeLinter-contrib-hdevtools`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
