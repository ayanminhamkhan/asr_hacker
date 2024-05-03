import gradio as gr
import os
import wave
import numpy as np
import scipy.io.wavfile as wav

# Function to save the audio file to the specified directory with a specified filename
def save_audio(audio_path, save_path):
    try:
        # Read the audio file from the given path
        sample_rate, data = wav.read(audio_path)  # Read audio from given path

        # Ensure the directory exists, create it if not
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Save the audio in WAV format
        with wave.open(save_path, 'wb') as wav_file:
            wav_file.setnchannels(1 if len(data.shape) == 1 else data.shape[1])
            wav_file.setsampwidth(2)  # Default 16-bit PCM (2 bytes per sample)
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(data.tobytes())
        
        return f"Audio saved to: {save_path}"
    
    except Exception as e:
        return f"Error while saving audio: {str(e)}"

# Gradio components for audio recording and path input
audio_input = gr.Audio(source="microphone", type="filepath", label="Record your audio")
path_input = gr.Textbox(label="Enter the path to save the audio (including filename and extension)")

# Interface for Gradio
interface = gr.Interface(
    fn=save_audio,
    inputs=[audio_input, path_input],
    outputs="text",
    description="Record audio and save it to a specified directory with a given filename",
)

# Launch the Gradio interface
interface.launch()

