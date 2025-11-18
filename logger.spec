# -*- mode: python ; coding: utf-8 -*-

CAMINHO_DO_REQUESTS_PASTA = "C:/Users/Bruno/Desktop/projetos/pythonKeylogger/venv/Lib/site-packages/requests"
CAMINHO_DO_CERTIFI_PASTA = "C:/Users/Bruno/Desktop/projetos/pythonKeylogger/venv/Lib/site-packages/certifi"
CAMINHO_DO_URLLIB3_PASTA = "C:/Users/Bruno/Desktop/projetos/pythonKeylogger/venv/Lib/site-packages/urllib3"
CAMINHO_DO_IDNA_PASTA = "C:/Users/Bruno/Desktop/projetos/pythonKeylogger/venv/Lib/site-packages/idna"


a = Analysis(
    ['logger.py'],
    pathex=[],
    binaries=[],
   datas=[
        (CAMINHO_DO_REQUESTS_PASTA, 'requests'), 
        (CAMINHO_DO_CERTIFI_PASTA, 'certifi'),
        (CAMINHO_DO_URLLIB3_PASTA, 'urllib3'),
        (CAMINHO_DO_IDNA_PASTA, 'idna')
    ],
    
    # 2. ADICIONE MAIS MÓDULOS NA LISTA DE IMPORTAÇÕES OCULTAS
    hiddenimports=[
        'requests', 'idna', 'certifi', 'charset_normalizer', 'urllib3', 
        'http','http.client', 'ssl', 'hmac', 'mimetypes', 'http.cookiejar', 'http.cookies'# <-- NOVOS
    ],
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
    name='logger',
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
)
