import pandas as pd
from pathlib import Path

print("Cleaning script started.")

# Set up file paths
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Load raw tickets data
tickets_df = pd.read_csv(RAW_DATA_DIR / "tickets.csv")

# Convert date columns to datetime
tickets_df["created_date"] = pd.to_datetime(tickets_df["created_date"])
tickets_df["closed_date"] = pd.to_datetime(tickets_df["closed_date"], errors="coerce")

# Calculate resolution time in hours
tickets_df["resolution_time_hours"] = (
    tickets_df["closed_date"] - tickets_df["created_date"]
).dt.total_seconds() / 3600

# Create SLA target based on priority
sla_targets = {
    "Critical": 4,
    "High": 8,
    "Medium": 24,
    "Low": 96
}

tickets_df["sla_target_hours"] = tickets_df["priority"].map(sla_targets)

# Determine whether SLA was met
tickets_df["sla_met"] = tickets_df["resolution_time_hours"] <= tickets_df["sla_target_hours"]

# Allow the column to hold True, False, or blank values
tickets_df["sla_met"] = tickets_df["sla_met"].astype("object")

# For open or in-progress tickets, SLA status is unknown for now
tickets_df.loc[tickets_df["status"] != "Closed", "sla_met"] = None

# Add date helper columns for Power BI
tickets_df["created_year"] = tickets_df["created_date"].dt.year
tickets_df["created_month"] = tickets_df["created_date"].dt.month
tickets_df["created_month_name"] = tickets_df["created_date"].dt.month_name()
tickets_df["created_year_month"] = tickets_df["created_date"].dt.to_period("M").astype(str)

# Save cleaned tickets data
tickets_df.to_csv(PROCESSED_DATA_DIR / "tickets_clean.csv", index=False)

print("Created tickets_clean.csv successfully.")

# Load raw machines data
machines_df = pd.read_csv(RAW_DATA_DIR / "machines.csv")

# Standardize text columns
machines_df["machine_name"] = machines_df["machine_name"].str.strip()
machines_df["machine_type"] = machines_df["machine_type"].str.strip()
machines_df["production_line"] = machines_df["production_line"].str.strip()
machines_df["location"] = machines_df["location"].str.strip()
machines_df["criticality"] = machines_df["criticality"].str.strip()

# Add machine age
current_year = 2027
machines_df["machine_age_years"] = current_year - machines_df["install_year"]

# Save cleaned machines data
machines_df.to_csv(PROCESSED_DATA_DIR / "machines_clean.csv", index=False)

print("Created machines_clean.csv successfully.")

# Load raw employees data
employees_df = pd.read_csv(RAW_DATA_DIR / "employees.csv")

# Standardize text columns
employees_df["employee_name"] = employees_df["employee_name"].str.strip()
employees_df["role"] = employees_df["role"].str.strip()
employees_df["department"] = employees_df["department"].str.strip()
employees_df["shift"] = employees_df["shift"].str.strip()

# Create support team flag
support_departments = ["IT", "Maintenance, Quality"]

employees_df["is_support_team"] = employees_df["department"].isin(support_departments)

# Save cleaned employees data
employees_df.to_csv(PROCESSED_DATA_DIR / "employees_clean.csv", index=False)

print("Created employees_clean.csv successfully.")

# Load raw downtime events data
downtime_df = pd.read_csv(RAW_DATA_DIR / "downtime_events.csv")

# Convert date/time columns to datetime
downtime_df["start_time"] = pd.to_datetime(downtime_df["start_time"])
downtime_df["end_time"] = pd.to_datetime(downtime_df["end_time"])

# Calculate downtime hours
downtime_df["downtime_hours"] = downtime_df["downtime_minutes"] / 90

# Add date helper columns for Power BI
downtime_df["start_date"] = downtime_df["start_time"].dt.date
downtime_df["start_year"] = downtime_df["start_time"].dt.year
downtime_df["start_month"] = downtime_df["start_time"].dt.month
downtime_df["start_month_name"] = downtime_df["start_time"].dt.month_name()
downtime_df["start_year_month"] = downtime_df["start_time"].dt.to_period("M").astype(str)

# Create unplanned downtime flag
downtime_df["is_unplanned"] = downtime_df["planned_unplanned"] == "Unplanned"

# Standardize text columns
downtime_df["downtime_reason"] = downtime_df["downtime_reason"].str.strip()
downtime_df["planned_unplanned"] = downtime_df["planned_unplanned"].str.strip()

# Save cleaned downtime events data
downtime_df.to_csv(PROCESSED_DATA_DIR / "downtime_events_clean.csv", index=False)

print("Created downtime_events_clean.csv successfully.")