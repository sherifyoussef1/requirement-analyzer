ANALYZE_PROMPT = """You are a business analyst.
Analyze this software requirement:
{requirement}

Reply with JSON only, no other text, using exactly these keys:
"summary": short text
"missing_info": list of texts
"assumptions": list of texts
"questions": list of texts
"""
IMPROVE_PROMPT="""{requirement} and {analysis} 
Reply with JSON only, no other text, using exactly these keys:
"improved_requirement": text 
"acceptance_criteria"" list of texts"
"""
TESTS_PROMPT="""{improved}
Reply with JSON only, no other text, using exactly these keys:
"happy_path": list of short test descriptions
"validation": list of short test descriptions
"edge_cases": list of short test descriptions
"failures": list of short test descriptions
"""