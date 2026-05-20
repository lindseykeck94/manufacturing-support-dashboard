# Manufacturing Support Dashboard

This project simulates an IT ticketing and manufacturing operations environment using Python-generated dummy data and a Power BI dashboard.

## Project Goal

The goal of this project is to create a portfolio-ready analytics project that tracks:

- IT support ticket volume
- Ticket priority and status
- Department support needs
- Machine downtime
- Manufacturing operations trends

## Tools Used

- Python
- pandas
- Faker
- Power BI
- VS Code
- GitHub

## Project Status

In progress.

## Planned Dashboard Pages

1. Executive Overview
2. Ticket Operations
3. Manufacturing Downtime

## Project Overview

This project simulates a manufacturing support environment with IT ticketing, employee, machine, and downtime data.

The purpose of the project is to practice building a full analytics workflow:

1. Generate dummy business data with Python
2. Clean and transform the data with pandas
3. Prepare processed CSV files for Power BI
4. Build a dashboard to analyze ticket volume, SLA performance, and manufacturing downtime

## Current Status

Week 2 in progress: data cleaning and transformation complete.

## Data Files

### Raw Data

Located in `data/raw`:

- `tickets.csv`
- `machines.csv`
- `employees.csv`
- `downtime_events.csv`

### Processed Data

Located in `data/processed`:

- `tickets_clean.csv`
- `machines_clean.csv`
- `employees_clean.csv`
- `downtime_events_clean.csv`

## Project Workflow

```text
generate_dummy_data.py
        ↓
data/raw CSV files
        ↓
clean_transform_data.py
        ↓
data/processed CSV files
        ↓
Power BI dashboard

## Tools Used

- Python
- pandas
- Faker
- VS Code
- GitHub
- Power BI

## Python Libraries

- `pandas` for table cleaning and CSV export
- `Faker` for generating realistic dummy data
- `pathlib` for managing file paths
- `random` for randomized values

## Planned Power BI Dashboard Pages

1. Executive Overview
   - Total tickets
   - Open tickets
   - SLA performance
   - Total downtime hours

2. Ticket Operations
   - Tickets by priority
   - Tickets by category
   - Tickets by department
   - Average resolution time

3. Manufacturing Downtime
   - Downtime by machine
   - Downtime by reason
   - Planned vs unplanned downtime
   - Downtime by production line