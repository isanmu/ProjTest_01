# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\winswang\\PycharmProjects\\ProjTest_01\\images;', 'C:\\Users\\winswang\\PycharmProjects\\ProjTest_01\\alien_invasion.py'],
             pathex=['C:\\Users\\winswang\\PycharmProjects\\ProjTest_01\\venv\\lib\\site-packages', '', 'C:\\Users\\winswang\\PycharmProjects\\ProjTest_01'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='images;',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
