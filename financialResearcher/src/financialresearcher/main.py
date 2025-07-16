#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from financialresearcher.crew import FinancialResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """Run the financial researcher crew"""
    inputs = {
        "company": "Apple Inc."
    }

    result = FinancialResearcher().crew().kickoff(inputs=inputs)
    print(result.raw)

if __name__ == "__main__":
    run()