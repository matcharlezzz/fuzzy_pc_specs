from membership import PCSpecsMembership
import inference_engine as ig
import defuzzifier as dfz
import recommender as rcm
import toJSON
import pprint

def ezpc(in_val1, in_val2, in_val3):
    pc = PCSpecsMembership()

    val1 = pc.budget(float(in_val1))
    print(in_val1, ":", val1)
    val2 = pc.workload(float(in_val2))
    print(in_val2, ":", val2)
    val3 = pc.storage(float(in_val3))
    print(in_val3, ":",val3)

    all_inputs = ig.input_combiner(val1, val2, val3)
    aggregate = dfz.aggregate(ig.ruleset, ig.output_sets, all_inputs, False)

    defuzz_out = dfz.defuzzy(aggregate, ig.output_xmid)
    defuzz_outV2 = dfz.defuzzyV2(aggregate)

    defuzz_list = [defuzz_out, defuzz_outV2]

    closest_defuzz = min(defuzz_list, key=lambda x:abs(x-(int(in_val1)/10000)))


    print(f'\nFinal PC Score: {closest_defuzz}')

    recos = rcm.recommendation(closest_defuzz)
    pprint.pprint(recos)

    toJSON.pack_dict(recos)

    return recos