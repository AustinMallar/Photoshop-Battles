#!/bin/bash

sudo uwsgi --socket photoshopbattles.sock --module photoshopbattles.wsgi --chmod-socket=666
