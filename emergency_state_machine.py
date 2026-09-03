class EmergencyStateMachine:

    MEDICAL_CUT_STEPS = [
        {
            "instruction": (
                "First, grab any clean cloth or towel nearby and press down firmly on the cut "
                "to slow down and stop the bleeding. Hold it steady."
            ),
            "alternative": (
                "If you can't apply pressure yourself, ask anyone nearby to press down firmly "
                "for you, and try to keep your injured arm or leg raised up."
            )
        },
        {
            "instruction": (
                "Once the bleeding slows down, rinse the cut under clean running water, "
                "then cover it gently with a clean bandage or cloth."
            ),
            "alternative": (
                "If clean running water isn't nearby, keep it covered with a clean cloth "
                "and ask someone to take you to a clinic or pharmacy."
            )
        },
        {
            "instruction": (
                "Be sure to visit a pharmacy or clinic to ask if you need a tetanus shot, "
                "especially if the cut was dirty or caused by glass, metal, or a rusty object."
            ),
            "alternative": (
                "If you can't reach a clinic right now, ask a trusted friend or family member "
                "to help you get medical advice."
            )
        }
    ]

    MEDICAL_LABOR_STEPS = [
        {
            "instruction": (
                "Help the mother stay in a safe, comfortable position on her side, "
                "keep her warm, and stay right by her side."
            ),
            "alternative": (
                "If moving is too painful, keep her right where she is and ask someone "
                "nearby to stay with both of you."
            )
        },
        {
            "instruction": (
                "Call emergency medical services immediately and explain how fast contractions "
                "are coming, your exact location, and if there is any heavy bleeding."
            ),
            "alternative": (
                "If your phone isn't reaching them, ask someone nearby to call emergency services "
                "on speaker so you can follow the dispatcher's exact guidance."
            )
        },
        {
            "instruction": (
                "Stay calm, follow the emergency dispatcher's advice, and do not leave her alone."
            ),
            "alternative": (
                "If medical help is delayed, monitor her breathing and stay supportive. Tell "
                "responders immediately if anything changes."
            )
        }
    ]

    EMERGENCY_STEPS = {

        "FIRE": [
            {
                "instruction": (
                    "Stay low under any smoke and head immediately toward the nearest safe exit."
                ),
                "alternative": (
                    "If the exit is blocked, get into a room away from the fire, close the door, "
                    "seal cracks with cloth, and signal at a window for help."
                )
            },
            {
                "instruction": (
                    "Stay outside once you're clear, do not go back inside for anything, and "
                    "call the fire service."
                ),
                "alternative": (
                    "If you are stuck inside, stay near a floor window where air is cleaner "
                    "and shout or flash a light to alert responders."
                )
            },
            {
                "instruction": (
                    "Stay in a safe outdoor assembly area and follow instructions from firefighters."
                ),
                "alternative": (
                    "If firefighters haven't arrived, alert neighbors from a safe distance and call 112."
                )
            }
        ],

        "FLOOD": [
            {
                "instruction": (
                    "Move up to higher ground or a higher floor immediately without walking through moving water."
                ),
                "alternative": (
                    "If you can't reach higher ground safely, stay in the highest secure spot you can find "
                    "and signal for emergency help."
                )
            },
            {
                "instruction": (
                    "Stay completely away from floodwater and turn off main power if it is safe to reach."
                ),
                "alternative": (
                    "If power switches are near water, do not touch them. Stay elevated on dry furniture or stairs."
                )
            },
            {
                "instruction": (
                    "Keep your phone dry and ready, and wait for official evacuation instructions."
                ),
                "alternative": (
                    "If you feel unsafe waiting, contact emergency services with your exact location."
                )
            }
        ],

        "ROAD ACCIDENT": [
            {
                "instruction": (
                    "If you can move safely, step out of the path of traffic to the side of the road."
                ),
                "alternative": (
                    "If you are injured or trapped, stay still inside the vehicle and turn on hazard lights."
                )
            },
            {
                "instruction": (
                    "Do not move any severely injured person unless there is an immediate fire or traffic hazard."
                ),
                "alternative": (
                    "Keep injured people calm and warm where they are until paramedics arrive."
                )
            },
            {
                "instruction": (
                    "Call emergency services immediately with your location, road details, and number of injured."
                ),
                "alternative": (
                    "Ask any bystander or driver to call emergency services immediately."
                )
            }
        ],

        "MEDICAL": [
            {
                "instruction": (
                    "Rest in a comfortable, safe position and take deep, calm breaths."
                ),
                "alternative": (
                    "If you feel weak or faint, lie flat with your legs elevated slightly and ask someone nearby to stay with you."
                )
            },
            {
                "instruction": (
                    "Call emergency medical services or head to the nearest emergency room."
                ),
                "alternative": (
                    "Ask a family member, neighbor, or bystander to transport you or call for help."
                )
            },
            {
                "instruction": (
                    "Follow all instructions given by medical responders and keep someone informed of your location."
                ),
                "alternative": (
                    "Keep monitoring your symptoms carefully while waiting for assistance."
                )
            }
        ],

        "EARTHQUAKE": [
            {
                "instruction": (
                    "Drop to your hands and knees, take cover under a sturdy desk or table, and hold on tight."
                ),
                "alternative": (
                    "If no table is nearby, cover your head and neck with your arms away from glass and heavy objects."
                )
            },
            {
                "instruction": (
                    "Once the shaking stops completely, carefully walk outside into an open space away from buildings."
                ),
                "alternative": (
                    "If exits are blocked by debris, stay covered and shout or tap on pipes to signal rescuers."
                )
            },
            {
                "instruction": (
                    "Stay in the open space and prepare for possible aftershocks."
                ),
                "alternative": (
                    "If you are stuck inside, protect your head and call or text emergency contacts."
                )
            }
        ],

        "HEATWAVE": [
            {
                "instruction": (
                    "Move into a cool, shaded room or air-conditioned area immediately."
                ),
                "alternative": (
                    "If no air conditioning is available, sit near a fan, apply wet cloths to your skin, and open windows for breeze."
                )
            },
            {
                "instruction": (
                    "Sip cool water steadily to stay hydrated."
                ),
                "alternative": (
                    "If you don't have water nearby, ask someone to bring you water or a hydration solution."
                )
            },
            {
                "instruction": (
                    "Rest quietly and avoid any strenuous physical movement until you cool down."
                ),
                "alternative": (
                    "If you experience dizziness, confusion, or vomiting, call emergency medical help immediately."
                )
            }
        ],

        "CYCLONE / STORM": [
            {
                "instruction": (
                    "Go to an interior room without windows on the lowest floor of the building."
                ),
                "alternative": (
                    "If windows are nearby, stay under sturdy furniture and cover yourself with blankets or mattresses."
                )
            },
            {
                "instruction": (
                    "Listen to weather updates on your phone and do not go outside, even if the wind temporarily stops."
                ),
                "alternative": (
                    "If power/internet drops, stay sheltered until you hear local emergency sirens or announcements."
                )
            },
            {
                "instruction": (
                    "Remain indoors until official reports confirm the storm has completely passed."
                ),
                "alternative": (
                    "If your building takes severe structural damage, carefully move to a safer adjacent shelter."
                )
            }
        ]
    }

    def __init__(self, emergency_type, user_input=""):

        self.emergency_type = emergency_type.upper().strip()
        input_text = user_input.lower()

        if (
            self.emergency_type == "MEDICAL" and
            any(word in input_text for word in ("cut", "wound", "laceration"))
        ):
            self.steps = self.MEDICAL_CUT_STEPS
        elif (
            self.emergency_type == "MEDICAL" and
            any(word in input_text for word in (
                "pregnant", "pregrant", "pregnancy", "childbirth",
                "child birth", "giving birth", "labor", "labour",
                "contractions", "delivery"
            ))
        ):
            self.steps = self.MEDICAL_LABOR_STEPS
        elif self.emergency_type in self.EMERGENCY_STEPS:
            self.steps = self.EMERGENCY_STEPS[self.emergency_type]
        else:
            self.steps = [
                {
                    "instruction": (
                        "Move to a safer location if you can do so safely."
                    ),
                    "alternative": (
                        "If you cannot move safely, stay where you are "
                        "and seek help from a nearby trusted person."
                    )
                },
                {
                    "instruction": (
                        "Contact an appropriate emergency service "
                        "if the situation is dangerous."
                    ),
                    "alternative": (
                        "Ask a nearby trusted person to contact "
                        "emergency services for you."
                    )
                }
            ]

        self.current_step = 0

    def get_current_step(self):

        if self.is_finished():
            return None

        return self.steps[self.current_step]

    def get_instruction(self):

        step = self.get_current_step()

        if step is None:
            return "The emergency guidance is complete."

        return step["instruction"]

    def get_alternative(self):

        step = self.get_current_step()

        if step is None:
            return "There are no more alternative steps."

        return step["alternative"]

    def mark_step_complete(self):

        if not self.is_finished():
            self.current_step += 1

    def is_finished(self):

        return self.current_step >= len(self.steps)

    def get_progress(self):

        total_steps = len(self.steps)

        if total_steps == 0:
            return 100

        completed_steps = self.current_step

        return int(
            (completed_steps / total_steps) * 100
        )
