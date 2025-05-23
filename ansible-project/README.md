# Ansible Project

This project is structured to manage configurations and deployments using Ansible. Below is an overview of the project structure and its components.

## Project Structure

```
ansible-project
├── inventories
│   ├── development
│   │   └── hosts.yml
│   ├── production
│   │   └── hosts.yml
├── roles
│   ├── common
│   │   ├── tasks
│   │   │   └── main.yml
│   │   ├── handlers
│   │   │   └── main.yml
│   │   ├── templates
│   │   ├── files
│   │   ├── vars
│   │   │   └── main.yml
│   │   └── defaults
│   │       └── main.yml
├── group_vars
│   └── all.yml
├── host_vars
│   └── localhost.yml
├── ansible.cfg
├── playbook.yml
└── README.md
```

## Setup Instructions

1. **Clone the Repository**: 
   Clone this repository to your local machine using:
   ```
   git clone <repository-url>
   ```

2. **Install Ansible**: 
   Ensure that Ansible is installed on your machine. You can install it using pip:
   ```
   pip install ansible
   ```

3. **Configure Inventory**: 
   Modify the `inventories/development/hosts.yml` and `inventories/production/hosts.yml` files to define your hosts and their associated variables.

4. **Define Roles**: 
   Customize the tasks, handlers, and variables in the `roles/common` directory as per your requirements.

5. **Run the Playbook**: 
   Execute the playbook using the following command:
   ```
   ansible-playbook playbook.yml
   ```

## Usage Information

- The `playbook.yml` file is the entry point for executing your Ansible tasks.
- The `ansible.cfg` file contains configuration settings for Ansible, including the inventory location and roles path.
- Use the `group_vars` and `host_vars` directories to define variables that apply to specific groups or hosts.

## Testing and Limiting Playbook Execution

You can use the `--limit` flag to target specific devices or groups when running playbooks. Below are some examples:

### Examples

- **View devices from the site `houston`:**
  ```bash
  ansible-playbook playbooks/test_limit.yml --limit site_houston
  ```

- **View devices with the role `core-switch`:**
  ```bash
  ansible-playbook playbooks/test_limit.yml --limit role_core-switch
  ```

- **View devices with the tag `NetBox custom-config`:**
  ```bash
  ansible-playbook playbooks/test_limit.yml --limit tag_custom-config
  ```

- **Target a specific device by name:**
  ```bash
  ansible-playbook playbooks/test_limit.yml --limit switch-01
  ```

### Notes
- Replace `test_limit.yml` with the name of the playbook you want to execute.
- Ensure that the inventory and variables are properly configured to match the filters used in the `--limit` flag.

For more details on limiting playbook execution, refer to the [Ansible documentation on patterns](https://docs.ansible.com/ansible/latest/user_guide/intro_patterns.html).

For more detailed information on Ansible, refer to the [Ansible documentation](https://docs.ansible.com/).