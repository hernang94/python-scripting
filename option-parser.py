#! /usr/bin/env python

import sys
import optparse

parser = optparse.OptionParser()

parser.add_option("-n", "--name",dest="name",help="Your Name")

(options,args) = parser.parse_args()

print("Hi " + options.name)
