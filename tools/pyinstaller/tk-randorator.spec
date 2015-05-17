# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'tk_randorator.py'],
             pathex=['D:\\D\\DAP-DarkneSS-Randorator-2d70e46'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\tk-randorator', 'tk-randorator.exe'),
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
               name=os.path.join('dist', 'tk-randorator'))
