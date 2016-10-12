quiz_model_base = "@quiz this is a sample quiz\n"\
                    "@desc multi-choice quiz to to demonstrate qml\n"\
                    "@tags test, tag with spaces, other\n"


model_mc_q1 = quiz_model_base + "\n"\
                "? This is the first question\n"\
                "+ True\n"\
                "- False"

model_mc_q2 = model_mc_q1 + "\n"\
                "? This is the second question\n"\
                "+ False\n"\
                "- True"


model_invalid_no_question = quiz_model_base + "\n"\
                                "+ True\n"\
                                "- False"

model_mc_invalid_single_choice = quiz_model_base + "\n"\
                                "? This is the first question\n"\
                                "+ True\n"


model_dnd_q1 = quiz_model_base + "\n"\
                "? Sweden\n"\
                "+ Stockholm"
