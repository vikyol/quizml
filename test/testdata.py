quiz_model_base = "@quiz this is a sample quiz\n"\
                    "@desc multi-choice quiz to to demonstrate qml\n"\
                    "@tags test\n"

model_mc_q1 = quiz_model_base + "\n"\
                "? This is the first question\n"\
                "+ True\n"\
                "- False"

model_mc_q2_ = model_mc_q1 + "\n"\
                "? This is the first question\n"\
                "+ True\n"\
                "- False"


model_mc_invalid_no_question = quiz_model_base + "\n"\
                                "+ True\n"\
                                "- False"

model_mc_invalid_single_choice = quiz_model_base + "\n"\
                                "? This is the first question\n"\
                                "+ True\n"
