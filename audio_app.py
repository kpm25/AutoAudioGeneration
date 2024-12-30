import os
from gtts import gTTS
from gtts.tts import gTTSError
from pydub import AudioSegment


# Function to display accent menu and get user input
def select_accent():
    print("Select an accent:")
    print("1. British English")
    print("2. Australian English")
    print("3. Indian English")
    print("4. American English")
    choice = input("Enter your choice (1/2/3/4): ").strip()
    return choice


# Map user choice to tld values
accent_map = {
    '1': 'co.uk',
    '2': 'com.au',
    '3': 'co.in',
    '4': 'com'
}


# Function to display menu and get user input
def display_menu():
    print("Select an option:")
    print("1. Use default sound prefixes, which is 'sound', followed by a number")
    print("2. Use image names as mp3 filenames")
    print("3. Change the prefix")
    print("4. Use image names as mp3 filenames, but with words separated by '_' characters")
    print("5. Merge all sound files into one")
    choice = input("Enter your choice (1/2/3/4/5): ").strip()
    return choice


# Function to clean the sounds directory
def clean_sounds_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


# Function to merge all sound files into one
# Define the global pause duration
PAUSE_DURATION_MS = 1000


def merge_sounds(directory, output_file, pause_duration=PAUSE_DURATION_MS):
    combined = AudioSegment.empty()
    pause = AudioSegment.silent(duration=pause_duration)

    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.mp3'):
            sound = AudioSegment.from_mp3(os.path.join(directory, filename))
            combined += sound + pause

    combined.export(output_file, format="mp3")
    print(f"Merged file saved as: {output_file}")


# Prompt user to enter the directory path
directory = input("Enter the directory path containing image files: ").strip()

# Validate the directory
if not os.path.exists(directory):
    print(f"Directory does not exist: {directory}")
    exit()
else:
    print(f"Directory exists: {directory}")


# Function to display file type menu and get user input
def select_file_type():
    print("Select the file type to process:")
    print("1. PNG files (.png)")
    print("2. JPG files (.jpg)")
    print("3. GIF files (.gif)")
    choice = input("Enter your choice (1/2/3): ").strip()
    return choice


# Map user choice to file extensions
file_type_map = {
    '1': '.png',
    '2': '.jpg',
    '3': '.gif'
}

# Display file type menu and get user choice
file_type_choice = select_file_type()

# Validate choice and get corresponding file extension
if file_type_choice in file_type_map:
    file_extension = file_type_map[file_type_choice]
else:
    print("Invalid choice, exiting program.")
    exit()

# Ensure all files in the directory match the selected file type
for f in os.listdir(directory):
    if not f.endswith(file_extension):
        print(
            f"Non-{file_extension} file found: {f}, exiting program. Please ensure all files in the directory are {file_extension} files.")
        exit()

print(f"All files in the directory are {file_extension} files, proceeding to generate sound files.")

# List of words (filenames without extensions)
words = [os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith(file_extension)]

# Display menu and get user choice
choice = display_menu()

# Set prefix and use_prefix based on user choice
if choice == '1':
    prefix = "sound"
    use_prefix = True
    use_underscore = False
elif choice == '2':
    use_prefix = False
    use_underscore = False
elif choice == '3':
    prefix = input("Enter the new prefix: ").strip()
    use_prefix = True
    use_underscore = False
elif choice == '4':
    use_prefix = False
    use_underscore = True
elif choice == '5':
    # Merge all sound files into one
    sounds_directory = "sounds"
    merged_sounds_directory = "MergedSounds"
    os.makedirs(sounds_directory, exist_ok=True)
    os.makedirs(merged_sounds_directory, exist_ok=True)
    folder_name = os.path.basename(os.path.normpath(directory))
    print("Select an option for the merged file name:")
    print("1. Use default folder name")
    print("2. Enter a custom name")
    name_choice = input("Enter your choice (1/2): ").strip()
    if name_choice == '1':
        custom_name = folder_name
    elif name_choice == '2':
        custom_name = input("Enter the custom name: ").strip()
    else:
        print("Invalid choice, using default folder name.")
        custom_name = folder_name
    output_file = os.path.join(merged_sounds_directory, f"{custom_name}.mp3")
    merge_sounds(sounds_directory, output_file)
    exit()
else:
    print("Invalid choice, exiting program.")
    exit()

# Directory to save files
sounds_directory = "sounds"
os.makedirs(sounds_directory, exist_ok=True)

# Warning and user confirmation
print(f"Warning: This will clear all files in the '{sounds_directory}' directory.")
confirmation = input("Do you want to continue? (yes/no): ").strip().lower()

if confirmation == 'yes':
    # Clean the sounds directory
    clean_sounds_directory(sounds_directory)
    print(f"Cleared the '{sounds_directory}' directory.")
else:
    print("Exiting program, as operation cancelled.")
    exit()

# Display accent menu and get user choice
accent_choice = select_accent()

# Validate choice and get corresponding tld
if accent_choice in accent_map:
    tld = accent_map[accent_choice]
else:
    print("Invalid choice, using default accent (British English).")
    tld = 'co.uk'

# Generate new sound files
for i, word in enumerate(words, 1):
    try:
        tts = gTTS(text=word, lang='en', tld=tld)
        if use_prefix:
            filename = f"{sounds_directory}/{prefix}{i}.mp3"
        elif use_underscore:
            filename = f"{sounds_directory}/{word.replace(' ', '_')}.mp3"
        else:
            filename = f"{sounds_directory}/{word}.mp3"
        tts.save(filename)
        print(f"Generated: {filename}")
    except gTTSError as e:
        print(f"Failed to generate audio for '{word}': {e}")
