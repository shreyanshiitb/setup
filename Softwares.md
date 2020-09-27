- Download and install [Chrome](https://www.google.com/chrome/) sync your stuff
- Download and install [VScode](https://code.visualstudio.com/download) ( I recommend using VScode)
- Install Nvidia-drivers (method 1 is recommended) [Link](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-20-04-focal-fossa-linux)
- Install CUDA (method 1 recommended) [Link](https://linuxconfig.org/how-to-install-cuda-on-ubuntu-20-04-focal-fossa-linux)
    ```
    sudo apt update
    sudo apt install nvidia-cuda-toolkit
    ```
- Install openVPN, [download](https://www.cc.iitb.ac.in/page/configurevpn) VPN config file
    ```
    sudo apt install network-manager-openvpn network-manager-openvpn-gnome
    ```
- [Download](https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh) Anaconda, install it, add path of anaconda binary in bashrc
    ```
    bash Anaconda3-2020.07-Linux-x86_64.sh
    sudo gedit ~/.bashrc
    export PATH="/home/shreyansh/anaconda3/bin:$PATH"
    source ~/.bashrc
    conda init
    ```
- Create a pytorch environment
    ```
    conda create -n py15 python=3.8
    conda activate py15
    conda install pytorch=1.5 -c pytorch
    ``` 
- Setup git
    ```
    sudo apt-get update
    sudo apt-get install git
    git config --global user.email email@gmail.com
    git config --global user.name desiredeveloper
    ```
- Login to remote servers/git without password
    - Generate keys 
        ```
        ssh-keygen
        ```
    - You can find the key at this location --> .ssh/id_rsa.pub or at your specified location 
    - Append this key in .ssh/authorized_keys in your server