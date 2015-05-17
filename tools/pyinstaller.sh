#!/bin/bash

WINE_EXEC=wine

PYTHON_DIR=~/.wine/drive_c/Python27
PYTHON_EXEC=$PYTHON_DIR/python.exe
PYINSTALLER=$PYTHON_DIR/Lib/site-packages/pyinstaller-2.0/pyinstaller.py

PROJECT_DIR=~/Documents/Python/Randorator
SPEC=tools/wx-randorator.spec

cd $PROJECT_DIR
cat tools/0.patch | patch -p1
$WINE_EXEC $PYTHON_EXEC $PYINSTALLER $SPEC
cat tools/1.patch | patch -p0 --fuzz=0

VER=`git describe | sed "s/^v//g" | tr "-" "."`
DIST_DIR=randorator-$VER-pyinstaller-wxwidgets

mv tools/dist/wx-randorator tools/dist/randorator
mv tools/dist $DIST_DIR
cp COPYING* *.md randorator.ico randorator.ini $DIST_DIR/randorator

rm logdict*.log
rm -rf tools/build
cd $DIST_DIR/randorator
rm gdiplus.dll _ssl.pyd unicodedata.pyd _hashlib.pyd pyexpat.pyd

cd ..
zip -r -9 ../$DIST_DIR.zip randorator

cd randorator
$WINE_EXEC wx-randorator.exe