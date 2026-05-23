from typing import Tuple, Dict
import dotenv
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
EXCHANGERATE_API_KEY = os.getenv('EXCHANGERATE_API_KEY')


def get_exchange_rate(base: str, target: str, amount: str) -> Tuple:
    """Return a tuple of (base, target, amount, conversion_result (2 decimal places))"""
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGERATE_API_KEY}/pair/{base}/{target}/{amount}"

    response = json.loads(requests.get(url).text)

    return(base, target, amount, f'{response["conversion_result"]:.3f}')


print(get_exchange_rate("USD", "GBP", "350"))    

def call_llm(textbox_input) -> Dict:
    """Make a call to the LLM with the textbox_input as the prompt.
       The output from the LLM should be a JSON (dict) with the base, amount and target"""
    try:
        completion = ...
    except Exception as e:
        print(f"Exception {e} for {text}")
    else:
        return completion

def run_pipeline():
    """Based on textbox_input, determine if you need to use the tools (function calling) for the LLM.
    Call get_exchange_rate(...) if necessary"""

    if True: #tool_calls
        # Update this
        st.write(f'{base} {amount} is {target} {exchange_response["conversion_result"]:.2f}')

    elif True: #tools not used
        # Update this
        st.write(f"(Function calling not used) and response from the model")
    else:
        st.write("NotImplemented")

# import os
# import requests
# from typing import Tuple, Dict
# from dotenv import load_dotenv
#import streamlit as st  # Assuming you are using Streamlit based on st.write

# Load environment variables
# load_dotenv()
# EXCHANGERATE_API_KEY = os.getenv('EXCHANGERATE_API_KEY')

# def get_exchange_rate(base: str, target: str, amount: float) -> Tuple:
#     """Return a tuple of (base, target, amount, conversion_result (2 decimal places))"""
    
#     if not EXCHANGERATE_API_KEY:
#         raise ValueError("API Key is missing! Check your .env file setup.")
        
#     # Ensure amount is treated strictly as a float/number
#     amount_val = float(amount)
    
#     url = f"https://v6.exchangerate-api.com/v6/{EXCHANGERATE_API_KEY}/pair/{base}/{target}/{amount_val}"
    
#     # Safe request parsing using built-in .json()
#     res = requests.get(url)
#     response = res.json()
    
#     # Error checking: If the API failed, tell us exactly why
#     if response.get("result") == "error":
#         raise Exception(f"API Error: {response.get('error-type')}")
        
#     # Guard against missing keys seamlessly
#     if "conversion_result" not in response:
#         raise KeyError(f"Expected 'conversion_result' but received: {list(response.keys())}")
        
#     return (base, target, amount_val, round(response["conversion_result"], 2))


# # Test execution (Note: passed 350 as a number instead of a string)
# try:
#     print(get_exchange_rate("USD", "GBP", 350))    
# except Exception as e:
#     print(f"Error executing function: {e}")


# ==========================================
# LLM Pipeline Logic
# ==========================================

# def call_llm(textbox_input: str) -> Dict:
#     """Make a call to the LLM with the textbox_input as the prompt.
#        The output from the LLM should be a JSON (dict) with the base, amount and target"""
#     try:
#         # Placeholder for actual LLM SDK logic (OpenAI, Anthropic, etc.)
#         completion = {"base": "USD", "target": "GBP", "amount": 350} 
#     except Exception as e:
#         print(f"Exception {e} for {textbox_input}")
#         return {}
#     else:
#         return completion

# def run_pipeline(textbox_input: str):
#     """Based on textbox_input, determine if you need to use the tools (function calling) for the LLM.
#     Call get_exchange_rate(...) if necessary"""
    
#     # Example parsing logic from your LLM output
#     llm_response = call_llm(textbox_input)
    
#     if llm_response: # Mocking tool call structure
#         base = llm_response.get("base")
#         target = llm_response.get("target")
#         amount = llm_response.get("amount")
        
#         # Call your fixed function
#         b, t, amt, result = get_exchange_rate(base, target, amount)
        
#         # Update your UI string output
#         st.write(f'{b} {amt} is {t} {result:.2f}')

#     else: # tools not used
#         st.write("(Function calling not used) and response from the model")