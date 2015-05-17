# -*- mode: python -*-
a = Analysis(['wx_randorator.py'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\wx-randorator', 'wx-randorator.exe'),
          debug=False,
          strip=False,
          upx=False,
          console=False , icon='randorator.ico')
coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name=os.path.join('dist', 'wx-randorator'))
