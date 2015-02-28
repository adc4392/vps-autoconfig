#!/usr/bin/python
# vps_autoconfig.py
#
# This script's goal is to autoconfigure new VPSes with basic security/authentication stuff.
#
# Main configurations:
# - Create non-root user
# - Grant full sudo access
# - Generate SSH key for new user
# - Disable remote root access
# - Disable SSH password auth
# - Enable fail2ban
# - Enable unattended-upgrades