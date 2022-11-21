# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['amazon_bot.py'],
             pathex=['C:\\Users\\USER\\project_env\\Amazon BOT'],
             binaries=[],
             datas=[],
             hiddenimports=['pandas','matplotlib.pyplot','os','sys','gspread','df2gspread','webdriver_manager'],
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
          name='amazon_bot',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
