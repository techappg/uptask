#!/bin/bash

echo "Restarting.....!"

sudo systemctl daemon-reload

sudo systemctl restart uptask

sudo systemctl status uptask

echo "uptask has restarted."


