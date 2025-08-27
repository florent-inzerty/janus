# -*- mode: python ; coding: utf-8 -*-

added_files = [('C:\\Users\\reynald\\Pictures\\APP\\*.png', '.')]

a = Analysis(['test.py'],
    pathex=[''],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Janus',  # Change to your desired executable name
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # Set to False if you don't want UPX compression
    console=False,  # Set to True for console applications
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,  # Set to False if you don't want UPX compression
    upx_exclude=[],
    name='Projet_Janus',  # Change to your desired output folder name
)