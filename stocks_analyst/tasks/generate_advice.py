from crewai import Task
from agents.financial_strategist import financial_strategist

generate_advice_task = Task(
    description='Using sentiment and news, give actionable stock recommendations.',
    expected_output='List of 3-5 stock suggestions with reasoning.',
    agent=financial_strategist
)
