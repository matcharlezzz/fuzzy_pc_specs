from membership import PCSpecsMembership
import inference_engine as ig
import defuzzifier as dfz
import recommender as rcm
import toJSON
import pprint

pc = PCSpecsMembership()


val_budget = input("Type number for Budget: ")
val1 = pc.budget(float(val_budget))
print(val1)
val = input("Type number for Workload: ")
val2 = pc.workload(float(val))
print(val2)
val = input("Type number for Storage: ")
val3 = pc.storage(float(val))
print(val3)


all_inputs = ig.input_combiner(val1, val2, val3)
aggregate = dfz.aggregate(ig.ruleset, ig.output_sets, all_inputs, False)

defuzz_out = dfz.defuzzy(aggregate, ig.output_xmid)
defuzz_outV2 = dfz.defuzzyV2(aggregate)

defuzz_list = [defuzz_out, defuzz_outV2]

closest_defuzz = min(defuzz_list, key=lambda x:abs(x-(int(val_budget)/10000)))


print(f'\nFinal PC Score: {closest_defuzz}')

recos = rcm.recommendation(closest_defuzz)
pprint.pprint(recos)

toJSON.pack_dict(recos)
