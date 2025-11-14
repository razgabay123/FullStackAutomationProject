from datetime import datetime
import os


class CSVReporter:
    """Simple CSV reporter for performance tests."""
    
    def __init__(self):
        self.results = []
    
    def add_result(self, method, endpoint, response_time, success):
        self.results.append({
            'method': method,
            'endpoint': endpoint, 
            'response_time': response_time,
            'success': success
        })
    
    def save_csv_report(self):
        if not self.results:
            return
            
        os.makedirs("test-results", exist_ok=True)
        filename = f"test-results/performance_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        with open(filename, 'w') as f:
            # CSV header
            f.write("Method,Endpoint,Response_Time_ms,Success\n")
            
            # CSV data
            for r in self.results:
                f.write(f"{r['method']},{r['endpoint']},{r['response_time']:.0f},{r['success']}\n")
        
        print(f"📊 CSV Report saved: {filename}")


reporter = CSVReporter()