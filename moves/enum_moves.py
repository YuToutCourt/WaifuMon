from enum import Enum


class Moves(Enum):
    ATTACK_ORDER = 1
    BUG_BITE = 2
    FIRST_IMPRESSION = 3
    FURY_CUTTER = 4
    HEAL_ORDER = 5
    INFESTATION = 6
    LEECH_LIFE = 7
    MEGAHORN = 8
    PIN_MISSILE = 9
    POLLEN_PUFF = 10
    SIGNAL_BEAM = 14
    SILVER_WIND = 15
    TAIL_GLOW = 17
    X_SCISSOR = 19
    ASSURANCE = 20
    BADDY_BAD = 21
    BEAT_UP = 22
    BRUTAL_SWING = 24
    CEASELESS_EDGE = 25
    CRUNCH = 27
    DARKEST_LARIAT = 28
    DARK_VOID = 29
    FALSE_SURRENDER = 31
    FEINT_ATTACK = 32
    FOUL_PLAY = 34
    JAW_LOCK = 35
    KNOCK_OFF = 36
    KOWTOW_CLEAVE = 37
    LASH_OUT = 38
    MALICIOUS_MOONSAULT = 39
    NIGHT_DAZE = 40
    NIGHT_SLASH = 41
    PAYBACK = 42
    POWER_TRIP = 43
    PUNISHMENT = 44
    PURSUIT = 45
    RUINATION = 47
    SUCKER_PUNCH = 49
    THROAT_CHOP = 52
    WICKED_BLOW = 54
    WICKED_TORQUE = 55
    CLANGOROUS_SOULBLAZE = 56
    CORE_ENFORCER = 57
    DRAGON_CLAW = 59
    DRAGON_DARTS = 60
    DRAGON_ENERGY = 61
    DRAGON_HAMMER = 62
    DRAGON_PULSE = 63
    DRAGON_RAGE = 64
    DRAGON_TAIL = 65
    DUAL_CHOP = 66
    DYNAMAX_CANNON = 67
    ETERNABEAM = 68
    GLAIVE_RUSH = 69
    ORDER_UP = 70
    ROAR_OF_TIME = 71
    SPACIAL_REND = 72
    AURA_WHEEL = 73
    BOLT_BEAK = 74
    BUZZY_BUZZ = 75
    CATASTROPIKA = 76
    CHARGE_BEAM = 77
    DOUBLE_SHOCK = 78
    ELECTRO_BALL = 80
    ELECTRO_DRIFT = 81
    FUSION_BOLT = 82
    GIGAVOLT_HAVOC = 83
    MAGNET_RISE = 85
    NUZZLE = 86
    OVERDRIVE = 87
    PARABOLIC_CHARGE = 88
    PLASMA_FISTS = 90
    RISING_VOLTAGE = 91
    SHOCK_WAVE = 92
    STOKED_SPARKSURFER = 93
    THUNDER_CAGE = 94
    THUNDER_WAVE = 95
    VOLT_SWITCH = 96
    WILDBOLT_STORM = 97
    WILD_CHARGE = 98
    ZAP_CANNON = 99
    ZIPPY_ZAP = 100
    CRAFTY_SHIELD = 101
    DAZZLING_GLEAM = 102
    DISARMING_VOICE = 103
    DRAINING_KISS = 104
    FAIRY_WIND = 106
    FLORAL_HEALING = 107
    GUARDIAN_OF_ALOLA = 108
    LIGHT_OF_RUIN = 109
    MAGICAL_TORQUE = 110
    MISTY_EXPLOSION = 111
    MOONBLAST = 113
    MOONLIGHT = 114
    NATURE_MADNESS = 115
    PLAY_ROUGH = 116
    SPARKLY_SWIRL = 117
    STRANGE_STEAM = 118
    SWEET_KISS = 119
    TWINKLE_TACKLE = 120
    ARM_THRUST = 121
    AURA_SPHERE = 122
    AXE_KICK = 123
    BODY_PRESS = 124
    BRICK_BREAK = 125
    CIRCLE_THROW = 126
    COACHING = 127
    COLLISION_COURSE = 128
    COMBAT_TORQUE = 129
    COUNTER = 130
    CROSS_CHOP = 131
    DOUBLE_KICK = 133
    DRAIN_PUNCH = 134
    DYNAMIC_PUNCH = 135
    FINAL_GAMBIT = 136
    FLYING_PRESS = 137
    FOCUS_BLAST = 138
    FOCUS_PUNCH = 139
    HIGH_JUMP_KICK = 140
    JUMP_KICK = 141
    KARATE_CHOP = 142
    LOW_KICK = 143
    MACH_PUNCH = 144
    METEOR_ASSAULT = 146
    QUICK_GUARD = 147
    REVENGE = 148
    REVERSAL = 149
    ROCK_SMASH = 150
    SACRED_SWORD = 151
    SECRET_SWORD = 152
    SEISMIC_TOSS = 153
    SKY_UPPERCUT = 154
    STORM_THROW = 155
    SUBMISSION = 156
    THUNDEROUS_KICK = 157
    TRIPLE_ARROWS = 158
    TRIPLE_KICK = 159
    VACUUM_WAVE = 160
    VICTORY_DANCE = 161
    VITAL_THROW = 162
    WAKE_UP_SLAP = 163
    BITTER_BLADE = 164
    BLAST_BURN = 165
    BLAZING_TORQUE = 166
    BURNING_JEALOUSY = 167
    BURN_UP = 168
    ERUPTION = 169
    FIERY_DANCE = 170
    FIRE_PLEDGE = 171
    FIRE_SPIN = 172
    FLAME_BURST = 173
    FUSION_FLARE = 174
    HEAT_CRASH = 175
    INCINERATE = 176
    INFERNO = 177
    INFERNO_OVERDRIVE = 178
    MAGMA_STORM = 179
    MIND_BLOWN = 180
    RAGING_FURY = 181
    SHELL_TRAP = 182
    SIZZLY_SLIDE = 183
    TORCH_SONG = 185
    ACROBATICS = 186
    AERIAL_ACE = 187
    AEROBLAST = 188
    AIR_CUTTER = 189
    BEAK_BLAST = 190
    BLEAKWIND_STORM = 191
    BRAVE_BIRD = 192
    CHATTER = 193
    DRILL_PECK = 194
    DUAL_WINGBEAT = 195
    FLY = 196
    GUST = 197
    HURRICANE = 198
    OBLIVION_WING = 200
    PECK = 201
    PLUCK = 202
    ROOST = 203
    SKY_DROP = 204
    SUPERSONIC_SKYSTRIKE = 205
    TAILWIND = 206
    WING_ATTACK = 207
    ASTRAL_BARRAGE = 208
    BITTER_MALICE = 209
    CONFUSE_RAY = 210
    GRUDGE = 213
    HEX = 214
    INFERNAL_PARADE = 215
    LAST_RESPECTS = 216
    MENACING_MOONRAZE_MAELSTROM = 217
    MOONGEIST_BEAM = 218
    NIGHT_SHADE = 220
    OMINOUS_WIND = 221
    PHANTOM_FORCE = 222
    RAGE_FIST = 223
    SHADOW_BALL = 224
    SHADOW_BONE = 225
    SHADOW_CLAW = 226
    SHADOW_FORCE = 227
    SHADOW_PUNCH = 228
    SHADOW_SNEAK = 229
    SINISTER_ARROW_RAID = 230
    SPECTRAL_THIEF = 231
    SPIRIT_SHACKLE = 232
    SPITE = 233
    TRICK_OR_TREAT = 234
    ABSORB = 235
    AROMATHERAPY = 236
    BLOOM_DOOM = 237
    BRANCH_POKE = 238
    BULLET_SEED = 239
    CHLOROBLAST = 240
    ENERGY_BALL = 241
    FLOWER_TRICK = 242
    FOREST_CURSE = 243
    FRENZY_PLANT = 244
    GIGA_DRAIN = 245
    GRASSY_GLIDE = 246
    GRASSY_TERRAIN = 247
    GRASS_KNOT = 248
    GRASS_PLEDGE = 249
    HORN_LEECH = 250
    JUNGLE_HEALING = 252
    LEAFAGE = 253
    LEAF_BLADE = 254
    LEAF_TORNADO = 255
    MAGICAL_LEAF = 257
    MEGA_DRAIN = 258
    PETAL_BLIZZARD = 259
    POWER_WHIP = 260
    RAZOR_LEAF = 261
    SAPPY_SEED = 262
    SEED_BOMB = 263
    SEED_FLARE = 264
    SNAP_TRAP = 265
    SOLAR_BEAM = 266
    SOLAR_BLADE = 267
    SPIKY_SHIELD = 268
    STUN_SPORE = 269
    SYNTHESIS = 270
    TRAILBLAZE = 271
    TROP_KICK = 272
    VINE_WHIP = 273
    WOOD_HAMMER = 274
    BONEMERANG = 276
    BONE_RUSH = 277
    DIG = 278
    DRILL_RUN = 279
    EARTHQUAKE = 280
    EARTH_POWER = 281
    FISSURE = 282
    HIGH_HORSEPOWER = 283
    LAND_WRATH = 284
    MAGNITUDE = 285
    MUD_BOMB = 286
    PRECIPICE_BLADES = 288
    SANDSEAR_STORM = 289
    SAND_TOMB = 290
    SCORCHING_SANDS = 291
    SHORE_UP = 292
    STOMPING_TANTRUM = 294
    TECTONIC_RAGE = 295
    THOUSAND_ARROWS = 296
    THOUSAND_WAVES = 297
    AURORA_BEAM = 298
    AURORA_VEIL = 299
    AVALANCHE = 300
    FREEZY_FROST = 302
    FROST_BREATH = 303
    GLACIAL_LANCE = 304
    HAZE = 306
    ICE_BALL = 307
    ICE_SHARD = 308
    ICE_SPINNER = 309
    ICICLE_SPEAR = 310
    MIST = 311
    SHEER_COLD = 312
    SUBZERO_SLAMMER = 313
    TRIPLE_AXEL = 314
    AFTER_YOU = 315
    ASSIST = 316
    BARRAGE = 318
    BESTOW = 320
    BIDE = 321
    BIND = 322
    BLOCK = 323
    BOOMBURST = 324
    BREAKNECK_BLITZ = 325
    CAMOUFLAGE = 326
    CELEBRATE = 327
    CHIP_AWAY = 328
    COMET_PUNCH = 329
    CONSTRICT = 330
    CONVERSION = 331
    COVET = 335
    CRUSH_CLAW = 336
    CRUSH_GRIP = 337
    CUT = 338
    DIZZY_PUNCH = 340
    DOODLE = 341
    DOUBLE_EDGE = 342
    DOUBLE_HIT = 343
    DOUBLE_SLAP = 344
    ECHOED_VOICE = 345
    EGG_BOMB = 346
    ENCORE = 347
    ENDEAVOR = 348
    ENDURE = 349
    ENTRAINMENT = 350
    EXPLOSION = 351
    EXTREME_SPEED = 352
    FACADE = 353
    FAKE_OUT = 354
    FALSE_SWIPE = 355
    FEINT = 356
    FOCUS_ENERGY = 358
    FRUSTRATION = 361
    FURY_ATTACK = 362
    FURY_SWIPES = 363
    GIGA_IMPACT = 364
    GLARE = 365
    GUILLOTINE = 366
    HEAD_CHARGE = 368
    HEAL_BELL = 369
    HELPING_HAND = 370
    HIDDEN_POWER = 371
    HOLD_BACK = 372
    HORN_ATTACK = 374
    HORN_DRILL = 375
    HYPER_BEAM = 376
    HYPER_DRILL = 377
    HYPER_VOICE = 378
    JUDGMENT = 379
    LASER_FOCUS = 380
    LAST_RESORT = 381
    LOCK_ON = 382
    LUCKY_CHANT = 383
    MEGA_KICK = 385
    MEGA_PUNCH = 386
    MILK_DRINK = 389
    MIMIC = 390
    MIND_READER = 391
    MORNING_SUN = 392
    MULTI_ATTACK = 393
    PAIN_SPLIT = 397
    PAY_DAY = 398
    POPULATION_BOMB = 400
    POUND = 401
    POWER_SHIFT = 402
    PRESENT = 403
    PROTECT = 404
    PSYCH_UP = 405
    PULVERIZING_PANCAKE = 406
    QUICK_ATTACK = 407
    RAGING_BULL = 408
    RAZOR_WIND = 409
    RECOVER = 410
    RECYCLE = 411
    REFLECT_TYPE = 412
    REFRESH = 413
    RELIC_SONG = 414
    RETALIATE = 415
    RETURN_ = 416
    REVELATION_DANCE = 417
    ROCK_CLIMB = 420
    SCRATCH = 423
    SECRET_POWER = 424
    SELF_DESTRUCT = 425
    SLACK_OFF = 429
    SLAM = 430
    SLASH = 431
    SLEEP_TALK = 432
    SMELLING_SALTS = 433
    SOFT_BOILED = 434
    SONIC_BOOM = 435
    SPIKE_CANNON = 436
    SPLASH = 438
    STRENGTH = 441
    STRUGGLE = 442
    SUPERSONIC = 444
    SUPER_FANG = 445
    SWIFT = 447
    TACKLE = 448
    TAIL_SLAP = 449
    TAIL_WHIP = 450
    TAKE_DOWN = 451
    TECHNO_BLAST = 454
    TEETER_DANCE = 455
    TERA_BLAST = 456
    TERRAIN_PULSE = 457
    TICKLE = 458
    TRUMP_CARD = 461
    UPROAR = 462
    VISE_GRIP = 464
    WEATHER_BALL = 465
    WISH = 467
    WORK_UP = 468
    WRAP = 469
    WRING_OUT = 470
    ACID = 471
    ACID_DOWNPOUR = 472
    BARB_BARRAGE = 474
    BELCH = 475
    CLEAR_SMOG = 476
    DIRE_CLAW = 478
    MORTAL_SPIN = 480
    NOXIOUS_TORQUE = 481
    POISON_GAS = 482
    POISON_JAB = 483
    POISON_POWDER = 484
    POISON_STING = 485
    PURIFY = 486
    TOXIC = 487
    TOXIC_THREAD = 489
    VENOM_DRENCH = 490
    VENOSHOCK = 491
    CONFUSION = 493
    DREAM_EATER = 494
    EERIE_SPELL = 495
    EXPANDING_FORCE = 496
    FUTURE_SIGHT = 497
    GENESIS_SUPERNOVA = 498
    GLITZY_GLOW = 499
    HEAL_PULSE = 505
    LIGHT_THAT_BURNS_THE_SKY = 511
    LUNAR_BLESSING = 512
    LUSTER_PURGE = 514
    MIST_BALL = 520
    PHOTON_GEYSER = 521
    PRISMATIC_LASER = 525
    PSYBEAM = 526
    PSYBLADE = 527
    PSYCHIC = 528
    PSYCHIC_FANGS = 529
    PSYSHOCK = 533
    PSYSTRIKE = 534
    STORED_POWER = 542
    SYNCHRONOISE = 543
    TWIN_BEAM = 549
    ACCELEROCK = 551
    ANCIENT_POWER = 552
    DIAMOND_STORM = 554
    HEAD_SMASH = 555
    METEOR_BEAM = 556
    POWER_GEM = 557
    ROCK_BLAST = 558
    ROCK_THROW = 559
    ROCK_WRECKER = 560
    ROLLOUT = 561
    SALT_CURE = 562
    SMACK_DOWN = 564
    SPLINTERED_STORMSHARDS = 565
    STONE_AXE = 567
    STONE_EDGE = 568
    STEAMROLLER = 571
    TWINEEDLE = 572
    BITE = 573
    DARK_PULSE = 574
    FIERY_WRATH = 575
    TAUNT = 576
    DRAGON_BREATH = 577
    DRAGON_RUSH = 578
    OUTRAGE = 579
    TWISTER = 580
    BOLT_STRIKE = 581
    DISCHARGE = 582
    SPARK = 583
    THUNDER = 584
    THUNDERBOLT = 585
    THUNDER_FANG = 586
    THUNDER_PUNCH = 587
    THUNDER_SHOCK = 588
    VOLT_TACKLE = 589
    ZING_ZAP = 590
    FORCE_PALM = 591
    ROLLING_KICK = 592
    BLAZE_KICK = 593
    BLUE_FLARE = 594
    EMBER = 595
    FIRE_BLAST = 596
    FIRE_FANG = 597
    FIRE_PUNCH = 598
    FLAMETHROWER = 599
    FLAME_WHEEL = 600
    FLARE_BLITZ = 601
    HEAT_WAVE = 602
    LAVA_PLUME = 603
    PYRO_BALL = 604
    SACRED_FIRE = 605
    SEARING_SHOT = 606
    WILL_O_WISP = 607
    AIR_SLASH = 608
    BOUNCE = 609
    FLOATY_FALL = 610
    SKY_ATTACK = 611
    ASTONISH = 612
    LICK = 613
    GRASS_WHISTLE = 614
    NEEDLE_ARM = 615
    PETAL_DANCE = 616
    SLEEP_POWDER = 617
    SPORE = 618
    BONE_CLUB = 619
    BLIZZARD = 620
    FREEZE_DRY = 621
    FREEZE_SHOCK = 622
    ICE_BEAM = 623
    ICE_BURN = 624
    ICE_FANG = 625
    ICE_PUNCH = 626
    ICICLE_CRASH = 627
    POWDER_SNOW = 628
    BODY_SLAM = 629
    HEADBUTT = 630
    HYPER_FANG = 631
    LOVELY_KISS = 632
    SING = 633
    SNORE = 634
    STOMP = 635
    THRASH = 636
    TRI_ATTACK = 637
    YAWN = 638
    CROSS_POISON = 639
    GUNK_SHOT = 640
    POISON_FANG = 641
    POISON_TAIL = 642
    SHELL_SIDE_ARM = 643
    SLUDGE = 644
    SLUDGE_BOMB = 645
    SLUDGE_WAVE = 646
    SMOG = 647
    EXTRASENSORY = 648
    FREEZING_GLARE = 649
    HEART_STAMP = 650
    HYPNOSIS = 651
    ZEN_HEADBUTT = 652
    ROCK_SLIDE = 653
    DOUBLE_IRON_BASH = 654
    IRON_HEAD = 655
    SCALD = 656
    SPLISHY_SPLASH = 657
    STEAM_ERUPTION = 658
    WATERFALL = 659
    BUG_BUZZ = 660
    DEFEND_ORDER = 661
    FELL_STINGER = 662
    LUNGE = 663
    POUNCE = 664
    QUIVER_DANCE = 665
    SILK_TRAP = 666
    SKITTER_SMACK = 667
    STICKY_WEB = 668
    STRING_SHOT = 669
    STRUGGLE_BUG = 670
    FAKE_TEARS = 671
    FLATTER = 672
    HONE_CLAWS = 673
    HYPERSPACE_FURY = 674
    MEMENTO = 675
    NASTY_PLOT = 676
    OBSTRUCT = 677
    PARTING_SHOT = 678
    SNARL = 679
    BREAKING_SWIPE = 680
    CLANGING_SCALES = 681
    CLANGOROUS_SOUL = 682
    DRACO_METEOR = 683
    DRAGON_DANCE = 684
    SCALE_SHOT = 685
    CHARGE = 686
    EERIE_IMPULSE = 687
    ELECTROWEB = 688
    MAGNETIC_FLUX = 689
    AROMATIC_MIST = 690
    BABY_DOLL_EYES = 691
    CHARM = 692
    DECORATE = 693
    FLEUR_CANNON = 694
    FLOWER_SHIELD = 695
    GEOMANCY = 696
    SPIRIT_BREAK = 697
    SPRINGTIDE_STORM = 698
    BULK_UP = 699
    CLOSE_COMBAT = 700
    HAMMER_ARM = 701
    LOW_SWEEP = 702
    NO_RETREAT = 703
    OCTOLOCK = 704
    POWER_UP_PUNCH = 705
    SUPERPOWER = 706
    ARMOR_CANNON = 707
    FIRE_LASH = 708
    FLAME_CHARGE = 709
    MYSTICAL_FIRE = 710
    OVERHEAT = 711
    V_CREATE = 712
    DEFOG = 713
    DRAGON_ASCENT = 714
    FEATHER_DANCE = 715
    APPLE_ACID = 716
    COTTON_GUARD = 717
    COTTON_SPORE = 718
    DRUM_BEATING = 719
    GRAV_APPLE = 720
    LEAF_STORM = 721
    SPICY_EXTRACT = 722
    STRENGTH_SAP = 723
    BULLDOZE = 724
    HEADLONG_RUSH = 725
    MUD_SHOT = 726
    MUD_SLAP = 727
    ROTOTILLER = 728
    SAND_ATTACK = 729
    GLACIATE = 730
    ICE_HAMMER = 731
    ICY_WIND = 732
    MOUNTAIN_GALE = 733
    SNOWSCAPE = 734
    ACUPRESSURE = 735
    BELLY_DRUM = 736
    CAPTIVATE = 737
    CONFIDE = 738
    DEFENSE_CURL = 739
    DOUBLE_TEAM = 740
    EXTREME_EVOBOOST = 741
    FILLET_AWAY = 742
    FLASH = 743
    GROWL = 744
    GROWTH = 745
    HARDEN = 746
    HOWL = 747
    LEER = 748
    MINIMIZE = 749
    NOBLE_ROAR = 750
    PLAY_NICE = 751
    RAGE = 752
    RAPID_SPIN = 753
    SCARY_FACE = 754
    SCREECH = 755
    SHARPEN = 756
    SHELL_SMASH = 757
    SKULL_BASH = 758
    SMOKESCREEN = 759
    STUFF_CHEEKS = 760
    SWAGGER = 761
    SWEET_SCENT = 762
    SWORDS_DANCE = 763
    ACID_ARMOR = 764
    ACID_SPRAY = 765
    COIL = 766
    AGILITY = 767
    AMNESIA = 768
    BARRIER = 769
    CALM_MIND = 770
    COSMIC_POWER = 771
    ESPER_WING = 772
    KINESIS = 773
    LUMINA_CRASH = 774
    MEDITATE = 775
    MYSTICAL_POWER = 776
    PSYCHO_BOOST = 777
    PSYSHIELD_BASH = 778
    ROCK_POLISH = 779
    ROCK_TOMB = 780
    AUTOTOMIZE = 781
    IRON_DEFENSE = 782
    KING_SHIELD = 783
    MAKE_IT_RAIN = 784
    METAL_SOUND = 785
    SHELTER = 786
    SHIFT_GEAR = 787
    SPIN_OUT = 788
    AQUA_STEP = 789
    CHILLING_WATER = 790
    ANCHOR_SHOT = 791
    BEHEMOTH_BASH = 792
    BEHEMOTH_BLADE = 793
    BULLET_PUNCH = 794
    DOOM_DESIRE = 796
    FLASH_CANNON = 797
    GEAR_GRIND = 798
    GIGATON_HAMMER = 800
    IRON_TAIL = 803
    MAGNET_BOMB = 804
    METAL_CLAW = 806
    METEOR_MASH = 807
    MIRROR_SHOT = 808
    SEARING_SUNRAZE_SMASH = 809
    SMART_STRIKE = 810
    STEEL_BEAM = 811
    STEEL_ROLLER = 812
    STEEL_WING = 813
    SUNSTEEL_STRIKE = 814
    AQUA_CUTTER = 815
    AQUA_JET = 816
    AQUA_TAIL = 818
    BOUNCY_BUBBLE = 819
    BRINE = 820
    BUBBLE = 821
    BUBBLE_BEAM = 822
    CLAMP = 823
    CRABHAMMER = 824
    DIVE = 825
    FISHIOUS_REND = 826
    FLIP_TURN = 827
    HYDRO_CANNON = 828
    HYDRO_PUMP = 829
    HYDRO_STEAM = 830
    JET_PUNCH = 832
    LIQUIDATION = 834
    MUDDY_WATER = 835
    OCEANIC_OPERETTA = 836
    OCTAZOOKA = 837
    ORIGIN_PULSE = 838
    RAZOR_SHELL = 840
    SNIPE_SHOT = 841
    SPARKLING_ARIA = 843
    SURF = 844
    SURGING_STRIKES = 845
    TRIPLE_DIVE = 846
    WATER_GUN = 847
    WATER_PLEDGE = 848
    WATER_PULSE = 849
    WATER_SHURIKEN = 850
    WATER_SPOUT = 852
    WAVE_CRASH = 853
    WHIRLPOOL = 854
    NOTHING = 856
