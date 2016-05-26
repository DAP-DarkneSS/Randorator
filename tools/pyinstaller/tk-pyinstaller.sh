#!/bin/bash

WINE_EXEC=wine

PYTHON_DIR=~/.wine/drive_c/Python27
PYTHON_EXEC=$PYTHON_DIR/python.exe
PYINSTALLER=$PYTHON_DIR/Lib/site-packages/*nstaller-3.0/pyinstaller.py

PROJECT_DIR=~/Documents/Python/Randorator
TITLE=tk-randorator
SPECNAME=$TITLE.spec
SPEC=$PROJECT_DIR/tools/pyinstaller/$SPECNAME

cd $PROJECT_DIR
cat tools/stuff/0.patch | patch -p1
cp $SPEC $PROJECT_DIR
$WINE_EXEC $PYTHON_EXEC $PYINSTALLER $SPECNAME
rm $SPECNAME
git checkout HEAD randorator.py
rm randorator.py.orig

VER=`git describe | sed "s/^v//g" | tr "-" "."`
DIST=randorator-$VER-pyinstaller-tkinter
DIST_DIR=$PROJECT_DIR/build/$DIST/randorator

rm -rf $DIST_DIR
mkdir -p $PROJECT_DIR/build/$DIST
mv dist/$TITLE $DIST_DIR
cp COPYING* *.md randorator.gif randorator.ini $DIST_DIR

rm -rf build/$TITLE
cd $DIST_DIR
rm -rf future *32.dll msvc*90.dll pywintypes27.dll \
       _hashlib.pyd _ssl.pyd bz2.pyd pyexpat.pyd select.pyd unicodedata.pyd win32*.pyd
rm -rf tk/images tk/tkfbox.tcl include _bsddb.pyd _ctypes.pyd _testcapi.pyd \
       tcl/clock.tcl tcl/encoding t*/msgs tcl/tzdata

cd ..
rm -rf ../../dist/$DIST.zip
mkdir -p ../../dist
zip -r9Xv ../../dist/$DIST.zip randorator
7z a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on ../../dist/$DIST.7z randorator

cd randorator
$WINE_EXEC $TITLE.exe
