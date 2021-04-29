#!/bin/sh
sudo docker build -t summer_experience .
sudo docker run --rm -i -p 8080:8080 -t summer_experience