#!/bin/bash

WINE_EXEC=wine

PYTHON_DIR=~/.wine/drive_c/Python27
PYTHON_EXEC=$PYTHON_DIR/python.exe
PYINSTALLER=$PYTHON_DIR/Lib/site-packages/pyinstaller-2.0/pyinstaller.py

PROJECT_DIR=~/Documents/Python/Randorator
SPEC=wx-randorator.spec

cd $PROJECT_DIR
$WINE_EXEC $PYTHON_EXEC $PYINSTALLER $SPEC

VER=`git describe | sed "s/^v//g" | tr "-" "."`
DIST_DIR=randorator-$VER-pyinstaller-wxwidgets

mv dist/wx-randorator dist/randorator
mv dist $DIST_DIR
cp COPYING* *.md randorator.ico $DIST_DIR/randorator

rm logdict*.log
rm -rf build
cd $DIST_DIR/randorator
rm gdiplus.dll _ssl.pyd unicodedata.pyd _hashlib.pyd pyexpat.pyd

cd ..
zip -r -9 ../$DIST_DIR.zip randorator

cd randorator
$WINE_EXEC wx-randorator.exe