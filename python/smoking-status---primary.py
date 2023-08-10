# Caroline Fairhurst, Ian Watt, Fabiola Martin, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"137V","system":"readv2"},{"code":"137f","system":"readv2"},{"code":"137k","system":"readv2"},{"code":"13p1","system":"readv2"},{"code":"13p2","system":"readv2"},{"code":"13p3","system":"readv2"},{"code":"13p4","system":"readv2"},{"code":"13p7","system":"readv2"},{"code":"EGTONSM2","system":"readv2"},{"code":"EGTONSM6","system":"readv2"},{"code":"EMISNQSM14","system":"readv2"},{"code":"EMISOTS1","system":"readv2"},{"code":"EMISQGR1","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('smoking-status-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["smoking-status---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["smoking-status---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["smoking-status---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
