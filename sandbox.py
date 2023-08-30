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

    s_ip = os.getenv("SPLUNK_IP")
    s_tok = os.getenv("SPLUNK_TOKEN")

    splunk = Splunk(
        s_ip, s_tok, verify=False, indexer_ack=True
    )

    log_to_splunk(splunk, "Starting IP TESTICLE")
    print(f"{s_ip}   {s_tok}")



if __name__ == "__main__":
    main()
