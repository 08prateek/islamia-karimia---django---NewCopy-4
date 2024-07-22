import requests
import time
import openai
import json
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def validate_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            the_file = [json.loads(line) for line in lines]
            return True
    except Exception as e:
        print("Error reading file, invalid format: ", e)
        return False

def upload_file():
    try:
        ft_file = openai.File.create(file=open("data.jsonl", "rb"), purpose='fine-tune')
        return ft_file["id"]
    except Exception as e:
        print("Error uploading file: ", e)
        sys.exit()

def create_model(training_file_id):
    try:
        ft_job = openai.FineTuningJob.create(training_file=training_file_id, model="gpt-3.5-turbo-0613")
        return ft_job["id"]
    except Exception as e:
        print("Error creating fine-tuning job: ", e)
        sys.exit()

def test_model(model_id, prompt):
    try:
        completion = openai.ChatCompletion.create(
            model=model_id,
            temperature=0.0,
            messages=[
                {"role": "system", "content": "You are a helpful and professional customer service representative and expert in student support"},
                {"role": "user", "content": prompt},
            ]
        )
        print(completion.choices[0].message["content"])
    except Exception as e:
        print("Error testing model: ", e)

def main():
    # Validate the file
    is_file_valid = validate_file("data.jsonl")
    if not is_file_valid:
        print("File is not valid")
        sys.exit()

    print("\nFile is valid and now uploading...\n")

    # Upload the file and wait for it to be processed
    file_id = upload_file()
    sleep_time_file = 5
    looptime = 0
    while True:
        print(f"Waiting for OpenAI to process the file... {looptime}")
        file_status = openai.File.retrieve(file_id)
        if file_status["status"] == "processed":
            print(f"\nFile processed: {file_status['id']}\n")
            break
        looptime += sleep_time_file
        time.sleep(sleep_time_file)

    # Create the fine-tuned model and wait for it to be processed
    fine_tuning_job = create_model(file_id)
    model_id = ""
    looptime = 0
    sleep_time_model = 30
    while True:
        print(f"Waiting for OpenAI to create the model... {looptime}")
        model_status = openai.FineTuningJob.retrieve(fine_tuning_job)
        if model_status["status"] == "succeeded":
            model_id = model_status["fine_tuned_model"]
            break
        looptime += sleep_time_model
        time.sleep(sleep_time_model)

    print(f"\nModel created: {model_id}")

    # Test the model
    print("\nTesting the new OpenAI model\n")
    prompt = "How can I contact Islamia Karimia Society?"
    print(f"Prompt: {prompt}")
    test_model(model_id, prompt)

if __name__ == "__main__":
    main()
