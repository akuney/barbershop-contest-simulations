import numpy, operator
from collections import Counter

from data import *

input_data = prelims_2016
num_trials = 1000
num_simulations = 1



def compute_summary_data(input_data):
	summary_data = {}

	for qtet_name in input_data:
		summary_data[qtet_name] = {}
		summary_data[qtet_name]['mean'] = numpy.mean(input_data[qtet_name])
		summary_data[qtet_name]['std'] = numpy.std(input_data[qtet_name]) * 1.5
		# summary_data[qtet_name]['std'] = 2

		# multiply by 1.5 for quartet
		# just hardcode the stdev for choruses, b/c they only sing 2 songs
	return summary_data

def compute_contest_results(input_data, summary_data):
	simulated_scores = {}
	contest_results = {qtet_name: [] for qtet_name in input_data.keys()}

	for i in range(num_trials):
		simulated_scores[i] = {}

		for qtet_name in summary_data:
			mean = summary_data[qtet_name]['mean']
			std = summary_data[qtet_name]['std']

			simulated_score = 0
			for j in range(num_simulations):
				simulated_score = simulated_score + mean + (std * numpy.random.randn())
			simulated_score = simulated_score / 6.0
			simulated_scores[i][qtet_name] = simulated_score

		sorted_result = sorted(
			simulated_scores[i].items(), key=operator.itemgetter(1), reverse=True
		)

		for qtet_result in sorted_result:
			qtet_name = qtet_result[0]
			placement = sorted_result.index(qtet_result) + 1
			contest_results[qtet_name].append(placement)

	return contest_results

summary_data = compute_summary_data(input_data)
contest_results = compute_contest_results(input_data, summary_data)

for qtet_name in contest_results:
	print qtet_name
	placements = Counter(contest_results[qtet_name])
	print sum(i[1] for i in placements.items() if i[0] < 6)
	print sum(i[1] for i in placements.items() if i[0] < 2)
	# print sorted(placements.items(), key=operator.itemgetter(0))

