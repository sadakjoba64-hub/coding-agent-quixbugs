import  subprocess
import  sys
result = subprocess.run(
    [sys.executable, "-m", "pytest", "python_testcases/test_gcd.py"],
    cwd="QuixBugs",
    capture_output=True,
    text=True,
    timeout=10,
)
print(result.returncode)
print(result.stdout)

