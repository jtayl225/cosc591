import streamlit as st

def main():
    st.title("Pitch")
    
    st.radio("Select ear", ("right","left"))
    pitch = st.slider("Change Pitch:", 0, 100, 0)
    
    
if __name__ == "__main__":
    main()


