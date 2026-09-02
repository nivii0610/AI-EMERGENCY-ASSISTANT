import csv
import os
from datetime import datetime


# ==========================================
# LOG FILE
# ==========================================

FILE_NAME = "emergency_logs.csv"


# ==========================================
# SAVE EMERGENCY RECORD
# ==========================================

def log_emergency(
    emergency,
    severity,
    description,
    location,
    similarity
):

    file_exists = os.path.exists(FILE_NAME)


    # ==========================================
    # OPEN LOG FILE
    # ==========================================

    with open(
        FILE_NAME,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)


        # ==========================================
        # CREATE HEADER
        # ==========================================

        if not file_exists:

            writer.writerow([
                "Date",
                "Time",
                "Emergency",
                "Severity",
                "Description",
                "Location",
                "Similarity Score"
            ])


        # ==========================================
        # CURRENT DATE & TIME
        # ==========================================

        now = datetime.now()


        # ==========================================
        # SAVE RECORD
        # ==========================================

        writer.writerow([

            now.strftime("%Y-%m-%d"),

            now.strftime("%H:%M:%S"),

            emergency,

            severity,

            description,

            location,

            round(similarity, 2)

        ])


    print(
        "\n💾 Emergency record saved successfully."
    )