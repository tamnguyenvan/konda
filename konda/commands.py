import os
import json
import shutil
import subprocess
import platform

def get_mamba_path():
    """
    Get the path to the mamba executable.
    """
    # Check for installed mamba by konda
    from .install import get_install_path, is_mamba_installed
    
    install_path = get_install_path()
    
    if is_mamba_installed(install_path):
        system = platform.system().lower()
        if system == "windows":
            return os.path.join(install_path, "Scripts", "mamba.exe")
        else:
            return os.path.join(install_path, "bin", "mamba")
    
    # Check for system-installed mamba
    mamba_path = shutil.which("mamba")
    if mamba_path:
        return mamba_path
    
    raise FileNotFoundError("Mamba not found. Please run konda.install() first.")

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

def run_mamba_command(args):
    """
    Run a mamba command with the appropriate prefix if needed.
    
    Args:
        args: List of command arguments to pass to mamba
    """
    from .install import get_install_path
    
    install_path = get_install_path()
    mamba_path = os.path.join(install_path, "bin", "mamba")
    
    # Handle special commands
    if args and args[0] == "activate":
        if len(args) > 1:
            env_name = args[1]
            save_active_env(env_name)
            
        # For Google Colab, we need to source conda.sh and mamba.sh first
        conda_sh = os.path.join(install_path, "etc", "profile.d", "conda.sh")
        mamba_sh = os.path.join(install_path, "etc", "profile.d", "mamba.sh")
        print(f"Activating environment: {env_name}")
        
        # Use ". " instead of "source " for better shell compatibility
        cmd = f". {conda_sh} && . {mamba_sh} && mamba activate {env_name}"
        
        # Ensure we use bash for this command
        return subprocess.run(cmd, shell=True, executable="/bin/bash")
    elif args and args[0] == "deactivate":
        env_name = "base"
        save_active_env(env_name)
            
        # For Google Colab, we need to source conda.sh and mamba.sh first
        conda_sh = os.path.join(install_path, "etc", "profile.d", "conda.sh")
        mamba_sh = os.path.join(install_path, "etc", "profile.d", "mamba.sh")
        print(f"Deactivating environment")
        
        # Use ". " instead of "source " for better shell compatibility
        cmd = f". {conda_sh} && . {mamba_sh} && mamba deactivate"
        
        # Ensure we use bash for this command
        return subprocess.run(cmd, shell=True, executable="/bin/bash")
    elif args and args[0] == "run":
        if len(args) < 2:
            print("❌ Error: No command specified for konda run")
            return subprocess.CompletedProcess(args=args, returncode=1)
            
        env_name = get_active_env()
        cmd_to_run = args[1]
        
        # For Google Colab, we need to source conda.sh and mamba.sh first
        conda_sh = os.path.join(install_path, "etc", "profile.d", "conda.sh")
        mamba_sh = os.path.join(install_path, "etc", "profile.d", "mamba.sh")
        
        # Build the command
        cmd = f". {conda_sh} && . {mamba_sh} && mamba activate {env_name} && {cmd_to_run}"
        
        # Ensure we use bash for this command
        return subprocess.run(cmd, shell=True, executable="/bin/bash")
    else:
        # Normal mamba commands
        return subprocess.run([mamba_path] + args)

def print_help():
    """
    Print the help information for konda.
    """
    print("konda - A wrapper for mamba commands with automatic Miniforge installation")
    print("\nUsage:")
    print("  konda <mamba_command> [args...]  - Run a mamba command")
    print("  konda activate <env>            - Set the active environment")
    print("  konda run \"<command>\"           - Run a command in the active environment")
    print("  konda uninstall                 - Uninstall Miniforge installed by konda")
    print("  konda --help                    - Show this help message")
    print("\nExamples:")
    print("  konda create -n my_env python=3.11 -y")
    print("  konda activate my_env")
    print("  konda run \"pip install tensorflow==2.4.0\"")
    print("  konda run \"python my_script.py\"")
    print("  konda list")
    print("  konda uninstall")