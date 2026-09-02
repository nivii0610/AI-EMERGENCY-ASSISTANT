import tkinter as tk
import csv
import os
from collections import Counter

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


FILE_NAME = "emergency_logs.csv"


def load_records():
    """Load emergency records from the CSV file."""

    records = []

    if not os.path.exists(FILE_NAME):
        return records

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    return records


def create_emergency_chart(records, dashboard):
    """Create a bar chart showing emergency types."""

    emergency_types = []

    for row in records:
        emergency_types.append(row["Emergency"])

    counts = Counter(emergency_types)

    if not counts:
        return

    figure = Figure(figsize=(7, 4))
    axis = figure.add_subplot(111)

    axis.bar(
        list(counts.keys()),
        list(counts.values())
    )

    axis.set_title("Emergency Types Detected")
    axis.set_xlabel("Emergency Type")
    axis.set_ylabel("Number of Cases")

    axis.tick_params(axis="x", rotation=30)

    figure.tight_layout()

    chart = FigureCanvasTkAgg(
        figure,
        master=dashboard
    )

    chart.draw()

    chart.get_tk_widget().pack(
        pady=15
    )


def show_dashboard():

    records = load_records()

    critical = 0
    medium = 0
    low = 0

    for row in records:

        severity = row.get("Severity", "").upper()

        if severity == "CRITICAL":
            critical += 1

        elif severity == "MEDIUM":
            medium += 1

        elif severity == "LOW":
            low += 1

    # Create dashboard window
    dashboard = tk.Toplevel()

    dashboard.title("Emergency Dashboard")
    dashboard.geometry("950x850")

    # Title
    title = tk.Label(
        dashboard,
        text="🚨 EMERGENCY DASHBOARD",
        font=("Arial", 24, "bold")
    )

    title.pack(pady=20)

    # Statistics
    stats = tk.Label(
        dashboard,
        text=(
            f"🔴 CRITICAL: {critical}     "
            f"🟡 MEDIUM: {medium}     "
            f"🟢 LOW: {low}"
        ),
        font=("Arial", 16, "bold")
    )

    stats.pack(pady=10)

    # Total emergencies
    total = tk.Label(
        dashboard,
        text=f"Total Emergencies: {len(records)}",
        font=("Arial", 14)
    )

    total.pack(pady=5)

    # History title
    history_title = tk.Label(
        dashboard,
        text="📋 Recent Emergency History",
        font=("Arial", 16, "bold")
    )

    history_title.pack(pady=10)

    # History box
    history = tk.Text(
        dashboard,
        width=110,
        height=15,
        font=("Arial", 10)
    )

    history.pack(
        padx=20,
        pady=5
    )

    if not records:

        history.insert(
            tk.END,
            "No emergency records found."
        )

    else:

        # Show newest records first
        for row in reversed(records[-10:]):

            history.insert(
                tk.END,
                f"Date: {row.get('Date', 'N/A')}   "
                f"Time: {row.get('Time', 'N/A')}\n"
            )

            history.insert(
                tk.END,
                f"Emergency: {row.get('Emergency', 'N/A')}   "
                f"Severity: {row.get('Severity', 'N/A')}\n"
            )

            history.insert(
                tk.END,
                f"Location: {row.get('Location', 'N/A')}\n"
            )

            history.insert(
                tk.END,
                f"Description: {row.get('Description', 'N/A')}\n"
            )

            history.insert(
                tk.END,
                f"Similarity Score: "
                f"{row.get('Similarity Score', 'N/A')}\n"
            )

            history.insert(
                tk.END,
                "-" * 90 + "\n"
            )

    history.config(state=tk.DISABLED)

    # Create chart
    create_emergency_chart(
        records,
        dashboard
    )