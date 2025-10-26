import subprocess
import sys
import importlib.util

def is_installed(package_name):
    """Check if a Python package is installed."""
    return importlib.util.find_spec(package_name) is not None

def install_package(package_name):
    """Install or update a package via pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package_name])
        print(f"✅ '{package_name}' installed or updated successfully.")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install '{package_name}'.")

def main():
    print("🔍 Checking required packages...")

    for pkg in ["kitecmd", "InstallerReady"]:
        if is_installed(pkg):
            print(f"✅ {pkg} is already installed.")
        else:
            print(f"⚙️ Installing {pkg}...")
            install_package(pkg)

    print("\nAll required packages are installed and ready.")

if __name__ == "__main__":
    main()
