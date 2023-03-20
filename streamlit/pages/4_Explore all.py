import streamlit as st

def main():
    st.title("Free roam")
    
    st.radio("Select ear", ("right","left"))

    delay = st.slider("Select delay:", 0, 100, 0)
    pitch = st.slider("Select Pitch:", 0, 100, 0)
    volume = st.slider("Select volume:", 0, 100, 0)


    
if __name__ == "__main__":
    main()


