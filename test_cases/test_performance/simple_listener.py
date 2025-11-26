from locust import events
from utilities.performance_reporting import reporter

@events.request.add_listener
def record_request(request_type, name, response_time, response_length, exception, **kwargs):
    reporter.add_result(request_type, name, response_time, exception is None)

@events.test_stop.add_listener  
def save_report(**kwargs):
    reporter.save_csv_report()
# Last updated: 2025-11-26
