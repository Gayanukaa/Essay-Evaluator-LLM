import dspy

ollama_model = dspy.OllamaLocal(
    model="llama2",
    model_type='text',
    max_tokens=350,
    temperature=0.0,
    top_p=0.8,
    frequency_penalty=1.17,
    top_k=40
)

dspy.settings.configure(lm=ollama_model)

sentiment_model = dspy.Predict('sentence -> sentiment')
sentiment = dspy.OutputField(desc="Possible choices: excellent, good, neutral, bad, very poor, fail.")

def generate_remarks(essay_text, criteria):
    criteria_str = ", ".join(criteria)
    prompt = f"Evaluate this essay based on the following criteria: {criteria_str}. Provide remarks: {essay_text} all in one paragraph"
    response = ollama_model(prompt)
    #print("Ollama Model Response:", response) #Testing
    if isinstance(response, list) and response:
        remarks = "\n".join(response)
        return remarks.strip()
    elif isinstance(response, str):
        return response.strip()
    raise ValueError("Unexpected response format from Ollama model")

def analyze_sentiment(remarks):
    sentiment_response = sentiment_model(sentence=remarks)
    #print("Sentiment Model Response:", sentiment_response) #Testing
    sentiment = sentiment_response['sentiment'].strip().lower()
    return sentiment

def grade_essay(sentiment):
    if "excellent" in sentiment:
        return "A"
    elif "good" in sentiment:
        return "B"
    elif "neutral" in sentiment:
        return "C"
    elif "bad" in sentiment:
        return "S"
    elif "very poor" in sentiment:
        return "D"
    else:
        return "F"

def load_essay(input_path):
    with open(input_path, "r") as file:
        essay_text = file.read()
    return essay_text

def save_evaluation(output_path, remarks, sentiment, grade):
    with open(output_path, "w") as file:
        file.write("Evaluative Remarks:\n" + remarks + "\n\n")
        #file.write("Sentiment: " + sentiment.capitalize() + "\n")
        file.write("Grade: " + grade)

def main_pipeline(input_path, output_path, criteria):
    essay_text = load_essay(input_path)
    remarks = generate_remarks(essay_text, criteria)
    sentiment = analyze_sentiment(remarks)
    grade = grade_essay(sentiment)
    save_evaluation(output_path, remarks, sentiment, grade)

input_path = "/home/gayanukaa/llm-test/dspy-test/essay/essay.txt"
output_path = "/home/gayanukaa/llm-test/dspy-test/essay/evaluation.txt"
criteria = ["clarity", "coherency", "grammar"]
main_pipeline(input_path, output_path, criteria)
