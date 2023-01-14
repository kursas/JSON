import json
from pprint import pprint
file = open("states.json")
data = json.load(file)
print(data)
pprint(data)
for item in data["states"]:
  print(f'states names:{item["name"]} and states abbreviations:{item["abbreviation"]}')
  print(item['area_codes'])
  for j in range(len(item['area_codes'])):
      value=item['area_codes'][j]
      print(f'saraso elemento numeris{j}-saraso elementas:{value}')
      if j==6:
          print(f'tai saraso reiksme:{value}- o saraso numeris:{j},o statas yra:{item["name"]}')
          
#output
{'states': [{'name': 'Alabama', 'abbreviation': 'AL', 'area_codes': ['205', '251', '256', '334', '938']}, {'name': 'Alaska', 'abbreviation': 'AK', 'area_codes': ['907']}, {'name': 'Arizona', 'abbreviation': 'AZ', 'area_codes': ['480', '520', '602', '623', '928']}, {'name': 'Arkansas', 'abbreviation': 'AR', 'area_codes': ['479', '501', '870']}, {'name': 'California', 'abbreviation': 'CA', 'area_codes': ['209', '213', '310', '323', '408', '415', '424', '442', '510', '530', '559', '562', '619', '626', '628', '650', '657', '661', '669', '707', '714', '747', '760', '805', '818', '831', '858', '909', '916', '925', '949', '951']}, {'name': 'Colorado', 'abbreviation': 'CO', 'area_codes': ['303', '719', '720', '970']}, {'name': 'Connecticut', 'abbreviation': 'CT', 'area_codes': ['203', '475', '860', '959']}, {'name': 'Delaware', 'abbreviation': 'DE', 'area_codes': ['302']}, {'name': 'Florida', 'abbreviation': 'FL', 'area_codes': ['239', '305', '321', '352', '386', '407', '561', '727', '754', '772', '786', '813', '850', '863', '904', '941', '954']}, {'name': 'Georgia', 'abbreviation': 'GA', 'area_codes': ['229', '404', '470', '478', '678', '706', '762', '770', '912']}, {'name': 'Hawaii', 'abbreviation': 'HI', 'area_codes': ['808']}, {'name': 'Idaho', 'abbreviation': 'ID', 'area_codes': ['208']}, {'name': 'Illinois', 'abbreviation': 'IL', 'area_codes': ['217', '224', '309', '312', '331', '618', '630', '708', '773', '779', '815', '847', '872']}, {'name': 'Indiana', 'abbreviation': 'IN', 'area_codes': ['219', '260', '317', '463', '574', '765', '812', '930']}, {'name': 'Iowa', 'abbreviation': 'IA', 'area_codes': ['319', '515', '563', '641', '712']}, {'name': 'Kansas', 'abbreviation': 'KS', 'area_codes': ['316', '620', '785', '913']}, {'name': 'Kentucky', 'abbreviation': 'KY', 'area_codes': ['270', '364', '502', '606', '859']}, {'name': 'Louisiana', 'abbreviation': 'LA', 'area_codes': ['225', '318', '337', '504', '985']}, {'name': 'Maine', 'abbreviation': 'ME', 'area_codes': ['207']}, {'name': 'Maryland', 'abbreviation': 'MD', 'area_codes': ['240', '301', '410', '443', '667']}, {'name': 'Massachusetts', 'abbreviation': 'MA', 'area_codes': ['339', '351', '413', '508', '617', '774', '781', '857', '978']}, {'name': 'Michigan', 'abbreviation': 'MI', 'area_codes': ['231', '248', '269', '313', '517', '586', '616', '734', '810', '906', '947', '989']}, {'name': 'Minnesota', 'abbreviation': 'MN', 'area_codes': ['218', '320', '507', '612', '651', '763', '952']}, {'name': 'Mississippi', 'abbreviation': 'MS', 'area_codes': ['228', '601', '662', '769']}, {'name': 'Missouri', 'abbreviation': 'MO', 'area_codes': ['314', '417', '573', '636', '660', '816']}, {'name': 'Montana', 'abbreviation': 'MT', 'area_codes': ['406']}, {'name': 'Nebraska', 'abbreviation': 'NE', 'area_codes': ['308', '402', '531']}, {'name': 'Nevada', 'abbreviation': 'NV', 'area_codes': ['702', '725', '775']}, {'name': 'New Hampshire', 'abbreviation': 'NH', 'area_codes': ['603']}, {'name': 'New Jersey', 'abbreviation': 'NJ', 'area_codes': ['201', '551', '609', '732', '848', '856', '862', '908', '973']}, {'name': 'New Mexico', 'abbreviation': 'NM', 'area_codes': ['505', '575']}, {'name': 'New York', 'abbreviation': 'NY', 'area_codes': ['212', '315', '332', '347', '516', '518', '585', '607', '631', '646', '680', '716', '718', '845', '914', '917', '929', '934']}, {'name': 'North Carolina', 'abbreviation': 'NC', 'area_codes': ['252', '336', '704', '743', '828', '910', '919', '980', '984']}, {'name': 'North Dakota', 'abbreviation': 'ND', 'area_codes': ['701']}, {'name': 'Ohio', 'abbreviation': 'OH', 'area_codes': ['216', '220', '234', '330', '380', '419', '440', '513', '567', '614', '740', '937']}, {'name': 'Oklahoma', 'abbreviation': 'OK', 'area_codes': ['405', '539', '580', '918']}, {'name': 'Oregon', 'abbreviation': 'OR', 'area_codes': ['458', '503', '541', '971']}, {'name': 'Pennsylvania', 'abbreviation': 'PA', 'area_codes': ['215', '267', '272', '412', '484', '570', '610', '717', '724', '814', '878']}, {'name': 'Rhode Island', 'abbreviation': 'RI', 'area_codes': ['401']}, {'name': 'South Carolina', 'abbreviation': 'SC', 'area_codes': ['803', '843', '854', '864']}, {'name': 'South Dakota', 'abbreviation': 'SD', 'area_codes': ['605']}, {'name': 'Tennessee', 'abbreviation': 'TN', 'area_codes': ['423', '615', '629', '731', '865', '901', '931']}, {'name': 'Texas', 'abbreviation': 'TX', 'area_codes': ['210', '214', '254', '281', '325', '346', '361', '409', '430', '432', '469', '512', '682', '713', '737', '806', '817', '830', '832', '903', '915', '936', '940', '956', '972', '979']}, {'name': 'Utah', 'abbreviation': 'UT', 'area_codes': ['385', '435', '801']}, {'name': 'Vermont', 'abbreviation': 'VT', 'area_codes': ['802']}, {'name': 'Virginia', 'abbreviation': 'VA', 'area_codes': ['276', '434', '540', '571', '703', '757', '804']}, {'name': 'Washington', 'abbreviation': 'WA', 'area_codes': ['206', '253', '360', '425', '509']}, {'name': 'West Virginia', 'abbreviation': 'WV', 'area_codes': ['304', '681']}, {'name': 'Wisconsin', 'abbreviation': 'WI', 'area_codes': ['262', '414', '534', '608', '715', '920']}, {'name': 'Wyoming', 'abbreviation': 'WY', 'area_codes': ['307']}]}
{'states': [{'abbreviation': 'AL',
             'area_codes': ['205', '251', '256', '334', '938'],
             'name': 'Alabama'},
            {'abbreviation': 'AK', 'area_codes': ['907'], 'name': 'Alaska'},
            {'abbreviation': 'AZ',
             'area_codes': ['480', '520', '602', '623', '928'],
             'name': 'Arizona'},
            {'abbreviation': 'AR',
             'area_codes': ['479', '501', '870'],
             'name': 'Arkansas'},
            {'abbreviation': 'CA',
             'area_codes': ['209',
                            '213',
                            '310',
                            '323',
                            '408',
                            '415',
                            '424',
                            '442',
                            '510',
                            '530',
                            '559',
                            '562',
                            '619',
                            '626',
                            '628',
                            '650',
                            '657',
                            '661',
                            '669',
                            '707',
                            '714',
                            '747',
                            '760',
                            '805',
                            '818',
                            '831',
                            '858',
                            '909',
                            '916',
                            '925',
                            '949',
                            '951'],
             'name': 'California'},
            {'abbreviation': 'CO',
             'area_codes': ['303', '719', '720', '970'],
             'name': 'Colorado'},
            {'abbreviation': 'CT',
             'area_codes': ['203', '475', '860', '959'],
             'name': 'Connecticut'},
            {'abbreviation': 'DE', 'area_codes': ['302'], 'name': 'Delaware'},
            {'abbreviation': 'FL',
             'area_codes': ['239',
                            '305',
                            '321',
                            '352',
                            '386',
                            '407',
                            '561',
                            '727',
                            '754',
                            '772',
                            '786',
                            '813',
                            '850',
                            '863',
                            '904',
                            '941',
                            '954'],
             'name': 'Florida'},
            {'abbreviation': 'GA',
             'area_codes': ['229',
                            '404',
                            '470',
                            '478',
                            '678',
                            '706',
                            '762',
                            '770',
                            '912'],
             'name': 'Georgia'},
            {'abbreviation': 'HI', 'area_codes': ['808'], 'name': 'Hawaii'},
            {'abbreviation': 'ID', 'area_codes': ['208'], 'name': 'Idaho'},
            {'abbreviation': 'IL',
             'area_codes': ['217',
                            '224',
                            '309',
                            '312',
                            '331',
                            '618',
                            '630',
                            '708',
                            '773',
                            '779',
                            '815',
                            '847',
                            '872'],
             'name': 'Illinois'},
            {'abbreviation': 'IN',
             'area_codes': ['219',
                            '260',
                            '317',
                            '463',
                            '574',
                            '765',
                            '812',
                            '930'],
             'name': 'Indiana'},
            {'abbreviation': 'IA',
             'area_codes': ['319', '515', '563', '641', '712'],
             'name': 'Iowa'},
            {'abbreviation': 'KS',
             'area_codes': ['316', '620', '785', '913'],
             'name': 'Kansas'},
            {'abbreviation': 'KY',
             'area_codes': ['270', '364', '502', '606', '859'],
             'name': 'Kentucky'},
            {'abbreviation': 'LA',
             'area_codes': ['225', '318', '337', '504', '985'],
             'name': 'Louisiana'},
            {'abbreviation': 'ME', 'area_codes': ['207'], 'name': 'Maine'},
            {'abbreviation': 'MD',
             'area_codes': ['240', '301', '410', '443', '667'],
             'name': 'Maryland'},
            {'abbreviation': 'MA',
             'area_codes': ['339',
                            '351',
                            '413',
                            '508',
                            '617',
                            '774',
                            '781',
                            '857',
                            '978'],
             'name': 'Massachusetts'},
            {'abbreviation': 'MI',
             'area_codes': ['231',
                            '248',
                            '269',
                            '313',
                            '517',
                            '586',
                            '616',
                            '734',
                            '810',
                            '906',
                            '947',
                            '989'],
             'name': 'Michigan'},
            {'abbreviation': 'MN',
             'area_codes': ['218', '320', '507', '612', '651', '763', '952'],
             'name': 'Minnesota'},
            {'abbreviation': 'MS',
             'area_codes': ['228', '601', '662', '769'],
             'name': 'Mississippi'},
            {'abbreviation': 'MO',
             'area_codes': ['314', '417', '573', '636', '660', '816'],
             'name': 'Missouri'},
            {'abbreviation': 'MT', 'area_codes': ['406'], 'name': 'Montana'},
            {'abbreviation': 'NE',
             'area_codes': ['308', '402', '531'],
             'name': 'Nebraska'},
            {'abbreviation': 'NV',
             'area_codes': ['702', '725', '775'],
             'name': 'Nevada'},
            {'abbreviation': 'NH',
             'area_codes': ['603'],
             'name': 'New Hampshire'},
            {'abbreviation': 'NJ',
             'area_codes': ['201',
                            '551',
                            '609',
                            '732',
                            '848',
                            '856',
                            '862',
                            '908',
                            '973'],
             'name': 'New Jersey'},
            {'abbreviation': 'NM',
             'area_codes': ['505', '575'],
             'name': 'New Mexico'},
            {'abbreviation': 'NY',
             'area_codes': ['212',
                            '315',
                            '332',
                            '347',
                            '516',
                            '518',
                            '585',
                            '607',
                            '631',
                            '646',
                            '680',
                            '716',
                            '718',
                            '845',
                            '914',
                            '917',
                            '929',
                            '934'],
             'name': 'New York'},
            {'abbreviation': 'NC',
             'area_codes': ['252',
                            '336',
                            '704',
                            '743',
                            '828',
                            '910',
                            '919',
                            '980',
                            '984'],
             'name': 'North Carolina'},
            {'abbreviation': 'ND',
             'area_codes': ['701'],
             'name': 'North Dakota'},
            {'abbreviation': 'OH',
             'area_codes': ['216',
                            '220',
                            '234',
                            '330',
                            '380',
                            '419',
                            '440',
                            '513',
                            '567',
                            '614',
                            '740',
                            '937'],
             'name': 'Ohio'},
            {'abbreviation': 'OK',
             'area_codes': ['405', '539', '580', '918'],
             'name': 'Oklahoma'},
            {'abbreviation': 'OR',
             'area_codes': ['458', '503', '541', '971'],
             'name': 'Oregon'},
            {'abbreviation': 'PA',
             'area_codes': ['215',
                            '267',
                            '272',
                            '412',
                            '484',
                            '570',
                            '610',
                            '717',
                            '724',
                            '814',
                            '878'],
             'name': 'Pennsylvania'},
            {'abbreviation': 'RI',
             'area_codes': ['401'],
             'name': 'Rhode Island'},
            {'abbreviation': 'SC',
             'area_codes': ['803', '843', '854', '864'],
             'name': 'South Carolina'},
            {'abbreviation': 'SD',
             'area_codes': ['605'],
             'name': 'South Dakota'},
            {'abbreviation': 'TN',
             'area_codes': ['423', '615', '629', '731', '865', '901', '931'],
             'name': 'Tennessee'},
            {'abbreviation': 'TX',
             'area_codes': ['210',
                            '214',
                            '254',
                            '281',
                            '325',
                            '346',
                            '361',
                            '409',
                            '430',
                            '432',
                            '469',
                            '512',
                            '682',
                            '713',
                            '737',
                            '806',
                            '817',
                            '830',
                            '832',
                            '903',
                            '915',
                            '936',
                            '940',
                            '956',
                            '972',
                            '979'],
             'name': 'Texas'},
            {'abbreviation': 'UT',
             'area_codes': ['385', '435', '801'],
             'name': 'Utah'},
            {'abbreviation': 'VT', 'area_codes': ['802'], 'name': 'Vermont'},
            {'abbreviation': 'VA',
             'area_codes': ['276', '434', '540', '571', '703', '757', '804'],
             'name': 'Virginia'},
            {'abbreviation': 'WA',
             'area_codes': ['206', '253', '360', '425', '509'],
             'name': 'Washington'},
            {'abbreviation': 'WV',
             'area_codes': ['304', '681'],
             'name': 'West Virginia'},
            {'abbreviation': 'WI',
             'area_codes': ['262', '414', '534', '608', '715', '920'],
             'name': 'Wisconsin'},
            {'abbreviation': 'WY', 'area_codes': ['307'], 'name': 'Wyoming'}]}
states names:Alabama and states abbreviations:AL
['205', '251', '256', '334', '938']
saraso elemento numeris0-saraso elementas:205
saraso elemento numeris1-saraso elementas:251
saraso elemento numeris2-saraso elementas:256
saraso elemento numeris3-saraso elementas:334
saraso elemento numeris4-saraso elementas:938
states names:Alaska and states abbreviations:AK
['907']
saraso elemento numeris0-saraso elementas:907
states names:Arizona and states abbreviations:AZ
['480', '520', '602', '623', '928']
saraso elemento numeris0-saraso elementas:480
saraso elemento numeris1-saraso elementas:520
saraso elemento numeris2-saraso elementas:602
saraso elemento numeris3-saraso elementas:623
saraso elemento numeris4-saraso elementas:928
states names:Arkansas and states abbreviations:AR
['479', '501', '870']
saraso elemento numeris0-saraso elementas:479
saraso elemento numeris1-saraso elementas:501
saraso elemento numeris2-saraso elementas:870
states names:California and states abbreviations:CA
['209', '213', '310', '323', '408', '415', '424', '442', '510', '530', '559', '562', '619', '626', '628', '650', '657', '661', '669', '707', '714', '747', '760', '805', '818', '831', '858', '909', '916', '925', '949', '951']
saraso elemento numeris0-saraso elementas:209
saraso elemento numeris1-saraso elementas:213
saraso elemento numeris2-saraso elementas:310
saraso elemento numeris3-saraso elementas:323
saraso elemento numeris4-saraso elementas:408
saraso elemento numeris5-saraso elementas:415
saraso elemento numeris6-saraso elementas:424
tai saraso reiksme:424- o saraso numeris:6,o statas yra:California
saraso elemento numeris7-saraso elementas:442
saraso elemento numeris8-saraso elementas:510
saraso elemento numeris9-saraso elementas:530
saraso elemento numeris10-saraso elementas:559
saraso elemento numeris11-saraso elementas:562
saraso elemento numeris12-saraso elementas:619
saraso elemento numeris13-saraso elementas:626
saraso elemento numeris14-saraso elementas:628
saraso elemento numeris15-saraso elementas:650
saraso elemento numeris16-saraso elementas:657
saraso elemento numeris17-saraso elementas:661
saraso elemento numeris18-saraso elementas:669
saraso elemento numeris19-saraso elementas:707
saraso elemento numeris20-saraso elementas:714
saraso elemento numeris21-saraso elementas:747
saraso elemento numeris22-saraso elementas:760
saraso elemento numeris23-saraso elementas:805
saraso elemento numeris24-saraso elementas:818
saraso elemento numeris25-saraso elementas:831
saraso elemento numeris26-saraso elementas:858
saraso elemento numeris27-saraso elementas:909
saraso elemento numeris28-saraso elementas:916
saraso elemento numeris29-saraso elementas:925
saraso elemento numeris30-saraso elementas:949
saraso elemento numeris31-saraso elementas:951
states names:Colorado and states abbreviations:CO
['303', '719', '720', '970']
saraso elemento numeris0-saraso elementas:303
saraso elemento numeris1-saraso elementas:719
saraso elemento numeris2-saraso elementas:720
saraso elemento numeris3-saraso elementas:970
states names:Connecticut and states abbreviations:CT
['203', '475', '860', '959']
saraso elemento numeris0-saraso elementas:203
saraso elemento numeris1-saraso elementas:475
saraso elemento numeris2-saraso elementas:860
saraso elemento numeris3-saraso elementas:959
states names:Delaware and states abbreviations:DE
['302']
saraso elemento numeris0-saraso elementas:302
states names:Florida and states abbreviations:FL
['239', '305', '321', '352', '386', '407', '561', '727', '754', '772', '786', '813', '850', '863', '904', '941', '954']
saraso elemento numeris0-saraso elementas:239
saraso elemento numeris1-saraso elementas:305
saraso elemento numeris2-saraso elementas:321
saraso elemento numeris3-saraso elementas:352
saraso elemento numeris4-saraso elementas:386
saraso elemento numeris5-saraso elementas:407
saraso elemento numeris6-saraso elementas:561
tai saraso reiksme:561- o saraso numeris:6,o statas yra:Florida
saraso elemento numeris7-saraso elementas:727
saraso elemento numeris8-saraso elementas:754
saraso elemento numeris9-saraso elementas:772
saraso elemento numeris10-saraso elementas:786
saraso elemento numeris11-saraso elementas:813
saraso elemento numeris12-saraso elementas:850
saraso elemento numeris13-saraso elementas:863
saraso elemento numeris14-saraso elementas:904
saraso elemento numeris15-saraso elementas:941
saraso elemento numeris16-saraso elementas:954
states names:Georgia and states abbreviations:GA
['229', '404', '470', '478', '678', '706', '762', '770', '912']
saraso elemento numeris0-saraso elementas:229
saraso elemento numeris1-saraso elementas:404
saraso elemento numeris2-saraso elementas:470
saraso elemento numeris3-saraso elementas:478
saraso elemento numeris4-saraso elementas:678
saraso elemento numeris5-saraso elementas:706
saraso elemento numeris6-saraso elementas:762
tai saraso reiksme:762- o saraso numeris:6,o statas yra:Georgia
saraso elemento numeris7-saraso elementas:770
saraso elemento numeris8-saraso elementas:912
states names:Hawaii and states abbreviations:HI
['808']
saraso elemento numeris0-saraso elementas:808
states names:Idaho and states abbreviations:ID
['208']
saraso elemento numeris0-saraso elementas:208
states names:Illinois and states abbreviations:IL
['217', '224', '309', '312', '331', '618', '630', '708', '773', '779', '815', '847', '872']
saraso elemento numeris0-saraso elementas:217
saraso elemento numeris1-saraso elementas:224
saraso elemento numeris2-saraso elementas:309
saraso elemento numeris3-saraso elementas:312
saraso elemento numeris4-saraso elementas:331
saraso elemento numeris5-saraso elementas:618
saraso elemento numeris6-saraso elementas:630
tai saraso reiksme:630- o saraso numeris:6,o statas yra:Illinois
saraso elemento numeris7-saraso elementas:708
saraso elemento numeris8-saraso elementas:773
saraso elemento numeris9-saraso elementas:779
saraso elemento numeris10-saraso elementas:815
saraso elemento numeris11-saraso elementas:847
saraso elemento numeris12-saraso elementas:872
states names:Indiana and states abbreviations:IN
['219', '260', '317', '463', '574', '765', '812', '930']
saraso elemento numeris0-saraso elementas:219
saraso elemento numeris1-saraso elementas:260
saraso elemento numeris2-saraso elementas:317
saraso elemento numeris3-saraso elementas:463
saraso elemento numeris4-saraso elementas:574
saraso elemento numeris5-saraso elementas:765
saraso elemento numeris6-saraso elementas:812
tai saraso reiksme:812- o saraso numeris:6,o statas yra:Indiana
saraso elemento numeris7-saraso elementas:930
states names:Iowa and states abbreviations:IA
['319', '515', '563', '641', '712']
saraso elemento numeris0-saraso elementas:319
saraso elemento numeris1-saraso elementas:515
saraso elemento numeris2-saraso elementas:563
saraso elemento numeris3-saraso elementas:641
saraso elemento numeris4-saraso elementas:712
states names:Kansas and states abbreviations:KS
['316', '620', '785', '913']
saraso elemento numeris0-saraso elementas:316
saraso elemento numeris1-saraso elementas:620
saraso elemento numeris2-saraso elementas:785
saraso elemento numeris3-saraso elementas:913
states names:Kentucky and states abbreviations:KY
['270', '364', '502', '606', '859']
saraso elemento numeris0-saraso elementas:270
saraso elemento numeris1-saraso elementas:364
saraso elemento numeris2-saraso elementas:502
saraso elemento numeris3-saraso elementas:606
saraso elemento numeris4-saraso elementas:859
states names:Louisiana and states abbreviations:LA
['225', '318', '337', '504', '985']
saraso elemento numeris0-saraso elementas:225
saraso elemento numeris1-saraso elementas:318
saraso elemento numeris2-saraso elementas:337
saraso elemento numeris3-saraso elementas:504
saraso elemento numeris4-saraso elementas:985
states names:Maine and states abbreviations:ME
['207']
saraso elemento numeris0-saraso elementas:207
states names:Maryland and states abbreviations:MD
['240', '301', '410', '443', '667']
saraso elemento numeris0-saraso elementas:240
saraso elemento numeris1-saraso elementas:301
saraso elemento numeris2-saraso elementas:410
saraso elemento numeris3-saraso elementas:443
saraso elemento numeris4-saraso elementas:667
states names:Massachusetts and states abbreviations:MA
['339', '351', '413', '508', '617', '774', '781', '857', '978']
saraso elemento numeris0-saraso elementas:339
saraso elemento numeris1-saraso elementas:351
saraso elemento numeris2-saraso elementas:413
saraso elemento numeris3-saraso elementas:508
saraso elemento numeris4-saraso elementas:617
saraso elemento numeris5-saraso elementas:774
saraso elemento numeris6-saraso elementas:781
tai saraso reiksme:781- o saraso numeris:6,o statas yra:Massachusetts
saraso elemento numeris7-saraso elementas:857
saraso elemento numeris8-saraso elementas:978
states names:Michigan and states abbreviations:MI
['231', '248', '269', '313', '517', '586', '616', '734', '810', '906', '947', '989']
saraso elemento numeris0-saraso elementas:231
saraso elemento numeris1-saraso elementas:248
saraso elemento numeris2-saraso elementas:269
saraso elemento numeris3-saraso elementas:313
saraso elemento numeris4-saraso elementas:517
saraso elemento numeris5-saraso elementas:586
saraso elemento numeris6-saraso elementas:616
tai saraso reiksme:616- o saraso numeris:6,o statas yra:Michigan
saraso elemento numeris7-saraso elementas:734
saraso elemento numeris8-saraso elementas:810
saraso elemento numeris9-saraso elementas:906
saraso elemento numeris10-saraso elementas:947
saraso elemento numeris11-saraso elementas:989
states names:Minnesota and states abbreviations:MN
['218', '320', '507', '612', '651', '763', '952']
saraso elemento numeris0-saraso elementas:218
saraso elemento numeris1-saraso elementas:320
saraso elemento numeris2-saraso elementas:507
saraso elemento numeris3-saraso elementas:612
saraso elemento numeris4-saraso elementas:651
saraso elemento numeris5-saraso elementas:763
saraso elemento numeris6-saraso elementas:952
tai saraso reiksme:952- o saraso numeris:6,o statas yra:Minnesota
states names:Mississippi and states abbreviations:MS
['228', '601', '662', '769']
saraso elemento numeris0-saraso elementas:228
saraso elemento numeris1-saraso elementas:601
saraso elemento numeris2-saraso elementas:662
saraso elemento numeris3-saraso elementas:769
states names:Missouri and states abbreviations:MO
['314', '417', '573', '636', '660', '816']
saraso elemento numeris0-saraso elementas:314
saraso elemento numeris1-saraso elementas:417
saraso elemento numeris2-saraso elementas:573
saraso elemento numeris3-saraso elementas:636
saraso elemento numeris4-saraso elementas:660
saraso elemento numeris5-saraso elementas:816
states names:Montana and states abbreviations:MT
['406']
saraso elemento numeris0-saraso elementas:406
states names:Nebraska and states abbreviations:NE
['308', '402', '531']
saraso elemento numeris0-saraso elementas:308
saraso elemento numeris1-saraso elementas:402
saraso elemento numeris2-saraso elementas:531
states names:Nevada and states abbreviations:NV
['702', '725', '775']
saraso elemento numeris0-saraso elementas:702
saraso elemento numeris1-saraso elementas:725
saraso elemento numeris2-saraso elementas:775
states names:New Hampshire and states abbreviations:NH
['603']
saraso elemento numeris0-saraso elementas:603
states names:New Jersey and states abbreviations:NJ
['201', '551', '609', '732', '848', '856', '862', '908', '973']
saraso elemento numeris0-saraso elementas:201
saraso elemento numeris1-saraso elementas:551
saraso elemento numeris2-saraso elementas:609
saraso elemento numeris3-saraso elementas:732
saraso elemento numeris4-saraso elementas:848
saraso elemento numeris5-saraso elementas:856
saraso elemento numeris6-saraso elementas:862
tai saraso reiksme:862- o saraso numeris:6,o statas yra:New Jersey
saraso elemento numeris7-saraso elementas:908
saraso elemento numeris8-saraso elementas:973
states names:New Mexico and states abbreviations:NM
['505', '575']
saraso elemento numeris0-saraso elementas:505
saraso elemento numeris1-saraso elementas:575
states names:New York and states abbreviations:NY
['212', '315', '332', '347', '516', '518', '585', '607', '631', '646', '680', '716', '718', '845', '914', '917', '929', '934']
saraso elemento numeris0-saraso elementas:212
saraso elemento numeris1-saraso elementas:315
saraso elemento numeris2-saraso elementas:332
saraso elemento numeris3-saraso elementas:347
saraso elemento numeris4-saraso elementas:516
saraso elemento numeris5-saraso elementas:518
saraso elemento numeris6-saraso elementas:585
tai saraso reiksme:585- o saraso numeris:6,o statas yra:New York
saraso elemento numeris7-saraso elementas:607
saraso elemento numeris8-saraso elementas:631
saraso elemento numeris9-saraso elementas:646
saraso elemento numeris10-saraso elementas:680
saraso elemento numeris11-saraso elementas:716
saraso elemento numeris12-saraso elementas:718
saraso elemento numeris13-saraso elementas:845
saraso elemento numeris14-saraso elementas:914
saraso elemento numeris15-saraso elementas:917
saraso elemento numeris16-saraso elementas:929
saraso elemento numeris17-saraso elementas:934
states names:North Carolina and states abbreviations:NC
['252', '336', '704', '743', '828', '910', '919', '980', '984']
saraso elemento numeris0-saraso elementas:252
saraso elemento numeris1-saraso elementas:336
saraso elemento numeris2-saraso elementas:704
saraso elemento numeris3-saraso elementas:743
saraso elemento numeris4-saraso elementas:828
saraso elemento numeris5-saraso elementas:910
saraso elemento numeris6-saraso elementas:919
tai saraso reiksme:919- o saraso numeris:6,o statas yra:North Carolina
saraso elemento numeris7-saraso elementas:980
saraso elemento numeris8-saraso elementas:984
states names:North Dakota and states abbreviations:ND
['701']
saraso elemento numeris0-saraso elementas:701
states names:Ohio and states abbreviations:OH
['216', '220', '234', '330', '380', '419', '440', '513', '567', '614', '740', '937']
saraso elemento numeris0-saraso elementas:216
saraso elemento numeris1-saraso elementas:220
saraso elemento numeris2-saraso elementas:234
saraso elemento numeris3-saraso elementas:330
saraso elemento numeris4-saraso elementas:380
saraso elemento numeris5-saraso elementas:419
saraso elemento numeris6-saraso elementas:440
tai saraso reiksme:440- o saraso numeris:6,o statas yra:Ohio
saraso elemento numeris7-saraso elementas:513
saraso elemento numeris8-saraso elementas:567
saraso elemento numeris9-saraso elementas:614
saraso elemento numeris10-saraso elementas:740
saraso elemento numeris11-saraso elementas:937
states names:Oklahoma and states abbreviations:OK
['405', '539', '580', '918']
saraso elemento numeris0-saraso elementas:405
saraso elemento numeris1-saraso elementas:539
saraso elemento numeris2-saraso elementas:580
saraso elemento numeris3-saraso elementas:918
states names:Oregon and states abbreviations:OR
['458', '503', '541', '971']
saraso elemento numeris0-saraso elementas:458
saraso elemento numeris1-saraso elementas:503
saraso elemento numeris2-saraso elementas:541
saraso elemento numeris3-saraso elementas:971
states names:Pennsylvania and states abbreviations:PA
['215', '267', '272', '412', '484', '570', '610', '717', '724', '814', '878']
saraso elemento numeris0-saraso elementas:215
saraso elemento numeris1-saraso elementas:267
saraso elemento numeris2-saraso elementas:272
saraso elemento numeris3-saraso elementas:412
saraso elemento numeris4-saraso elementas:484
saraso elemento numeris5-saraso elementas:570
saraso elemento numeris6-saraso elementas:610
tai saraso reiksme:610- o saraso numeris:6,o statas yra:Pennsylvania
saraso elemento numeris7-saraso elementas:717
saraso elemento numeris8-saraso elementas:724
saraso elemento numeris9-saraso elementas:814
saraso elemento numeris10-saraso elementas:878
states names:Rhode Island and states abbreviations:RI
['401']
saraso elemento numeris0-saraso elementas:401
states names:South Carolina and states abbreviations:SC
['803', '843', '854', '864']
saraso elemento numeris0-saraso elementas:803
saraso elemento numeris1-saraso elementas:843
saraso elemento numeris2-saraso elementas:854
saraso elemento numeris3-saraso elementas:864
states names:South Dakota and states abbreviations:SD
['605']
saraso elemento numeris0-saraso elementas:605
states names:Tennessee and states abbreviations:TN
['423', '615', '629', '731', '865', '901', '931']
saraso elemento numeris0-saraso elementas:423
saraso elemento numeris1-saraso elementas:615
saraso elemento numeris2-saraso elementas:629
saraso elemento numeris3-saraso elementas:731
saraso elemento numeris4-saraso elementas:865
saraso elemento numeris5-saraso elementas:901
saraso elemento numeris6-saraso elementas:931
tai saraso reiksme:931- o saraso numeris:6,o statas yra:Tennessee
states names:Texas and states abbreviations:TX
['210', '214', '254', '281', '325', '346', '361', '409', '430', '432', '469', '512', '682', '713', '737', '806', '817', '830', '832', '903', '915', '936', '940', '956', '972', '979']
saraso elemento numeris0-saraso elementas:210
saraso elemento numeris1-saraso elementas:214
saraso elemento numeris2-saraso elementas:254
saraso elemento numeris3-saraso elementas:281
saraso elemento numeris4-saraso elementas:325
saraso elemento numeris5-saraso elementas:346
saraso elemento numeris6-saraso elementas:361
tai saraso reiksme:361- o saraso numeris:6,o statas yra:Texas
saraso elemento numeris7-saraso elementas:409
saraso elemento numeris8-saraso elementas:430
saraso elemento numeris9-saraso elementas:432
saraso elemento numeris10-saraso elementas:469
saraso elemento numeris11-saraso elementas:512
saraso elemento numeris12-saraso elementas:682
saraso elemento numeris13-saraso elementas:713
saraso elemento numeris14-saraso elementas:737
saraso elemento numeris15-saraso elementas:806
saraso elemento numeris16-saraso elementas:817
saraso elemento numeris17-saraso elementas:830
saraso elemento numeris18-saraso elementas:832
saraso elemento numeris19-saraso elementas:903
saraso elemento numeris20-saraso elementas:915
saraso elemento numeris21-saraso elementas:936
saraso elemento numeris22-saraso elementas:940
saraso elemento numeris23-saraso elementas:956
saraso elemento numeris24-saraso elementas:972
saraso elemento numeris25-saraso elementas:979
states names:Utah and states abbreviations:UT
['385', '435', '801']
saraso elemento numeris0-saraso elementas:385
saraso elemento numeris1-saraso elementas:435
saraso elemento numeris2-saraso elementas:801
states names:Vermont and states abbreviations:VT
['802']
saraso elemento numeris0-saraso elementas:802
states names:Virginia and states abbreviations:VA
['276', '434', '540', '571', '703', '757', '804']
saraso elemento numeris0-saraso elementas:276
saraso elemento numeris1-saraso elementas:434
saraso elemento numeris2-saraso elementas:540
saraso elemento numeris3-saraso elementas:571
saraso elemento numeris4-saraso elementas:703
saraso elemento numeris5-saraso elementas:757
saraso elemento numeris6-saraso elementas:804
tai saraso reiksme:804- o saraso numeris:6,o statas yra:Virginia
states names:Washington and states abbreviations:WA
['206', '253', '360', '425', '509']
saraso elemento numeris0-saraso elementas:206
saraso elemento numeris1-saraso elementas:253
saraso elemento numeris2-saraso elementas:360
saraso elemento numeris3-saraso elementas:425
saraso elemento numeris4-saraso elementas:509
states names:West Virginia and states abbreviations:WV
['304', '681']
saraso elemento numeris0-saraso elementas:304
saraso elemento numeris1-saraso elementas:681
states names:Wisconsin and states abbreviations:WI
['262', '414', '534', '608', '715', '920']
saraso elemento numeris0-saraso elementas:262
saraso elemento numeris1-saraso elementas:414
saraso elemento numeris2-saraso elementas:534
saraso elemento numeris3-saraso elementas:608
saraso elemento numeris4-saraso elementas:715
saraso elemento numeris5-saraso elementas:920
states names:Wyoming and states abbreviations:WY
['307']
saraso elemento numeris0-saraso elementas:307

Process finished with exit code 0
