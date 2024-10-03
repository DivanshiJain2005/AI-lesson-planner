import time
import json
import openai
import statistics
from tqdm import tqdm

# Make sure to set your OpenAI API key
openai.api_key = "your-api-key-here"

def generate_lesson_plan(lesson_details):
    system_message = """
    You are an AI assistant that generates lesson plans. Create a detailed lesson plan based on the provided information.
    Output should be in JSON format with the following structure:
    {
        "Learning outcomes": {
            "knowledge": "",
            "skills": "",
            "understanding": ""
        },
        "Learning experiences": {
            "Prepare": "",
            "Plan": "",
            "Investigate": "",
            "Apply": "",
            "Connect": "",
            "Evaluate": ""
        },
        "Assessment": "",
        "Reflection": ""
    }
    """
    
    user_message = f"Generate a lesson plan for: {json.dumps(lesson_details)}"
    
    start_time = time.time()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
    )
    end_time = time.time()
    
    return {
        "response": response.choices[0].message['content'],
        "time": end_time - start_time,
        "tokens": response['usage']['total_tokens']
    }

def evaluate_quality(lesson_plan):
    try:
        plan = json.loads(lesson_plan)
        score = 0
        score += len(plan.get("Learning outcomes", {}).get("knowledge", "").split()) / 10
        score += len(plan.get("Learning outcomes", {}).get("skills", "").split()) / 10
        score += len(plan.get("Learning outcomes", {}).get("understanding", "").split()) / 10
        score += sum(len(v.split()) for v in plan.get("Learning experiences", {}).values()) / 50
        score += len(plan.get("Assessment", "").split()) / 20
        score += len(plan.get("Reflection", "").split()) / 20
        return min(score, 10)  # Cap at 10
    except json.JSONDecodeError:
        return 0  # If it's not valid JSON, it's a failed generation

def run_performance_test(num_tests=10):
    lesson_details = [
        {"title": "Introduction to Photosynthesis", "subject": "Biology", "grade": 9, "duration": 2},
        {"title": "World War II Overview", "subject": "History", "grade": 11, "duration": 3},
        {"title": "Basic Algebraic Equations", "subject": "Math", "grade": 8, "duration": 1},
        {"title": "Shakespeare's Macbeth", "subject": "Literature", "grade": 10, "duration": 4},
        {"title": "States of Matter", "subject": "Chemistry", "grade": 7, "duration": 2}
    ]
    
    results = []
    
    for _ in tqdm(range(num_tests)):
        for details in lesson_details:
            result = generate_lesson_plan(details)
            result['quality'] = evaluate_quality(result['response'])
            results.append(result)
    
    # Analyze results
    avg_time = statistics.mean(r['time'] for r in results)
    avg_tokens = statistics.mean(r['tokens'] for r in results)
    avg_quality = statistics.mean(r['quality'] for r in results)
    
    print(f"Average response time: {avg_time:.2f} seconds")
    print(f"Average tokens used: {avg_tokens:.2f}")
    print(f"Average quality score: {avg_quality:.2f} / 10")
    
    with open('performance_results.json', 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    run_performance_test()