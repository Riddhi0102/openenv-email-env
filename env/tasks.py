from .models import Action


def easy(env):
    env.reset()
    env.step(Action(type="reply", email_id="1", content="ok"))
    return env.state()


def medium(env):
    env.reset()
    env.step(Action(type="reply", email_id="1", content="ok"))
    env.step(Action(type="reply", email_id="1", content="ok"))
    return env.state()


def hard(env):
    env.reset()
    env.step(Action(type="reply", email_id="1", content="ok"))
    env.step(Action(type="reply", email_id="1", content="ok"))
    env.step(Action(type="reply", email_id="1", content="ok"))
    return env.state()


def grade_easy(state):
    return 1.0 if len(state.get("sent_emails", [])) >= 1 else 0.0


def grade_medium(state):
    return 1.0 if len(state.get("sent_emails", [])) >= 2 else 0.0


def grade_hard(state):
    return 1.0 if len(state.get("sent_emails", [])) >= 3 else 0.0