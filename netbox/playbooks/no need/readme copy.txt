Filler readme for place playbooks here
ubnt@10.100.10.80 -oHostKeyAlgorithms=ssh-rsa
Todos los downlink tienen spanning tree guard root
  loop:
    - "configure"
    - "interface {{ vlan_configurations[0].downlink_trunk_ports }}"
    - "description 'trunk downlink to south network'"
    - "switchport mode trunk"
    - "spanning-tree guard root"
    - "exit"
    - "exit"

- name: Check current trunk port configuration
  ansible.netcommon.cli_command:
    command: "show spanning-tree interface {{ item }}"
  loop: "{{ vlan_configurations[0].downlink_trunk_ports.split(',') }}"
  register: result

# - name: Debug output of result
#   ansible.builtin.debug:
#     var: "(result.results | map(attribute='stdout'))"
     
- name: Set spanning-tree guard root on downlink trunk ports
  ansible.netcommon.cli_command:
    command: "{{ item }}"
  loop:
    - "configure"
    - "interface {{ vlan_configurations[0].downlink_trunk_ports }}"
    - "spanning-tree guard root"
    - "exit"
    - "exit"
  when: 
    - vlan_configurations[0].downlink_trunk_ports != '0/0'
    - "(result.results | map(attribute='stdout') | select('search', 'Root Guard..................................... TRUE') | list | length) == 0"