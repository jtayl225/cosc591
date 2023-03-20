import streamlit as st

def main():
    st.title("Volume")
    
    st.radio("Select ear", ("right","left"))
    volume = st.slider("Change volume:", 0, 100, 0)
    
    
if __name__ == "__main__":
    main()


