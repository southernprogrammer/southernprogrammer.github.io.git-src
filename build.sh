#!/usr/bin/env bash
make html && (sleep 2; open http://localhost:8000) & make serve