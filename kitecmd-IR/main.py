import subprocess
import sys
import importlib.util

def is_installed(package_name):
    """Check if a package is installed."""
    spec = importlib.util.find_spec(package_name)
    return spec is not None

def install_package(package_name):
    """Install a package via pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package_name])
        print(f"✅ Successfully installed or updated '{package_name}'")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install '{package_name}'")

def main():
    print("🔍 Checking for 'InstallerReady'...")

    if is_installed("InstallerReady"):
        print("✅ InstallerReady is already installed.")
    else:
        print("⚙️ Installing InstallerReady...")
        install_package("InstallerReady")

if __name__ == "__main__":
    main()
