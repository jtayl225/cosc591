import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import sys
sys.path.insert(0, './scripts')
from scripts import delay,pitch,volume
import wave
import io
import tempfile
import os
import soundfile as sf
import numpy as np
import sounddevice as sd
import librosa

################
# Global Parameters
################
audio_options = {
    "Drum Track":"drums_96k.wav",
    "Singer":"singer_96k.wav",
    "Thunder":"thunder_96k.wav"
}


#################
#Page
#################
st.set_page_config(
    page_title="Audio Workshop",
    page_icon="🔊",
    layout="wide"
)

def main():
    st.sidebar.success("Flick between Sections here!")
    st.title("Have you ever wondered how we locate a sound's origin?")


    st.markdown("The human auditory system is the sensory system for the sense of hearing and involves identifying the sound source as well as the location of sounds in the environment. Our minds determine where sound is coming from using multiple clues and some types of sound are easier to locate (eg: Bird calls) than others (eg. Continuous tone)")

    ###
    # DELAY SECTION
    ###
    st.header("Delay")
    st.markdown("The ear which sound hits first is a major indicator of the direction the sound came from. So the time delay between left and right ears is a major player. For example, if the sound hits your right ear first, the sound likely originated to the right of your body. If it hits both ears at the same time, it likely originated from directly in front or behind you.<br><br><b>Below you can play with the sound and change the delay.</b><br> Choose the sound you want to hear, and the time delay you want between your right and left ear. Notice that depending on the ear you choose to have a delay the sound appears to come from a different direction.",unsafe_allow_html=True)

    #interactive section
    col1, col2 = st.columns(2)

    with col1:
        delay_selected_ear = st.radio("Pick an ear", ("left", "right"))

    with col2:
        delay_selected_sound = st.selectbox("Choose a sound:", list(audio_options.keys()))

    # Add slider to select delay
    format_dict = {
        0.0: "no delay",
        1.0: "large delay"
    }

    delay_selected_time = st.slider("Choose a delay:", 0.0, 0.75, 0.0, 0.01,format="%g seconds")
    #note that this function is simply called and does not actually play from memory. I dont know if this will work in the server
    delay.delay(ear=delay_selected_ear, file=audio_options[delay_selected_sound], delay_time=delay_selected_time)
    st.markdown("<b>Play Audio",unsafe_allow_html=True)
    st.audio("./data/audio/delay_overwrite.wav", format='audio/wav')


    st.header("Volume")


    st.header("Pitch")
    
    
    st.header("Explore them all")






if __name__ == "__main__":
    main()
