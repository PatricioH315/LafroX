@echo off
rem Abre el prototipo LafroX en el navegador predeterminado. No requiere instalacion ni servidor.
if not exist "%~dp0index.html" (
  echo No se encontro index.html junto a este archivo.
  pause
  exit /b 1
)
start "" "%~dp0index.html"
