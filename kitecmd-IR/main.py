import subprocess
import sys
import importlib.util
import json
import urllib.request
import pkg_resources

PACKAGE_NAME = "kitecmd-IR"

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

def get_latest_version(package_name):
    """Fetch the latest version of a PyPI package."""
    try:
        with urllib.request.urlopen(f"https://pypi.org/pypi/{package_name}/json") as response:
            data = json.load(response)
            return data["info"]["version"]
    except Exception:
        return None

def check_for_self_update():
    """Check if kitecmd-IR is up to date."""
    try:
        current_version = pkg_resources.get_distribution(PACKAGE_NAME).version
    except Exception:
        current_version = "0.0"

    latest_version = get_latest_version(PACKAGE_NAME)
    if not latest_version:
        print("⚠️ Unable to check for updates.")
        return

    if current_version != latest_version:
        print(f"🔄 Update available: {PACKAGE_NAME} {current_version} → {latest_version}")
        install_package(PACKAGE_NAME)
        print("✅ Restart the command to use the latest version.")
        sys.exit(0)
    else:
        print("✅ kitecmd-IR is up to date.")

def main():
    print("🔍 Checking for kitecmd-IR updates...")
    check_for_self_update()

    print("\n🔍 Checking required packages...")
    for pkg in ["kitecmd", "InstallerReady"]:
        if is_installed(pkg):
            print(f"✅ {pkg} is already installed.")
        else:
            print(f"⚙️ Installing {pkg}...")
            install_package(pkg)

    print("\n🚀 All systems ready — kitecmd-IR, kitecmd, and InstallerReady are installed and current!")

if __name__ == "__main__":
    main()
