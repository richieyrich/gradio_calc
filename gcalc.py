import gradio as gr

def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"

demo = gr.Interface(
    fn=calculator,
    inputs=["number", gr.Radio(["add", "subtract", "multiply", "divide"]), "number"],
    outputs=["number"],
    title="Simple Calculator",
    description="Perform basic arithmetic operations."
)

demo.launch()
