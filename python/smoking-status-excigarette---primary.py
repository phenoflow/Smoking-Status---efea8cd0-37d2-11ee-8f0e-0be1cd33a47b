# Caroline Fairhurst, Ian Watt, Fabiola Martin, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"1372","system":"readv2"},{"code":"1373","system":"readv2"},{"code":"1374","system":"readv2"},{"code":"1375","system":"readv2"},{"code":"1376","system":"readv2"},{"code":"137J","system":"readv2"},{"code":"137M","system":"readv2"},{"code":"137O","system":"readv2"},{"code":"137P","system":"readv2"},{"code":"137X","system":"readv2"},{"code":"137Y","system":"readv2"},{"code":"137g","system":"readv2"},{"code":"137j","system":"readv2"},{"code":"137l","system":"readv2"},{"code":"EGTON1024","system":"readv2"},{"code":"EGTON1026","system":"readv2"},{"code":"EGTON1027","system":"readv2"},{"code":"EGTON321","system":"readv2"},{"code":"EGTON322","system":"readv2"},{"code":"EMISQDA1","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('smoking-status-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["smoking-status-excigarette---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["smoking-status-excigarette---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["smoking-status-excigarette---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
