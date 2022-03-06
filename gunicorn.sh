#!/bin/bash

sudo systemctl daemon-reload

sudo systemctl restart uptask

sudo systemctl status uptask

echo "uptask has restarted."

