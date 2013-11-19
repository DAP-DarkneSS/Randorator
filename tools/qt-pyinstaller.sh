#!/bin/bash

WINE_EXEC=wine

PYTHON_DIR=~/.wine/drive_c/Python27
PYTHON_EXEC=$PYTHON_DIR/python.exe
PYINSTALLER=$PYTHON_DIR/Lib/site-packages/pyinstaller-2.0/pyinstaller.py

PROJECT_DIR=~/Documents/Python/Randorator
SPEC=tools/qt-randorator.spec

cd $PROJECT_DIR
$WINE_EXEC $PYTHON_EXEC $PYINSTALLER $SPEC

VER=`git describe | sed "s/^v//g" | tr "-" "."`
DIST_DIR=randorator-$VER-pyinstaller-pyqt

mv tools/dist/qt-randorator tools/dist/randorator
mv tools/dist $DIST_DIR
cp COPYING COPYING.RU *.md randorator.gif $DIST_DIR/randorator

rm logdict*.log
rm -rf tools/build
cd $DIST_DIR/randorator
rm -rf _ssl.pyd unicodedata.pyd _hashlib.pyd pyexpat.pyd QtOpenGL4.dll QtSvg4.dll QtXml4.dll qt4_plugins/accessible qt4_plugins/accessible qt4_plugins/graphicssystems qt4_plugins/iconengines qt4_plugins/imageformats/qico4.dll qt4_plugins/imageformats/qjpeg4.dll qt4_plugins/imageformats/qmng4.dll qt4_plugins/imageformats/qsvg4.dll qt4_plugins/imageformats/qtga4.dll qt4_plugins/imageformats/qtiff4.dll

# cd ..
# zip -r -9 ../$DIST_DIR.zip randorator

# cd randorator
$WINE_EXEC qt-randorator.exe