# Script version date 2026-01-28
import glob
import os
import shutil
import sys

# Get and check profile name for current pipeline session
def define_hamai_profile():
	profile_name = ""
	if os.getenv('HAMAI_PROFILE') is not None and os.getenv('HAMAI_PROFILE') != "":
		profile_name = os.environ['HAMAI_PROFILE'] 
	else:
		print(f"[ERROR] The 'HAMAI_PROFILE' environment variable is not defined or empty!")
		sys.exit(1)
	
	if not os.path.isdir("profiles/" + profile_name):
		print(f"[ERROR] No profile directory found for profile '{profile_name}'")
		sys.exit(1)
	
	return profile_name

# Get next file from pipeline using path and profile name
def get_next_file_from_pipeline(directory_path,profile_name):
	path = directory_path + '/' + profile_name + '_*'
	try:
		files = glob.glob(path)
		if files:
			return files[0]
		else:
			return None
	except FileNotFoundError:
		print(f"Error: Directory '{directory_path}' not found.")
		return None

# Move file to processed directory # need to decode STT or other!!! move_to_processed
def move_file(file_path):
	destination_file = os.path.join("processed/stt", os.path.basename(file_path))
	try:
		shutil.move(file_path, destination_file)
		#print(f"File '{file_path}' moved successfully to '{destination_file}'")
	except FileNotFoundError:
		print(f"Error: Source file '{file_path}' not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

# Move processed file to processed directory
def move_processed_file(file_path):
	dirname = os.path.dirname(file_path)
	destination_file = ""
	match dirname:
		case "pipeline/rx":
			destination_file = os.path.join("processed/rx", os.path.basename(file_path))
		case "pipeline/stt":
			destination_file = os.path.join("processed/stt", os.path.basename(file_path))
		case "pipeline/gpt":
			destination_file = os.path.join("processed/gpt", os.path.basename(file_path))
		case "pipeline/tts":
			destination_file = os.path.join("processed/tts", os.path.basename(file_path))
		case "pipeline/tx":
			destination_file = os.path.join("processed/tx", os.path.basename(file_path))
		case _:
			print(f"An error encountered while moving processed file")
			sys.exit(1)
	
	try:
		shutil.move(file_path, destination_file)
		#print(f"File '{file_path}' moved successfully to '{destination_file}'")
	except FileNotFoundError:
		print(f"Error: Source file '{file_path}' not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

