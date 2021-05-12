from datadog import initialize, statsd
import time
import os

# This env var is to get the IP of the kubernetes host
# It assumes this env var is set in a container
DD_AGENT_IP = os.getenv('DD_AGENT_IP')

options = {
    "statsd_host": DD_AGENT_IP,
    "statsd_port": 8125,
}

initialize(**options)


def test_metrics():
    while(1):
        statsd.increment('immuta_test.increment', tags=["environment:dev"])
        statsd.decrement('immuta_test.decrement', tags=["environment:dev"])
        time.sleep(10)


def data_source_metrics():

