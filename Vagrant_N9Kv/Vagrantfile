# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

# https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/7-x/nx-osv/configuration/guide/b_NX-OSv_9000/b_NX-OSv_chapter_01.html#task_jhy_dwv_qy


Vagrant.configure(2) do |config|
  config.vm.define "n9kv1" do |n9kv|

    # Ensure to change this to the correct Vagrant Box name that you have created
    # Verify via # vagrant box list
    n9kv.vm.box = "n9kv.7.0.3.I7.3"

    # Modify the BASE MAC address to allow communication between instances
    # Change this per INSTANCE
    n9kv.vm.base_mac = "080027BEEFAA"

    # Dont try to change the insecure public key
    n9kv.ssh.insert_key = false
    n9kv.ssh.password = "vagrant"

    # Give the VM time to boot as Vagrant cannot tell when it is booted
    n9kv.vm.boot_timeout = 180

    # Disable default host to guest synced folder
    n9kv.vm.synced_folder '.', '/vagrant', disabled: true

    # n9000v defaults to 8G RAM, but only needs 4G
    n9kv.vm.provider "virtualbox" do |vb|
      # Customize the amount of memory on the VM:
      vb.memory = "4096"

      #####
      # Needed to disable the Serial Ports - as was causing the following error on the second+ VM
      #
      # Stderr: VBoxManage: error: DrvTCP#0 failed to create server socket (VERR_NET_ADDRESS_IN_USE)
      # VBoxManage: error: Details: code NS_ERROR_FAILURE (0x80004005), component ConsoleWrap, interface IConsole
      #####
      vb.customize ['modifyvm', :id, '--uart1', '0x3F8', 4, '--uartmode1', 'disconnected']
      vb.customize ['modifyvm', :id, '--uart2', '0x2F8', 3, '--uartmode2', 'disconnected']
    end

    # Explicity set SSH Port to avoid conflict and for provisioning
    n9kv.vm.network :forwarded_port, guest: 22, host: 3122, id: 'ssh', auto_correct: true

    # Forward API Ports
    # Change the ports to be different between instances as well
    n9kv.vm.network :forwarded_port, guest: 80, host: 3180, id: 'http', auto_correct: true
    n9kv.vm.network :forwarded_port, guest: 443, host: 3143, id: 'https', auto_correct: true
    n9kv.vm.network :forwarded_port, guest: 830, host: 3130, id: 'netconf', auto_correct: true

    # Additional interfaces. Be sure to change MAC address per INSTANCE
    # All connections currently between n9kv1 and n9kv2
    # Order is Eth1/1, Eth1/2, Eth1/3 through to Eth1/7 on nxosv_net7
    # n9kv.vm.network :private_network, ip: "10.10.1.1", auto_config: false, virtualbox__intnet: "nxosv_net1", mac: "0800276CEE11"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net1"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net2"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net3"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net4"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net5"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net6"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net7"

    # Make the interfaces promiscuous. nicpromisc1 is mgmt0, therefore start from 2-8 to match above 7 interfaces
    n9kv.vm.provider :virtualbox do |vb|
        vb.customize ['modifyvm',:id,'--nicpromisc2','allow-all']
        vb.customize ['modifyvm',:id,'--nicpromisc3','allow-all']
        vb.customize ['modifyvm',:id,'--nicpromisc4','allow-all']
        vb.customize ['modifyvm',:id,'--nicpromisc5','allow-all']
        vb.customize ['modifyvm',:id,'--nicpromisc6','allow-all']
        vb.customize ['modifyvm',:id,'--nicpromisc7','allow-all']
        vb.customize ['modifyvm',:id,'--nicpromisc8','allow-all']
    end
  end


  config.vm.define "n9kv2" do |n9kv|

    # Ensure to change this to the correct Vagrant Box name that you have created
    # Verify via # vagrant box list
    n9kv.vm.box = "n9kv.7.0.3.I7.3"

    # Modify the BASE MAC address to allow communication between instances
    # Change this per INSTANCE
    n9kv.vm.base_mac = "080027BEEFBB"

    # Dont try to change the insecure public key
    n9kv.ssh.insert_key = false
    n9kv.ssh.password = "vagrant"

    # Give the VM time to boot as Vagrant cannot tell when it is booted
    n9kv.vm.boot_timeout = 180

    # Disable default host to guest synced folder
    n9kv.vm.synced_folder '.', '/vagrant', disabled: true

    # n9000v defaults to 8G RAM, but only needs 4G
    n9kv.vm.provider "virtualbox" do |vb|
      # Customize the amount of memory on the VM:
      vb.memory = "4096"

      #####
      # Needed to disable the Serial Ports - as was causing the following error on the second+ VM
      #
      # Stderr: VBoxManage: error: DrvTCP#0 failed to create server socket (VERR_NET_ADDRESS_IN_USE)
      # VBoxManage: error: Details: code NS_ERROR_FAILURE (0x80004005), component ConsoleWrap, interface IConsole
      #####
      vb.customize ['modifyvm', :id, '--uart1', '0x3F8', 4, '--uartmode1', 'disconnected']
      vb.customize ['modifyvm', :id, '--uart2', '0x2F8', 3, '--uartmode2', 'disconnected']
    end

    # Explicity set SSH Port to avoid conflict and for provisioning
    # Change the ports to be different between instances as well
    n9kv.vm.network :forwarded_port, guest: 22, host: 3222, id: 'ssh', auto_correct: true

    # Forward API Ports
    # Change the ports to be different between instances as well
    n9kv.vm.network :forwarded_port, guest: 80, host: 3280, id: 'http', auto_correct: true
    n9kv.vm.network :forwarded_port, guest: 443, host: 3243, id: 'https', auto_correct: true
    n9kv.vm.network :forwarded_port, guest: 830, host: 3230, id: 'netconf', auto_correct: true

    # Additional interfaces. Be sure to change MAC address per INSTANCE
    # All connections currently between n9kv1 and n9kv2
    # Order is Eth1/1, Eth1/2, Eth1/3 through to Eth1/7 on nxosv_net7
    # n9kv.vm.network :private_network, ip: "10.10.1.2", auto_config: false, virtualbox__intnet: "nxosv_net1", mac: "0800276CBB11"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net1"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net2"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net3"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net4"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net5"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net6"
    n9kv.vm.network :private_network, auto_config: false, virtualbox__intnet: "nxosv_net7"

    # Make the interfaces promiscuous. nicpromisc1 is mgmt0, therefore start from 2-8 to match above 7 interfaces
    n9kv.vm.provider :virtualbox do |vb|
        vb.customize ['modifyvm',:id,'--nicpromisc2','allow-all']
        vb.customize ['modifyvm',:id,'--nicpromisc3','allow-all']
        vb.customize ['modifyvm',:id,'--nicpromisc4','allow-all']
        vb.customize ['modifyvm',:id,'--nicpromisc5','allow-all']
        vb.customize ['modifyvm',:id,'--nicpromisc6','allow-all']
        vb.customize ['modifyvm',:id,'--nicpromisc7','allow-all']
        vb.customize ['modifyvm',:id,'--nicpromisc8','allow-all']
    end
  end

  # Make use of Ansible to configure/provision the N9Kv instances
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible_provision.yaml"
    ansible.inventory_path = "./hosts"
    # Enable verbose logging for debugging issues
    # ansible.verbose = "vvvv"
  end
end


# 1st Time - bring up the first switch
# vagrant up

# 2nd Time - provision first switch, bring up second switch
# vagrant up

# 3rd Time - provision second switch
# vagrant up
