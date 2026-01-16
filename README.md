[![PyPI version](https://badge.fury.io/py/konda.svg)](https://badge.fury.io/py/konda)
[![Python Versions](https://img.shields.io/pypi/pyversions/konda.svg)](https://pypi.org/project/konda/)
[![Downloads](https://img.shields.io/pepy/dt/konda)](https://pepy.tech/project/konda)
[![CI](https://github.com/tamnguyenvan/konda/actions/workflows/publish.yml/badge.svg)](https://github.com/tamnguyenvan/konda/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🔍 Why Konda?

Installing mamba/miniforge and creating virtual environments on Google Colab is a common need, but it can be quite a hassle. Konda solves this problem by helping you do everything with a single command. Essentially, Konda makes mamba installation and usage in Colab straightforward and painless.

There's no learning curve since Konda commands are simply wrappers around mamba commands you already know.

## ✨ Features

- 🔄 **One-command Miniforge Installation**: Installs Miniforge with mamba with just one line of code
- 🌐 **Built for Google Colab**: Optimized for the Colab environment where mamba integration is typically tricky 
- 🛠️ **Simple Command Wrapper**: Run mamba commands without worrying about environment setup
- 🚀 **Seamless Environment Activation**: Automatically handles the special activation requirements in Colab
- 🧹 **Easy Cleanup**: Remove the Miniforge installation when you're done
- ⚡ **Fast Package Management**: Uses mamba for faster dependency resolution and package installation

## 📦 Installation

```bash
!pip install konda
```

## 🚀 Quick Start

### 1️⃣ Install Miniforge

```python
import konda
konda.install()

!conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
!conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
```

### 2️⃣ Use mamba commands with konda
Konda is a simple wrapper around mamba.
```bash
# Create a new environment
!konda create -n my_env python=3.8 -y

# Activate the environment
!konda activate my_env

# Run a command in the environment
!konda run "mamba install anaconda::tensorflow-gpu=2.4.1 -y"
!konda run "pip install requests"
!konda run "mamba install nvidia/label/cuda-12.4.0::cuda-toolkit"
!konda run "pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124"

# Run a script
!konda run "python my_script.py"

# Deactivate the environment
!konda deactivate
```

### Example
To see how konda works in action, check out the [example](https://github.com/tamnguyenvan/konda/blob/main/assets/example.ipynb).

## 🗑️ Uninstallation

To remove the Miniforge installation created by konda:

```bash
konda uninstall
```

To uninstall the konda package itself:

```bash
pip uninstall konda
```

## 🔍 How It Works

Konda simplifies mamba management in Google Colab by:

1. 📥 Downloading and installing Miniforge in the Colab environment
2. 🔧 Setting up the necessary environment paths and variables
3. 🔄 Handling the `source ~/conda/etc/profile.d/conda.sh` and `source ~/conda/etc/profile.d/mamba.sh` requirements under the hood
4. 🚀 Providing a consistent interface for all mamba commands

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🔧 Create a feature branch
3. 💻 Commit your changes
4. 📤 Push to the branch
5. 🔄 Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## Follow me
- X: [@tamnvvn](https://x.com/tamnvvn)
- Ko-fi: [https://ko-fi.com/tamnguyenvan](https://ko-fi.com/tamnv)
- Email: [tamnvhustcc@gmail.com](mailto:tamnvhustcc@gmail.com)

---

<p align="center">Made with ❤️ to simplify your Colab experience</p>
