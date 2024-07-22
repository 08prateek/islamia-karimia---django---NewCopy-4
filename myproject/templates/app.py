from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app)

model_id = "ft:gpt-3.5-turbo-0613:designlab-international::9lC7VbRj"  # Replace with the actual model ID after fine-tuning

# Few-shot examples to guide the model
few_shot_examples = [
    {"role": "system", "content": "You are a helpful and professional customer service representative and expert in student support"},
    {"role": "user", "content": "What is the email id of Islamia Karimia College (Palasia) Indore?"},
    {"role": "assistant", "content": "The email id of Islamia Karimia College (Palasia) is info@ikcollegeindore.org."},
    {"role": "user", "content": "How can I contact Islamia Karimia Society?"},
    {"role": "assistant", "content": "You can contact Islamia Karimia Society via their official email or phone number listed on their website."},
    {"role": "user", "content": "What is the contact number of Islamia Karimia Society?"},
    {"role": "assistant", "content": "The contact number for Islamia Karimia Society is 0731-2701777 or 9827235238."},
    {"role": "user", "content": "what is the facebook profile of islamia karimia society?"}, 
    {"role": "assistant", "content": "the facebook profile of islamia karimia society is - https://www.facebook.com/Iksociety"},
    {"role": "user", "content": "What is the email address of Islamia Karimia Society?"}, 
    {"role": "assistant", "content": "The email address of Islamia Karimia Society is iksocietyoffice@gmail.com"},
    {"role": "user", "content": "what is the instagram profile of islamia karimia society?"}, 
    {"role": "assistant", "content": "the instagram profile of islamia karimia society is - https://www.instagram.com/ik_society/"},
    {"role": "user", "content": "what is the linkedin profile of islamia karimia society?"}, 
    {"role": "assistant", "content": "the linkedin profile of islamia karimia society is - https://www.linkedin.com/in/ik-group-of-institution-441357252/"},
    {"role": "user", "content": "what is the youtube channel of islamia karimia society?"}, 
    {"role": "assistant", "content": "the youtube channel of islamia karimia society is - https://www.youtube.com/@ikgroupofinstitution5748"},
    {"role": "user", "content": "what is the contact number of islamia karimia college (Palasia) indore?"}, 
    {"role": "assistant", "content": "the contact number of islamia karimia college (Palasia) is - +91-731-2565112, 2560234"},
    {"role": "user", "content": "what is the email id of Islamia Karimia BAB girls college (Ushaganj)?"}, 
    {"role": "assistant", "content": "the email id of Islamia Karimia BAB girls college (Ushaganj) is babgirlscollege@gmail.com"},
    {"role": "user", "content": "what is the contact number of islamia karimia BAB girls college (Ushaganj)?"}, 
    {"role": "assistant", "content": "the contact number of islamia karimia BAB girls college (Ushaganj) is 0731-2702954, 64254-78536"},
    {"role": "user", "content": "what is the email id of Islamia institute of computer science and management, indore?"}, 
    {"role": "assistant", "content": "the email id of Islamia institute of computer science and management, indore is iksocietyoffice@gmail.com"},
    {"role": "user", "content": "what is the contact number of Islamia institute of computer science and management, indore?"}, 
    {"role": "assistant", "content": "the contact number of Islamia institute of computer science and management, indore is +917312562399"},
    {"role": "user", "content": "what is the email id of Islamia Private ITI(sanyogitaganj, chhawni)?"}, 
    {"role": "assistant", "content": "the email id of Islamia Private ITI(sanyogitaganj, chhawni)is- ik_iti@yahoo.com"},
    {"role": "user", "content": "what is the contact number of Islamia Private ITI(sanyogitaganj, chhawni)?"}, 
    {"role": "assistant", "content": "the contact number of Islamia Private ITI(sanyogitaganj, chhawni) is- 0731-2705781 , +91-9826822003"},
    {"role": "user", "content": "what is the email id of Islamia Technical and vocational institute?"}, 
    {"role": "assistant", "content": "the email id of Islamia Technical and vocational institute is- ik_itvi@yahoo.com"},
    {"role": "user", "content": "what is the contact number of Islamia Technical and vocational institute?"}, 
    {"role": "assistant", "content": "the contact number of Islamia Technical and vocational institute is- 0731-2705781, 9826822003"},
    {"role": "user", "content": "what is the email id of St. Umar Hr. Sec. School English Medium?"}, 
    {"role": "assistant", "content": "the email id of St. Umar Hr. Sec. School English Medium is- stumarinfo@gmail.com"},
    {"role": "user", "content": "what is the contact number of St. Umar Hr. Sec. School English Medium?"}, 
    {"role": "assistant", "content": "the contact number of St. Umar Hr. Sec. School English Medium is- 0731-2560039"},
    {"role": "user", "content": "what is the email id of St. Umar Academy CBSE?"}, 
    {"role": "assistant", "content": "the email id  of St. Umar Academy CBSE is- stumaracademy@gmail.com"},
    {"role": "user", "content": "what is the contact number of St. Umar Academy CBSE?"}, 
    {"role": "assistant", "content": "the contact number of St. Umar Academy CBSE is 0731-2560033"},
    {"role": "user", "content": "what is the email id of  IK Boys Hr. Sec. School(Sanyogita ganj chhawni)?"}, 
    {"role": "assistant", "content": "the email id of IK Boys Hr. Sec. School(Sanyogita ganj chhawni) is- ikboysschool@gmail.com "},
    {"role": "user", "content": "what is the contact number of IK Boys Hr. Sec. School(Sanyogita ganj chhawni)?"}, 
    {"role": "assistant", "content": " the contact number of IK Boys Hr. Sec. School(Sanyogita ganj chhawni) is- 0731-2701777"},
    {"role": "user", "content": "what is the email id of IK Girls Hr. Sec. School (Ushaganj, Chhawni)?"}, 
    {"role": "assistant", "content": "the email id of  IK Girls Hr. Sec. School (Ushaganj, Chhawni) is- info@ikcollegeindore.org"},
    {"role": "user", "content": "what is the contact number of IK Girls Hr. Sec. School (Ushaganj, Chhawni)?"}, 
    {"role": "assistant", "content": "the contact number of  IK Girls Hr. Sec. School (Ushaganj, Chhawni) is- +91-731-2565112, 2560234"},
    {"role": "user", "content": "what is the email id of St. Mustafa Raza High School (Azad Nagar)?"}, 
    {"role": "assistant", "content": "the email id of St. Mustafa Raza High School (Azad Nagar) is- IKstmustufarazaschool@gmail.com"},
    {"role": "user", "content": "what is the contact number of St. Mustafa Raza High School (Azad Nagar)?"}, 
    {"role": "assistant", "content": "the contact number of St. Mustafa Raza High School (Azad Nagar) is- +91-9907557585"},
    {"role": "user", "content": "what is the email id of IK Sky Height International Prep School?"}, 
    {"role": "assistant", "content": "the email id of IK Sky Height International Prep School is- Ikskyheightsinternationalschool@gmail.com"},
    {"role": "user", "content": "what is the contact number of IK Sky Height International Prep School?"}, 
    {"role": "assistant", "content": "the contact number of IK Sky Height International Prep School is- +91-9171099929,+91-9171099930"},
    {"role": "user", "content": "what is the email id of IK Coaching classes?"}, 
    {"role": "assistant", "content": "the email id of IK Coaching classes is- iksocietyoffice@gmail.com"},
    {"role": "user", "content": "what is the contact number of IK Coaching classes?"}, 
    {"role": "assistant", "content": "the contact number of IK Coaching classes  is- 0731-2701777, 0731-2705781"},
    {"role": "user", "content": "Islamia Karimia Society ka email address kya hai?"}, 
    {"role": "assistant", "content": "Islamia Karimia Society ka email address iksocietyoffice@gmail.com hai."},
    {"role": "user", "content": "Islamia Karimia Society ka contact number kya hai?"}, 
    {"role": "assistant", "content": "Islamia Karimia Society ka contact number 0731-2701777 ya 9827235238 hai."},
    {"role": "user", "content": "Islamia Karimia Society ka facebook profile kya hai?"}, 
    {"role": "assistant", "content": "Islamia Karimia Society ka facebook profile hai - https://www.facebook.com/Iksociety"},
    {"role": "user", "content": "Islamia Karimia Society ka instagram profile kya hai?"}, 
    {"role": "assistant", "content": "Islamia Karimia Society ka instagram profile hai - https://www.instagram.com/ik_society/"},
    {"role": "user", "content": "islamia karimia society ka linkedin profile kya hai?"}, 
    {"role": "assistant", "content": "islamia karimia society ka linkedin profile hai - https://www.linkedin.com/in/ik-group-of-institution-441357252/"},
    {"role": "user", "content": "islamia karimia society ka youtube channel kya hai?"}, 
    {"role": "assistant", "content": "islamia karimia society ka youtube channel hai - https://www.youtube.com/@ikgroupofinstitution5748"},
    {"role": "user", "content": "Islamia Karimia College (Palasia) indore ka email id kya hai?"}, 
    {"role": "assistant", "content": "Islamia Karimia College (Palasia) ka email id hai- info@ikcollegeindore.org"},
    {"role": "user", "content": "Islamia Karimia College (Palasia) indore ka contact number kya hai?"}, 
    {"role": "assistant", "content": "Islamia Karimia College (Palasia) ka contact number hai - +91-731-2565112, 2560234"},
    {"role": "user", "content": "Islamia Karimia BAB girls college (Ushaganj) ka email id kya hai?"}, 
    {"role": "assistant", "content": "Islamia Karimia BAB girls college (Ushaganj) ka email id hai babgirlscollege@gmail.com"},
    {"role": "user", "content": "Islamia Karimia BAB girls college (Ushaganj) ka contact number kya hai?"}, 
    {"role": "assistant", "content": "Islamia Karimia BAB girls college (Ushaganj) ka contact number hai 0731-2702954, 64254-78536"},
    {"role": "user", "content": "Islamia institute of computer science and management, indore ka email id kya hai?"}, 
    {"role": "assistant", "content": "Islamia institute of computer science and management, indore ka email id hai iksocietyoffice@gmail.com"},
    {"role": "user", "content": "Islamia institute of computer science and management, indore ka contact number kya hai?"}, 
    {"role": "assistant", "content": "Islamia institute of computer science and management, indore ka contact number hai +917312562399"},
    {"role": "user", "content": "Islamia Private ITI(sanyogitaganj, chhawni) ka email id kya hai?"}, 
    {"role": "assistant", "content": "Islamia Private ITI(sanyogitaganj, chhawni)ka email id hai- ik_iti@yahoo.com"},
    {"role": "user", "content": "Islamia Private ITI(sanyogitaganj, chhawni) ka contact number kya hai?"}, 
    {"role": "assistant", "content": "Islamia Private ITI(sanyogitaganj, chhawni) ka contact number hai- 0731-2705781 , +91-9826822003"},
    {"role": "user", "content": "Islamia Technical and vocational institute ka email id kya hai?"}, 
    {"role": "assistant", "content": "Islamia Technical and vocational institute ka email id hai- ik_itvi@yahoo.com"},
    {"role": "user", "content": "Islamia Technical and vocational institute ka contact number kya hai?"}, 
    {"role": "assistant", "content": "Islamia Technical and vocational institute ka contact number hai- 0731-2705781, 9826822003"},
    {"role": "user", "content": "St. Umar Hr. Sec. School English Medium ka email id kya hai?"}, 
    {"role": "assistant", "content": "St. Umar Hr. Sec. School English Medium ka email id hai- stumarinfo@gmail.com"},
    {"role": "user", "content": "St. Umar Hr. Sec. School English Medium ka contact number kya hai?"}, 
    {"role": "assistant", "content": "St. Umar Hr. Sec. School English Medium ka contact number hai- 0731-2560039"},
    {"role": "user", "content": "St. Umar Academy CBSE ka email id kya hai?"}, 
    {"role": "assistant", "content": "St. Umar Academy CBSE ka email id hai- stumaracademy@gmail.com"},
    {"role": "user", "content": "St. Umar Academy CBSE ka contact number kya hai?"}, 
    {"role": "assistant", "content": "St. Umar Academy CBSE ka contact number hai- 0731-2560033"},
    {"role": "user", "content": "IK Boys Hr. Sec. School(Sanyogita ganj chhawni) ka email id kya hai?"}, 
    {"role": "assistant", "content": "IK Boys Hr. Sec. School(Sanyogita ganj chhawni) ka email id hai- ikboysschool@gmail.com "},
    {"role": "user", "content": "IK Boys Hr. Sec. School(Sanyogita ganj chhawni) ka contact number kya hai?"}, 
    {"role": "assistant", "content": "IK Boys Hr. Sec. School(Sanyogita ganj chhawni) ka contact number hai- 0731-2701777"},
    {"role": "user", "content": "IK Girls Hr. Sec. School (Ushaganj, Chhawni) ka email id kya hai?"}, 
    {"role": "assistant", "content": "IK Girls Hr. Sec. School (Ushaganj, Chhawni) ka email id hai- info@ikcollegeindore.org"},
    {"role": "user", "content": "IK Girls Hr. Sec. School (Ushaganj, Chhawni) ka contact number kya hai?"}, 
    {"role": "assistant", "content": "IK Girls Hr. Sec. School (Ushaganj, Chhawni) ka contact number hai- +91-731-2565112, 2560234"},
    {"role": "user", "content": "St. Mustafa Raza High School (Azad Nagar) ka email id kya hai?"}, 
    {"role": "assistant", "content": "St. Mustafa Raza High School (Azad Nagar) ka email id hai- IKstmustufarazaschool@gmail.com"},
    {"role": "user", "content": "St. Mustafa Raza High School (Azad Nagar) ka contact number kya hai?"}, 
    {"role": "assistant", "content": "St. Mustafa Raza High School (Azad Nagar) ka contact number hai- +91-9907557585"},
    {"role": "user", "content": "IK Sky Height International Prep School ka email id kya hai?"}, 
    {"role": "assistant", "content": "IK Sky Height International Prep School ka email id hai- Ikskyheightsinternationalschool@gmail.com"},
    {"role": "user", "content": "IK Sky Height International Prep School ka contact number kya hai?"}, 
    {"role": "assistant", "content": "IK Sky Height International Prep School ka contact number hai- +91-9171099929,+91-9171099930"},
    {"role": "user", "content": "IK Coaching classes ka email id kya hai?"}, 
    {"role": "assistant", "content": "IK Coaching classes ka email id hai- iksocietyoffice@gmail.com"},
    {"role": "user", "content": "IK Coaching classes ka contact number kya hai?"}, 
    {"role": "assistant", "content": "IK Coaching classes ka contact number hai- 0731-2701777, 0731-2705781"},
    {"role": "user", "content": "IK Sky Height International Prep School ka address kya hai?"}, 
    {"role": "assistant", "content": "IK Sky Height International Prep School ka address hai 2/2, Opposite Greater kailash Nursing Home,new palasia,indore."},
    {"role": "user", "content": "IK Coaching classes ka address kya hai?"}, 
    {"role": "assistant", "content": "IK Coaching classes ka address hai Sanyogitaganj chawni, Indore"},
    {"role": "user", "content": "St. Mustafa Raza High School (Azad Nagar) ka address kya hai?"}, 
    {"role": "assistant", "content": "St. Mustafa Raza High School (Azad Nagar) ka address hai Kohinoor Colony, Azad Nagar, Indore (M.P.)"},
    {"role": "user", "content": "IK Girls Hr. Sec. School (Ushaganj, Chhawni) ka address kya hai?"}, 
    {"role": "assistant", "content": "IK Girls Hr. Sec. School (Ushaganj, Chhawni) ka address hai 14/1, Ushaganj Main Road, Jaora Compound, Indore (M.P.)"},
    {"role": "user", "content": "IK Boys Hr. Sec. School(Sanyogita ganj chhawni) ka address kya hai?"}, 
    {"role": "assistant", "content": "IK Boys Hr. Sec. School(Sanyogita ganj chhawni) ka address hai Sanyogita Ganj, Chhawni, Indore (M.P.)"},
    {"role": "user", "content": "St. Umar Academy CBSE ka address kya hai?"}, 
    {"role": "assistant", "content": "St. Umar Academy CBSE ka address hai- 325/5/10 &325/4/3 Khajrana Near bypass, Indore (M.P.) Opposite Patel Hospital"},
    {"role": "user", "content": "St. Umar Hr. Sec. School English Medium ka address kya hai?"}, 
    {"role": "assistant", "content": "St. Umar Hr. Sec. School English Medium ka address hai 2/2, Opposite Greater kailash Nursing Home,new palasia,indore."},
    {"role": "user", "content": "Islamia Technical and vocational institute ka address kya hai?"}, 
    {"role": "assistant", "content": "Islamia Technical and vocational institute ka address hai 2/2, Opposite Greater kailash Nursing Home,new palasia,indore."},
    {"role": "user", "content": "Islamia Private ITI(sanyogitaganj, chhawni) ka address kya hai?"}, 
    {"role": "assistant", "content": "Islamia Private ITI(sanyogitaganj, chhawni)ka address hai- 16/4, Sharddhanand Marg, Chhawani Hat Maidan, Indore (M.P.)"},
    {"role": "user", "content": "Islamia institute of computer science and management, indore ka address kya hai?"}, 
    {"role": "assistant", "content": "Islamia institute of computer science and management, indore ka address hai 2/2, Opposite Greater kailash Nursing Home,new palasia,indore."},
    {"role": "user", "content": "Islamia Karimia BAB girls college (Ushaganj) ka address kya hai?"}, 
    {"role": "assistant", "content": "Islamia Karimia BAB girls college (Ushaganj) ka address hai 14/1, Ushaganj, Chawni, Indore (M.P.)"},
    {"role": "user", "content": "Islamia Karimia College (Palasia) indore ka address kya hai?"}, 
    {"role": "assistant", "content": "Islamia Karimia College (Palasia) ka address hai 2/2, Opposite Greater kailash Nursing Home,new palasia,indore."},
    {"role": "user", "content": "What are the Undergraduate courses available in IK College palasia?"},
    {"role": "assistant", "content": "Islamia Karimia College (IK College) in Palasia, Indore, offers a variety of undergraduate courses across different streams. For More information you can visit official website."},
    

]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    try:
        print(f"Received prompt: {data['prompt']}")  # Debugging line
        
        # Include the few-shot examples in the prompt
        messages = few_shot_examples.copy()
        messages.append({"role": "user", "content": data['prompt']})
        
        completion = openai.ChatCompletion.create(
            model=model_id,
            temperature=0.1,  # Adjusting temperature for less randomness
            messages=messages
        )
        
        response = completion.choices[0].message["content"]
        print(f"Model response: {response}")  # Debugging line
        return jsonify({"response": response})

    except Exception as e:
        print(f"Error: {e}")  # Debugging line
        return jsonify({"response": f"Error: {e}"})
    
@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        user_query = request.json['query']
        if user_query.strip() == "":
            return jsonify({"response": "Please provide a valid query."}), 400
        
        prompt = f"User: {user_query}\nAssistant:"
        response = openai.Completion.create(
            model=model_id,
            prompt=prompt,
            max_tokens=150
        )
        
        assistant_response = response['choices'][0]['text'].strip()
        return jsonify({"response": assistant_response})
    else:
        return jsonify({"error": "Method not allowed."}), 405

if __name__ == '__main__':
    app.run(debug=True)
