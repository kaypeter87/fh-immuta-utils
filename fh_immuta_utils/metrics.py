from datadog import initialize, statsd
import time

options = {
    "statsd_host": "127.0.0.1",
    "statsd_port": 8125,
}

initialize(**options)


def test_metrics():
    while(1):
        statsd.increment('test.increment', tags=["environment:dev"])
        statsd.decrement('test.decrement', tags=["environment:dev"])
        time.sleep(10)
