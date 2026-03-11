# 2026-03-11 - Netmiko Integration

## Objective

Develop Python scripts capable of establishing SSH sessions to network devices and executing operational commands. Integrate the network-backup-tool with Netmiko to collect device information.

## Tools Used

- Python 3
- Netmiko
- SSH
- Git Submodules

## Configuration Steps

1. Created basic scripts for connectivity to network devices
2. Developed scripts to execute operational commands via SSH
3. Integrated Netmiko with the network-backup-tool
4. Implemented functionality to connect to all devices, run `show version`, and store output in the `scripts/python/network-backup-tool/backups/` directory

## Validation

- Verified successful SSH connectivity to:
  - Cisco Catalyst 3650
  - Juniper SRX240
  - Adtran NetVanta 5660
- Executed `show version` on each device
- Confirmed output files were written to the `scripts/python/network-backup-tool/backups/` directory

## Issues / Notes

- Successfully modified methods to work with actual SSH connections instead of simulated connections
- Updated objects and files to match Netmiko connection requirements
- Added the network-backup-tool repository as a Git submodule within the home-lab repository

## Next Steps

- Extend backup functionality to capture full running configurations
- Introduce structured device inventory