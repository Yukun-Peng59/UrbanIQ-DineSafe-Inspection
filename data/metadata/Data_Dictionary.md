# Data Dictionary – DineSafe Inspection Dataset

| Column Name | Data Type | Example | Description | Entity |
|--------------|-----------|----------|--------------|---------|
| EstablishmentID | String | 10653 | Unique identifier for each restaurant | Establishment |
| InspectionDate | Date | 2024-06-15 | Date of inspection | Inspection |
| Status | Category | Pass / Conditional Pass / Closed | Result of inspection | Inspection |
| Severity | Category | C / S / M | Violation severity | Infraction |
| Latitude | Float | 43.654 | Geographic coordinate | Establishment |
| Longitude | Float | -79.383 | Geographic coordinate | Establishment |
