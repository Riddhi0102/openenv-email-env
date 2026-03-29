def grade_easy(state):
    if "1" in state.drafted_responses:
        return 1.0
    return 0.0


def grade_medium(state):
    score = 0

    if "1" in state.drafted_responses:
        score += 0.5

    if state.step_count <= 2:
        score += 0.5

    return score


def grade_hard(state):
    score = 0

    if "1" in state.drafted_responses:
        score += 0.3

    if state.step_count <= 2:
        score += 0.3

    if len(state.inbox) == 1:
        score += 0.4

    return score