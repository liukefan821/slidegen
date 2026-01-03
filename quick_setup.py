import os

# 创建目录
dirs = [
    'backend/app/schemas',
    'backend/app/services/pptx_engine',
    'backend/tests/test_pptx_engine',
    'docs',
    'notebooks'
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    print(f'创建目录: {d}')

# 创建空文件
files = [
    'backend/app/__init__.py',
    'backend/app/schemas/__init__.py',
    'backend/app/services/__init__.py',
    'backend/app/services/pptx_engine/__init__.py',
    'backend/tests/__init__.py',
    'backend/tests/test_pptx_engine/__init__.py',
    'docs/PPTX_ENGINE_README.md',
    'docs/LLM_PPTX_INTERFACE.md',
    'requirements.txt',
    'notebooks/demo.ipynb'
]

for f in files:
    open(f, 'w').close()
    print(f'创建文件: {f}')

print('✅ 完成！')
