import streamlit as st

# App title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Simple Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# Operation selection
operation = st.selectbox(
    "Select an operation",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

# Perform calculation
result = None
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (×)":
        result = num1 * num2
    elif operation == "Division (÷)":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Error: Division by zero is not allowed.")

    if result is not None:
        st.success(f"✅ Result: {result}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
