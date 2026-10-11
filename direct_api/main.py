import os
import json
from dotenv import load_dotenv
from google import genai
from prompts import ANALYZE_PROMPT
from prompts import IMPROVE_PROMPT
from prompts import TESTS_PROMPT

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
requirement = open("samples/input.txt").read()
prompt = ANALYZE_PROMPT.format(requirement=requirement)
reply = client.models.generate_content(
    model="gemini-3.8-flash", contents=prompt)  
#print(reply.text)

def parse_json(text):
    text = text.strip().removeprefix("```json").removeprefix("```").removesuffix("```")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        print("The AI did not return valid JSON:\n", text)
        raise SystemExit(1)
        
analysis = parse_json(reply.text)
print("Sum: ",analysis["summary"])

prompt = IMPROVE_PROMPT.format(
    requirement=requirement,
    analysis=json.dumps(analysis, indent=2))
reply = client.models.generate_content( model="gemini-3.8-flash", contents=prompt)
improved = parse_json(reply.text)
print(improved["improved_requirement"])

prompt = TESTS_PROMPT.format(improved=improved["improved_requirement"])
reply = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)
tests = parse_json(reply.text)
for group in ["happy_path", "validation", "edge_cases", "failures"]:
    print(group)
    for test in tests[group]:
        print(" -", test)