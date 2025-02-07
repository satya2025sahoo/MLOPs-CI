import streamlit as st

def main():
    st.title("Square Calculator")
    
    # Take integer input from user
    num = st.number_input("Enter an integer:", value=0, step=1, format="%d")
    
    # Calculate square
    square = num ** 2
    
    # Display result
    st.write(f"The square of {num} is {square}")

if __name__ == "__main__":
    main()
