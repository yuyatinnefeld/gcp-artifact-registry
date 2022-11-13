############### TEST My Packages 1 ###############

print(f"{'#'*10} TEST - My Packages 1 {'#'*10}")

import sys

from analytics_lib import analytics_lib_module_1, analytics_lib_module_2

print(f"{'*'*5} TEST - Analytics Module 1 {'*'*5}")
analytics_lib_module_1()

print(f"{'*'*5} TEST - Analytics Module 2 {'*'*5}")
analytics_lib_module_2()

############### TEST My Packages 2 ###############

print(f"{'#'*10} TEST - My Packages 2 {'#'*10}")

from frontend_lib import frontend_module_1, frontend_module_2

print(f"{'*'*5} TEST - Frontend Module 1 {'*'*5}")
frontend_module_1()

print(f"{'*'*5} TEST - Frontend Module 2 {'*'*5}")
frontend_module_2()