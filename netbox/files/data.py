import csv
import yaml

# Open the CSV file
with open('CNL Camera Network Switches IPs V2 (2).csv', 'r') as f:
    # Use csv.DictReader to convert it into a list of dictionaries
    devices = list(csv.DictReader(f))

# Convert the list of dictionaries into the desired YAML format
yaml_data = yaml.dump({'devices': devices}, default_flow_style=False)

# Print the YAML formatted data
print(yaml_data)