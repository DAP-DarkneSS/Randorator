#!/bin/bash

WINE_EXEC=wine

PYTHON_DIR=~/.wine/drive_c/Python27
PYTHON_EXEC=$PYTHON_DIR/python.exe
PYINSTALLER=$PYTHON_DIR/Lib/site-packages/pyinstaller-2.0/pyinstaller.py

PROJECT_DIR=~/Documents/Python/Randorator
SPEC=$PROJECT_DIR/tools/pyinstaller/qt-randorator.spec

cd $PROJECT_DIR
cat tools/stuff/0.patch | patch -p1
$WINE_EXEC $PYTHON_EXEC $PYINSTALLER $SPEC
cat tools/stuff/1.patch | patch -p0

VER=`git describe | sed "s/^v//g" | tr "-" "."`
DIST=randorator-$VER-pyinstaller-pyqt
DIST_DIR=$PROJECT_DIR/build/$DIST/randorator

rm -rf $DIST_DIR
mkdir -p $PROJECT_DIR/build/$DIST
mv dist/qt-randorator $DIST_DIR
cp COPYING* *.md randorator.gif randorator.ini $DIST_DIR

rm -rf build/qt-randorator
cd $DIST_DIR
rm -rf _ctypes.pyd bz2.pyd pywintypes27.dll select.pyd win32api.pyd win32pipe.pyd
rm -rf _ssl.pyd unicodedata.pyd _hashlib.pyd pyexpat.pyd QtOpenGL4.dll QtSvg4.dll QtXml4.dll qt4_plugins/accessible qt4_plugins/accessible qt4_plugins/graphicssystems qt4_plugins/iconengines qt4_plugins/imageformats/qico4.dll qt4_plugins/imageformats/qjpeg4.dll qt4_plugins/imageformats/qmng4.dll qt4_plugins/imageformats/qsvg4.dll qt4_plugins/imageformats/qtga4.dll qt4_plugins/imageformats/qtiff4.dll

# cd ..
# rm -rf ../../dist/$DIST.zip
# mkdir -p ../../dist
# zip -r9 ../../dist/$DIST.zip randorator

# cd randorator
$WINE_EXEC qt-randorator.exe