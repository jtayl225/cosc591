import streamlit as st

def main():
    st.title("delay")
    
    st.radio("Select ear", ("right","left"))
    delay = st.slider("Change delay:", 0, 100, 0)
    
    
if __name__ == "__main__":
    main()


