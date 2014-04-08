# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'wx_randorator.py'],
             pathex=['D:\\D\\DAP-DarkneSS-Randorator-2d70e46'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\wx-randorator', 'wx-randorator.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='randorator.ico')
coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=os.path.join('dist', 'wx-randorator'))
