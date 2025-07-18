#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from coderai.crew import coderai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

assignment = "Write a python code to generate a multiplication table for 2 till the result is 100"

def run():
    inputs = {"assignment": assignment}
    result= coderai().crew().kickoff(inputs=inputs)
    print(result.raw)
