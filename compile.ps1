mkdir build
cd build
rm -R *
python -m PyInstaller --onefile --noconsole ..\source\app.py

mkdir regular-defecation
mv dist/app.exe regular-defecation
cp -R ../resources regular-defecation/resources
Compress-Archive -Path regular-defecation\* -DestinationPath regular-defecation.zip

rm -R build, dist, regular-defecation, app.spec
cd ..
