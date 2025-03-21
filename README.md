# 🐍 Konda - Conda Installer/Wrapper for Google Colab 🚀

[![PyPI version](https://badge.fury.io/py/konda.svg)](https://badge.fury.io/py/konda)
[![Python Versions](https://img.shields.io/pypi/pyversions/konda.svg)](https://pypi.org/project/konda/)
[![CI](https://github.com/tamnguyenvan/konda/actions/workflows/publish.yml/badge.svg)](https://github.com/tamnguyenvan/konda/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🔍 Why Konda?

Installing conda/miniconda and creating virtual environments on Google Colab is a common need, but it can be quite a hassle. Konda solves this problem by helping you do everything with a single command. Essentially, Konda makes conda installation and usage in Colab straightforward and painless.

There's no learning curve since Konda commands are simply wrappers around conda commands you already know.

## ✨ Features

- 🔄 **One-command Miniconda Installation**: Installs Miniconda with just one line of code
- 🌐 **Built for Google Colab**: Optimized for the Colab environment where conda integration is typically tricky 
- 🛠️ **Simple Command Wrapper**: Run conda commands without worrying about environment setup
- 🚀 **Seamless Environment Activation**: Automatically handles the special activation requirements in Colab
- 🧹 **Easy Cleanup**: Remove the Miniconda installation when you're done

## 📦 Installation

```bash
pip install konda
```

## 🚀 Quick Start

### 1️⃣ Install Miniconda

```python
import konda
konda.install()
```

### 2️⃣ Use conda commands with konda
Konda is a simple wrapper around conda.
```bash
# Create a new environment
konda create -n my_env python=3.8 -y

# Activate the environment
konda activate my_env

# Run a command in the environment
konda run "conda install anaconda::tensorflow-gpu=2.4.1 -y"
konda run "pip install requests"

# Deactivate the environment
konda deactivate
```

### Example
To see how konda works in action, check out the [example](https://github.com/tamnguyenvan/konda/blob/main/assets/example.ipynb).

## 🗑️ Uninstallation

To remove the Miniconda installation created by konda:

```bash
konda uninstall
```

To uninstall the konda package itself:

```bash
pip uninstall konda
```

## 🔍 How It Works

Konda simplifies conda management in Google Colab by:

1. 📥 Downloading and installing Miniconda in the Colab environment
2. 🔧 Setting up the necessary environment paths and variables
3. 🔄 Handling the `source /usr/local/etc/profile.d/conda.sh` requirement under the hood
4. 🚀 Providing a consistent interface for all conda commands

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🔧 Create a feature branch
3. 💻 Commit your changes
4. 📤 Push to the branch
5. 🔄 Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

---

<p align="center">Made with ❤️ to simplify your Colab experience</p>