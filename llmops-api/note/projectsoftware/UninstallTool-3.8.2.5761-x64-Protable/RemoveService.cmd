@ECHO OFF&(PUSHD "%~DP0")&(REG QUERY "HKU\S-1-5-19">NUL 2>&1)||(
powershell -Command "Start-Process '%~sdpnx0' -Verb RunAs"&&EXIT)
net stop CisUtMonitor  >NUL 2>NUL
sc delete CisUtMonitor  >NUL 2>NUL
rmdir/s/q "%AppData%\CrystalIdea Software"2>NUL
del/f/q "%SystemRoot%\System32\drivers\CisUtMonitor.sys" >NUL 2>NUL
reg delete "HKLM\SYSTEM\CurrentControlSet\Services\CisUtMonitor" /f >NUL 2>NUL
reg delete "HKCU\Software\CrystalIdea Software" /f >NUL 2>NUL
@Echo On
Exit