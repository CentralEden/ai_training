#!/usr/bin/env python3
"""
GPUの有無を判定して、適切なPyTorchバージョンを動的にインストールするスクリプト
"""

import subprocess
import sys
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
                    match = re.search(r'CUDA Version:\s*(\d+\.\d+)', line)
                    if match:
                        return match.group(1)
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


def install_pytorch():
    """PyTorchをインストール"""
    has_gpu = check_nvidia_gpu()
    cuda_version = get_cuda_version()
    
    print(f"GPU利用可能: {has_gpu}")
    if cuda_version:
        print(f"CUDAバージョン: {cuda_version}")
    
    if has_gpu and cuda_version:
        # GPU版をインストール
        major_version = int(cuda_version.split('.')[0])
        if major_version >= 12:
            print("CUDA 12.x用のPyTorchをインストール中...")
            cmd = [
                "poetry", "run", "pip", "install",
                "torch==2.0.1+cu121", "torchvision==0.15.2+cu121", "torchaudio==2.0.1+cu121",
                "-f", "https://download.pytorch.org/whl/torch_stable.html"
            ]
        elif major_version >= 11:
            print("CUDA 11.x用のPyTorchをインストール中...")
            cmd = [
                "poetry", "run", "pip", "install",
                "torch==2.0.1+cu118", "torchvision==0.15.2+cu118", "torchaudio==2.0.1+cu118",
                "-f", "https://download.pytorch.org/whl/torch_stable.html"
            ]
        else:
            print("デフォルトGPU版のPyTorchをインストール中...")
            cmd = [
                "poetry", "run", "pip", "install",
                "torch==2.0.1+cu118", "torchvision==0.15.2+cu118", "torchaudio==2.0.1+cu118",
                "-f", "https://download.pytorch.org/whl/torch_stable.html"
            ]
    else:
        # CPU版をインストール
        print("CPU版のPyTorchをインストール中...")
        cmd = [
            "poetry", "run", "pip", "install",
            "torch==2.0.1+cpu", "torchvision==0.15.2+cpu", "torchaudio==2.0.1+cpu",
            "-f", "https://download.pytorch.org/whl/torch_stable.html"
        ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("PyTorchのインストールが完了しました！")
        return True
    except subprocess.CalledProcessError as e:
        print(f"PyTorchのインストールに失敗しました: {e}")
        print(f"エラー出力: {e.stderr}")
        return False


def main():
    """メイン関数"""
    print("PyTorchインストーラーを開始します...")
    
    # 基本的な依存関係をインストール
    print("基本的な依存関係をインストール中...")
    try:
        subprocess.run(["poetry", "install", "--with", "dev", "--no-interaction"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"基本的な依存関係のインストールに失敗しました: {e}")
        return False
    
    # PyTorchをインストール
    success = install_pytorch()
    
    if success:
        print("✅ インストールが完了しました！")
        print("PyTorchの動作確認:")
        try:
            result = subprocess.run(["poetry", "run", "python", "-c", "import torch; print(f'PyTorch version: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}')"], 
                                  capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(f"動作確認でエラーが発生しました: {e}")
    else:
        print("❌ インストールに失敗しました。")
        return False
    
    return True


if __name__ == '__main__':
    main() 