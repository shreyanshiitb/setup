## Solutions for install issues 

- Security boot disable (change this in BIOS, for MSI computers reboot system and press delete a couple of times before the OS is loaded)

-  To avoid screen freezing while installing
    - Reboot system
    - Go to the Install Ubuntu option (BUT DONT PRESS ENTER)
    - Press e
    - Find the line that starts with linux then add modprobe.blacklist=nouveau after quiet splash.
- Blurry pixels/bad graphics after installation if above step is not followed
    - create a file with this content to disable nouveau
    ```
    sudo bash -c "echo blacklist nouveau > /etc/modprobe.d/blacklist-nvidia-nouveau.conf"
    
    sudo bash -c "echo options nouveau modeset=0 >> /etc/modprobe.d/blacklist-nvidia-nouveau.conf"
    
    sudo reboot
    ```

- Read about disk partitioning, swap allocation and other detailed info [Here](https://levelup.gitconnected.com/dual-booting-windows-10-with-ubuntu-16-04-mission-msi-1efd3e131dc)