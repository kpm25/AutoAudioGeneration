# AutoAudioGeneration

## Overview
This project contains scripts that can automatically generate audio files in MP3 format for word/sentence lists.
It will generate audio files for each word/sentence in the list and save them in the audio directory.

## Prerequisites
- Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Ensure `pydub` Can Handle Audio Files

To ensure `pydub` can handle audio files, you need to install `ffmpeg` on your system and add it to your system's PATH. Follow these steps:

### Install `ffmpeg` on Your System

#### Download and Install `ffmpeg`:
1. Go to the [FFmpeg download page](https://ffmpeg.org/download.html).
2. Download the appropriate version for your operating system.
3. Follow the installation instructions provided on the website.

#### Add `ffmpeg` to System PATH:
**Windows:**
1. Extract the downloaded `ffmpeg` zip file.
2. Copy the `bin` folder path (e.g., `C:\ffmpeg\bin`).
3. Open the Start Menu, search for "Environment Variables", and select "Edit the system environment variables".
4. In the System Properties window, click on the "Environment Variables" button.
5. In the Environment Variables window, find the "Path" variable in the "System variables" section and click "Edit".
6. Click "New" and paste the `bin` folder path.
7. Click "OK" to close all windows.

#### Verify Installation:
1. Open a new command prompt and type `ffmpeg -version` to verify that `ffmpeg` is correctly installed and accessible from the command line.

After completing these steps, the warning should no longer appear, and `pydub` should be able to use `ffmpeg` for audio processing.

## Setup

### 1. Clone the Repository
Clone the repository to your local machine using the following command:
```bash
git clone https://github.com/kpm25/AutoAudioGeneration.git
cd AutoAudioGeneration
```

2. Install Required Libraries
Run the following command to install the required libraries:


```bash
pip install -r requirements.txt
``` 

3. Run the Script
Run the following command to generate audio files:

```bash
python generate_audio.py
```

## Plan

- Extend support to include `.wav` file generation.
- Implement image generation to match the sounds.
- Enhance error handling and logging.
- Add more customization options for audio and image outputs.

   Usage
The script reads the word/sentence list from the data/words.txt file and generates audio files for each word/sentence in the list. The audio files are saved in the audio directory.  
License
This project is licensed under the MIT License - see the LICENSE file for details.
