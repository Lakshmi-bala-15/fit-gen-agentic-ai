# Fit-Gen Agentic AI

This project generates personalized **workout plans** and **meal plans** using three AI agents:
1. Intake Agent – collects user health details  
2. Workout Agent – generates workout routine  
3. Nutrition Agent – creates meal plan  

## How the project works

The main file `app.py` collects user input and sends it to:
- `intake_agent.py`
- `workout_agent.py`
- `nutrition_agent.py`

Each agent handles one task and returns results.  
Finally, the user gets a full **custom fitness + diet plan**.

## Project Structure

fit-gen-agentic-ai/
│── app.py  
│── README.md  
│── agents/  
      ├── intake_agent.py  
      ├── workout_agent.py  
      └── nutrition_agent.py  

## How to run (optional)

You can run this app using Python:

python app.py

## Hackathon Summary

This project shows **Agentic AI** because:
- Each file acts as a separate AI agent  
- Each agent has a role and task  
- All agents work together to solve one problem  
- Produces personalized output for the user
