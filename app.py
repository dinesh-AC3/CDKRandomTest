#!/usr/bin/env python3

from aws_cdk import core

from firstproject.firstproject_stack import FirstprojectStack


app = core.App()
FirstprojectStack(app, "firstproject")

app.synth()
