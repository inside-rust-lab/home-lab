# 2026-03-12 - Backup Tool v1.0

## Objective

Develop Python scripts capable of establishing SSH sessions to network devices and executing operational commands. Integrate the network-backup-tool with Netmiko to collect and store device configurations.

## Tools Used

- Python 3
- Netmiko
- SSH
- Git
- Git Submodules

## Configuration Steps

1. Integrated Netmiko into the network-backup-tool.
2. Implemented SSH connectivity to all lab devices.
3. Added logic to run vendor-specific commands for retrieving running configurations.
4. Implemented functionality to write configuration outputs to timestamped files.
5. Added device inventory validation and argument validation.
6. Implemented secure password prompting using `getpass`.
7. Integrated the network-backup-tool repository into the home-lab repository using Git submodules.

## Validation

- Verified successful SSH connectivity to:
  - Cisco Catalyst 3650
  - Juniper SRX240
  - Adtran NetVanta 5660
- Confirmed the correct configuration command was executed for each vendor:
  - Cisco IOS: `show running-config`
  - Adtran OS: `show running-config`
  - Juniper JunOS: `show configuration`
- Verified configuration files were written to: `scripts/python/network-backup-tool/backups/`
- Confirmed backup files were timestamped and uniquely named.

Example backup file:

`SW-LAB-01_03-12-26_08:09:23.conf`


## Issues / Notes

- Updated `device.py` to validate device types and run appropriate commands for each vendor.
- Modified `main.py`, `backupmanager.py`, and `devices.py` to properly validate arguments and device inventory files.
- Adjusted credential handling so users are prompted for credentials only when required.
- Confirmed Netmiko successfully handles SSH session setup and teardown for each device.
- Added nbtool bash script which can be added to PATH to execute commands

Example command:

`nbtool -b SW-LAB-01`

## Lessons Learned

- Vendor abstraction is important when automating across multi-vendor environments.
- Structuring device-specific commands in a mapping dictionary simplifies the codebase.
- Separating device logic and backup logic makes the tool easier to maintain and extend.
- Git submodules allow external tools to be integrated into a larger project while maintaining independent version control.

## Next Steps

- Implement logging using Python's `logging` module.
- Add structured output parsing using TextFSM or NTC templates.
- Implement parallel backups using `ThreadPoolExecutor`.
- Add support for YAML-based inventory.
- Implement configuration diffing between backups.