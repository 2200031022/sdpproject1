import random
from datetime import datetime, timedelta

random_int_0_to_5 = random.randrange(0, 6)
random_int_5_to_9 = random.randrange(5, 10)
random_int_0_to_10_step_3 = random.randrange(0, 11, 3)

start_date = datetime.now() - timedelta(days=365)
end_date = datetime.now()
random_date = start_date + timedelta(days=random.randrange((end_date - start_date).days))

print("Random Integer between 0 and 5:", random_int_0_to_5)
print("Random Integer between 5 and 9:", random_int_5_to_9)
print("Random Integer between 0 and 10 with step of 3:", random_int_0_to_10_step_3)
print("Random Date between", start_date.date(), "and", end_date.date(), ":", random_date.date())