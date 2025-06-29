#!/usr/bin/env python3
"""
GPUの有無を判定し、適切なPyTorchバージョンを決定するスクリプト
"""

import subprocess
import sys
import platform
import re
from pathlib import Path


def check_nvidia_gpu():
    """NVIDIA GPUの有無をチェック"""
    try:
        result = subprocess.run(['nvidia-smi'], 
                              capture_output=True, 
                              text=True, 
                              timeout=10)
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def get_cuda_version():
    """CUDAバージョンを取得"""
    try:
        result = subprocess.run(['nvidia-smi'], 
                              capture_output=True, 
                              text=True, 
                              timeout=10)
        if result.returncode == 0:
            for line in result.stdout.split('\n'):
                if 'CUDA Version' in line:
                    # "CUDA Version: 12.8" から "12.8" を抽出
                    match = re.search(r'CUDA Version:\s*(\d+\.\d+)', line)
                    if match:
                        return match.group(1)
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


def get_system_info():
    """システム情報を取得"""
    return {
        'platform': platform.system(),
        'architecture': platform.machine(),
        'python_version': platform.python_version()
    }


def determine_pytorch_version():
    """PyTorchバージョンを決定"""
    system_info = get_system_info()
    has_gpu = check_nvidia_gpu()
    cuda_version = get_cuda_version()
    
    print(f"システム情報: {system_info}")
    print(f"GPU利用可能: {has_gpu}")
    if cuda_version:
        print(f"CUDAバージョン: {cuda_version}")
    
    if has_gpu and cuda_version:
        # GPU版を推奨
        major_version = int(cuda_version.split('.')[0])
        if major_version >= 12:
            return 'gpu-cuda12'
        elif major_version >= 11:
            return 'gpu-cuda11'
        else:
            return 'gpu-cuda11'  # デフォルト
    else:
        # CPU版
        return 'cpu'


def main():
    """メイン関数"""
    pytorch_version = determine_pytorch_version()
    print(f"推奨PyTorchバージョン: {pytorch_version}")
    
    # 結果をファイルに出力（GitHub Actionsで使用）
    output_file = Path('pytorch_version.txt')
    output_file.write_text(pytorch_version)
    
    return pytorch_version


if __name__ == '__main__':
    main() 