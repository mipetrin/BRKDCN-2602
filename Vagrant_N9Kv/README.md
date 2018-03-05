Created by Michael Petrinovic 2018

Sample Vagrant and Nexus 9000v deployment for Cisco Live Melbourne 2018: BRKDCN-2602


Simply based off the N9Kv image from Cisco.com " Developer Tools "
https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/7-x/nx-osv/configuration/guide/b_NX-OSv_9000/b_NX-OSv_chapter_01.html


* Make sure to download the N9Kv box image from Cisco.com
https://software.cisco.com/download/release.html?mdfid=286312239&flowid=81422&softwareid=282088129&release=7.0(3)I7(3)&relind=AVAILABLE&rellifecycle=&reltype=latest

* Once you have downloaded the Box image, be sure to add it to your local Vagrant repo so that it is possible to be consumed to boot instances of that image

* Vagrantfile contains the deployment configuration for Vagrant regarding each N9Kv instance. Be sure to specify the name of the imported Box image (per above step) if you are using a different name and/or image.  n9kv.vm.box = "n9kv.7.0.3.I7.3
"
* ansible_provision.yaml continues the configuration specified in Ansible YAML format using Cisco NXOS modules

* host_vars folder contains the specific host configuration for each N9Kv instance. Again, if you are using a different version, be sure to update the boot_nxos variable for each host YAML file within this directory. Specify the name of the version that you are using, as written in the output of "dir bootflash:" within the N9Kv

Requirements:
* Ensure that you have Vagrant / Virtualbox / Ansible installed

My Test Environment:
* Vagrant 2.0.2
* Ansible 2.4.3.0
* Virtualbox 5.3.6
* nxosv-final.7.0.3.I7.3.box
* Mac OSX 10.13.2
