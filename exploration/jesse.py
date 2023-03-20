# ********************
# import libraries
# ********************
import pyaudio
import wave

# ********************
# define functions
# ********************
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    # If len(data) is less than requested frame_count, PyAudio automatically
    # assumes the stream is finished, and the stream stops.
    return (data, pyaudio.paContinue)

# ********************
# play audio (wave file)
# ********************
file_name = 'sine.wav'
wf = wave.open(file_name, 'rb')
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                frames_per_buffer=1024,
                stream_callback=callback)

# Wait for stream to finish (4)
while stream.is_active():
    pass # time.sleep(0.1)

# stop
stream.stop_stream()

# Close the stream (5)
stream.close()

# Release PortAudio system resources (6)
p.terminate()

# close wave file
wf.close()
