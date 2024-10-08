from swarms import Agent
from swarm_models import OpenAIChat
from typing import List
from swarms_memory import ChromaDB

memory = ChromaDB(
    metric="cosine",
    output_dir="metric_qa",
    # docs_folder="data",
    n_results=1,
)


def patient_query_intake_agent_prompt():
    return (
        "You are the Patient Query Intake Agent. Your task is to receive and log initial patient queries. "
        "Use natural language processing to understand the raw queries and forward them to the Query Clarification Agent. "
        "Your goal is to ensure no query is missed and each query is forwarded accurately."
    )


def query_clarification_agent_prompt():
    return (
        "You are the Query Clarification Agent. Your task is to make sure the patient's query is clear and specific. "
        "Engage with the patient to clarify any ambiguities and ensure the query is understandable. "
        "Forward the clarified queries to the Data Retrieval Agent. "
        "Your goal is to remove any confusion and ensure the query is precise."
    )


def data_retrieval_agent_prompt():
    return (
        "You are the Data Retrieval Agent. Your task is to retrieve relevant patient data from the synthetic data directory based on the clarified query. "
        "Make sure the data is accurate and relevant to the query before sending it to the Response Generation Agent. "
        "Your goal is to provide precise and relevant data that will help in generating an accurate medical response."
    )


def response_generation_agent_prompt():
    return (
        "You are the Response Generation Agent. Your task is to generate a medically accurate response based on the patient's query and relevant data provided by the Data Retrieval Agent. "
        "Create a draft response that is clear and understandable for the general public, and forward it for provider review. "
        "Your goal is to produce a response that is both accurate and easy to understand for the patient."
    )


def supervising_agent_prompt():
    return (
        "You are the Supervising Agent. Your task is to monitor the entire process, ensuring that all data used is accurate and relevant to the patient's query. "
        "Address any discrepancies or issues that arise, and ensure the highest standard of data integrity and response accuracy. "
        "Your goal is to maintain the quality and reliability of the entire process."
    )


def patient_llm_agent_prompt():
    return (
        "You are the Patient LLM Agent. Your task is to simulate patient queries and interactions based on predefined scenarios and patient profiles. "
        "Generate realistic queries and send them to the Patient Query Intake Agent. "
        "Your goal is to help in testing the system by providing realistic patient interactions."
    )


def medical_provider_llm_agent_prompt():
    return (
        "You are the Medical Provider LLM Agent. Your task is to simulate medical provider responses and evaluations. "
        "Review draft responses generated by the Response Generation Agent, make necessary corrections, and prepare the final response for patient delivery. "
        "Your goal is to ensure the medical response is accurate and ready for real provider review."
    )


# Generate the prompts by calling each function
prompts = [
    query_clarification_agent_prompt(),
    # data_retrieval_agent_prompt(),
    response_generation_agent_prompt(),
    supervising_agent_prompt(),
    medical_provider_llm_agent_prompt(),
]


# Define the agent names and system prompts
agent_names = [
    "Query Clarification Agent",
    "Response Generation Agent",
    "Supervising Agent",
    "Medical Provider Agent",
]

# Define the system prompts for each agent
system_prompts = [
    # patient_llm_agent_prompt(),
    query_clarification_agent_prompt(),
    response_generation_agent_prompt(),
    supervising_agent_prompt(),
    medical_provider_llm_agent_prompt(),
]

# Create agents for each prompt

agents = []
for name, prompt in zip(agent_names, system_prompts):
    # agent = Agent(agent_name=name, agent_description="", llm=OpenAIChat(), system_prompt=prompt)
    # Initialize the agent
    agent = Agent(
        agent_name=name,
        system_prompt=prompt,
        agent_description=prompt,
        llm=OpenAIChat(
            max_tokens=3000,
        ),
        max_loops=1,
        autosave=True,
        # dashboard=False,
        verbose=True,
        # interactive=True,
        state_save_file_type="json",
        saved_state_path=f"{name.lower().replace(' ', '_')}.json",
        # docs_folder="data", # Folder of docs to parse and add to the agent's memory
        # long_term_memory=memory,
        # pdf_path="docs/medical_papers.pdf",
        # list_of_pdf=["docs/medical_papers.pdf", "docs/medical_papers_2.pdf"],
        # docs=["docs/medicalx_papers.pdf", "docs/medical_papers_2.txt"],
        dynamic_temperature_enabled=True,
        # memory_chunk_size=2000,
    )

    agents.append(agent)


# Run the agent
def run_agents(agents: List[Agent] = agents, task: str = None):
    output = None
    for i in range(len(agents)):
        if i == 0:
            output = agents[i].run(task)

        else:
            output = agents[i].run(output)

        # Add extensive logging for each agent
        print(f"Agent {i+1} - {agents[i].agent_name}")
        print("-----------------------------------")


task = "what should I be concerned about in my results for Anderson? What results show for Anderson. He has lukeima and is 45 years old and has a fever."
out = run_agents(agents, task)
print(out)
