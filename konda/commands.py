import os
import json
import shutil
import subprocess
import platform

def get_conda_path():
    """
    Get the path to the conda executable.
    """
    # Check for installed conda by konda
    from .install import get_install_path, is_conda_installed
    
    install_path = get_install_path()
    
    if is_conda_installed(install_path):
        system = platform.system().lower()
        if system == "windows":
            return os.path.join(install_path, "Scripts", "conda.exe")
        else:
            return os.path.join(install_path, "bin", "conda")
    
    # Check for system-installed conda
    conda_path = shutil.which("conda")
    if conda_path:
        return conda_path
    
    raise FileNotFoundError("Conda not found. Please run konda.install() first.")

def get_state_file_path():
    """
    Get the path to the state file that stores the active environment.
    """
    from .install import get_install_path
    install_path = get_install_path()
    return os.path.join(install_path, "konda_state.json")

def save_active_env(env_name):
    """
    Save the active environment name to a state file.
    
    Args:
        env_name: Name of the active environment
    """
    state_file = get_state_file_path()
    with open(state_file, 'w') as f:
        json.dump({"active_env": env_name}, f)
    print(f"✅ Set active environment to: {env_name}")

def get_active_env():
    """
    Get the active environment name from the state file.
    
    Returns:
        str: Name of the active environment, defaults to 'base'
    """
    state_file = get_state_file_path()
    if os.path.exists(state_file):
        try:
            with open(state_file, 'r') as f:
                state = json.load(f)
                return state.get("active_env", "base")
        except (json.JSONDecodeError, IOError):
            return "base"
    return "base"

def run_conda_command(args):
    """
    Run a conda command with the appropriate prefix if needed.
    
    Args:
        args: List of command arguments to pass to conda
    """
    from .install import get_install_path
    
    install_path = get_install_path()
    conda_path = os.path.join(install_path, "bin", "conda")
    
    # Handle special commands
    if args and args[0] == "activate":
        if len(args) > 1:
            env_name = args[1]
            save_active_env(env_name)
            
        # For Google Colab, we need to source conda.sh first
        conda_sh = os.path.join(install_path, "etc", "profile.d", "conda.sh")
        print(f"Activating conda environment: {env_name}")
        
        # Use ". " instead of "source " for better shell compatibility
        cmd = f". {conda_sh} && conda activate {env_name}"
        
        # Ensure we use bash for this command
        return subprocess.run(cmd, shell=True, executable="/bin/bash")
    elif args and args[0] == "deactivate":
        env_name = "base"
        save_active_env(env_name)
            
        # For Google Colab, we need to source conda.sh first
        conda_sh = os.path.join(install_path, "etc", "profile.d", "conda.sh")
        print(f"Deactivating conda environment")
        
        # Use ". " instead of "source " for better shell compatibility
        cmd = f". {conda_sh} && conda deactivate"
        
        # Ensure we use bash for this command
        return subprocess.run(cmd, shell=True, executable="/bin/bash")
    elif args and args[0] == "run":
        if len(args) < 2:
            print("❌ Error: No command specified for konda run")
            return subprocess.CompletedProcess(args=args, returncode=1)
            
        env_name = get_active_env()
        cmd_to_run = args[1]
        
        # For Google Colab, we need to source conda.sh first
        conda_sh = os.path.join(install_path, "etc", "profile.d", "conda.sh")
        
        # Build the command
        cmd = f". {conda_sh} && conda activate {env_name} && {cmd_to_run}"
        
        # Ensure we use bash for this command
        return subprocess.run(cmd, shell=True, executable="/bin/bash")
    else:
        # Normal conda commands
        return subprocess.run([conda_path] + args)

def print_help():
    """
    Print the help information for konda.
    """
    print("konda - A wrapper for conda commands with automatic Miniconda installation")
    print("\nUsage:")
    print("  konda <conda_command> [args...]  - Run a conda command")
    print("  konda activate <env>            - Set the active environment")
    print("  konda run \"<command>\"           - Run a command in the active environment")
    print("  konda uninstall                 - Uninstall Miniconda installed by konda")
    print("  konda --help                    - Show this help message")
    print("\nExamples:")
    print("  konda create -n my_env python=3.11 -y")
    print("  konda activate my_env")
    print("  konda run \"pip install tensorflow==2.4.0\"")
    print("  konda run \"python my_script.py\"")
    print("  konda list")
    print("  konda uninstall")