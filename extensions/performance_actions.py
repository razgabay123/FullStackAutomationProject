import time
import psutil
import threading
from locust import events
from utilities.performance_reporting import PerformanceReporting
from utilities.common_ops import get_data


class PerformanceMonitor:
    """Enhanced performance monitoring with system resource tracking."""
    
    def __init__(self) -> None:
        self.reporter = PerformanceReporting()
        self.system_monitor_thread = None
        self.monitoring_active = False
        self.setup_event_listeners()
        
        # Set test configuration
        self.reporter.set_test_config({
            'host': get_data('Host'),
            'api_key': get_data('API_KEY'),
            'users': 'Dynamic',  # Will be updated during test
            'test_type': 'API Load Test'
        })
    
    def setup_event_listeners(self) -> None:
        """Set up Locust event listeners to capture metrics."""
        
        @events.request.add_listener
        def on_request(request_type, name, response_time, response_length, exception, context, **kwargs):
            """Capture individual request metrics."""
            self.reporter.add_metric(
                timestamp=time.time(),
                request_type=request_type,
                name=name,
                response_time=response_time,
                response_length=response_length,
                exception=str(exception) if exception else None
            )
        
        @events.test_start.add_listener
        def on_test_start(environment, **kwargs):
            """Start system monitoring when test begins."""
            print("🚀 Starting enhanced performance monitoring...")
            self.start_system_monitoring()
            
            # Update user count in config
            if hasattr(environment, 'runner') and hasattr(environment.runner, 'user_count'):
                config = self.reporter.test_config.copy()
                config['users'] = environment.runner.user_count
                self.reporter.set_test_config(config)
        
        @events.test_stop.add_listener
        def on_test_stop(environment, **kwargs):
            """Generate reports when test ends."""
            print("🛑 Test completed. Generating enhanced reports...")
            self.stop_system_monitoring()
            
            # Generate comprehensive reports
            try:
                html_report = self.reporter.generate_html_report()
                csv_report = self.reporter.export_to_csv()
                json_report = self.reporter.export_summary_json()
                
                print(f"📊 Reports generated:")
                print(f"  📄 HTML Report: {html_report}")
                print(f"  📊 CSV Data: {csv_report}")
                print(f"  📋 JSON Summary: {json_report}")
                
            except Exception as e:
                print(f"❌ Error generating reports: {e}")
        
        @events.user_add.add_listener
        def on_user_add(user_instance, **kwargs):
            """Update user count when users are added."""
            if hasattr(user_instance.environment, 'runner'):
                config = self.reporter.test_config.copy()
                config['users'] = user_instance.environment.runner.user_count
                self.reporter.set_test_config(config)
        
        @events.user_remove.add_listener
        def on_user_remove(user_instance, **kwargs):
            """Update user count when users are removed."""
            if hasattr(user_instance.environment, 'runner'):
                config = self.reporter.test_config.copy()
                config['users'] = user_instance.environment.runner.user_count
                self.reporter.set_test_config(config)
    
    def start_system_monitoring(self) -> None:
        """Start monitoring system resources in a separate thread."""
        self.monitoring_active = True
        self.system_monitor_thread = threading.Thread(target=self._monitor_system_resources)
        self.system_monitor_thread.daemon = True
        self.system_monitor_thread.start()
    
    def stop_system_monitoring(self) -> None:
        """Stop system resource monitoring."""
        self.monitoring_active = False
        if self.system_monitor_thread:
            self.system_monitor_thread.join(timeout=5)
    
    def _monitor_system_resources(self) -> None:
        """Monitor system resources continuously."""
        while self.monitoring_active:
            try:
                # Get system metrics
                cpu_percent = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                disk_io = psutil.disk_io_counters()
                
                # Add to reporter
                self.reporter.add_system_metric(
                    timestamp=time.time(),
                    cpu_percent=cpu_percent,
                    memory_percent=memory.percent,
                    disk_io=disk_io._asdict() if disk_io else {}
                )
                
                # Sleep for 5 seconds before next measurement
                time.sleep(5)
                
            except Exception as e:
                print(f"⚠️ Error monitoring system resources: {e}")
                time.sleep(5)
    
    @staticmethod
    def get_system_info() -> dict:
        """Get current system information."""
        try:
            return {
                'cpu_count': psutil.cpu_count(),
                'memory_total_gb': round(psutil.virtual_memory().total / (1024**3), 2),
                'disk_usage_percent': psutil.disk_usage('/').percent,
                'boot_time': psutil.boot_time(),
                'platform': psutil.WINDOWS if hasattr(psutil, 'WINDOWS') else 'Unknown'
            }
        except Exception as e:
            print(f"⚠️ Error getting system info: {e}")
            return {}
    
    def generate_real_time_stats(self) -> dict:
        """Generate real-time statistics during test execution."""
        stats = self.reporter.calculate_statistics()
        
        if stats:
            print("\n" + "="*60)
            print("📊 REAL-TIME PERFORMANCE STATS")
            print("="*60)
            print(f"🔢 Total Requests: {stats.get('total_requests', 0):,}")
            print(f"✅ Success Rate: {100 - stats.get('failure_rate', 0):.2f}%")
            print(f"⏱️  Avg Response Time: {stats.get('avg_response_time', 0):.0f}ms")
            print(f"📈 95th Percentile: {stats.get('p95_response_time', 0):.0f}ms")
            print(f"🚀 Requests/Second: {stats.get('requests_per_second', 0):.1f}")
            print("="*60)
        
        return stats


# Global instance to be used across tests
performance_monitor = PerformanceMonitor()
# Last updated: 2025-11-26
