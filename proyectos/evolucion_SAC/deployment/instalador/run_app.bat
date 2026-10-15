@echo off
cd /d "%~dp0"
start "" "Monitor_Logistico_SAC.exe" -m streamlit run dashboard.py --server.headless true
