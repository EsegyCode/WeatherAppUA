# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['MainW.py'],
    pathex=[],
    binaries=[],
    datas=[('img/src.png', 'img'), ('img/src_ic.png', 'img'), ('img/weather.png', 'img'), ('img/box.png', 'img')],
    hiddenimports=['tkinter', 'requests', 'geopy', 'timezonefinder', 'translate', 'pytz', 'os', 'sys'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='MainW',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['planet.ico'],
)
