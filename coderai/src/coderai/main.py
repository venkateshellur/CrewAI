#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from coderai.crew import coderai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

programmingLanguage = "cobol"
assignment = "Write a "+programmingLanguage+" code to generate a multiplication table for 2 till the result is 100"
outputFileName="output//cobol.md"

def run():
    inputs = {"assignment": assignment, "programingLanguage": programmingLanguage, "outputFileName": outputFileName}
    result= coderai().crew().kickoff(inputs=inputs)
    print(result.raw)
