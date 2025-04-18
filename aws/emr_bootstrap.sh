#!/bin/bash

# Non-standard and non-Amazon Machine Image Python modules:
sudo python3 -m pip install \
  langchain            \
  langchain-aws              \
  langsmith             \
  langchain-community

sudo python3 -m pip install langgraph-supervisor 
# sudo yum install -y python-psycopg2