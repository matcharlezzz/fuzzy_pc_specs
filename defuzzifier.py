#   activation is fuzzy conjunction of all rules/ membership degree of all rules
#   output_sets is the fuzzy disjunction/ maximum value of all activation in output membership

def aggregate(ruleset, output_sets, inputs, enable_weights=True):
    in_middle = 0

    for rule in ruleset:
        inp_budget, inp_workload, inp_storage, out_set = rule
        if enable_weights:
            if inputs['budget'][inp_budget][0] == 0.5 and in_middle == 0:
                inputs['budget'][inp_budget][0] += 0.3
                in_middle += 1
            elif inputs['budget'][inp_budget][0] == 0.5 and in_middle > 0:
                inputs['budget'][inp_budget][0] -= 0.35

        activation = min(inputs['budget'][inp_budget], inputs['workload'][inp_workload], inputs['storage'][inp_storage])
        output_sets[out_set] = max(output_sets[out_set], activation[0])

    return output_sets


def defuzzy(output_sets, output_xmid):
    defuzzified_output = sum(output_sets[key] * output_xmid[key] for key in output_sets.keys()) / sum(
        output_sets.values())

    return defuzzified_output
