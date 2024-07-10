#   activation is fuzzy conjunction of all rules/ membership degree of all rules
#   output_sets is the fuzzy disjunction/ maximum value of all activation in output membership

def aggregate(ruleset, output_sets, inputs):
    for rule in ruleset:
        inp_budget, inp_workload, inp_storage, out_set = rule
        activation = min(inputs['budget'][inp_budget], inputs['workload'][inp_workload], inputs['storage'][inp_storage])
        output_sets[out_set] = max(output_sets[out_set], activation[0])

    return output_sets


def defuzzy(output_sets, output_xmid):
    defuzzified_output = sum(output_sets[key] * output_xmid[key] for key in output_sets.keys()) / sum(
        output_sets.values())

    return defuzzified_output
