#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ********************
# import libraries
# ********************
import streamlit as st
import numpy as np
import wave
import io
from netCDF4 import Dataset # to read Spatially Oriented Format for Acoustics (SOFA) files

# ********************
# define functions
# ********************
def count_channels(wave_file):
    # Open the WAV file
    with wave.open(wave_file, 'rb') as wf:
        # Get the number of channels
        nchannels = wf.getnchannels()
    return nchannels

def wave_to_float_array(wave_file):
    """
    Reads a WAV file and converts it to a numpy float array.
    
    Args:
        wave_file: The path to the WAV file.
        
    Returns:
        A numpy float array representing the audio data.
    """
    # Open the WAV file
    with wave.open(wave_file, 'rb') as wf:
        # Get the number of channels and sample width
        nchannels = wf.getnchannels()
        sample_width = wf.getsampwidth()
        
        # Read all the audio data as a byte string
        data = wf.readframes(wf.getnframes())
        
    # Convert the byte string to a numpy array
    dtype_map = {1: np.int8, 2: np.int16, 4: np.int32}
    data_type = dtype_map[sample_width]
    array = np.frombuffer(data, dtype=data_type)
    
    # Convert the array to a float array
    max_val = np.iinfo(data_type).max
    array = array.astype(np.float32) / max_val
    
    # Reshape the array to have nchannels columns
    array = array.reshape(-1, nchannels)
    
    return array

def float_array_to_wave(array, sample_rate=44100, nchannels=1, sample_width=2):
    """
    Writes a numpy float array to a WAV file.
    
    Args:
        array: The numpy float array to write.
        sample_rate: The sample rate of the audio data (default 44100 Hz).
        nchannels: The number of channels (default 1).
        sample_width: The sample width in bytes (default 2).
    """
    # Scale the float array to the range [-1, 1]
    array = np.clip(array, -1, 1)
    max_val = np.iinfo(np.int16).max
    array = (array * max_val).astype(np.int16)
    
    # Reshape the array to have nchannels columns
    array = array.reshape(-1, nchannels)
    
    return array.tobytes()

def convolve_mono(audio_array, hrir_left, hrir_right):
    # left
    audio_left = audio_array[:,0]
    left = np.convolve(audio_left, hrir_left, mode='same')

    # right
    audio_right = audio_array[:,0]
    right = np.convolve(audio_right, hrir_right, mode='same')

    # convert to wave
    float_array = np.column_stack((left, right))
    stereo_audio = float_array_to_wave(array = float_array,
                                       sample_rate = 44100,
                                       nchannels = 2,
                                       sample_width = 2)
    
    return stereo_audio

def convolve_stereo(audio_array, hrir_left, hrir_right):
    # left
    audio_left = audio_array[:,0]
    left = np.convolve(audio_left, hrir_left, mode='same')

    # right
    audio_right = audio_array[:,1]
    right = np.convolve(audio_right, hrir_right, mode='same')

    # convert to wave
    float_array = np.column_stack((left, right))
    stereo_audio = float_array_to_wave(array = float_array,
                                       sample_rate = 44100,
                                       nchannels = 2,
                                       sample_width = 2)
    
    return stereo_audio
        
# ********************
# streamlit dashboard
# ********************
tab1, tab2 = st.tabs(["Introduction", "Experiment"])

with tab1:
   pass

with tab2:
   st.title("Directional Hearing")
   st.header("Head-Related Transfer Functions (HRTF)")

   st.header("Audio Input")

   col1, col2 = st.columns(2)

   with col1:
      audio_selection = st.radio(label = 'Select Input Audio',
                                 options = ['Sine Wave', 'Drum Track', 'Other'],
                                 horizontal = True)


   with col2:
      hrir_selection = st.radio(label = 'Select Head Related Impulse Response (HRIR)',
                                 options = ['Subject 1', 'Subject 2', 'Subject 3'],
                                 horizontal = True)
   
   # read HRIR from .sofa file
   if hrir_selection == 'Subject 1':
       sofa_file_name = 'Subject1_HRIRs.sofa'
   elif hrir_selection == 'Subject 2':
       sofa_file_name = 'Subject44_HRIRs.sofa'
   elif hrir_selection == 'Subject 3':
       sofa_file_name = 'Subject1_HRIRs.sofa'
   else:
       sofa_file_name = 'Subject1_HRIRs.sofa'
       
   sofa_data = Dataset(sofa_file_name, 'r', format='NETCDF4')

   # I think HRIR data set have left and right the wrong way around, so I flipped the index
   HRIRs_l = np.squeeze(sofa_data['Data.IR'][:, 1, :]) # [:, 0, :]
   HRIRs_r = np.squeeze(sofa_data['Data.IR'][:, 0, :]) # [:, 1, :]
   Az, El, R = np.squeeze(np.hsplit(sofa_data['SourcePosition'][:], 3))
   # fs = sofa_data['Data.SamplingRate'][:][0]    
    
   # Add a slider for azimuth angle
   st.header("Parameters")
   col1, col2 = st.columns(2)

   with col1:
      azimuth = st.select_slider(label = "Azimuth angle (degrees)",
                                 options = [*range(0,360,5)],
                                 value = 0)


   with col2:
      elevation = st.select_slider(label = "Elevation angle (degrees)",
                                   options = [-57, -30, -15, 0, 15, 30, 45, 60, 75],
                                   value = 0)

   # Find the index of the measurement position that corresponds to the desired azimuth and elevation
   mp_indices = np.where((Az == azimuth) & (El == elevation))[0]

   if len(mp_indices) == 0:
       raise ValueError(f"No measurement position found for azimuth={azimuth} and elevation={elevation}")
   elif len(mp_indices) > 1:
       raise ValueError(f"Multiple measurement positions found for azimuth={azimuth} and elevation={elevation}")
   index = mp_indices[0]
   print(index)

   # define wave file name based on user selection
   if audio_selection == 'Sine Wave':
       audio_file = 'sine.wav'
   elif audio_selection == 'Drum Track':
       audio_file = 'drums.wav'
   else:
       audio_file = 'drums.wav'
   
   # get number of channels from wave file
   n_channels = count_channels(wave_file = audio_file)

   # read wave file and convert to float array
   audio_array = wave_to_float_array(wave_file = audio_file)

   if n_channels == 1:
      audio_data = convolve_mono(audio_array = audio_array,
                    hrir_left = HRIRs_l[index,:],
                    hrir_right = HRIRs_r[index,:])  
   elif n_channels == 2:
      audio_data = convolve_stereo(audio_array = audio_array,
                      hrir_left = HRIRs_l[index,:],
                      hrir_right = HRIRs_r[index,:])  

   st.header("Play Audio")

   # Save the modified audio as a wave file in memory
   with io.BytesIO() as buffer:
       with wave.open(buffer, "wb") as wave_file:
           wave_file.setframerate(44100)
           wave_file.setnchannels(2)
           wave_file.setsampwidth(2)
           wave_file.writeframes(audio_data)

       # Get the wave file data as a byte string
       buffer.seek(0)
       wave_data = buffer.read()

   st.audio(wave_data, format='audio/wav')


