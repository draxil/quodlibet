#!/bin/bash

trap 'exit 1' SIGINT;

DIR="$( cd "$( dirname "$0" )" && pwd )"
export WINEPREFIX="$DIR"/_wine_prefix
export WINEDEBUG=-all
export WINEARCH=win32
export WINEDLLOVERRIDES="mscoree,mshtml="

(cd "$DIR" && wine cmd /c test.bat)
exit $?
