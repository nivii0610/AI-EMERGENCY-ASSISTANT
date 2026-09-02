import tkinter as tk
from tkinter import messagebox

from semantic_search import find_similar_emergency
from severity_detector import detect_severity
from response_generator import get_emergency_response
from emergency_actions import get_actions
from alert_system import generate_alert
from emergency_logger import log_emergency
from voice_input import get_voice_input
from dashboard import show_dashboard

def voice_input_gui():

    text = get_voice_input()

    if text:
        emergency_text.delete("1.0", tk.END)
        emergency_text.insert(tk.END, text)


def analyze_emergency():

    user_input = emergency_text.get("1.0", tk.END).strip()
    location = location_entry.get().strip()

    if not user_input:
        messagebox.showwarning(
            "Missing Information",
            "Please describe your emergency."
        )
        return

    if not location:
        location = "Location not provided"

    # AI detection
    emergency, similarity = find_similar_emergency(user_input)

    # Severity detection
    severity = detect_severity(user_input, similarity)

    # Display emergency
    emergency_result.config(
        text=f"Detected Emergency: {emergency}"
    )

    similarity_result.config(
        text=f"AI Similarity Score: {similarity:.2f}"
    )

    severity_result.config(
        text=f"Severity: {severity}"
    )

    # Get response
    response = get_emergency_response(emergency)

    actions = get_actions(emergency)

    # Safety guidance
    guidance_box.delete("1.0", tk.END)

    for point in response["guidance"]:
        guidance_box.insert(tk.END, "• " + point + "\n")

    # Safety actions
    actions_box.delete("1.0", tk.END)

    for action in actions:
        actions_box.insert(tk.END, "→ " + action + "\n")

    # Alert
    generate_alert(
        emergency,
        severity,
        user_input,
        location
    )

    # Save record
    log_emergency(
        emergency,
        severity,
        user_input,
        location,
        similarity
    )


# ==============================
# MAIN WINDOW
# ==============================

window = tk.Tk()

window.title("AI Emergency Assistant")
window.geometry("800x700")

title = tk.Label(
    window,
    text="🚨 AI EMERGENCY ASSISTANT",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)


# Emergency description

tk.Label(
    window,
    text="Describe your emergency:",
    font=("Arial", 14)
).pack()

emergency_text = tk.Text(
    window,
    height=5,
    width=70
)

emergency_text.pack(pady=10)


# Location

tk.Label(
    window,
    text="📍 Location:",
    font=("Arial", 14)
).pack()

location_entry = tk.Entry(
    window,
    width=60
)

location_entry.pack(pady=10)


# Analyze button
voice_button = tk.Button(
    window,
    text="🎤 SPEAK EMERGENCY",
    font=("Arial", 13, "bold"),
    command=voice_input_gui
)

voice_button.pack(pady=10)

analyze_button = tk.Button(
    window,
    text="🚨 ANALYZE EMERGENCY",
    font=("Arial", 14, "bold"),
    command=analyze_emergency
)

analyze_button.pack(pady=15)


# Results

emergency_result = tk.Label(
    window,
    text="Detected Emergency: --",
    font=("Arial", 14, "bold")
)

emergency_result.pack(pady=5)


similarity_result = tk.Label(
    window,
    text="AI Similarity Score: --",
    font=("Arial", 12)
)

similarity_result.pack(pady=5)


severity_result = tk.Label(
    window,
    text="Severity: --",
    font=("Arial", 14, "bold")
)

severity_result.pack(pady=5)


# Guidance

tk.Label(
    window,
    text="📚 Safety Guidance",
    font=("Arial", 14, "bold")
).pack(pady=10)

guidance_box = tk.Text(
    window,
    height=7,
    width=75
)

guidance_box.pack()


# Actions

tk.Label(
    window,
    text="⚠️ Immediate Safety Actions",
    font=("Arial", 14, "bold")
).pack(pady=10)

actions_box = tk.Text(
    window,
    height=7,
    width=75
)
dashboard_button = tk.Button(
    window,
    text="📊 VIEW EMERGENCY DASHBOARD",
    font=("Arial", 13, "bold"),
    command=show_dashboard
)

dashboard_button.pack(pady=15)

actions_box.pack()


window.mainloop()