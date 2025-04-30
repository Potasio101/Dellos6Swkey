# Netbox Windows Playbooks

This repository contains a collection of Ansible playbooks and roles designed for managing Windows environments using Netbox.

## Project Structure

- **playbooks/**: Contains the main playbooks for setup, deployment, and cleanup.
  - `setup.yml`: Playbook for preparing the Windows environment.
  - `deploy.yml`: Playbook for deploying applications or configurations to Windows hosts.
  - `cleanup.yml`: Playbook for removing or reverting changes made during deployment.

- **inventory/**: Contains inventory files and group variables.
  - `hosts.ini`: Lists the Windows hosts that Ansible will manage.
  - `group_vars/`: Contains variables that apply to all hosts in the inventory.
    - `all.yml`: Group variables for all hosts.

- **roles/**: Contains roles for common tasks and Windows-specific tasks.
  - **common/**: Role for tasks applicable to all Windows hosts.
    - `tasks/main.yml`: Main tasks file for the common role.
    - `templates/`: Templates used in the common role.
    - `vars/main.yml`: Variables specific to the common role.
  
  - **windows/**: Role for tasks specific to Windows hosts.
    - `tasks/main.yml`: Main tasks file for the Windows role.
    - `templates/`: Templates used in the Windows role.
    - `vars/main.yml`: Variables specific to the Windows role.

- `ansible.cfg`: Ansible configuration file defining settings for the Ansible environment.

## Usage

1. **Setup**: Run the setup playbook to prepare your Windows environment.
   ```
   ansible-playbook playbooks/setup.yml
   ```

2. **Deploy**: Use the deploy playbook to deploy applications or configurations.
   ```
   ansible-playbook playbooks/deploy.yml
   ```

3. **Cleanup**: Execute the cleanup playbook to revert changes made during deployment.
   ```
   ansible-playbook playbooks/cleanup.yml
   ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or suggestions.

## License

This project is licensed under the MIT License. See the LICENSE file for details.