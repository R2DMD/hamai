import os
import shutil
import time
import whisper

def get_first_file_os(directory_path):
    try:
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        if files:
            return os.path.join(directory_path, files[0])
        else:
            return None
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
        return None

def move_file(file_path):
	destination_file = os.path.join("processed/stt", os.path.basename(file_path))
	try:
		shutil.move(file_path, destination_file)
		#print(f"File '{file_path}' moved successfully to '{destination_file}'")
	except FileNotFoundError:
		print(f"Error: Source file '{file_path}' not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

model = whisper.load_model("turbo")

while True:
	first_file_path = get_first_file_os("pipeline/stt")
	if first_file_path:
		print(f"[STT] File found: {first_file_path}")
		
		start_time = time.time()
		
		# Whisper call
		result = model.transcribe(first_file_path, language="ru")
		
		# Saving output to pipeline
		filename_with_extension = os.path.basename(first_file_path)
		output_filename = os.path.splitext(filename_with_extension)[0]
		output_filename += ".txt"
		gpt_prompt_file_path = os.path.join("pipeline/gpt", output_filename)
		with open(gpt_prompt_file_path, "w") as gpt_prompt_file:
			gpt_prompt_file.write(result["text"])
		
		# Moving processed file
		move_file(first_file_path)
		
		end_time = time.time()
		execution_time = end_time - start_time
		print(f"[STT] Processing time: {execution_time:.6f} seconds")
		print(f"[STT] File added: {gpt_prompt_file_path}")

	time.sleep(0.5)
