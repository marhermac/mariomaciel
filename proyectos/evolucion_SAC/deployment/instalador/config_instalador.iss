[Setup]
AppName=Monitor Logistico SAC
AppVersion=1.0
AppPublisher=Mario Maciel Portfolio
DefaultDirName={autopf}\MonitorLogisticoSAC
DefaultGroupName=Monitor Logistico SAC
AllowNoIcons=yes
; Aquí se guardará el instalador final (en tu escritorio)
OutputDir=userdocs:../Desktop
OutputBaseFilename=Instalador_Monitor_SAC
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; ⚠️ ¡MUY IMPORTANTE!: Cambiá esta ruta de abajo por la ruta real donde guardaste tu carpeta "dist"
Source: "E:\credito_alco\riga-alimentos\proyectos\evolucion_SAC\dist\Monitor_Logistico_SAC\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Monitor Logistico SAC"; Filename: "{app}\run_app.bat"
Name: "{autodesktop}\Monitor Logistico SAC"; Filename: "{app}\run_app.bat"; Tasks: desktopicon

[Run]
Filename: "{app}\run_app.bat"; Description: "{cm:LaunchProgram,Monitor Logistico SAC}"; Flags: nowait postinstall skipifsilent
