import argparse
import math

def granularity_range_check(granularity):
    granularity = int(granularity)
    if granularity < 1 or granularity > 365:
        raise argparse.ArgumentTypeError('Granularity must be between 1 and 365.')
    return granularity

parser = argparse.ArgumentParser('Granular CnGR compounding calculator')
parser.add_argument(
    '--principal',
    type=float,
    help='The starting principal.',
    required=True)
parser.add_argument(
    '--expenses',
    type=float,
    help='The annual expenses, e.g. 87000.',
    required=True)
parser.add_argument(
    '--interest',
    type=float,
    help='The annual interest rate as a percentage, e.g. for 8.5% type "8.5".',
    required=True)
parser.add_argument(
    '--granularity',
    type=granularity_range_check,
    help='The granularity divider, the number of times to compound throughout the year. A value between 1 and 365. For examples, enter 12 for monthly, 365 for daily, or 4 for quarterly.',
    required=True
)
    

args = parser.parse_args()

# extract args
granularity = args.granularity
interest = args.interest
expenses = args.expenses
principal = args.principal

# transform e.g. 8.5 --> 1.085
interest_multiplier = (interest / 100) + 1

# take the n'th root of the interest for granular compounding per time period specified
granular_interest_multiplier = interest_multiplier ** (1 / granularity)
granular_expenses = expenses / granularity

print('Starting principal: {}'.format(principal))

granularity_mod_target = math.floor(granularity / 20)

for i in range(granularity):
    # Pay up first
    principal -= granular_expenses

    # Then apply interest
    principal *= granular_interest_multiplier

    # Suppress noisy output for granularity >= 20... only print out 20 time periods maximum, and always print out the last period
    if granularity < 20 or i % granularity_mod_target == 0 or i == (granularity - 1):
        print('Period {}: {}'.format(i, principal))

