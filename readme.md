# Scrapy Hub / Zyte API test

This repo is a tiny test just to prove how the Scrapy Hub / Zyte API actually works.

Given this, I was able to prove that the `spider.jobs` only returns finished jobs despite the API supposedly returning all jobs if not given a `status` filter.

See the used [JobQ.list method](https://github.com/scrapinghub/python-scrapinghub/blob/c70137acf2bec5f86d1eac38605dd7ffe68d1e52/scrapinghub/hubstorage/jobq.py#L53-L75) and compare with the [Job list API](https://docs.zyte.com/scrapy-cloud/reference/http/jobs.html#jobs-list-json-jl)


## Running

First, you have to copy the `.env.example` to a local `.env` file and set your API key, project id and scraper name.

```shell
pipenv install
pipenv run python test.py
```