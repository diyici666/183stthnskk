import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

# 要执行的目录
TARGET_DIR = "./scripts"  # 换成你的目录路径

# 获取目录下所有 .py 文件（不包含当前文件）
py_files = [
    os.path.join(TARGET_DIR, f)
    for f in os.listdir(TARGET_DIR)
    if f.endswith(".py")
]

def run_script(file_path):
    """运行单个脚本并返回输出"""
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        return file_path, result.stdout.strip(), None
    except subprocess.CalledProcessError as e:
        return file_path, e.stdout.strip(), e.stderr.strip()

# 使用多线程执行
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(run_script, f) for f in py_files]

    for future in as_completed(futures):
        file_path, stdout, stderr = future.result()
        print(f"=== {file_path} ===")
        print(stdout)
        if stderr:
            print("[Error]", stderr)
