class EmergencyStateMachine:
    """
    Controls step-by-step emergency guidance.

    The assistant gives one instruction at a time
    and moves to the next step only after the
    current step is completed.
    """

    def __init__(self, emergency_type):

        self.emergency_type = emergency_type.upper()

        self.current_step = 0

        self.steps = self.get_steps()


    # ==========================================
    # EMERGENCY STEPS
    # ==========================================

    def get_steps(self):

        emergency_steps = {

            # ==================================
            # FIRE
            # ==================================

            "FIRE": [

                {
                    "instruction":
                    "Move away from the fire and smoke "
                    "if you can do so safely.",

                    "alternative":
                    "If you cannot move away safely, "
                    "stay as far from the fire and smoke "
                    "as possible and seek help."
                },

                {
                    "instruction":
                    "Move toward a safe exit if one is "
                    "available. Tell me when you are outside.",

                    "alternative":
                    "If an exit is blocked, do not force "
                    "your way through the danger. Look for "
                    "another safe exit if available."
                },

                {
                    "instruction":
                    "Stay away from the building and follow "
                    "instructions from emergency responders.",

                    "alternative":
                    "If you are already outside, remain at "
                    "a safe distance from the building."
                }
            ],


            # ==================================
            # FLOOD
            # ==================================

            "FLOOD": [

                {
                    "instruction":
                    "Move to a safer elevated location "
                    "away from floodwater.",

                    "alternative":
                    "If you cannot move safely, stay away "
                    "from moving water and seek help."
                },

                {
                    "instruction":
                    "Stay away from floodwater and electrical "
                    "equipment.",

                    "alternative":
                    "If electrical equipment is nearby, "
                    "move away from it if you can do so safely."
                },

                {
                    "instruction":
                    "Keep your phone with you and follow "
                    "official evacuation instructions.",

                    "alternative":
                    "If you receive an evacuation order, "
                    "follow the instructions of local authorities."
                }
            ],


            # ==================================
            # ROAD ACCIDENT
            # ==================================

            "ROAD ACCIDENT": [

                {
                    "instruction":
                    "Move away from ongoing traffic if you "
                    "can do so safely.",

                    "alternative":
                    "If you cannot move safely, stay where "
                    "you are if possible and seek help."
                },

                {
                    "instruction":
                    "Stay away from additional traffic danger "
                    "and avoid creating further danger.",

                    "alternative":
                    "Ask nearby people to keep a safe distance "
                    "from the accident area."
                },

                {
                    "instruction":
                    "Seek appropriate emergency assistance "
                    "if someone needs urgent help.",

                    "alternative":
                    "If you cannot contact emergency services, "
                    "ask a nearby person to do so."
                }
            ],


            # ==================================
            # MEDICAL
            # ==================================

            "MEDICAL": [

                {
                    "instruction":
                    "Stay in a safe place and remain as calm "
                    "as possible.",

                    "alternative":
                    "If you are not in a safe place, ask someone "
                    "nearby to help you reach one."
                },

                {
                    "instruction":
                    "Seek professional medical assistance "
                    "if it is needed.",

                    "alternative":
                    "If you cannot contact medical assistance "
                    "yourself, ask a nearby person for help."
                },

                {
                    "instruction":
                    "Follow instructions from trained medical "
                    "responders.",

                    "alternative":
                    "Continue listening to instructions from "
                    "emergency responders."
                }
            ],


            # ==================================
            # EARTHQUAKE
            # ==================================

            "EARTHQUAKE": [

                {
                    "instruction":
                    "Protect yourself from falling objects "
                    "and stay away from windows if possible.",

                    "alternative":
                    "If you cannot move immediately, protect "
                    "yourself from falling objects."
                },

                {
                    "instruction":
                    "After the shaking stops, stay alert "
                    "for possible aftershocks.",

                    "alternative":
                    "Avoid damaged or unstable structures "
                    "when it is safe to move."
                },

                {
                    "instruction":
                    "Follow instructions from local "
                    "emergency authorities.",

                    "alternative":
                    "Continue listening for official "
                    "emergency information."
                }
            ],


            # ==================================
            # HEATWAVE
            # ==================================

            "HEATWAVE": [

                {
                    "instruction":
                    "Move to a cool or well-ventilated place.",

                    "alternative":
                    "If you cannot reach a cooler place, "
                    "reduce exposure to extreme heat and seek help."
                },

                {
                    "instruction":
                    "Drink water regularly if you can "
                    "safely do so.",

                    "alternative":
                    "If you cannot access drinking water, "
                    "ask a nearby person for assistance."
                },

                {
                    "instruction":
                    "Avoid unnecessary strenuous activity "
                    "during extreme heat.",

                    "alternative":
                    "Rest in a cooler location and follow "
                    "local heat-health guidance."
                }
            ],


            # ==================================
            # CYCLONE / STORM
            # ==================================

            "CYCLONE / STORM": [

                {
                    "instruction":
                    "Move indoors and stay away from windows.",

                    "alternative":
                    "If you cannot get indoors safely, move "
                    "away from windows and unsecured objects."
                },

                {
                    "instruction":
                    "Follow official weather warnings and "
                    "stay in the safest available indoor area.",

                    "alternative":
                    "Continue listening for official instructions."
                },

                {
                    "instruction":
                    "Follow evacuation instructions from "
                    "local authorities.",

                    "alternative":
                    "If you cannot evacuate safely, seek help "
                    "from nearby people or emergency responders."
                ]
            ]
        }


        # ==========================================
        # DEFAULT EMERGENCY
        # ==========================================

        return emergency_steps.get(

            self.emergency_type,

            [

                {
                    "instruction":
                    "Move to a safer location if possible.",

                    "alternative":
                    "If you cannot move safely, stay where "
                    "you are and seek help."
                },

                {
                    "instruction":
                    "Follow official emergency instructions.",

                    "alternative":
                    "Continue listening for instructions "
                    "from emergency authorities."
                }
            ]
        )


    # ==========================================
    # CURRENT STEP
    # ==========================================

    def get_current_step(self):

        if self.current_step >= len(self.steps):

            return None

        return self.steps[self.current_step]


    # ==========================================
    # GET INSTRUCTION
    # ==========================================

    def get_instruction(self):

        step = self.get_current_step()

        if step is None:

            return None

        return step["instruction"]


    # ==========================================
    # GET ALTERNATIVE
    # ==========================================

    def get_alternative(self):

        step = self.get_current_step()

        if step is None:

            return None

        return step["alternative"]


    # ==========================================
    # COMPLETE STEP
    # ==========================================

    def mark_step_complete(self):

        if self.current_step < len(self.steps):

            self.current_step += 1


    # ==========================================
    # CHECK FINISHED
    # ==========================================

    def is_finished(self):

        return self.current_step >= len(self.steps)


    # ==========================================
    # PROGRESS
    # ==========================================

    def get_progress(self):

        return {

            "current_step":
                min(
                    self.current_step + 1,
                    len(self.steps)
                ),

            "total_steps":
                len(self.steps),

            "finished":
                self.is_finished()
        }
