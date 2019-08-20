# -*- mode: python ; coding: utf-8 -*-

# Default spec file except the data file (.kv) is added and
# console is set to False, and the icon file added too.
block_cipher = None


a = Analysis(['main.py'],
             pathex=['/home/dtron/kivybitcoinpricechecker'],
             binaries=[],
             datas=[('bitcoinchecker.kv', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='icon.png' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
