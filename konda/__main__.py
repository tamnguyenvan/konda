import sys
from .install import uninstall, install
from .commands import run_mamba_command, print_help

def main():
    """
    Main entry point for the konda command-line interface.
    """
    # No arguments provided
    if len(sys.argv) < 2:
        print_help()
        return 0
    
    # Get the command
    command = sys.argv[1]
    
    # Handle konda-specific commands
    if command in ["--help", "-h", "help"]:
        print_help()
        return 0
    elif command == "uninstall":
        uninstall()
        return 0
    
    # Forward all other commands to mamba
    try:
        from .install import is_mamba_installed, get_install_path
        
        # Check if mamba is installed
        install_path = get_install_path()
        if not is_mamba_installed(install_path):
            print("❌ Mamba not found. Installing Miniforge first...")
            from .install import install
            install()
        
        # Run the mamba command
        result = run_mamba_command(sys.argv[1:])
        return result.returncode
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())