from scrapinghub import ScrapinghubClient
from dotenv import load_dotenv
import os

load_dotenv()
scraping_client = ScrapinghubClient(os.environ['SCRAPY_API_KEY'])

project = scraping_client.get_project(os.environ['SCRAPY_PROJECT_ID'])

print("Listing available spiders..")
for spider in project.spiders.list():
    print(spider)


selected_spider = os.environ['SCRAPY_SPIDER_NAME']
print(f"\nAvailable jobs for {selected_spider}:")
running_jobs = project.spiders.get(selected_spider).jobs.list(state='running')
finished_jobs = project.spiders.get(selected_spider).jobs.list()
jobs = running_jobs + finished_jobs
print("Found %s jobs" % len(jobs))
for job in jobs:
    print(job)

print("\nGetting last job items..")
last_job_key = jobs[0]['key']
items = list(scraping_client.get_job(last_job_key).items.iter())
print(f"Found {len(items)} items")