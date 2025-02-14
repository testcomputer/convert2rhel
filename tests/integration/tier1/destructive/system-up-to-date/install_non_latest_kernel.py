from conftest import SYSTEM_RELEASE_ENV


def test_install_non_latest_kernel(shell, hybrid_rocky_image):
    """
    Install specific kernel version and configure
    the system to boot to it. The kernel version is not the
    latest one available in repositories.
    """

    # Set default kernel
    if "centos-7" in SYSTEM_RELEASE_ENV:
        assert shell("yum install kernel-3.10.0-1160.el7.x86_64 -y").returncode == 0
        shell("grub2-set-default 'CentOS Linux (3.10.0-1160.el7.x86_64) 7 (Core)'")
    elif "oracle-7" in SYSTEM_RELEASE_ENV:
        assert shell("yum install kernel-3.10.0-1160.el7.x86_64 -y").returncode == 0
        shell("grub2-set-default 'Oracle Linux Server 7.9, with Linux 3.10.0-1160.el7.x86_64'")
    elif "centos-8" in SYSTEM_RELEASE_ENV:
        assert shell("yum install kernel-4.18.0-348.el8 -y").returncode == 0
        shell("grub2-set-default 'CentOS Stream (4.18.0-348.el8.x86_64) 8'")
    # Test is being run only for the latest released oracle-linux
    elif "oracle-8" in SYSTEM_RELEASE_ENV:
        assert shell("yum install kernel-4.18.0-80.el8.x86_64 -y").returncode == 0
        shell("grub2-set-default 'Oracle Linux Server (4.18.0-80.el8.x86_64) 8.0'")
    elif "alma-8" in SYSTEM_RELEASE_ENV:
        if "alma-8.6" in SYSTEM_RELEASE_ENV:
            assert shell("yum install kernel-4.18.0-372.13.1.el8_6.x86_64 -y")
            shell("grub2-set-default 'AlmaLinux (4.18.0-372.13.1.el8_6.x86_64) 8.6 (Sky Tiger)'")
        else:
            assert shell("yum install kernel-4.18.0-477.10.1.el8_8.x86_64 -y")
            shell("grub2-set-default 'AlmaLinux (4.18.0-477.10.1.el8_8.x86_64) 8.8 (Sapphire Caracal)'")
    elif "rocky-8" in SYSTEM_RELEASE_ENV:
        if "rocky-8.6" in SYSTEM_RELEASE_ENV:
            assert shell("yum install kernel-4.18.0-372.13.1.el8_6.x86_64 -y")
            shell("grub2-set-default 'Rocky Linux (4.18.0-372.13.1.el8_6.x86_64) 8.6 (Green Obsidian)'")
        else:
            assert shell("yum install kernel-4.18.0-477.10.1.el8_8.x86_64 -y")
            shell("grub2-set-default 'Rocky Linux (4.18.0-477.10.1.el8_8.x86_64) 8.8 (Green Obsidian)'")
