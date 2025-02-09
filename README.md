# Fake Data Generator for Power BI

This repository contains a Python script that generates fake test data based on a data model exported from Tabular Editor. The generated data can be used to create measures and visuals in Power BI, especially when the real data source contains little or no data.

## Table of Contents
- [Purpose](#purpose)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Exporting Data Model from Tabular Editor](#exporting-data-model-from-tabular-editor)
- [Script Overview](#script-overview)

## Purpose

The purpose of this script is to generate fake test or fixture data that can be imported into Power BI. This allows for the development of measures and visuals even when the real data source is incomplete or contains insufficient data.

## Getting Started

### Prerequisites

- Python 3.6 or later
- `Faker` library

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/fake-data-generator.git
   cd fake-data-generator
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Export your data model from Tabular Editor (instructions below) and save it as `data_model.json` in the root directory of this repository.
2. Run the script to generate fake data:
   ```bash
   python generate_fake_data.py
   ```
3. The generated CSV files will be saved in the `generated_csv` directory.

## Exporting Data Model from Tabular Editor

1. Open your data model in Tabular Editor.
2. Go to `File` > `Save As`.
3. Choose the `.bim` format and save the file.
4. Convert the `.bim` file to JSON format by renaming the file extension to `.json` or using a suitable tool.
5. Place the `data_model.json` file in the root directory of this repository.

## Script Overview

The script performs the following tasks:

1. **Initialize Faker**: Initializes the Faker library to generate fake data.
2. **Load JSON Data**: Loads the data model from the `data_model.json` file.
3. **Extract Tables and Relationships**: Extracts tables and relationships from the data model.
4. **Generate Fake Data**: Generates fake data for each column based on its data type.
5. **Ensure Relationships Are Respected**: Ensures that relationships between tables are maintained by matching foreign keys appropriately.
6. **Write Data to CSV**: Writes the generated fake data to CSV files in the `generated_csv` directory.

### Example Output

Generated CSV files will be saved in the `generated_csv` directory with names corresponding to the table names in the data model, suffixed with `_test_data.csv`.


