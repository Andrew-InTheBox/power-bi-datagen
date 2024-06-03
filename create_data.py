import json
import random
import csv
from faker import Faker

# Initialize Faker
fake = Faker()

# Load the JSON data
with open('data_model.json') as file:
    data_model = json.load(file)

# Extract tables and relationships from the data model
tables = data_model['model']['tables']
relationships = data_model['model']['relationships']

# Function to generate fake data for a column based on its data type
def generate_fake_data(column):
    data_type = column['dataType']
    if data_type == 'string':
        return fake.word()
    elif data_type == 'int64':
        return fake.random_int(min=1, max=100)
    elif data_type == 'double':
        return fake.pyfloat(left_digits=2, right_digits=2, positive=True)
    elif data_type == 'boolean':
        return fake.boolean()
    elif data_type == 'dateTime':
        return fake.date_time().isoformat()
    else:
        return None

# Function to generate fake data for a table
def generate_table_data(table, num_rows):
    table_data = []
    for _ in range(num_rows):
        row_data = {}
        for column in table['columns']:
            row_data[column['name']] = generate_fake_data(column)
        table_data.append(row_data)
    return table_data

# Generate fake data for each table
fake_data = {}
for table in tables:
    table_name = table['name']
    num_rows = fake.random_int(min=10, max=100)  # Adjust the range as needed
    fake_data[table_name] = generate_table_data(table, num_rows)

# Ensure relationships are respected
for relationship in relationships:
    from_table = relationship['fromTable']
    from_column = relationship['fromColumn']
    to_table = relationship['toTable']
    to_column = relationship['toColumn']

    # Get the unique values from the "to" table's column
    to_values = [row[to_column] for row in fake_data[to_table]]

    # Update the "from" table's column with random values from the "to" table's column
    for row in fake_data[from_table]:
        row[from_column] = random.choice(to_values)

# Write the generated fake data to CSV files
for table_name, table_data in fake_data.items():
    file_name = f"./generated_csv/{table_name}_test_data.csv"
    with open(file_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=table_data[0].keys())
        writer.writeheader()
        writer.writerows(table_data)
    print(f"Generated {file_name}")