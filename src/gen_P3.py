from typing import List
import json

def load_json(filename):
    with open(filename, "r", encoding="utf8") as f:
        return json.load(f)

# Convert json puzzles into src and test files for synth to process
# js_puzzles = load_json("397puzzles.json")
js_puzzles = load_json("puzzles.json")

# create files for src code and test code, write out header info to them
f_src = open("src_gen_P3.py", "w", encoding="utf8")
f_src.write("from typing import List\n\n")
f_tst = open("test_gen_P3.py", "w", encoding="utf8")
f_tst.write("from typing import List\n")
f_tst.write("from src_gen_P3 import *\n\n")

# Enumerate through all the puzzle records in the json file, generate src and test code
for index, puzzle in enumerate(js_puzzles):
    # In the src file put the standard sat/sol/assert so sol has context of sat() and docstring.
    # Synth will mask functions in src and try to regenerate functionally equivalent from the context.
    # Synth will run the test code to see if it succeeded.

    # if no sol is provided for the sat problem, skip it, we can't use it
    if len(puzzle["sol_bodies"]) == 0:
        continue

    # Add the index # to the sat() and sol() functions
    sat_func = puzzle["sat"]
    sat_func = sat_func.replace("sat(", f"sat{index}(")
    f_src.write(sat_func)
    f_src.write("\n")
    sol_header = puzzle["sol_header"]
    sol_header = sol_header.replace("sol(", f"sol{index}(")
    f_src.write(sol_header)
    f_src.write("\n")

    f_src.write(puzzle["sol_docstring"])
    f_src.write("\n")

    # sol_body could have recursive calls, or calls to sat, fix them too
    sol_body = puzzle["sol_bodies"][0]

    if sol_body.find("sat(") != -1:
        print("sol_body has sat( in it", index)
        # print(sol_body, "\n")
        sol_body = sol_body.replace("sat(", f"sat{index}(")

    if sol_body.find("sol(") != -1:
        print("sol_body has sol( in it", index)
        sol_body = sol_body.replace("sol(", f"sol{index}(")

    f_src.write(sol_body)
    f_src.write("\n")
    f_src.write("assert sat" + str(index) + "(sol" + str(index) + "())\n\n")
    
    # In the test file write the test
    f_tst.write("def test" + str(index) + "():\n")
    f_tst.write("    assert sat" + str(index) + "(sol" + str(index) + "())\n\n")
    
f_src.close()
f_tst.close()
exit()
