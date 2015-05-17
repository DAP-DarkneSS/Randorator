#!/bin/bash

WINE_EXEC=wine

PYTHON_DIR=~/.wine/drive_c/Python27
PYTHON_EXEC=$PYTHON_DIR/python.exe
PYINSTALLER=$PYTHON_DIR/Lib/site-packages/PyInstaller-2.1/pyinstaller.py

PROJECT_DIR=~/Documents/Python/Randorator
SPEC=$PROJECT_DIR/tools/pyinstaller/wx-randorator.spec

cd $PROJECT_DIR
cat tools/stuff/0.patch | patch -p1
$WINE_EXEC $PYTHON_EXEC $PYINSTALLER $SPEC
cat tools/stuff/1.patch | patch -p0

VER=`git describe | sed "s/^v//g" | tr "-" "."`
DIST=randorator-$VER-pyinstaller-wxwidgets
DIST_DIR=$PROJECT_DIR/build/$DIST/randorator

rm -rf $DIST_DIR
mkdir -p $PROJECT_DIR/build/$DIST
mv dist/wx-randorator $DIST_DIR
cp COPYING* *.md randorator.ico randorator.ini $DIST_DIR

rm -rf build/wx-randorator
cd $DIST_DIR
rm -rf _ctypes.pyd bz2.pyd pywintypes27.dll select.pyd win32api.pyd win32pipe.pyd
rm gdiplus.dll _ssl.pyd unicodedata.pyd _hashlib.pyd pyexpat.pyd

cd ..
rm -rf ../../dist/$DIST.zip
mkdir -p ../../dist
zip -r9 ../../dist/$DIST.zip randorator

cd randorator
$WINE_EXEC wx-randorator.exe