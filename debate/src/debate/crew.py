from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Debate():
    """Debate crew"""

    #agents: List[BaseAgent]
    #tasks: List[Task]

    agents_config = "config/OpenAIagents.yaml"
    #agents_config = "config/GeminiAgents.yaml"
    tasks_config = "config/tasks.yaml"


    @agent
    def debater(self) -> Agent:
        return Agent( config=self.agents_config['debater'], verbose=True )

    @agent
    def judge(self) -> Agent:
        return Agent( config=self.agents_config['judge'], verbose=True )

    @task
    def propose(self) -> Task:
        return Task(config=self.tasks_config['propose'],)

    @task
    def oppose(self) -> Task:
        return Task( config=self.tasks_config['oppose'],)

    @task
    def decide(self) -> Task:
        return Task( config=self.tasks_config['decide'],)


    @crew
    def crew(self) -> Crew:
        """Creates the Debate crew"""
      
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
