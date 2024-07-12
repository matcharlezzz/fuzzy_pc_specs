def input_combiner(inp_budget: dict, inp_workload: dict, inp_storage: dict) -> dict:
    inputs = {'budget': inp_budget, 'workload': inp_workload, 'storage': inp_storage}

    return inputs


# ruleset (budget, workload, storage, output)


ruleset = [
    ('budget', 'off', 'light', 'BF'),
    ('budget', 'off', 'everyday', 'BF'),
    ('budget', 'off', 'power', 'BF'),
    ('budget', 'lmt', 'light', 'BF'),
    ('budget', 'lmt', 'everyday', 'BF'),
    ('budget', 'lmt', 'power', 'BF'),
    ('budget', 'lgm', 'light', 'BF'),
    ('budget', 'lgm', 'everyday', 'BF'),
    ('budget', 'lgm', 'power', 'BF'),
    ('budget', 'hvy', 'light', 'NA'),
    ('budget', 'hvy', 'everyday', 'NA'),
    ('budget', 'hvy', 'power', 'NA'),

    ('entry', 'off', 'light', 'VF'),
    ('entry', 'off', 'everyday', 'VF'),
    ('entry', 'off', 'power', 'VF'),
    ('entry', 'lmt', 'light', 'VF'),
    ('entry', 'lmt', 'everyday', 'VF'),
    ('entry', 'lmt', 'power', 'VF'),
    ('entry', 'lgm', 'light', 'VF'),
    ('entry', 'lgm', 'everyday', 'VF'),
    ('entry', 'lgm', 'power', 'VF'),
    ('entry', 'hvy', 'light', 'BE'),
    ('entry', 'hvy', 'everyday', 'BE'),
    ('entry', 'hvy', 'power', 'BE'),

    ('entry_mid', 'off', 'light', 'VF'),
    ('entry_mid', 'off', 'everyday', 'VF'),
    ('entry_mid', 'off', 'power', 'VF'),
    ('entry_mid', 'lmt', 'light', 'VF'),
    ('entry_mid', 'lmt', 'everyday', 'BE'),
    ('entry_mid', 'lmt', 'power', 'BE'),
    ('entry_mid', 'lgm', 'light', 'BE'),
    ('entry_mid', 'lgm', 'everyday', 'BE'),
    ('entry_mid', 'lgm', 'power', 'BE'),
    ('entry_mid', 'hvy', 'light', 'BE'),
    ('entry_mid', 'hvy', 'everyday', 'BE'),
    ('entry_mid', 'hvy', 'power', 'BE'),

    ('mid', 'off', 'light', 'BE'),
    ('mid', 'off', 'everyday', 'BE'),
    ('mid', 'off', 'power', 'BE'),
    ('mid', 'lmt', 'light', 'BE'),
    ('mid', 'lmt', 'everyday', 'BE'),
    ('mid', 'lmt', 'power', 'BE'),
    ('mid', 'lgm', 'light', 'BE'),
    ('mid', 'lgm', 'everyday', 'AA'),
    ('mid', 'lgm', 'power', 'AA'),
    ('mid', 'hvy', 'light', 'AA'),
    ('mid', 'hvy', 'everyday', 'AE'),
    ('mid', 'hvy', 'power', 'AE'),

    ('mid_high', 'off', 'light', 'BE'),
    ('mid_high', 'off', 'everyday', 'BE'),
    ('mid_high', 'off', 'power', 'AA'),
    ('mid_high', 'lmt', 'light', 'AA'),
    ('mid_high', 'lmt', 'everyday', 'AA'),
    ('mid_high', 'lmt', 'power', 'AA'),
    ('mid_high', 'lgm', 'light', 'AE'),
    ('mid_high', 'lgm', 'everyday', 'AE'),
    ('mid_high', 'lgm', 'power', 'AE'),
    ('mid_high', 'hvy', 'light', 'AE'),
    ('mid_high', 'hvy', 'everyday', 'SP'),
    ('mid_high', 'hvy', 'power', 'SP'),

    ('high', 'off', 'light', 'AA'),
    ('high', 'off', 'everyday', 'AA'),
    ('high', 'off', 'power', 'AA'),
    ('high', 'lmt', 'light', 'AA'),
    ('high', 'lmt', 'everyday', 'AA'),
    ('high', 'lmt', 'power', 'SP'),
    ('high', 'lgm', 'light', 'SP'),
    ('high', 'lgm', 'everyday', 'SP'),
    ('high', 'lgm', 'power', 'SP'),
    ('high', 'hvy', 'light', 'PR'),
    ('high', 'hvy', 'everyday', 'PR'),
    ('high', 'hvy', 'power', 'EW'),

    ('very_high', 'off', 'light', 'AA'),
    ('very_high', 'off', 'everyday', 'AA'),
    ('very_high', 'off', 'power', 'SP'),
    ('very_high', 'lmt', 'light', 'SP'),
    ('very_high', 'lmt', 'everyday', 'SP'),
    ('very_high', 'lmt', 'power', 'SP'),
    ('very_high', 'lgm', 'light', 'SP'),
    ('very_high', 'lgm', 'everyday', 'PR'),
    ('very_high', 'lgm', 'power', 'PR'),
    ('very_high', 'hvy', 'light', 'EW'),
    ('very_high', 'hvy', 'everyday', 'EW'),
    ('very_high', 'hvy', 'power', 'EW')
]


output_sets = {
    'NA': 0,
    'BF': 0,
    'VF': 0,
    'BE': 0,
    'AA': 0,
    'AE': 0,
    'SP': 0,
    'PR': 0,
    'EW': 0
}

output_xmid = {
    'NA': 0,
    'BF': 1,
    'VF': 3,
    'BE': 4,
    'AA': 5,
    'AE': 6,
    'SP': 7,
    'PR': 8,
    'EW': 10
}

# test input
'''inputs = {
    'budget': {'budget': 0, 'entry': 0, 'entry_mid': 0.5, 'mid': 0.5, 'mid_high': 0, 'high': 0, 'very_high': 0},
    'workload': {'off': 0, 'lmt': 0, 'lgm': 0.33, 'hvy': 0.5},
    'storage': {'light': 0, 'everyday': 0.0, 'power': 1}
}'''





