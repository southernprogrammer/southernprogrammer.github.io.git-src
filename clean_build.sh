#!/usr/bin/env bash
(rm -Rf output/*) && make html && (sleep 2; open http://localhost:8000) & make serve