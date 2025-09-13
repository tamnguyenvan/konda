import os
import subprocess
import shutil
import platform
from pathlib import Path

def get_install_path():
    """
    Return the default installation path for Miniforge.
    """
    return os.path.expanduser("~/conda")

def is_mamba_installed(install_path=None):
    """
    Check if mamba is already installed at the specified path.
    
    Args:
        install_path: Path to check for mamba installation. If None, uses default path.
    
    Returns:
        bool: True if mamba is installed, False otherwise.
    """
    if install_path is None:
        install_path = get_install_path()
    
    mamba_path = os.path.join(install_path, "bin", "mamba")
    return os.path.exists(mamba_path)

def install():
    """
    Download and install Miniforge on Google Colab.
    """
    install_path = get_install_path()
    
    # Get system architecture for the download URL
    system_name = platform.system()
    machine_arch = platform.machine()
    
    # Construct the appropriate download URL
    if system_name == "Darwin":  # macOS
        download_url = f"https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-{machine_arch}.sh"
    else:  # Linux and others
        download_url = f"https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-{system_name}-{machine_arch}.sh"
    
    # Download Miniforge installation script
    print(f"Downloading Miniforge installer for {system_name}-{machine_arch}...")
    subprocess.run(["wget", "-O", "Miniforge3.sh", download_url], check=True)
    
    # Install Miniforge
    print(f"Installing Miniforge to {install_path}...")
    subprocess.run(["bash", "Miniforge3.sh", "-b", "-p", install_path], check=True)
    
    # Update environment variables
    mamba_bin = os.path.join(install_path, "bin")
    os.environ["PATH"] = f"{mamba_bin}:{os.environ['PATH']}"
    os.environ["MAMBA"] = f"{mamba_bin}/mamba"
    
    # Source conda and mamba profile scripts
    conda_sh = os.path.join(install_path, "etc", "profile.d", "conda.sh")
    mamba_sh = os.path.join(install_path, "etc", "profile.d", "mamba.sh")
    
    print("Setting up conda and mamba environments...")
    if os.path.exists(conda_sh):
        subprocess.run([f"source {conda_sh}"], shell=True, executable="/bin/bash")
    if os.path.exists(mamba_sh):
        subprocess.run([f"source {mamba_sh}"], shell=True, executable="/bin/bash")
    
    # Remove installer to save space
    os.remove("Miniforge3.sh")
    
    print("✅ Miniforge installed successfully!")
    print("Run '!mamba --version' to check if mamba is working.")

    # Print usage information
    print("\n📋 Usage examples:")
    print("  konda create -n my_env python=3.11 -y")
    print("  konda activate my_env")

def uninstall():
    """
    Uninstall Miniforge installed by konda.
    """
    install_path = get_install_path()
    
    if not os.path.exists(install_path):
        print(f"❌ Konda installation not found at {install_path}")
        return
    
    print(f"🗑️ Removing Miniforge installation from {install_path}")
    # Remove the entire installation directory since it's in user's home
    shutil.rmtree(install_path)
            
    print("✅ Konda uninstalled successfully")

def get_mamba_path():
    """
    Get the path to the mamba executable.
    """
    install_path = get_install_path()
    
    if is_mamba_installed(install_path):
        return os.path.join(install_path, "bin", "mamba")
    
    # Check for system-installed mamba
    mamba_path = shutil.which("mamba")
    if mamba_path:
        return mamba_path
    
    raise FileNotFoundError("Mamba not found. Please run konda.install() first.")