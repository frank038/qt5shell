#!/bin/bash
thisdir=$(dirname "$0")
cd $thisdir
python3 qt5dock.py &
cd $HOME
