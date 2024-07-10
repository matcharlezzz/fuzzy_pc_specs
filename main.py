from membership import PCSpecsMembership
import inference_engine as ig
import defuzzifier as dfz

pc = PCSpecsMembership()


val = input("Type number for Budget: ")
val1 = pc.budget(float(val))
print(val1)
val = input("Type number for Workload: ")
val2 = pc.workload(float(val))
print(val2)
val = input("Type number for Storage: ")
val3 = pc.storage(float(val))
print(val3)


all_inputs = ig.input_combiner(val1, val2, val3)
aggregate = dfz.aggregate(ig.ruleset, ig.output_sets, all_inputs)
defuzz_out = dfz.defuzzy(aggregate, ig.output_xmid)

print(f'Final PC Score: {defuzz_out}')
