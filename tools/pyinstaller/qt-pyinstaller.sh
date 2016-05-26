#!/bin/bash

WINE_EXEC=wine

PYTHON_DIR=~/.wine/drive_c/Python27
PYTHON_EXEC=$PYTHON_DIR/python.exe
PYINSTALLER=$PYTHON_DIR/Lib/site-packages/*nstaller-3.0/pyinstaller.py

PROJECT_DIR=~/Documents/Python/Randorator
TITLE=qt-randorator
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
DIST=randorator-$VER-pyinstaller-pyqt
DIST_DIR=$PROJECT_DIR/build/$DIST/randorator

rm -rf $DIST_DIR
mkdir -p $PROJECT_DIR/build/$DIST
mv dist/$TITLE $DIST_DIR
cp COPYING* *.md randorator.gif randorator.ini $DIST_DIR

rm -rf build/$TITLE
cd $DIST_DIR
$WINE_EXEC $TITLE.exe
