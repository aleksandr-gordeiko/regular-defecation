OutFile "regular-defecation-install.exe"

InstallDir $PROGRAMFILES64\regular-defecation

Section
    MessageBox MB_YESNO "Install?" /SD IDYES IDNO endInstall
        CreateDirectory $INSTDIR
        SetOutPath $INSTDIR
        File /r ".\regular-defecation\*" 
        CreateShortCut "$APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\rd.lnk" "$INSTDIR\app.exe"

        WriteUninstaller $INSTDIR\uninstall.exe
        Goto endInstall
    endInstall:
SectionEnd
 
Section "Uninstall"
    RMDir /r $INSTDIR
    Delete "$APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\rd.lnk"
SectionEnd
