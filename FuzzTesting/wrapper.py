# from Fuzz import FuzzTestor as ft

# fuzz_testor = ft.Fuzz_Testor()
# fuzz_test = ft.Fuzz_Test(drone_id="Polkadot",
# modes=['OFFBOARD'],
# # states=['BriarWaypoint2'],
# geofence=[1, 2, 3, 4, 5],
# throttle=[1, 2, 3, 4, 5]
# )
# fuzz_testor.run_test(fuzz_test)

# import subprocess

# def run_original_script():
#     try:
#         subprocess.run(["python", "original_script.py"], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error running original script: {e}")

# if __name__ == "__main__":
#     run_original_script()


# from Fuzz import FuzzTestor as ft

# fuzz_testor = ft.Fuzz_Testor()
# fuzz_test = ft.Fuzz_Test(drone_id="Polkadot",
# modes=['OFFBOARD'],
# # states=['BriarWaypoint2'],
# geofence=[1, 2, 3, 4, 5],
# throttle=[1, 2, 3, 4, 5]
# )
# fuzz_testor.run_test(fuzz_test)


import subprocess

def run_fuzz_test():
    # Call the fuzz_test_script.py using subprocess
    result = subprocess.run(["python", "original_script.py"], text=True)
    return result

if __name__ == "__main__":
    result = run_fuzz_test()
    if result.returncode == 0:
        print("Fuzz test ran successfully.")
        print(result.stdout)
    else:
        print("Fuzz test failed.")
        print(result.stderr)
