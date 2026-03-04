# Home Lab Automation

The purpose of this project is to familiarize myself with modern networking automation practices and to build the skills needed to implement them. My lab consists of an Adtran NetVanta 5660, Juniper SRX240, Cisco Catalyst 3650, two Ubuntu servers, and a Windows host running WSL2. The goal is to fully automate the network and servers using tools such as Ansible, Python libraries like Netmiko and NAPALM, and Netconf APIs. Future plans include extending automation into the cloud and exploring infrastructure-as-code tools like Terraform.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Lab Journal](#lab-journal)

---

## Project Structure

- `configs/` – device configurations, organized by vendor and device.
- `scripts/` – Python automation scripts (Netmiko, NAPALM, Ansible playbooks, etc.)
- `venv/` – Python virtual environment (ignored by Git)
- `docs/` – lab journal and step-by-step documentation

---

## Lab Journal

Detailed step-by-step notes and lab progress are maintained in the `docs/` folder. Each entry is timestamped or labeled by the date:

- [Day 1 - Initial Lab Setup](docs/2026-03-04-lab-setup.md)