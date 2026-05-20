# Data Dictionary

## tickets_clean.csv

| Column | Meaning |
|---|---|
| ticket_id | Unique ticket identifier |
| created_date | Date and time the ticket was created |
| closed_date | Date and time the ticket was closed |
| status | Current ticket status |
| priority | Ticket urgency level |
| category | Type of support issue |
| department | Department that submitted the ticket |
| technician | Assigned support technician |
| resolution_time_hours | Number of hours between creation and closure |
| sla_target_hours | Expected resolution time based on priority |
| sla_met | Whether the ticket was resolved within SLA |

## machines_clean.csv

| Column | Meaning |
|---|---|
| machine_id | Unique machine identifier |
| machine_name | Machine name |
| machine_type | Type of equipment |
| production_line | Area or line where the machine is used |
| location | Plant or warehouse location |
| install_year | Year the machine was installed |
| criticality | Business importance of the machine |
| machine_age_years | Current year minus install year |

## employees_clean.csv

| Column | Meaning |
|---|---|
| employee_id | Unique employee identifier |
| employee_name | Fake employee name |
| role | Employee role |
| department | Employee department |
| shift | Assigned shift |
| is_support_team | Whether employee belongs to IT or Maintenance |

## downtime_events_clean.csv

| Column | Meaning |
|---|---|
| downtime_id | Unique downtime event identifier |
| machine_id | Machine connected to the downtime event |
| start_time | Downtime start timestamp |
| end_time | Downtime end timestamp |
| downtime_minutes | Downtime duration in minutes |
| downtime_hours | Downtime duration in hours |
| downtime_reason | Reason for downtime |
| planned_unplanned | Whether downtime was planned or unplanned |
| is_unplanned | True if downtime was unplanned |