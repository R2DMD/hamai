# Script version date 2026-01-28
import time
import whisper
from hamai_functions import *

profile_name = define_hamai_profile()

model = whisper.load_model("turbo")

while True:
	stt_file_path = get_next_file_from_pipeline("pipeline/stt",profile_name)
	if stt_file_path:
		start_time = time.time()
		#print(f"[STT] File found: {stt_file_path}")
				
		# Whisper call
		result = model.transcribe(stt_file_path, language="ru")
		
		# Check if anything valuable was decoded
		result_text = result["text"]
		result_text = result_text.strip()
		if not result_text or result_text=="Продолжение следует...":
			print(f"[STT] Empty file: {stt_file_path}")
			move_processed_file(stt_file_path)
			continue
		
		# Generate filename for GPT prompt file
		filename_with_extension = os.path.basename(stt_file_path)
		output_filename = os.path.splitext(filename_with_extension)[0]
		output_filename += ".txt"
		gpt_prompt_file_path = os.path.join("pipeline/gpt", output_filename)
		
		# Save text to GPT prompt file
		with open(gpt_prompt_file_path, "w") as gpt_prompt_file:
			gpt_prompt_file.write(result_text)
		
		# Moving processed STT file
		move_processed_file(stt_file_path)
		
		end_time = time.time()
		execution_time = end_time - start_time
		#print(f"[STT] Processing time: {execution_time:.6f} seconds")
		#print(f"[STT => GPT] File added: {gpt_prompt_file_path}")
		print(f"[STT] {stt_file_path} => {gpt_prompt_file_path} in {execution_time:.1f} seconds")
	time.sleep(0.1)
