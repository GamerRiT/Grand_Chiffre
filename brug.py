import sqlite3

connect=sqlite3.connect('chiffre.db')
cursor=connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS code_alfabet(
    symbol TEXT,
    digit BIGINT
    )
""")

connect.commit()

code_list=['а', 106]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['б', 120]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['в', 130]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['г', 136]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['д', 162]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['е', 100]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['ё', 114]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['ж', 104]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['з', 132]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['и', 118]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['й', 146]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['к', 158]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['л', 126]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['м', 108]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['н', 156]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['о', 124]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['п', 116]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['р', 138]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['с', 164]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['т', 110]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['у', 154]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['ф', 112]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['х', 140]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['ц', 144]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['ч', 122]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['ш', 152]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['щ', 102]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['ъ', 150]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['ы', 148]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['ь', 160]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['э', 142]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['ю', 128]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

code_list=['я', 134]
cursor.execute("INSERT INTO code_alfabet VALUES(?,?);", code_list)

connect.commit()


cursor.execute("""CREATE TABLE IF NOT EXISTS code_slogi(
    symbol TEXT,
    digit BIGINT
    )
""")

code_list=['пре', 1]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

code_list=['при', 10]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

code_list=['ани', 4]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

code_list=['ени', 11]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

code_list=['онн', 7]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

code_list=['лив', 8]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

code_list=['ичн', 9]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

code_list=['ыва', 15]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

code_list=['ова', 6]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

code_list=['ева', 20]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

code_list=['вши', 19]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

code_list=['енн', 13]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

code_list=['ённ', 12]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

code_list=['езд', 2]
cursor.execute("INSERT INTO code_slogi VALUES(?,?);", code_list)

connect.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS code_slogi_1(
    symbol TEXT,
    digit BIGINT
    )
""")

code_list=['на', 257]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ма', 668]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['та', 200]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ка', 266]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ха', 674]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ба', 356]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ва', 515]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['га', 242]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['да', 731]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['жа', 461]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['за', 392]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ла', 296]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['па', 758]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ра', 320]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['са', 593]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['фа', 533]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ца', 416]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ча', 764]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ша', 548]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ща', 581]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['йа', 767]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

connect.commit()

code_list=['ну', 395]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['му', 635]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ту', 782]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ку', 464]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ху', 785]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['бу', 419]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ву', 701]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['гу', 212]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ду', 590]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['жу', 443]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['зу', 725]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['лу', 230]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['пу', 542]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ру', 269]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['су', 350]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['фу', 434]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['цу', 734]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['чу', 476]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['шу', 305]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['щу', 554]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['йу', 497]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['но', 323]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['мо', 245]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['то', 374]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ко', 425]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['хо', 398]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['бо', 509]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['во', 596]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['го', 521]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['до', 662]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['жо', 737]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['зо', 254]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ло', 260]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['по', 290]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ро', 728]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['со', 689]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['фо', 287]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['цо', 686]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['чо', 719]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['шо', 209]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['що', 707]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['йо', 467]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ны', 437]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['мы', 680]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ты', 362]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['хы', 446]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['бы', 503]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['вы', 449]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['зы', 659]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['лы', 692]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['пы', 401]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ры', 698]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['сы', 779]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['фы', 602]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['цы', 644]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ни', 566]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ми', 329]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ти', 584]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ки', 482]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['хи', 455]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['би', 746]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ви', 281]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ги', 704]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ди', 794]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['жи', 500]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['зи', 470]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ли', 248]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['пи', 491]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ри', 716]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['си', 620]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['фи', 572]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ци', 389]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['чи', 665]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ши', 695]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['щи', 218]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['йи', 263]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['не', 539]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ме', 626]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['те', 440]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ке', 656]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['хе', 206]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['бе', 458]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ве', 770]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ге', 203]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['де', 614]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['же', 371]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['зе', 413]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ле', 341]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ре', 713]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['се', 752]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['фе', 272]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['це', 407]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['че', 365]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ше', 524]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ще', 368]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ня', 587]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['мя', 275]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['тя', 410]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['кя', 527]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['хя', 647]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['бя', 311]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['вя', 557]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['гя', 452]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['дя', 485]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['фя', 710]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['зя', 404]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ля', 284]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['пя', 353]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ря', 740]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ся', 251]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['нё', 560]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['мё', 332]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['тё', 302]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['кё', 422]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['хё', 638]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['бё', 347]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['вё', 761]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['гё', 278]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['дё', 215]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['жё', 506]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['зё', 326]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['лё', 518]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['пё', 683]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['рё', 749]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['сё', 479]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['фё', 308]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['щё', 293]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['чё', 551]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['шё', 671]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ню', 722]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['мю', 677]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['тю', 233]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['кю', 632]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['хю', 380]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['бю', 563]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['вю', 383]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['гю', 608]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['дю', 611]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['фю', 224]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['зю', 617]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['лю', 776]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['пю', 344]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['рю', 650]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['сю', 605]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['нэ', 386]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['мэ', 569]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['тэ', 377]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['кэ', 797]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['хэ', 236]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['бэ', 743]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['вэ', 623]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['гэ', 512]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['дэ', 335]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['фэ', 578]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['зэ', 221]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['лэ', 431]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['пэ', 314]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['рэ', 338]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['сэ', 428]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['нь', 575]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['мь', 536]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ть', 227]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['кь', 788]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['хь', 791]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['бь', 494]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['вь', 599]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['гь', 629]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['дь', 359]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['жь', 473]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['зь', 773]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['ль', 545]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['пь', 653]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['рь', 317]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['сь', 239]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['фь', 530]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['щь', 488]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['чь', 641]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

code_list=['шь', 755]
cursor.execute("INSERT INTO code_slogi_1 VALUES(?,?);", code_list)

connect.commit()