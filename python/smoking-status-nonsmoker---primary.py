# Caroline Fairhurst, Ian Watt, Fabiola Martin, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"137-1","system":"readv2"},{"code":"1371-1","system":"readv2"},{"code":"1372-1","system":"readv2"},{"code":"1377","system":"readv2"},{"code":"137A","system":"readv2"},{"code":"137B","system":"readv2"},{"code":"137L","system":"readv2"},{"code":"137P-1","system":"readv2"},{"code":"137R","system":"readv2"},{"code":"137S","system":"readv2"},{"code":"13WF-1","system":"readv2"},{"code":"ASDFGNO1","system":"readv2"},{"code":"EGTON1025","system":"readv2"},{"code":"EGTON324","system":"readv2"},{"code":"EGTON326","system":"readv2"},{"code":"EGTON327","system":"readv2"},{"code":"EGTONGR13","system":"readv2"},{"code":"EMISNQPR396","system":"readv2"},{"code":"EMISQCO3","system":"readv2"},{"code":"EMISSMRE1","system":"readv2"},{"code":"PCSDT1DE9","system":"readv2"},{"code":"PCSDT1HE1","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('smoking-status-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["smoking-status-nonsmoker---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["smoking-status-nonsmoker---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["smoking-status-nonsmoker---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
