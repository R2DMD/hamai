# Script version date 2026-01-28
import requests
import json
import pickle
import time
from hamai_functions import *

def chat_with_ollama(model_name, messages):
    """
    Sends a chat request to the Ollama API and returns the model's response.

    Args:
        model_name (str): The name of the Ollama model to use (e.g., "llama3.2").
        messages (list): A list of message dictionaries, including 'role' and 'content'.
                         Example: [{"role": "user", "content": "Hello!"}]
    Returns:
        dict: The JSON response from the Ollama API.
    """
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model_name,
        "messages": messages,
        "stream": False  # Set to True for streaming responses
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama: {e}")
        return None

def write_chat_history(profile_name,chat_history_data):
	chat_history_filename = 'profiles/' + profile_name + '/' + 'ollama-chat-history.pkl'
	with open(chat_history_filename, 'wb') as f:
		pickle.dump(chat_history_data, f)
	
def read_chat_history(profile_name):
	profile_context_filename = 'profiles/' + profile_name + '/' + 'context.txt'
	chat_history_filename = 'profiles/' + profile_name + '/' + 'ollama-chat-history.pkl'
	chat_history = []
		
	if not os.path.exists(chat_history_filename):
		# Load contest as first message to chat_history
		with open(profile_context_filename, 'r') as context_file:
			profile_context = context_file.read()
		
		current_timestamp = time.time()
		chat_history.append({"role": "system", "content": profile_context, "time": current_timestamp})				
		# Save chat history
		with open(chat_history_filename, 'wb') as f:
			pickle.dump(chat_history, f)
	else:
		try:
			with open(chat_history_filename, 'rb') as f:
				while True:
					try:
						chat_history = pickle.load(f)
					except EOFError:
						break # Reached the end of the file
		except pickle.UnpicklingError as e:
			return None
		except Exception as e:
			return None
	
	#Exclude old messages
	for message in chat_history:
		if message['time'] < (time.time()- 300):
			chat_history.remove(message)

	return chat_history
	
if __name__ == "__main__":
	profile_name = define_hamai_profile()

	#model = "yandex/YandexGPT-5-Lite-8B-instruct-GGUF:latest"  # Replace with your desired Ollama model
	model = "gemma3:latest"
    # Initial message history
    #chat_history = []
	user_message = ""
    
	#print(chat_history)
	#user_input = input("Enter your input: ")
	#current_timestamp = time.time()
	#chat_history.append({"role": "user", "content": user_input, "time": current_timestamp})
	#write_chat_history(chat_history)
	#chat_history = read_chat_history(profile_name)
	#response_data = chat_with_ollama(model, chat_history)
	#print(response_data)
	#sys.exit()
	
	while True:
		gpt_file_path = get_next_file_from_pipeline("pipeline/gpt",profile_name)
		if gpt_file_path:
			#print(f"[GPT] File found: {gpt_file_path}")
			
			start_time = time.time()
		
			#read user message from file
			try:
				with open(gpt_file_path, 'r') as file:
					user_message = file.read()
				
				#print(f"[GPT] User message: {user_message}")

			except FileNotFoundError:
				print(f"Error: The file '{gpt_file_path}' was not found.")
			except Exception as e:
				print(f"An error occurred: {e}")
			#load history
			chat_history = read_chat_history(profile_name)
			
			#add user message to chat history and save
			current_timestamp = time.time()
			chat_history.append({"role": "user", "content": user_message, "time": current_timestamp})
			write_chat_history(profile_name,chat_history)
			#print(chat_history)
			
			#perform request to assistant

			response_data = chat_with_ollama(model, chat_history)

			if response_data and "message" in response_data:
				model_response = response_data["message"]["content"]
				#print(f"Ollama: {model_response}")
				# Add model's response to history
				current_timestamp = time.time()
				chat_history.append({"role": "assistant", "content": model_response, "time": current_timestamp})
				write_chat_history(profile_name,chat_history)
				
				# Saving output to pipeline
				filename_with_extension = os.path.basename(gpt_file_path)
				output_filename = os.path.splitext(filename_with_extension)[0]
				output_filename += ".txt"
				tts_prompt_file_path = os.path.join("pipeline/tts", output_filename)
				with open(tts_prompt_file_path, "w") as tts_prompt_file:
					tts_prompt_file.write(model_response)
				
				# Moving processed file
				move_processed_file(gpt_file_path)
				
				end_time = time.time()
				execution_time = end_time - start_time
				#print(f"[GPT] Processing time: {execution_time:.6f} seconds")
				#print(f"[GPT] File added: {tts_prompt_file_path}")
				print(f"[GPT] {gpt_file_path} => {tts_prompt_file_path} in {execution_time:.1f} seconds")
			else:
				print("Ollama: I'm sorry, I couldn't get a response.")
		
		time.sleep(0.1)
