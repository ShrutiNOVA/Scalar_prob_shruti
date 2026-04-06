import gradio as gr

# Core logic
def review_code(code):
    code = str(code)

    issues = []
    suggestions = []

    if "currentValue" in code:
        issues.append("Unused variable detected: currentValue")
        suggestions.append("Remove or use the variable")

    if code.count("* 2") > 1:
        issues.append("Repeated computation detected")
        suggestions.append("Store computed value instead of repeating")

    if code.count("for(") >= 2:
        issues.append("Nested loops detected")
        suggestions.append("Try optimizing nested loops")

    if "* 2" in code:
        issues.append("Magic number detected (hardcoded value)")
        suggestions.append("Use a named variable instead")

    if not issues:
        return "✅ No issues found.\n🔥 Code Quality Score: 10/10"

    output = "🔥 Code Quality Score: {}/10\n\n".format(10 - len(issues)*2)
    output += "Detected issues:\n"

    for i in issues:
        output += f"- {i}\n"

    output += "\nSuggestions:\n"

    for s in suggestions:
        output += f"- {s}\n"

    return output

# UI
with gr.Blocks() as demo:
    gr.Markdown("# 🚀 Code Review AI")
    gr.Markdown("Analyze your code and get instant feedback")

    code_input = gr.Textbox(lines=15, label="Code")
    output = gr.Textbox(lines=15, label="AI Review")

    btn = gr.Button("Submit")
    btn.click(fn=review_code, inputs=code_input, outputs=output)

# Run app
if __name__ == "__main__":
    demo.launch()
