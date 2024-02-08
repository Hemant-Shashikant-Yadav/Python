import wave

def get_wav_info(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        # Get audio properties
        channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        frame_rate = wav_file.getframerate()
        frames = wav_file.getnframes()
        compression_type = wav_file.getcomptype()  # Compression type (if any)
        sample_format = f'{sample_width * 8}bit PCM'  # Sample format

        # Calculate duration
        duration = frames / float(frame_rate)

        # Get additional information
        params = wav_file.getparams()
        sample_count = params.nframes
        audio_format = wav_file.getsampwidth()  # Sample width in bytes

    return {
        'channels': channels,
        'sample_width': sample_width,
        'frame_rate': frame_rate,
        'duration': duration,
        'sample_format': sample_format,
        'compression_type': compression_type,
        'sample_count': sample_count,
        'audio_format': audio_format
    }

file_path = 'audacityTesting.wav'

wav_info = get_wav_info(file_path)

# Print the information
print("Channels:", wav_info['channels'])
print("Sample Width:", wav_info['sample_width'])
print("Frame Rate:", wav_info['frame_rate'])
print("Duration:", wav_info['duration'], "seconds")
print("Sample Format:", wav_info['sample_format'])
print("Compression Type:", wav_info['compression_type'])
print("Sample Count:", wav_info['sample_count'])
print("Audio Format:", wav_info['audio_format'])
