import streamlit as st

st.set_page_config(
    page_title="Audio Demonstration",
    page_icon="🔊",
)

def main():
    st.title("Audio Hearing Demonstration")
    
    st.sidebar.success("Select audio manipulation")
    
    st.markdown(
        """
## Project Aim

Develop software to teach the key ideas involved in directional hearing to middle high school students.

## Background

The ability of humans (and other animals) to identify the direction of a sound source in a transverse plane is due to having two ears. It is thought that the key factors in identifying direction are differences in L-R sound:

- Arrival time
- Volume
- Frequency content

That is, sound arriving from the left is received by the right ear delayed, at a lower volume and with reduced high-pitch content.

Localising sources from any direction (not necessarily in a transverse plane) involves the directional characteristics of each ear, mainly the pinna (outer ear).

Some types of sound are easier to locate (eg bird calls) than others (eg continuous tone).

The software will allow students to learn about these ideas.

### Project

Complete as many of the following tasks as would fit in the time:

1. Develop a design requirement, relating the requirements to educational purposes (directed instruction, directed experiment, self-directed experiment, game...?)
2. Compare alternative approaches to realizing the software (stand alone application, web-based...? waterfall, agile...?).
3. Implement the software
4. Test the software with a target group

The requirements are deliberately vague to give the COSC students scope for creativity.
        
        """

    )
    
if __name__ == "__main__":
    main()


