from faker import Faker
import pandas as pd
import random
from datetime import timedelta
from pathlib import Path

print("Script started.")

fake = Faker()

# Set up file paths
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Lists for fake ticket data
departments = [
    "Production",
    "Maintenance",
    "Quality",
    "Shipping",
    "HR",
    "Finance",
    "Admin Office",
    "IT",
    "Engineering"
]

priorities = ["Low", "Medium", "High", "Critical"]

categories = [
    "Hardware",
    "Software",
    "Network",
    "Login / Access",
    "ERP / Business System",
    "Printer / Scanner",
    "Manufacturing System",
    "Machine Interface",
    "Data Issue"
]

statuses = ["Open", "In Progress", "Closed"]

technicians = [
    "Jordan Lee",
    "Morgan Patel",
    "Casey Brooks",
    "Taylor Nguyen",
    "Riley Johnson"
]

machine_types = [
    "CNC Mill",
    "Packaging Line",
    "Injection Molder",
    "Conveyor",
    "Quality Scanner",
    "Label Printer",
    "Robot Arm"
    "Industrial Oven"
]

production_lines = [
    "Line A",
    "Line B",
    "Line C",
    "Quality",
    "Packaging"
]

locations = [
    "Plant 1",
    "Plant 2",
    "Warehouse"
]

criticality_levels = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

roles = [
    "IT Support Technician",
    "Systems Administrator",
    "Maintenance Technician",
    "Production Supervisor",
    "Quality Analyst",
    "Admin Coordinator"
    "ERP Analyst"
]

shifts = [
    "Day",
    "Evening",
    "Night"
]

# Generate fake tickets
tickets = []

for i in range(1, 251):
    created_date = fake.date_time_between(start_date="-6M", end_date="now")

    status = random.choices(
        statuses,
        weights=[20, 20, 60],
        k=1
    )[0]

    if status == "Closed":
        closed_date = created_date + timedelta(hours=random.randint(2, 120))
    else:
        closed_date = None

    ticket = {
        "ticket_id": f"TCK-{1000 + i}",
        "created_date": created_date,
        "closed_date": closed_date,
        "status": status,
        "priority": random.choice(priorities),
        "category": random.choice(categories),
        "department": random.choice(departments),
        "technician": random.choice(technicians),
        "description": fake.sentence(nb_words=10)
    }

    tickets.append(ticket)

# Convert list of tickets into a table
tickets_df = pd.DataFrame(tickets)

# Save the table as a CSV file
tickets_df.to_csv(RAW_DATA_DIR / "tickets.csv", index=False)

print("Created tickets.csv successfully.")

# Generate fake machines
machines = []

for i in range(1, 31):
    machine_type = random.choice(machine_types)

    machine = {
        "machine_id": f"MCH-{100 + i}",
        "machine_name": f"{machine_type} {i:02d}",
        "machine_type": machine_type,
        "production_line": random.choice(production_lines),
        "location": random.choice(locations),
        "install_year": random.randint(2005, 2024),
        "criticality": random.choice(criticality_levels)
    }

    machines.append(machine)

# Convert list of machines into a table
machines_df = pd.DataFrame(machines)

# Save the table as a CSV file
machines_df.to_csv(RAW_DATA_DIR / "machines.csv", index=False)

print("Created machines.csv successfully.")

# Generate fake employees
employees = []

for i in range(1, 51):
    role = random.choice(roles)

    if role in ["IT Support Technician", "Systems Administrator"]:
        department = "IT"
    elif role == "Maintenance Technician":
        department = "Maintenance"
    elif role == "Quality Analyst":
        department = "Quality"
    elif role == "Production Supervisor":
        department = "Production"
    elif role == "ERP Analyst":
        department = "IT"
    else:
        department = "Admin Office"

    employee = {
        "employee_id": f"EMP-{1000 + i}",
        "employee_name": fake.name(),
        "role": role,
        "department": department,
        "shift": random.choice(shifts)
    }

    employees.append(employee)

# Convert list of employees into a table
employees_df = pd.DataFrame(employees)

# Save the table as a CSV file
employees_df.to_csv(RAW_DATA_DIR / "employees.csv", index=False)

print("Created employees.csv successfully.")

# Generate fake downtime events
downtime_reasons = [
    "Mechanical failure",
    "Network disconnect",
    "Sensor fault",
    "Operator error",
    "Preventive maintenance",
    "Software interface issue",
    "Power interruption",
    "Unknown"
]

planned_unplanned_options = [
    "Planned",
    "Unplanned"
]

downtime_events = []

machine_ids = machines_df["machine_id"].tolist()

for i in range(1, 301):
    start_time = fake.date_time_between(start_date="-6M", end_date="now")
    downtime_minutes = random.randint(15, 480)
    end_time = start_time + timedelta(minutes=downtime_minutes)

    downtime_event = {
        "downtime_id": f"DT-{1000 + i}",
        "machine_id": random.choice(machine_ids),
        "start_time": start_time,
        "end_time": end_time,
        "downtime_minutes": downtime_minutes,
        "downtime_reason": random.choice(downtime_reasons),
        "planned_unplanned": random.choice(planned_unplanned_options)
    }

    downtime_events.append(downtime_event)

# Convert list of downtime events into a table
downtime_df = pd.DataFrame(downtime_events)

# Save the table as a CSV file
downtime_df.to_csv(RAW_DATA_DIR / "downtime_events.csv", index=False)

print("Created downtime_events.csv successfully.")