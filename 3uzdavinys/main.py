import json
from faker import Faker
fake = Faker()
FILEPATH = 'city.json'
def get_json_data():
    with open(FILEPATH) as json_file:
        data = json.load(json_file)
    return data
def store_json_data(data):
    with open(FILEPATH, 'w') as outfile:
        json.dump(data, outfile)
def add_city(city, state):
    current_data = {
        "name"  : city,
        "state" : state
    }
    data = get_json_data()
    data[city] = current_data
    store_json_data(data)
def get_all_cities():
    data = get_json_data()
    return data
def get_single_city(city_name):
    data = get_json_data()
    if(city_name in data):
        return data[city_name]
    # print(data)
    return None
def update_single_city(city_name, city_state):
    data = get_json_data()
    if(city_name in data):
        city_data = {
            'name' : city_name,
            'state' : city_state
        }
        data[city_name] = city_data
        store_json_data(data)
def delete_single_city(city_name):
    data = get_json_data()
    if(city_name in data):
        data.pop(city_name)
        store_json_data(data)
def delete_all_cities():
    data = get_json_data()
    city_list = list(data.keys())
    for current_city in city_list:
        print(current_city)
        data.pop(current_city)
    store_json_data(data)
def delete_all_cities_efficient():
    current_dict = {}
    store_json_data(current_dict)
def add_multiple_cities_test():

    Faker.seed(0)
    for c_index in range(1000):
        current_city = fake.city()
        current_state = fake.state()
        add_city(current_city, current_state)
        print(f'{c_index} Added: ', current_city, current_state)

def startpy():
    add_multiple_cities_test()
    print('\nCRUD Done!')
if __name__ == '__main__':
    startpy()
#output
9 Added:  Port Samanthatown Colorado
10 Added:  Pagetown South Carolina
11 Added:  Claytonmouth Kansas
12 Added:  Janeland Illinois
13 Added:  East Linda Georgia
14 Added:  Davismouth North Carolina
15 Added:  Rodriguezside Maine
16 Added:  New Marvinside Indiana
17 Added:  Seanfurt Massachusetts
18 Added:  West Ivan Idaho
19 Added:  New Tinaview New Mexico
20 Added:  North Erikaberg Georgia
21 Added:  Port Christopherside Utah
22 Added:  Masseyhaven Louisiana
23 Added:  Port Jason Utah
24 Added:  Rileymouth New York
25 Added:  Christopherville New York
26 Added:  Meganbury Alaska
27 Added:  Davebury Mississippi
28 Added:  West Ronald Arkansas
29 Added:  Port Dustinbury Arizona
30 Added:  North Davidborough Rhode Island
31 Added:  South Christopherville Arizona
32 Added:  East Susanburgh Virginia
33 Added:  South Jasonton Utah
34 Added:  New Ronaldville Kentucky
35 Added:  East Charlesport Minnesota
36 Added:  Whitehaven New Jersey
37 Added:  New Craigfurt Illinois
38 Added:  Michaelfort Oregon
39 Added:  Lake Emily Wyoming
40 Added:  Port Ericaburgh Michigan
41 Added:  Davidmouth Texas
42 Added:  North Thomas Nebraska
43 Added:  Deborahfurt Texas
44 Added:  Erictown New Jersey
45 Added:  West Joanneside Louisiana
46 Added:  East Kathleen New Mexico
47 Added:  Chelseastad Pennsylvania
48 Added:  Lake Kyle West Virginia
49 Added:  Pooleland Alabama
50 Added:  Lake Matthew Kansas
51 Added:  Lake Shane Virginia
52 Added:  Johnsonshire Nebraska
53 Added:  East Seanview Vermont
54 Added:  South Allison New York
55 Added:  North Troyport New Jersey
56 Added:  Port Mackenziechester Illinois
57 Added:  Port Jessicatown Montana
58 Added:  Stewartborough Alabama
59 Added:  Port Emmaville Illinois
60 Added:  New Debraport Louisiana
61 Added:  North Thomas Montana
62 Added:  North Joshuamouth Delaware
63 Added:  Dennishaven Tennessee
64 Added:  Darinberg Louisiana
65 Added:  North Billyview Oklahoma
66 Added:  Staceyshire Arizona
67 Added:  Josephmouth South Dakota
68 Added:  Watsonside Idaho
69 Added:  South Brenda Alabama
70 Added:  East Joseph Michigan
71 Added:  Jennifermouth Wyoming
72 Added:  North Josephberg Pennsylvania
73 Added:  Michaelside Florida
74 Added:  Dannybury Arkansas
75 Added:  Haydenhaven Washington
76 Added:  West Richardmouth Maryland
77 Added:  Rodriguezside New Mexico
78 Added:  Rogersmouth Delaware
79 Added:  Wilsonfort Nevada
80 Added:  West Matthewberg Hawaii
81 Added:  Drakeland California
82 Added:  East Karaton Missouri
83 Added:  North Philliphaven Maine
84 Added:  Morashire Virginia
85 Added:  South Christopher Iowa
86 Added:  Brendaburgh Nevada
87 Added:  West Danny Vermont
88 Added:  New Shannonborough Delaware
89 Added:  Sandersborough Tennessee
90 Added:  Port Jasonberg Connecticut
91 Added:  South Nicholas Ohio
92 Added:  North Vanessa New York
93 Added:  New Richard Utah
94 Added:  Richfort Utah
95 Added:  Marthafort South Dakota
96 Added:  New Chelsea Iowa
97 Added:  West Janicemouth Massachusetts
98 Added:  New Eddieview Rhode Island
99 Added:  Port Nicholas Maine
100 Added:  Jonesland North Dakota
101 Added:  North Jeffreyton Maryland
102 Added:  Port Meganmouth Hawaii
103 Added:  Port Diana Mississippi
104 Added:  Santanahaven Arizona
105 Added:  Lake Laurahaven Wisconsin
106 Added:  Lake Ronaldborough Maine
107 Added:  Petersenfort Missouri
108 Added:  Port Michelle Alaska
109 Added:  Lake Hunterhaven Oregon
110 Added:  Marvinfort Kentucky
111 Added:  Kendrafurt Missouri
112 Added:  East Danielleberg Kansas
113 Added:  Jessicamouth Arkansas
114 Added:  South Robertfort Rhode Island
115 Added:  Lake Hollystad Nebraska
116 Added:  New Stevenmouth Arkansas
117 Added:  South Kimberlytown Arizona
118 Added:  Lake Mario Vermont
119 Added:  Jamesfort Delaware
120 Added:  New Jaclynmouth Tennessee
121 Added:  Lake Jenniferport Florida
122 Added:  Lloydville North Dakota
123 Added:  North Kimberly New Hampshire
124 Added:  Katherinemouth Minnesota
125 Added:  North Rachelton New York
126 Added:  Rachelhaven Texas
127 Added:  East Clayton South Dakota
128 Added:  Hunterville Georgia
129 Added:  Snowchester Colorado
130 Added:  South Bryanchester Wyoming
131 Added:  Lake Stephanie New Hampshire
132 Added:  Parkstown New York
133 Added:  Jenniferland Minnesota
134 Added:  North Michaeltown Minnesota
135 Added:  Gregorybury Mississippi
136 Added:  New Patriciaborough Alabama
137 Added:  Lake Emily Delaware
138 Added:  West Miketown Rhode Island
139 Added:  Port Donald New Jersey
140 Added:  South Maxwellview Florida
141 Added:  East Michaelfort Maine
142 Added:  Sharonside South Dakota
143 Added:  Jackland Connecticut
144 Added:  Ericberg Florida
145 Added:  West William Kansas
146 Added:  West Nathan Texas
147 Added:  Port Davidtown Montana
148 Added:  Lake Charleschester Maryland
149 Added:  Yangberg Pennsylvania
150 Added:  Evansstad Colorado
151 Added:  South Cynthia South Dakota
152 Added:  South Rickychester Washington
153 Added:  Scottstad Maine
154 Added:  Davisburgh Connecticut
155 Added:  Danielberg Vermont
156 Added:  Hebertburgh Wyoming
157 Added:  Reynoldsbury New Jersey
158 Added:  Sharonberg Minnesota
159 Added:  Welchland New Mexico
160 Added:  West Aaron Vermont
161 Added:  Montgomerytown Indiana
162 Added:  Dannyport Ohio
163 Added:  South Jasmine New Mexico
164 Added:  Lake Tylerbury Ohio
165 Added:  Ramireztown Delaware
166 Added:  Nicoleton Alabama
167 Added:  Raymondshire Virginia
168 Added:  Wallaceview Minnesota
169 Added:  Monicaborough Rhode Island
170 Added:  North Chadview Maryland
171 Added:  Davidbury Wisconsin
172 Added:  North Robert Maine
173 Added:  Aprilshire North Dakota
174 Added:  New Daniel South Dakota
175 Added:  Figueroaview Maine
176 Added:  Watsonberg Hawaii
177 Added:  Lake Davidfurt Pennsylvania
178 Added:  Taylorport Minnesota
179 Added:  Newtonborough New Mexico
180 Added:  Nealmouth New York
181 Added:  South Kevinfort Arkansas
182 Added:  North Michael Montana
183 Added:  Port Alisonland Utah
184 Added:  Lake Stacyfurt Alabama
185 Added:  Blaketown Louisiana
186 Added:  Jessicabury Georgia
187 Added:  Jameschester New Jersey
188 Added:  Patrickmouth Nebraska
189 Added:  Hernandezberg North Dakota
190 Added:  Davidburgh New Hampshire
191 Added:  Kristinafurt Nevada
192 Added:  Pricebury Illinois
193 Added:  Bentleyshire Virginia
194 Added:  South Arthurland Idaho
195 Added:  Brianburgh Iowa
196 Added:  Cheyennehaven Wisconsin
197 Added:  Kelseystad Nebraska
198 Added:  Brownhaven Texas
199 Added:  Carpenterfort Kentucky
200 Added:  Lewisview Arizona
201 Added:  North Franciscotown Maine
202 Added:  East Brycechester Utah
203 Added:  New Randy Iowa
204 Added:  Leeville Rhode Island
205 Added:  Port Luisside New Jersey
206 Added:  Jonathanhaven Arizona
207 Added:  West Christopher North Dakota
208 Added:  Jacobborough Kentucky
209 Added:  Larryfurt Kentucky
210 Added:  Cooperbury Arizona
211 Added:  Sarahland Alabama
212 Added:  Simpsonmouth Arkansas
213 Added:  Wernermouth New Hampshire
214 Added:  North Christopherville Wisconsin
215 Added:  South Nicole Indiana
216 Added:  Salazarchester Oklahoma
217 Added:  Williamsburgh Kansas
218 Added:  Robinsonview Minnesota
219 Added:  Virginiaville Oklahoma
220 Added:  Chelseaborough Virginia
221 Added:  Kimberlyhaven Rhode Island
222 Added:  Herreraview Louisiana
223 Added:  North David Virginia
224 Added:  East Jessicabury Indiana
225 Added:  Nicholetown West Virginia
226 Added:  Trevinoville Missouri
227 Added:  Davidshire Minnesota
228 Added:  Lake Jennifer Ohio
229 Added:  Jeffreybury California
230 Added:  Emilybury Mississippi
231 Added:  Mitchellburgh Florida
232 Added:  New Williamstad Pennsylvania
233 Added:  Port Davidfurt Georgia
234 Added:  New Vickie Florida
235 Added:  Port Rose New York
236 Added:  East Jessica Iowa
237 Added:  Gomezshire Florida
238 Added:  Lesterville South Carolina
239 Added:  New Caitlinfort New Jersey
240 Added:  Alexanderbury Oklahoma
241 Added:  Lake Natasha West Virginia
242 Added:  Payneland Kentucky
243 Added:  New Richard Illinois
244 Added:  Kristenfurt Arkansas
245 Added:  North Leslie West Virginia
246 Added:  West Michelle Texas
247 Added:  West Max Hawaii
248 Added:  Andreshire Ohio
249 Added:  Lake Crystalstad Alaska
250 Added:  Burtontown Kansas
251 Added:  North Jeremiahmouth California
252 Added:  West Teresachester Florida
253 Added:  South Ryan Minnesota
254 Added:  Gregorymouth Washington
255 Added:  Reyeschester Kentucky
256 Added:  Maloneshire Delaware
257 Added:  Finleyburgh Alabama
258 Added:  New Misty North Carolina
259 Added:  North Mark Idaho
260 Added:  North Sue Hawaii
261 Added:  Lake Christian Rhode Island
262 Added:  New Courtneyberg South Carolina
263 Added:  West Matthewfurt Alaska
264 Added:  South Christopherport Texas
265 Added:  South Joel Minnesota
266 Added:  Lake Karen Michigan
267 Added:  Lindafurt Alabama
268 Added:  Alyssaport Oklahoma
269 Added:  Maddenside Oregon
270 Added:  Sarahton New Jersey
271 Added:  Griffithfurt Minnesota
272 Added:  Williamsview West Virginia
273 Added:  West Erinshire Vermont
274 Added:  Wandaborough Wisconsin
275 Added:  Paulview Indiana
276 Added:  New Tinabury Pennsylvania
277 Added:  Franciscoberg Michigan
278 Added:  New Lisashire Georgia
279 Added:  Michaelport Massachusetts
280 Added:  Pattonchester Hawaii
281 Added:  Port Donaldton New Hampshire
282 Added:  West Sarah Washington
283 Added:  Browningview West Virginia
284 Added:  North Ana Nevada
285 Added:  Stephanieburgh North Dakota
286 Added:  North Donna Hawaii
287 Added:  New Crystalside Rhode Island
288 Added:  Fischerview Maryland
289 Added:  Alexanderview Kentucky
290 Added:  Veronicaborough Virginia
291 Added:  Moodytown Wisconsin
292 Added:  Port Donna Oregon
293 Added:  Wardton Oklahoma
294 Added:  Fieldsbury Alaska
295 Added:  Allisonburgh Utah
296 Added:  Lake Michael Vermont
297 Added:  Smithbury Oregon
298 Added:  West Jacob Wisconsin
299 Added:  Millermouth Kansas
300 Added:  Shieldsville Illinois
301 Added:  South Sandra Nevada
302 Added:  Shepardview Nevada
303 Added:  Chelsealand Maryland
304 Added:  South Alexview Illinois
305 Added:  Hughesfurt Vermont
306 Added:  New Stevenshire Florida
307 Added:  Marktown Montana
308 Added:  Mccallberg Arizona
309 Added:  New Michellestad Alabama
310 Added:  East Jenniferside New Mexico
311 Added:  West Sarahtown Massachusetts
312 Added:  Whiteheadview Nebraska
313 Added:  New Dylan Maryland
314 Added:  East Davidberg New Mexico
315 Added:  Lake Madisonton Oklahoma
316 Added:  Herringstad Pennsylvania
317 Added:  North Anitaview Illinois
318 Added:  Markview Kentucky
319 Added:  Lutzberg Wisconsin
320 Added:  Tranton South Dakota
321 Added:  Lake William Wisconsin
322 Added:  Lisaland Illinois
323 Added:  Carrmouth North Dakota
324 Added:  Lake Matthew Tennessee
325 Added:  South Kelsey Arkansas
326 Added:  Port Zacharytown Wyoming
327 Added:  North Ronaldstad Oregon
328 Added:  Rogersfurt North Carolina
329 Added:  Vanessaville Florida
330 Added:  Saraburgh Washington
331 Added:  North Matthew Rhode Island
332 Added:  North Robert Arkansas
333 Added:  Lauraton Rhode Island
334 Added:  West Samantha California
335 Added:  Brownstad Rhode Island
336 Added:  Emilyshire New Jersey
337 Added:  Whitemouth Kentucky
338 Added:  South Caleb Connecticut
339 Added:  North Michaelburgh Montana
340 Added:  West Stephenside West Virginia
341 Added:  Alvarezton Ohio
342 Added:  Gibbsview Alaska
343 Added:  Port Margaretmouth Minnesota
344 Added:  South Tammyberg North Dakota
345 Added:  Susantown Missouri
346 Added:  Ericside Vermont
347 Added:  East Greg Hawaii
348 Added:  New Mark Alaska
349 Added:  Benjaminfurt Arizona
350 Added:  East Cynthia Michigan
351 Added:  East Michael Hawaii
352 Added:  Fordshire Florida
353 Added:  Cunninghamtown Hawaii
354 Added:  Lake Peterburgh Georgia
355 Added:  North Madisonhaven Alabama
356 Added:  North Kimberlyville Oregon
357 Added:  Port Eric Missouri
358 Added:  South Samuelmouth Virginia
359 Added:  East Michael Indiana
360 Added:  Joneschester Oregon
361 Added:  Tammychester Nevada
362 Added:  South Patrick Montana
363 Added:  Lake Timothy Pennsylvania
364 Added:  Port Johnnyview North Dakota
365 Added:  Amyfort Kansas
366 Added:  Billymouth Montana
367 Added:  New Natalieton Georgia
368 Added:  Johnsonchester Washington
369 Added:  Hamiltonville Virginia
370 Added:  Munozburgh Hawaii
371 Added:  Thomasburgh Pennsylvania
372 Added:  Kathleenville Mississippi
373 Added:  Douglasstad Wyoming
374 Added:  Mccoyton Illinois
375 Added:  Gregoryshire Massachusetts
376 Added:  Normanton Maine
377 Added:  Johnsonchester Louisiana
378 Added:  Lunastad Florida
379 Added:  North Christie Hawaii
380 Added:  South Barbaramouth California
381 Added:  Port Ronaldside Florida
382 Added:  East Jared Iowa
383 Added:  New Derekfort Minnesota
384 Added:  Jennifermouth Utah
385 Added:  Port Sydneychester Wyoming
386 Added:  Rachelmouth South Dakota
387 Added:  Amandaberg Missouri
388 Added:  Jimmyfurt Minnesota
389 Added:  Fryhaven Maryland
390 Added:  Forbesville Utah
391 Added:  East Adam Rhode Island
392 Added:  Lake Kimberlyborough Rhode Island
393 Added:  West Haleyburgh Missouri
394 Added:  Port Barryville Mississippi
395 Added:  Floresmouth Mississippi
396 Added:  Elizabethbury Hawaii
397 Added:  Port Melissaburgh Alaska
398 Added:  New Robert Texas
399 Added:  South Jean Montana
400 Added:  Andrewberg Missouri
401 Added:  South Annette Missouri
402 Added:  Lake Briannamouth Iowa
403 Added:  Williamsville Louisiana
404 Added:  Piercefurt New Mexico
405 Added:  Herbertside Mississippi
406 Added:  West Melissa Georgia
407 Added:  Jonesland New Mexico
408 Added:  Knightchester Oklahoma
409 Added:  West Timothyville Maine
410 Added:  West Lisa Florida
411 Added:  Port Elizabethshire Oklahoma
412 Added:  North Antonio Montana
413 Added:  Kleinville New Mexico
414 Added:  Nancymouth Connecticut
415 Added:  East Jeremyport Louisiana
416 Added:  North Tyler North Carolina
417 Added:  Christopherport Oregon
418 Added:  Perezstad Missouri
419 Added:  East Keith Illinois
420 Added:  Kellerstad Maine
421 Added:  Salazarville Montana
422 Added:  Vincentfort Iowa
423 Added:  Crystalstad Nevada
424 Added:  Michaelfurt Wyoming
425 Added:  Michellefort Maine
426 Added:  South Ericbury West Virginia
427 Added:  West Victor Delaware
428 Added:  Hestermouth North Carolina
429 Added:  Whitneyshire South Carolina
430 Added:  Lake Reginald Maryland
431 Added:  Hallhaven Utah
432 Added:  North Thomasfurt Iowa
433 Added:  Joyceshire Wyoming
434 Added:  South Claytonborough Washington
435 Added:  Gregoryburgh Vermont
436 Added:  Anthonyton Alabama
437 Added:  Nicholsberg Delaware
438 Added:  North Joyce Illinois
439 Added:  New Peggychester California
440 Added:  East Jeremy Nebraska
441 Added:  Wellstown Nevada
442 Added:  South Theresa Arizona
443 Added:  Anthonystad Virginia
444 Added:  Margaretmouth Tennessee
445 Added:  New Zachary Kentucky
446 Added:  Lake Daletown Vermont
447 Added:  New Kelsey Florida
448 Added:  Clarkmouth Illinois
449 Added:  Romeroville Oklahoma
450 Added:  Lake Rhondaville North Carolina
451 Added:  Harrisonmouth Oklahoma
452 Added:  Davidview Missouri
453 Added:  New Williambury New Jersey
454 Added:  West Timothy Nebraska
455 Added:  South Jennifertown Oklahoma
456 Added:  Benjaminmouth Iowa
457 Added:  Allenfort New Mexico
458 Added:  East Scott Mississippi
459 Added:  Greeneberg North Dakota
460 Added:  East Kevinhaven South Dakota
461 Added:  North Ericton Michigan
462 Added:  Port Rachel Missouri
463 Added:  South Tyler Hawaii
464 Added:  Williamsmouth Wisconsin
465 Added:  Lake Mark North Dakota
466 Added:  Hernandezfort Texas
467 Added:  New Scott Kansas
468 Added:  Steinmouth Oklahoma
469 Added:  North Bradley Florida
470 Added:  South Morgan South Carolina
471 Added:  Lake Gabrielle Wisconsin
472 Added:  Middletonport Utah
473 Added:  Trevorborough Hawaii
474 Added:  Angelastad Virginia
475 Added:  Myersmouth New Jersey
476 Added:  East Jeffreyville Wisconsin
477 Added:  South Stephanie Virginia
478 Added:  West Janet Alaska
479 Added:  Clarkchester Pennsylvania
480 Added:  Fernandeztown Texas
481 Added:  New Dawn New York
482 Added:  Omarside California
483 Added:  New Tarafort Wisconsin
484 Added:  East Robertstad Maryland
485 Added:  Lake Andrewbury South Carolina
486 Added:  New Michellehaven Mississippi
487 Added:  South Jonathan Pennsylvania
488 Added:  Ramirezbury Missouri
489 Added:  Reesemouth Iowa
490 Added:  Selenaton Georgia
491 Added:  Courtneyshire New York
492 Added:  New Timothymouth Missouri
493 Added:  North Ryanberg Wisconsin
494 Added:  North David Nevada
495 Added:  North Crystal Kentucky
496 Added:  Wilsonport Mississippi
497 Added:  Lake Makayla Ohio
498 Added:  West Zacharytown Hawaii
499 Added:  Weissview Michigan
500 Added:  West Wendy Connecticut
501 Added:  Mosesland Kentucky
502 Added:  New Charlesshire Florida
503 Added:  Johnsonbury Minnesota
504 Added:  New Maryborough Idaho
505 Added:  South James Vermont
506 Added:  Baileyview Washington
507 Added:  Terriside Illinois
508 Added:  South Maria Florida
509 Added:  Anntown Colorado
510 Added:  Kylemouth Arizona
511 Added:  New Alexisville Hawaii
512 Added:  Tiffanyhaven Oklahoma
513 Added:  Michelleland Nebraska
514 Added:  Martinezshire New Jersey
515 Added:  Grantbury South Dakota
516 Added:  Nunezport Arizona
517 Added:  Port Alanview California
518 Added:  Loganside Tennessee
519 Added:  Brandonbury Vermont
520 Added:  West Carla Missouri
521 Added:  Campbellbury Kentucky
522 Added:  Reneeside New York
523 Added:  Ericksonchester Mississippi
524 Added:  New Brett Virginia
525 Added:  Reyesbury Colorado
526 Added:  Coreyburgh Florida
527 Added:  Smithstad North Dakota
528 Added:  Martinezbury New York
529 Added:  Josephchester New Mexico
530 Added:  East Jennahaven Minnesota
531 Added:  East Edward Maryland
532 Added:  East Andrea Kentucky
533 Added:  East Jessechester Virginia
534 Added:  East Katherine Florida
535 Added:  Lake John Wyoming
536 Added:  Laurentown Washington
537 Added:  Tylerborough Arkansas
538 Added:  Jacksonhaven Missouri
539 Added:  South Amanda New York
540 Added:  East Melissaside Alabama
541 Added:  North Suzannebury West Virginia
542 Added:  Coleview Nebraska
543 Added:  Dorothyview Washington
544 Added:  Port Ericbury West Virginia
545 Added:  Port Brandon Arkansas
546 Added:  Lake Seanmouth Virginia
547 Added:  New Courtney North Carolina
548 Added:  Alexanderberg Minnesota
549 Added:  Michaelport North Carolina
550 Added:  Dennisfort Washington
551 Added:  New Randy New Mexico
552 Added:  Scottfort Maine
553 Added:  Michaelfurt Montana
554 Added:  Dominguezhaven Maryland
555 Added:  East Ryan Kentucky
556 Added:  New Donald Rhode Island
557 Added:  Starkview Nevada
558 Added:  Stephenhaven Arkansas
559 Added:  West Stephen California
560 Added:  East Carlaview Alabama
561 Added:  East Christine Texas
562 Added:  Chelseaview Alabama
563 Added:  North Cathyburgh Maryland
564 Added:  South Madeline West Virginia
565 Added:  Micheleland Pennsylvania
566 Added:  Caseytown Wyoming
567 Added:  North Brittney Louisiana
568 Added:  Joannafurt Illinois
569 Added:  Jackburgh New York
570 Added:  New Brittany Nebraska
571 Added:  North Brian Rhode Island
572 Added:  Lake Deborahberg North Carolina
573 Added:  South Kyleborough Virginia
574 Added:  West Teresamouth Texas
575 Added:  Toddfort Rhode Island
576 Added:  Josephland New Jersey
577 Added:  North William Oklahoma
578 Added:  Franklinchester Texas
579 Added:  New Sandra Wyoming
580 Added:  Lake Diane Wyoming
581 Added:  New Kiaraburgh West Virginia
582 Added:  Phillipsville Utah
583 Added:  Bakerville South Dakota
584 Added:  Williamside California
585 Added:  North Cathyberg Delaware
586 Added:  Cruzfort Alaska
587 Added:  Crystalberg Colorado
588 Added:  Schneiderbury Arkansas
589 Added:  South Robyn Alaska
590 Added:  New Kimberlyberg Oklahoma
591 Added:  Richardside Arkansas
592 Added:  Johnsberg Oklahoma
593 Added:  Lake Jared Hawaii
594 Added:  New Terrenceview Kentucky
595 Added:  South Gail South Dakota
596 Added:  New Kimland Alabama
597 Added:  Ericberg Wisconsin
598 Added:  North Stephanie Alabama
599 Added:  Marymouth Pennsylvania
600 Added:  North Nathanview New Hampshire
601 Added:  Faithfort Ohio
602 Added:  North Lesliefurt Wyoming
603 Added:  Danielsside Nevada
604 Added:  East Douglasfurt North Carolina
605 Added:  Eddieland Georgia
606 Added:  North Patrick Oregon
607 Added:  Lake Carlosview Oregon
608 Added:  Michaelfort Montana
609 Added:  Juliemouth North Carolina
610 Added:  Jessehaven Arizona
611 Added:  Harringtonstad Michigan
612 Added:  East Autumnfort Delaware
613 Added:  Ryanbury Ohio
614 Added:  New Williamton Oregon
615 Added:  Bernardstad Idaho
616 Added:  Josephfort Wisconsin
617 Added:  Smithbury Tennessee
618 Added:  Newtonstad Utah
619 Added:  North Kathleen New Mexico
620 Added:  Port Paul Maine
621 Added:  Lewistown Virginia
622 Added:  Lutzburgh South Carolina
623 Added:  Stewartmouth Nevada
624 Added:  New Russell Kansas
625 Added:  Parkerbury Indiana
626 Added:  Sydneyside Pennsylvania
627 Added:  Sheribury Rhode Island
628 Added:  Claireberg Massachusetts
629 Added:  East Megan Kentucky
630 Added:  New Janet Rhode Island
631 Added:  South Timothyburgh Rhode Island
632 Added:  Catherineland Ohio
633 Added:  Conwayport Missouri
634 Added:  Williamstad Nebraska
635 Added:  Jessicaton Illinois
636 Added:  New Marie Oklahoma
637 Added:  Millerhaven Maine
638 Added:  Barnesmouth Utah
639 Added:  Brownville Arkansas
640 Added:  Tonyaview South Carolina
641 Added:  Parkerchester New Mexico
642 Added:  Jeffreyland Washington
643 Added:  Port Courtneyhaven Alaska
644 Added:  Stephanieville Oregon
645 Added:  North Blake Connecticut
646 Added:  Christophershire Montana
647 Added:  Port Patricia South Carolina
648 Added:  West Kenneth Idaho
649 Added:  East David Iowa
650 Added:  Tylerport Georgia
651 Added:  Jamesberg Texas
652 Added:  Dicksonburgh Illinois
653 Added:  West Amandafort Utah
654 Added:  Port Lisa Louisiana
655 Added:  Lake Hollyview Rhode Island
656 Added:  North Patricia Indiana
657 Added:  South Davidfort Ohio
658 Added:  New Lucasbury Texas
659 Added:  South Leslie New Hampshire
660 Added:  Lake Dana Louisiana
661 Added:  North Michael Louisiana
662 Added:  Amandaport Indiana
663 Added:  Andrealand Idaho
664 Added:  Wilsonshire Tennessee
665 Added:  New Melissamouth Georgia
666 Added:  Greenside Illinois
667 Added:  Lake Casey New Hampshire
668 Added:  Nicholaston Minnesota
669 Added:  Fitzgeraldfurt Oklahoma
670 Added:  Port Jennifer Ohio
671 Added:  Lake Austin South Carolina
672 Added:  Blackshire Nebraska
673 Added:  South James Colorado
674 Added:  New Richardhaven Utah
675 Added:  Curryburgh Arizona
676 Added:  East John Rhode Island
677 Added:  Russellside Indiana
678 Added:  East Travis Illinois
679 Added:  New Davidborough Oklahoma
680 Added:  Burkeview Utah
681 Added:  Bowmantown Minnesota
682 Added:  Tinaborough Vermont
683 Added:  East Scotthaven Utah
684 Added:  Port Adrian Kansas
685 Added:  Ruizview Tennessee
686 Added:  Philipport Texas
687 Added:  New Davidfort Mississippi
688 Added:  East Michellechester Kansas
689 Added:  South Justinhaven South Dakota
690 Added:  Jocelynberg Delaware
691 Added:  Lukeland Mississippi
692 Added:  East Virginia North Dakota
693 Added:  Curtisfurt Montana
694 Added:  East Scottport South Dakota
695 Added:  New Jacob Rhode Island
696 Added:  Bellshire Georgia
697 Added:  Bakerborough Delaware
698 Added:  East Scott Ohio
699 Added:  Gileston Maryland
700 Added:  Berrystad Tennessee
701 Added:  North Troyhaven Arizona
702 Added:  Port Jennifershire Colorado
703 Added:  Underwoodshire Kentucky
704 Added:  Martinville Utah
705 Added:  South Debra South Dakota
706 Added:  North Jeremy Virginia
707 Added:  Port Dana Georgia
708 Added:  North Daniel Connecticut
709 Added:  Cindyshire Wyoming
710 Added:  Bethton Virginia
711 Added:  East Mariamouth Arkansas
712 Added:  Marvinchester Missouri
713 Added:  West Deniseborough Wyoming
714 Added:  New Jenniferbury North Dakota
715 Added:  South Luis Alabama
716 Added:  Roberthaven Oklahoma
717 Added:  Lake Martin Oregon
718 Added:  Bradshawport Connecticut
719 Added:  Banksview Kansas
720 Added:  Rebeccaport Colorado
721 Added:  Dustintown Missouri
722 Added:  Williamsport North Carolina
723 Added:  Mcdonaldshire West Virginia
724 Added:  East Mary Louisiana
725 Added:  Port Paulview Illinois
726 Added:  Beardview North Carolina
727 Added:  Andersonfort Louisiana
728 Added:  Lake Alexis Michigan
729 Added:  Jeanetteville Texas
730 Added:  South Kyleborough Michigan
731 Added:  Chanberg Tennessee
732 Added:  East Michaelfort New Hampshire
733 Added:  Lake Mary Nevada
734 Added:  Ortizshire Connecticut
735 Added:  New Laurenberg Connecticut
736 Added:  Port Aliciafurt Tennessee
737 Added:  Youngville Nebraska
738 Added:  Lake Maryburgh Maryland
739 Added:  Alisonside Texas
740 Added:  Aaronberg Alabama
741 Added:  West Karenmouth Illinois
742 Added:  West Nicole Oregon
743 Added:  Greenburgh New Hampshire
744 Added:  Smithtown Connecticut
745 Added:  Jennyport Ohio
746 Added:  New Kimberlyland Connecticut
747 Added:  Joybury Delaware
748 Added:  South Gabriel New Jersey
749 Added:  Rebeccaburgh New Hampshire
750 Added:  New Nicholasville Connecticut
751 Added:  Christopherfurt Indiana
752 Added:  Jenniferbury New Jersey
753 Added:  Jacobtown Pennsylvania
754 Added:  Wallerbury Maine
755 Added:  Williamfort South Dakota
756 Added:  Gilmoreview Minnesota
757 Added:  Kimberlyburgh Iowa
758 Added:  Morristown Mississippi
759 Added:  Howellport Utah
760 Added:  North Tina New Jersey
761 Added:  East Lisa Vermont
762 Added:  Andreaton New York
763 Added:  Mcclainmouth Mississippi
764 Added:  East Ashleyland New York
765 Added:  Lake Christopher North Dakota
766 Added:  Austinborough Colorado
767 Added:  Johnsonfort Virginia
768 Added:  Jocelyntown Illinois
769 Added:  Mariechester New Hampshire
770 Added:  Calebton Colorado
771 Added:  Nicholaschester Missouri
772 Added:  West Todd Montana
773 Added:  Lake Ryanport Utah
774 Added:  Moorechester Montana
775 Added:  Terrystad Maryland
776 Added:  Meyersshire Tennessee
777 Added:  West Benjamin New Hampshire
778 Added:  Collinsbury Michigan
779 Added:  South Andrew Michigan
780 Added:  East Lydia New York
781 Added:  Port Coryton Iowa
782 Added:  North Destiny Utah
783 Added:  Leonardburgh Maine
784 Added:  Alexanderside Arizona
785 Added:  South Eric Connecticut
786 Added:  South Lisaport Washington
787 Added:  Kevinton Pennsylvania
788 Added:  Martinmouth California
789 Added:  Port Debraport Iowa
790 Added:  Schultzside Indiana
791 Added:  Liuchester Arizona
792 Added:  Port Sarastad Alabama
793 Added:  Kyletown Arizona
794 Added:  East Nancyburgh New Mexico
795 Added:  New Donaldside Florida
796 Added:  North Jennaville Illinois
797 Added:  South Ryanville New Mexico
798 Added:  Benitezburgh Ohio
799 Added:  East Melissachester North Carolina
800 Added:  North Courtney Arizona
801 Added:  North Jessica Missouri
802 Added:  Allisonmouth Oklahoma
803 Added:  Stoutbury Oregon
804 Added:  East Cassidystad West Virginia
805 Added:  Sherrihaven Mississippi
806 Added:  North Aaronview West Virginia
807 Added:  Lake Rebecca Idaho
808 Added:  Port Tracyfort Texas
809 Added:  West Tammy Florida
810 Added:  East Samanthastad West Virginia
811 Added:  Jamesville North Carolina
812 Added:  Thomasview Massachusetts
813 Added:  Lake Darrell Texas
814 Added:  West Lauren Wyoming
815 Added:  West Kimfurt Oklahoma
816 Added:  Anthonymouth Iowa
817 Added:  Johnsonchester Ohio
818 Added:  Kimberlyburgh Kentucky
819 Added:  Lake Tinaland Michigan
820 Added:  Smithview Iowa
821 Added:  West Mike North Dakota
822 Added:  East Tylershire South Carolina
823 Added:  South Justinton Kentucky
824 Added:  North Laurenburgh Michigan
825 Added:  South Jim Oklahoma
826 Added:  North Dawn Wisconsin
827 Added:  South Nancy Texas
828 Added:  Watkinsmouth Minnesota
829 Added:  Davetown Nebraska
830 Added:  Jacobbury Washington
831 Added:  Durantown Texas
832 Added:  New Kaitlin Nebraska
833 Added:  Martinchester Missouri
834 Added:  Wilcoxborough Kentucky
835 Added:  Lake Sarahshire Alabama
836 Added:  Rhondaburgh Connecticut
837 Added:  West Gregory Kentucky
838 Added:  Floreschester New York
839 Added:  Wilsonmouth Kentucky
840 Added:  Jenniferfurt Rhode Island
841 Added:  South Sharonhaven North Carolina
842 Added:  South Joseph Tennessee
843 Added:  Bowentown Nebraska
844 Added:  Port Joshuatown Alaska
845 Added:  Sheltonfurt Ohio
846 Added:  Andreahaven New Hampshire
847 Added:  Laneshire Wisconsin
848 Added:  New Michaelport Nevada
849 Added:  East Connormouth South Dakota
850 Added:  South Leslie New Hampshire
851 Added:  South Kimberly Kentucky
852 Added:  Petersonhaven Washington
853 Added:  Port Brady North Carolina
854 Added:  Phillipside Tennessee
855 Added:  West Patriciahaven Florida
856 Added:  North Sarah Illinois
857 Added:  North Tracyland Oregon
858 Added:  East Courtneyshire Florida
859 Added:  Christopherstad Florida
860 Added:  Durhamton Michigan
861 Added:  North Claudiaville Maryland
862 Added:  Wendystad Idaho
863 Added:  Lake Karenfurt Montana
864 Added:  North Robert Louisiana
865 Added:  Reynoldsfort Missouri
866 Added:  South Lisa Wisconsin
867 Added:  Fullerborough Louisiana
868 Added:  Port Derrickmouth Mississippi
869 Added:  Laurenmouth Michigan
870 Added:  East Steven Florida
871 Added:  Lindafort Georgia
872 Added:  New Brendamouth Washington
873 Added:  Grantmouth Hawaii
874 Added:  Savannahville Delaware
875 Added:  Morrismouth Maryland
876 Added:  Melissatown Illinois
877 Added:  Danielleburgh Oklahoma
878 Added:  South Susan Colorado
879 Added:  Peggyville Arkansas
880 Added:  Garnerfurt New Jersey
881 Added:  Alvaradoberg Arkansas
882 Added:  East Crystalfurt Rhode Island
883 Added:  West Christophershire Connecticut
884 Added:  Port Julie Maryland
885 Added:  Barrerahaven New Hampshire
886 Added:  Kathrynburgh Tennessee
887 Added:  Greenburgh Hawaii
888 Added:  East Danastad Utah
889 Added:  Boothland Michigan
890 Added:  Roblesport New Jersey
891 Added:  East Michaelfort Iowa
892 Added:  North David Wisconsin
893 Added:  Hamiltonstad Wisconsin
894 Added:  North Marcus Illinois
895 Added:  New Amy Texas
896 Added:  Daltonshire South Dakota
897 Added:  Valenzuelaview Wyoming
898 Added:  Andrewburgh Louisiana
899 Added:  New Amy Delaware
900 Added:  Scottville Arkansas
901 Added:  Morenohaven Oklahoma
902 Added:  Bergmouth Rhode Island
903 Added:  Jeremymouth New York
904 Added:  New Jennifer Alaska
905 Added:  Draketown Colorado
906 Added:  Port Devonville Arkansas
907 Added:  Rebeccaborough Wyoming
908 Added:  Lake Brandonbury Washington
909 Added:  Port Michael Missouri
910 Added:  Paulaborough Montana
911 Added:  New Jillianshire Alabama
912 Added:  Rojaschester Georgia
913 Added:  North Beth Florida
914 Added:  Karenport Wyoming
915 Added:  Petersonchester New York
916 Added:  Lisahaven Maryland
917 Added:  Moodymouth Montana
918 Added:  Sarahview Vermont
919 Added:  East Marymouth Wisconsin
920 Added:  Richardberg Idaho
921 Added:  Leeburgh South Carolina
922 Added:  North Molly Louisiana
923 Added:  New Melissa Texas
924 Added:  Martinezbury Nevada
925 Added:  North Megan Arkansas
926 Added:  Lake Joland West Virginia
927 Added:  New Derrickshire Indiana
928 Added:  Michaelville Missouri
929 Added:  Martinezshire North Dakota
930 Added:  New Jeffrey Rhode Island
931 Added:  Morrisonville Florida
932 Added:  Larsenville West Virginia
933 Added:  Lake David Vermont
934 Added:  Joshuamouth Hawaii
935 Added:  Benitezmouth Ohio
936 Added:  Port Christophertown Arkansas
937 Added:  West Ryan Kansas
938 Added:  Sarashire Delaware
939 Added:  Cameronfort Maryland
940 Added:  South Monica Arkansas
941 Added:  Martinland Oklahoma
942 Added:  Sherrytown South Carolina
943 Added:  Port Donald Oklahoma
944 Added:  Erinmouth Vermont
945 Added:  Port Perryview New Jersey
946 Added:  Anthonytown New Jersey
947 Added:  East Lindsayport Michigan
948 Added:  Catherinefort New Hampshire
949 Added:  New Markberg Nebraska
950 Added:  West Melissashire Hawaii
951 Added:  South Michellehaven New Hampshire
952 Added:  South Lori Michigan
953 Added:  Lake Sarah Mississippi
954 Added:  Port Christopher Kansas
955 Added:  East Timothyborough Alaska
956 Added:  Riverastad Pennsylvania
957 Added:  Scotthaven West Virginia
958 Added:  West Morganchester Iowa
959 Added:  Smithfurt Virginia
960 Added:  Jasonshire Minnesota
961 Added:  Laurenburgh Washington
962 Added:  Jamesville Minnesota
963 Added:  Mooreview Virginia
964 Added:  Port Richard Texas
965 Added:  Port Jacobfurt Nebraska
966 Added:  North Ericabury Ohio
967 Added:  East Mariomouth Oklahoma
968 Added:  Port Gavinburgh Wyoming
969 Added:  Port Susanview Indiana
970 Added:  South Charleston Rhode Island
971 Added:  East Travis Texas
972 Added:  New Kelly West Virginia
973 Added:  East Nathanside Alabama
974 Added:  Dianaside Iowa
975 Added:  Alexanderchester Minnesota
976 Added:  West Sydneystad Connecticut
977 Added:  Annestad Arizona
978 Added:  Port Dawnfurt Alabama
979 Added:  Hallchester Oregon
980 Added:  Cartertown Idaho
981 Added:  Medinatown Texas
982 Added:  Port Christopherfurt Missouri
983 Added:  Lake Jeffrey Oklahoma
984 Added:  North Michellefurt Montana
985 Added:  Georgefurt Alaska
986 Added:  Crystalhaven Illinois
987 Added:  Caitlinton Nebraska
988 Added:  Palmerton Illinois
989 Added:  Stephenburgh Oregon
990 Added:  East Austin Delaware
991 Added:  Katherinemouth Washington
992 Added:  Lauraburgh Oregon
993 Added:  Hillfurt Delaware
994 Added:  Martinfurt Iowa
995 Added:  Gillberg Oklahoma
996 Added:  Stephensonstad Arizona
997 Added:  East William New York
998 Added:  New Jessica Ohio
999 Added:  East Nicholeport Alaska

CRUD Done!

Process finished with exit code 0
