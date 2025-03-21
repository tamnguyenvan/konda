import os
import subprocess
import shutil
import platform
from pathlib import Path

def get_install_path():
    """
    Return the default installation path for Miniconda.
    """
    return "/usr/local"

def is_conda_installed(install_path=None):
    """
    Check if conda is already installed at the specified path.
    
    Args:
        install_path: Path to check for conda installation. If None, uses default path.
    
    Returns:
        bool: True if conda is installed, False otherwise.
    """
    if install_path is None:
        install_path = get_install_path()
    
    conda_path = os.path.join(install_path, "bin", "conda")
    return os.path.exists(conda_path)

def install():
    """
    Download and install Miniconda on Google Colab.
    """
    miniconda_script = "Miniconda3-latest-Linux-x86_64.sh"
    install_path = get_install_path()
    
    # Download Miniconda installation script
    print(f"Downloading Miniconda installer...")
    subprocess.run(["wget", "-q", f"https://repo.anaconda.com/miniconda/{miniconda_script}", "-O", "miniconda.sh"], check=True)
    
    # Make the script executable
    subprocess.run(["chmod", "+x", "miniconda.sh"], check=True)
    
    # Install Miniconda
    print(f"Installing Miniconda to {install_path}...")
    subprocess.run(["bash", "./miniconda.sh", "-b", "-f", "-p", install_path], check=True)
    
    # Update environment variables
    conda_bin = os.path.join(install_path, "bin")
    os.environ["PATH"] = f"{conda_bin}:{os.environ['PATH']}"
    os.environ["CONDA"] = f"{conda_bin}/conda"
    
    # Remove installer to save space
    os.remove("miniconda.sh")
    
    print("✅ Miniconda installed successfully!")
    print("Run '!conda --version' to check if conda is working.")

    # Print usage information
    print("\n📋 Usage examples:")
    print("  konda create -n my_env python=3.11 -y")
    print("  konda activate my_env")

def uninstall():
    """
    Uninstall Miniconda installed by konda.
    """
    install_path = get_install_path()
    
    if not os.path.exists(install_path):
        print(f"❌ Konda installation not found at {install_path}")
        return
    
    print(f"🗑️ Removing Miniconda installation from {install_path}")
    # Only remove conda-related directories to avoid damaging the system
    for item in ["bin/conda", "bin/activate", "bin/deactivate", "etc/profile.d/conda.sh"]:
        full_path = os.path.join(install_path, item)
        if os.path.exists(full_path):
            os.remove(full_path)
            
    conda_dirs = ["conda-meta", "conda-bld", "pkgs", "envs"]
    for item in conda_dirs:
        full_path = os.path.join(install_path, item)
        if os.path.exists(full_path):
            shutil.rmtree(full_path)
            
    print("✅ Konda uninstalled successfully")

def get_conda_path():
    """
    Get the path to the conda executable.
    """
    install_path = get_install_path()
    
    if is_conda_installed(install_path):
        return os.path.join(install_path, "bin", "conda")
    
    # Check for system-installed conda
    conda_path = shutil.which("conda")
    if conda_path:
        return conda_path
    
    raise FileNotFoundError("Conda not found. Please run konda.install() first.")