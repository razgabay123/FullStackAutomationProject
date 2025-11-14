from locust import HttpUser, task, constant


class MyFirstTest(HttpUser):
    host = "file:///D:/Automation/test_automation/automation_html_css/page_spam.html"
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print("Launching the URL")

    @task
    def search(self):
        print("Searching")


class MySecondTest(HttpUser):
    weight = 2
    wait_time = constant(1)

    @task
    def search2(self):
        print("Second Search Test")

    @task
    def launch2(self):
        print("Second Test")
