import os
import platform
import subprocess


def install_tool(tool_name, install_command):
    try:
        print(f"Installing {tool_name}...")
        subprocess.run(install_command, shell=True, check=True)
        print(f"{tool_name} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {tool_name}: {e}")


def get_package_manager():
    os_type = platform.linux_distribution()[0]
    if os_type in ["Ubuntu", "Debian"]:
        return "apt-get"
    elif os_type in ["Fedora", "CentOS", "RHEL"]:
        return "dnf"
    else:
        return None


def install_tool_with_package_manager(tool_name, package_manager, package_name):
    package_manager_command = f"{package_manager} install -y {package_name}"
    install_tool(tool_name, package_manager_command)


def install_recon_ng():
    if platform.system() == "Linux":
        print(
            "Recon-ng requires manual installation. Please follow the instructions at: https://github.com/lanmaster53/recon-ng"
        )
    else:
        print("Recon-ng installation not supported for this operating system.")


def install_nmap():
    if platform.system() == "Linux":
        package_manager = get_package_manager()
        if package_manager:
            install_tool_with_package_manager("Nmap", package_manager, "nmap")
        else:
            print("Nmap installation not supported for this distribution.")
    else:
        print("Nmap installation not supported for this operating system.")


def install_metasploit():
    if platform.system() == "Linux":
        os_type = platform.linux_distribution()[0]
        if os_type == "Ubuntu" or os_type == "Debian":
            install_tool(
                "Metasploit",
                "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall",
            )
        else:
            print("Metasploit installation not supported for this distribution.")
    else:
        print("Metasploit installation not supported for this operating system.")


def install_zap():
    if platform.system() == "Linux":
        os_type = platform.linux_distribution()[0]
        if os_type == "Ubuntu" or os_type == "Debian":
            install_tool(
                "OWASP ZAP",
                "wget https://github.com/zaproxy/zaproxy/releases/download/v2.11.0/ZAP_2_11_0_unix.sh && chmod +x ZAP_2_11_0_unix.sh && ./ZAP_2_11_0_unix.sh",
            )
        else:
            print("OWASP ZAP installation not supported for this distribution.")
    else:
        print("OWASP ZAP installation not supported for this operating system.")


def install_aircrack_ng():
    if platform.system() == "Linux":
        package_manager = get_package_manager()
        if package_manager:
            install_tool_with_package_manager(
                "Aircrack-ng", package_manager, "aircrack-ng"
            )
        else:
            print("Aircrack-ng installation not supported for this distribution.")
    else:
        print("Aircrack-ng installation not supported for this operating system.")


def install_hashcat():
    if platform.system() == "Linux":
        package_manager = get_package_manager()
        if package_manager:
            install_tool_with_package_manager("Hashcat", package_manager, "hashcat")
        else:
            print("Hashcat installation not supported for this distribution.")
    else:
        print("Hashcat installation not supported for this operating system.")


def install_autopsy():
    if platform.system() == "Linux":
        package_manager = get_package_manager()
        if package_manager:
            install_tool_with_package_manager("Autopsy", package_manager, "autopsy")
        else:
            print("Autopsy installation not supported for this distribution.")
    else:
        print("Autopsy installation not supported for this operating system.")


def install_set():
    if platform.system() == "Linux":
        package_manager = get_package_manager()
        if package_manager:
            install_tool_with_package_manager("SET", package_manager, "python3-set")
        else:
            print("SET installation not supported for this distribution.")
    else:
        print("SET installation not supported for this operating system.")


def main():
    print("Select the tool you want to install:")
    print("1. Recon-ng")
    print("2. Nmap")
    print("3. Metasploit")
    print("4. OWASP ZAP")
    print("5. Aircrack-ng")
    print("6. Hashcat")
    print("7. Autopsy")
    print("8. SET")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        install_recon_ng()
    elif choice == "2":
        install_nmap()
    elif choice == "3":
        install_metasploit()
    elif choice == "4":
        install_zap()
    elif choice == "5":
        install_aircrack_ng()
    elif choice == "6":
        install_hashcat()
    elif choice == "7":
        install_autopsy()
    elif choice == "8":
        install_set()
    else:
        print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
