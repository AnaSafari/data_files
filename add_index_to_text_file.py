#### AppData\Roaming\JetBrains\PyCharmCE2020.3\scratches>

with open('C:/Users/anahita.safari\Downloads\883\FB_Exports_2022-03-24T2213_cz4h5R_v4\dashboard-f&b_exports/order_state_transitions.csv') as infile, open('C:/Users/anahita.safari\Downloads\883\FB_Exports_2022-03-24T2213_cz4h5R_v4\dashboard-f&b_exports/order_state_transitions_.csv', 'w') as outfile:
    for idx, line in enumerate(infile):
        outfile.write(f'{idx},{line}')