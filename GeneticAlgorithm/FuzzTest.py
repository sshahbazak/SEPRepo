import random
import itertools

def Fuzz_Test(drone_id, modes, throttle, states=None, GFACT=None):
    '''
    This function return - Mission state - Flying, Land, Disarm, Takeoff, Arm, Hover, ReceiveMission.
    GF - Yes, No
    GFPRED - Yes, No, None (only if GF is None)
    GFACT - Return mode, Hold mode, Warning, Land mode, None (Only if GF is None)
    KillSwitch - No
    Modes - POSCTL, STABILIZED, OFFBOARD, ALTCTL, AUTO.LOITER, AUTO.RTL, AUTO.LAND
    throttle - 0, 225, -100, 260, 600, 100, 550, 445, 435, 450, 615, 570, 300, None
    max_deviation - 0.009592 - 35.0130614 (regular normal distribution)
    max_altitude - 0.005654452 - 93.55165 (regular normal distribution)
    duration - 10 - 40178 (Normal distribution around 60 seconds)
    final_landing_state - True, False
    freefall_occurred - True, False
    mission_complete - True, False
    '''

    mission_states = states
    # ['Flying', 'Land', 'Disarm', 'Takeoff', 'Arm', 'Hover']
    GF = 'Yes' if GFACT else 'No'
    GFPRED = ['Yes', 'No'] if GFACT else None
    GFACT_states =  GFACT
    results = []

    if not GFACT:
        combinations = list(itertools.product(modes, mission_states, throttle))
        for mode, state, thr in combinations:
            result = {
                'mode': mode,
                'state': state,
                'throttle': thr,
                'GF': GF,
                'GFPRED': random.choice(GFPRED) if GFPRED else None,
                'GFACT': random.choice(GFACT_states) if GFACT_states else None,
                'KillSwitch': 'No',
                'max_deviation': random.uniform(0.009592, 35.0130614),
                'max_altitude': random.uniform(0.005654452, 93.55165),
                'duration': abs(int(random.gauss(60, 10))),
                'final_landing_state': random.choice([True, False]),
                'freefall_occurred': random.choice([True, False]),
                'mission_complete': random.choice([True, False]),
            }
            results.append(result)
    else:
        combinations = list(itertools.product(modes, GFACT_states, throttle))
        for mode, state, thr in combinations:
            result = {
                'mode': mode,
                'state': 'Flying',
                'throttle': thr,
                'GF': GF,
                'GFPRED': random.choice(GFPRED) if GFPRED else None,
                'GFACT': random.choice(GFACT_states) if GFACT_states else None,
                'KillSwitch': 'No',
                'max_deviation': random.uniform(0.009592, 35.0130614),
                'max_altitude': random.uniform(0.005654452, 93.55165),
                'duration': abs(int(random.gauss(60, 10))),
                'final_landing_state': random.choice([True, False]),
                'freefall_occurred': random.choice([True, False]),
                'mission_complete': random.choice([True, False]),
            }
            results.append(result)

    return results

# # Example call to the function
fuzz_test = Fuzz_Test(
    drone_id="Polkadot",
    modes=['POSCTL', 'OFFBOARD', 'STABILIZED'],
    states=['hover'],
    # GFACT=['Return mode', 'Hold mode'],
    throttle=[255, 600]
)

for res in fuzz_test:
    print(res)


