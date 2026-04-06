from environment import HospitalEnv

def choose_action(env, state):
    patient = state["patients"][0]

    # SMART DECISION
    if patient["severity"] == "high":
        if env.beds["ICU"] > 0:
            bed_type = "ICU"
        else:
            bed_type = "normal"
    else:
        if env.beds["normal"] > 0:
            bed_type = "normal"
        else:
            bed_type = "ICU"

    return {
        "patient_id": patient["id"],
        "bed_type": bed_type
    }


def run_task(difficulty):
    env = HospitalEnv()
    state = env.reset(difficulty)

    done = False
    total_reward = 0
    steps = 0

    while not done and steps < 50:
        if len(state["patients"]) == 0:
            break

        action = choose_action(env, state)

        state, reward, done = env.step(action)
        total_reward += reward
        steps += 1

    max_reward = 20
    score = total_reward / max_reward

    return max(0.0, min(1.0, score))


if __name__ == "__main__":

    print("\nRunning all tasks...\n")

    easy = run_task("easy")
    print("EASY SCORE:", easy)

    medium = run_task("medium")
    print("MEDIUM SCORE:", medium)

    hard = run_task("hard")
    print("HARD SCORE:", hard)


# ✅ VERY IMPORTANT (leave one empty line above)
def run(task):
    return run_task(task["difficulty"])