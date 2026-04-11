def task_easy(env):
    env.reset()
    return env.state()


def task_medium(env):
    env.reset()
    return env.state()


def task_hard(env):
    env.reset()
    return env.state()


def grade_easy(state):
    sent = state.get("sent_emails", [])
    return 1.0 if len(sent) >= 1 else 0.0


def grade_medium(state):
    sent = state.get("sent_emails", [])
    return 1.0 if len(sent) >= 2 else 0.0


def grade_hard(state):
    sent = state.get("sent_emails", [])
    return 1.0 if len(sent) >= 3 else 0.0