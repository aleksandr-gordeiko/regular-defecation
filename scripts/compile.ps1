mkdir build
cd build
rm -R *
python -m PyInstaller --onefile --noconsole ..\source\app.py

mkdir regular-defecation
mv dist/app.exe regular-defecation
cp -R ../resources regular-defecation/resources
Compress-Archive -Path regular-defecation\* -DestinationPath regular-defecation.zip

cp ../scripts/make_installer.nsi .
makensis make_installer.nsi

rm -R build, dist, app.spec, make_installer.nsi
cd ..
