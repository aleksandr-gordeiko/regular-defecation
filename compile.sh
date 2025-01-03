#!/bin/bash

mkdir build
cd build
rm -rf *
pyinstaller -F ../source/app.py

mv dist/app .
zip -r regular-defecation.zip app ../resources

rm -rf build dist app app.spec
