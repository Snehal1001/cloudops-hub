##At backend level ##
To Activate python env - source venv/bin/activate
To run Server - uvicorn main:app --reload

##Why Repository Pattern?
Separates:
DB logic
from
business logic

Benefits:
easier testing
cleaner architecture
reusable queries

Very common in enterprise systems.

##Why Service Layer?

This is where future business logic goes:

validation
permissions
workflows
events
Azure Service Bus integration later