# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['PoneleLlave.py'],
             pathex=['C:\\Users\\Whatro\\Desktop\\Python\\eclipse workspace\\PoneleLlave2.0\\com\\whatro\\PoneleLlave'],
             binaries=[],
             datas=[('icono.ico', '.')],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='PoneleLlave',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='icono.ico')
