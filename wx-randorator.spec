# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'wx-randorator.py'],
             pathex=['D:\\D\\python\\DAP-DarkneSS-Randorator-be344f3'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\wx-randorator', 'wx-randorator.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=os.path.join('dist', 'wx-randorator'))
