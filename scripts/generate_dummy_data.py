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

# Generate fake tickets
tickets = []

for i in range(1, 101):
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