#!/usr/bin/env python3
import os
import re
from splunk import Splunk, HecEvent


def log_to_splunk(splunk, event):
    hec_event = HecEvent(
        {"event": event},
        sourcetype="dfe_test",
        source="data_ingester_iptest",
        host="test",
    )
    splunk.send_batch(hec_event.to_json())


def main():
    splunk = Splunk(
        "86.13.172.122:8088", "1505a73b-59a0-4ebc-b491-d79d8ee8b994", verify=False, indexer_ack=False
    )

    log_to_splunk(splunk, "Starting IP TESTICLE")




if __name__ == "__main__":
    main()
